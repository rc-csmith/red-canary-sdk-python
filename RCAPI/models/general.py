from RCAPI.models.common import BaseObject
from RCAPI.models.primitives import OperatingSystemProcess, IpAddress, MacAddress

class ActivityMonitor(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)

    self.__dict__['id'] = entry.get('id')

    for key in entry.get('attribute'):
      self.__dict__[key] = (entry.get('attribute'))[key]

class ActivityMonitorMatch(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)

    self.__dict__['id'] = entry.get('id')
    
    for key in entry.get('attribute'):
      self.__dict__[key] = (entry.get('attribute'))[key]
    
    for key in entry['relationships']:
      self.__dict__[key] = Relationship(entry['relationships'][key])
  
class FileIntegrityMatch(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)

    self.__dict__['id'] = entry.get('id')
    
    for key in entry.get('attributes'): #TODO: endpoint and endpoint_user and undefined objects
      if key != 'activity_monitor':
        self.__dict__[key] = (entry.get('attributes'))[key]
      else:
        self.__dict__[key] = ActivityMonitor((entry.get('attributes'))[key])

class PortalUser(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    
    for key in entry.get('attributes'):
      self.__dict__[key] = (entry.get('attributes'))[key]

class DetectionSummary(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    
    for key in entry:
      if key == 'last_remediated_status':
        self.__dict__[key] = LastRemediatedStatus(entry[key])
      elif key != 'type':
        self.__dict__[key] = entry[key]

class LastRemediatedStatus(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)

    for key in entry:
      if key == 'marked_by':
        self.__dict__[key] = PortalUser(entry[key])
      else:
        self.__dict__[key] = entry[key]

class Detection(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)

    for key in entry:
      if key == 'attributes':
        self.__dict__['detection_details'] = DetectionDetails(entry[key])
      elif key == 'relationships':
        self.__dict__['affected_endpoint'] = Relationship(entry['relationships']['affected_endpoint'])
        self.__dict__['related_endpoint_user'] = Relationship(entry['relationships']['related_endpoint_user'])
      elif key != 'type':
        self.__dict__[key] = entry[key]

class DetectionDetails(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    
    for key in entry:
      if key == 'classification':
        self.__dict__[key] = Classification(entry[key])
      elif key == 'last_acknowledged_by':
        self.__dict__[key] = PortalUser(entry[key])
      elif key == 'last_remediated_status':
        self.__dict__[key] = LastRemediatedStatus(entry[key])
      else:
        self.__dict__[key] = entry[key]
  
class Classification(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['primary'] = entry['superclassification']
    self.__dict__['secondary'] = entry['subclassification']  

class Relationship(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    for key in entry:
      self.__dict__[key] = entry[key]

class Event(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['id'] = entry['id']
  
    for key in entry['attributes']:
      if key == 'latest_state':
        self.__dict__['updated_at'] = entry['attributes']['latest_state']['updated_at']
        self.__dict['state_reason'] = entry['attributes']['latest_state']['state_reason']
      elif key == 'process':
        self.__dict__[key] = OperatingSystemProcess(entry['attributes'][key])
      elif key == 'detectors':
        self.__dict__[key] = Detector(entry['attributes'][key])
      else:
        self.__dict__[key] = entry['attributes'][key]
  
    for key in entry['relationships']:
      self.__dict__[key] = Relationship(entry['relationships'][key])

class Detector(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['id'] = entry['id']

    for key in entry['attributes']:
      self.__dict__[key] = entry['attributes'][key]
    
    for key in entry['relationships']:
      self.__dict__[key] = entry['relationships'][key]

class AttackTactic(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)

    for key in entry['attributes']:
      self.__dict__[key] = entry['attributes'][key]
    for key in entry['relationships']:
      self.__dict__[key] = Relationship(entry['relationships'][key])

class AttackTechnique(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    for key in entry['attributes']:
      self.__dict__[key] = entry['attributes'][key]
    for key in entry['relationships']:
      self.__dict__[key] = Relationship(entry['relationships'][key])

class EndpointUser(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)

    self.__dict__['id'] = entry['id']
    for key in entry['attributes']:
      self.__dict__[key] = entry['attributes'][key]
  
class Endpoint(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['id'] = entry['id']
    for key in entry['attributes']:
      if key == 'endpoint_network_address':
        results = []
        for item in entry['attributes'][key]:
          results.append(EndpointNetworkAddress(item))
        self.__dict__[key] = results
      elif key == 'sensor':
        self.__dict__[key] = Sensor(entry['attributes'][key])
      else:
        self.__dict__[key] = entry['attributes'][key]

class EndpointNetworkAddress(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    for key in entry['attributes']:
      if key == 'mac_address':
        self.__dict__[key] = MacAddress(entry['attributes'][key])
      elif key == 'ip_address':
        self.__dict__[key] = IpAddress(entry['attributes'][key])
      else:
        self.__dict__[key] = entry['attributes'][key]
    for key in entry['relationships']:
      self.__dict__[key] = entry['relationships'][key]

class EndpointSensorMetadata(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['id'] = entry['id']
    for key in entry['attributes']:
      self.__dict__[key] = entry['attributes'][key]

class ExternalService(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['id'] = entry['id']
    for key in entry['attributes']:
      self.__dict__[key] = entry['attributes'][key]

class PortalRole(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    for key in entry['attributes']:
      self.__dict__[key] = entry['attributes'][key]

class ManagedPortalUser(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    for key in entry['attributes']:
      if key == 'current_roles':
        results = []
        for item in entry['attributes'][key]:
          results.append(PortalUserRole(item))
        self.__dict__[key] = results
      elif key == 'abilities':
        self.__dict__[key] = entry['attributes']['abilities'][key]
      else:
        self.__dict__[key] = entry['attributes'][key]

class PortalUserRole(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    for key in entry['attributes']:
      self.__dict__[key] = entry['attributes'][key]    

class Sensor(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry

class Report(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    for key in entry['attributes']:
      self.__dict__[key] = entry['attributes'][key]

class SuppressionRule(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['id'] = entry['id']
    for key in entry['attributes']:
      self.__dict__[key] = entry['attributes'][key]
    for key in entry['relationships']:
      self.__dict__[key] = Relationship(entry['relationships'][key])
    
class SharedFile(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['id'] = entry['id']
    for key in entry['attributes']:
      if key == 'creator':
        self.__dict__[key] = PortalUser(entry['attributes'][key])
      else:
        self.__dict__[key] = entry['attributes'][key]

class TargetedProduct(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['id'] = entry['id']
    for key in entry['attributes']: #TODO: atomic_indicators is an object
      self.__dict__[key] = entry['attributes'][key]
    for key in entry['relationships']:
      self.__dict__[key] = entry['relationships'][key]

class Indicator(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self.__dict__['id'] = entry['id']
    for key in entry['attributes']:
      self.__dict__[key] = entry['attributes'][key]

class StandardErrorResponse(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    try:
      self.__dict__['api_version'] = entry['meta']['api_version']
      self.__dict__['error_code'] = entry['error']['code']
      self.__dict__['error_message'] = entry['error']['message']
      self.__dict__['errors'] = entry['error']['errors']
    except: #If it fails, do nothing
      True