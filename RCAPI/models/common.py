"""
Common
"""
import six
import json

class FinishedObject(object):
  """
  Adds functionality to BaseObject or Resource to print in non-empty JSON format
  """
  def __init__(self, entry):
    self = entry
    
  def to_json(self):
    """
    Return data in json format
    """
    orig_json = self.__dict__
    non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
    return non_empty_json
    
class BaseObject(FinishedObject):
  """
  Formats basic object returned from API into a FinishedObject
  """
  def __init__(self, entry, type_mapping={}):
    known_keys = ['attributes', 'data', 'relationships', 'meta', 'error', 'flash']
    if entry is not None:
      for key in entry:
        # Kinda "hacky-hacky" and not an elegant fix for PlaybookAction objects
        if key == 'actions' and 'actions' in type_mapping:
          temp = []
          for action in entry[key]:
            temp.append(type_mapping['actions'](action))
          self.__dict__['actions'] = temp
        # Again, "hacky-hacky" fix for TriggerCondition objects
        elif key == 'conditions' and 'conditions' in type_mapping:
          temp = []
          for condition in entry[key]:
            temp.append(type_mapping['conditions'](condition))
          self.__dict__['conditions'] = temp
        elif not isinstance(key, dict):
          if key in type_mapping:
            self.__dict__[key] = type_mapping[key](entry[key])
          elif key in known_keys:
            for item in entry[key]:
              if not isinstance(item, dict):
                if item in type_mapping:
                  # Again, "hacky-hacky" fix for Detector objects
                  if item == 'detectors':
                    temp = []
                    for detector in entry[key][item]:
                      temp.append(type_mapping['detectors'](detector))
                    self.__dict__['detectors'] = temp
                  else:
                    self.__dict__[item] = type_mapping[item](entry[key][item])
                else:
                  try:
                    self.__dict__[item] = entry[key][item]
                  except:
                    self.__dict__[key] = entry[key]
          else:
            self.__dict__[key] = entry[key]
    super().__init__(self)

class SelectableObject(BaseObject):
  """
  Formats selectable object as a basic object
  """
  def __init__(self, entry, type_mapping={}):
    super().__init__(entry, type_mapping)

class Resource(FinishedObject):
  """
  Formats Resource into an array of FinishedObjects with `api_version` defined
  """
  def __init__(self, entry, object_type, base=None, client=None):
    if base is not None:
      self = base
    self.__dict__['api_version'] = entry['meta']['api_version']
    if entry['meta']['total_items']:
      self.__dict__['total_items'] = entry['meta']['total_items']
    temp = []
    for item in entry['data']:
      # hacky-hacky way to handle reporting_tag_associations
      if str(object_type.__name__) == 'ReportingTagAssociation':
        temp.append(object_type(entry['data'][item] | {'endpoint_id': item}))
      else:
        if issubclass(object_type, SelectableObject) and client is not None:
          temp.append(object_type(item, client))
        else:
          temp.append(object_type(item))
    self.__dict__['data'] = temp
    super().__init__(self)

class Collection(Resource):
  """
  Formats Collection into a Resource with `links` defined
  """
  def __init__(self, entry, object_type, client=None):
    temp_dict = {}
    for item in entry['links']:
      temp_dict[item] = entry['links'][item]
    self.__dict__['links'] = temp_dict
    super().__init__(entry, object_type, self, client)