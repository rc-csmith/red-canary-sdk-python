"""
Activity Timelines
"""

from .common import BaseObject, FinishedObject
from .primitive_activities import FileModification, NetworkConnection, \
                                              RegistryModification, ProcessExecution, ModuleLoad
from .exec import PlaybookExecution, ActionExecution

class ActivityOccurred(BaseObject):
  """
  Activity Occurred object
  Includes FileModification, NetworkConnection, RegistryModification, ProcessExecution, and ModuleLoad
  """
  def __init__(self, entry):
    type_mapping = {
      'file_modification': FileModification,
      'network_connection': NetworkConnection,
      'registry_modification': RegistryModification,
      'process_execution': ProcessExecution,
      'module_load': ModuleLoad
    }
    super().__init__(entry, type_mapping)

class TimelineEntry(BaseObject):
  """
  Timeline Entry object
  """

class Timeline(FinishedObject):
  """
  Timeline object
  Array of multipe different types and includes ActivityOccurred, PlaybookExecution, and ActionExecution
  """
  def __init__(self, entry):
    ## Can't use the common pre-built objects since Timelines are an array of multiple different types
    ## Parse the Collection portion of the Timeline object
    temp_dict = {}
    for item in entry['links']:
      temp_dict[item] = entry['links'][item]
    self.__dict__['links'] = temp_dict

    type_mapping = {
      'activity_timelines.ActivityOccurred': ActivityOccurred,
      'exec.PlaybookExecution': PlaybookExecution,
      'exec.ActionExecution': ActionExecution
    }

    ## Parse the Resource portion of the Timeline object
    self.__dict__['api_version'] = entry['meta']['api_version']
    if entry['meta']['total_items']:
      self.__dict__['total_items'] = entry['meta']['total_items']
    temp = []
    for item in entry['data']:
      if item['type'] in type_mapping:
        object_type = type_mapping.get(item['type'])
      else:
        object_type = TimelineEntry
      temp.append(object_type(item))
    self.__dict__['data'] = temp

    super().__init__(self)
