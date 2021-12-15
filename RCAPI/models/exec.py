from RCAPI.models.general import PortalUser, Indicator
from RCAPI.models.common import BaseObject

class Playbook(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    for key in entry:
      if key == 'actions':
        self.__dict__[key] = PlaybookAction(entry[key])
      elif not (isinstance(key, dict)):
        self.__dict__[key] = entry[key]

class PlaybookAction(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    for key in entry:
      if key == 'indicator':
        self.__dict__[key] = Indicator(entry[key])
      elif not (isinstance(key, dict)):
        self.__dict__[key] = entry[key]

class TriggerCondition(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    for key in entry:
      if not (isinstance(key, dict)):
        self.__dict__[key] = entry[key]
    
class Trigger(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    for key in entry:
      if key == 'condition':
        self.__dict__[key] = TriggerCondition(entry[key])
      elif not (isinstance(key, dict)):
        self.__dict__[key] = entry[key]

class PlaybookExecution(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    for key in entry:
      if key == 'playbook':
        self.__dict__[key] = Playbook(entry[key])
      elif key == 'trigger':
        self.__dict__[key] = Trigger(entry[key])
      elif key == 'executing_user':
        self.__dict__[key] = PortalUser(entry[key])
      if not (isinstance(key, dict)):
        self.__dict__[key] = entry[key]

class ActionExecution(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    for key in entry:
      if key == 'action':
        self.__dict__[key] = PlaybookAction(entry[key])
      elif key == 'approved_by':
        self.__dict__[key] = PortalUser(entry[key])
      elif key == 'denied_by':
        self.__dict__[key] = PortalUser(entry[key])
      elif key == 'playbook_execution':
        self.__dict__[key] = PlaybookExecution(entry[key])
      elif key == 'playbook':
        self.__dict__[key] = Playbook(entry[key])
      elif not (isinstance(key, dict)):
        self.__dict__[key] = entry[key]

class PlaybookResource(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['api_version'] = entry['meta']['api_version']

    temp = []
    for item in entry['data']:
      temp.append(Playbook(item))

    self.__dict__['data'] = temp

class TriggerConditionCollection(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['api_version'] = entry['meta']['api_version']
  
    temp = []
    for item in entry['data']:
      temp.append(TriggerCondition(item))
    self.__dict__['data'] = temp

class TriggerConditionResource(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['api_version'] = entry['meta']['api_version']

    temp = []
    for item in entry['data']:
      temp.append(TriggerCondition(item))
    self.__dict__['data'] = temp

class TriggerResource(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['api_version'] = entry['meta']['api_version']
  
    temp = []
    for item in entry['data']:
      temp.append(Trigger(item))
    self.__dict__['data'] = temp

class TriggerCollection(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['api_version'] = entry['meta']['api_version']
  
    temp = []
    for item in entry['data']:
      temp.append(Trigger(item))
    self.__dict__['data'] = temp

class PlaybookActionResource(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['api_version'] = entry['meta']['api_version']
  
    temp = []
    for item in entry['data']:
      temp.append(PlaybookAction(item))
    self.__dict__['data'] = temp

class PlaybookCollection(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['api_version'] = entry['meta']['api_version']
  
    temp = []
    for item in entry['data']:
      temp.append(Playbook(item))
    self.__dict__['data'] = temp
  
class Configuration(BaseObject): #TODO: Undefined objects here
  def __init__(self, entry):
    super().__init__(entry)
    for key in entry:
      if not (isinstance(key, dict)):
        self.__dict__[key] = entry[key]