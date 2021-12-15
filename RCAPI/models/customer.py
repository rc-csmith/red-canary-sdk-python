from RCAPI.models.general import PortalUser
from common import BaseObject

class SystemActivity(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['id'] = entry['id']
    for key in entry['attributes']:
      self.__dict__[key] = entry['attributes'][key]
    
class IgnoredTargetedProduct(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['id'] = entry['id']
    for key in entry['attributes']:
      self.__dict__[key] = entry['attributes'][key]

class IntelReporting(BaseObject): #TODO: Lots of objects with no models defined
  def __init__(self, entry):
    super().__init__(entry)
    for key in entry:
      self.__dict__[key] = entry[key]

class ExternalAlertSuppressionRule(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['id'] = entry['id']
    for key in entry['attributes']:
      if key == "created_by":
        self.__dict__[key] = PortalUser(entry['attributes'][key])
      else:
        self.__dict__[key] = entry['attributes'][key]

class ExternalAlertSource(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['id'] = entry['id']
    for key in entry['attributes']:
      if key == 'statistics':
        self.__dict__[key] = entry['attributes']['statistics'][key]
      else:
        self.__dict__[key] = entry['attributes'][key]
    for key in entry['relationships']:
      self.__dict__[key] = entry['relationships'][key]

class ExternalAlertSourcePlatform(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['id'] = entry['id']
    for key in entry['attributes']:
      self.__dict__[key] = entry['attributes'][key]

class ExternalAlert(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['id'] = entry['id']
    for key in entry['attributes']:
      self.__dict__[key] = entry['attributes'][key]
    for key in entry['relationships']:
      self.__dict__[key] = entry['relationships'][key]

