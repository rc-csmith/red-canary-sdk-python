"""
General
"""
from typing import Optional, Union, Any
from .common import SelectableObject, BaseObject, Resource, Collection
from .primitives import OperatingSystemProcess, IpAddress, MacAddress, File, Domain, RegistryKey

class SuppressionRule(SelectableObject):
  """
  Suppression Rule object
  """
  def __init__(self, entry=None, client=None):
    if client:
      self.client = client

    if entry:
      super().__init__(entry)

  def get_list(self):
    """
    Get a list of suppression rules
    """
    if hasattr(self,'client'):
      return SuppressionRuleService(self.client).list_suppression_rules()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")

  def get_item(self, unique_id: str):
    """
    Get a single suppression rule
    
    Parameters
    ----------
    unique_id : str
      unique id for the suppression rule
    """
    if hasattr(self,'client'):
      return SuppressionRuleService(self.client).get(int(unique_id))
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

  def delete(self):
    """
    Delete current suppression rule
    """
    try:
      return SuppressionRuleService(self.client).delete(self.id)
    except Exception as e:
      raise SyntaxError(e)

class SuppressionRuleResource(Resource):
  """
  Suppression Rule resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, SuppressionRule, client=client)

class SuppressionRuleCollection(Collection):
  """
  Suppression Rule collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, SuppressionRule, client=client)

class TelemetrySearch(BaseObject):
  """
  Telemetry Search object
  """

class TelemetrySearchCollection(Collection):
  """
  Telemetry Search collection
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, TelemetrySearch, client=client)

class ActivityMonitor(SelectableObject):
  """
  Activity Monitor object
  """
  def __init__(self, entry=None, client=None):
    if client:
      self.client = client

    if entry:
      super().__init__(entry, {})
  
  def get_list(self):
    """
    Get a list of activity monitors
    """
    if hasattr(self,'client'):
      return ActivityMonitorService(self.client).list_monitors()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")
  
  def get_item(self, unique_id: str):
    """
    Get a single activity monitor
    
    Parameters
    ----------
    unique_id : str
      unique id for the activity monitor
    """
    if hasattr(self,'client'):
      return ActivityMonitorService(self.client).get(int(unique_id))
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

  def deactivate(self):
    """
    Deactivate current activity monitor
  """
    try:
      return ActivityMonitorService(self.client).deactivate(self.id)
    except Exception as e:
      raise SyntaxError(e)
  
  def create_item(self, params: Optional[str] = None):
    """
    Create a new activity monitor
    
    Parameters
    ----------
    params : dict
      parameters for the new activity monitor
    """
    if hasattr(self,'client'):
      return ActivityMonitorService(self.client).create(params)
    else:
      raise SyntaxError(f"Class {self.__class__.name__} cannot be used to create a new item")
  
  def list_matches(self):
    """
    List matches for the current activity monitor
    """
    try:
      return ActivityMonitorService(self.client).list_matches(self.id)
    except Exception as e:
      raise SyntaxError(e)

class ActivityMonitorMatch(SelectableObject):
  """
  Activity Monitor Match object
  Includes affected_endpoint and related_endpoint_user
  """
  def __init__(self, entry=None, client=None):
    type_mapping = {
      'affected_endpoint': ResourceRelationship,
      'related_endpoint_user': ResourceRelationship
    }
    if client:
      self.client = client

    if entry:
      super().__init__(entry, type_mapping)

  def get_list(self):
    """
    Get a list of activity monitor matches
    """
    if hasattr(self,'client'):
      return ActivityMonitorService(self.client).list_all_matches()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")

  def get_item(self, unique_id: str):
    """
    Get a single activity monitor match
    """
    if hasattr(self,'client'):
      temp_list = ActivityMonitorService(self.client).list_all_matches()
      for item in temp_list:
        if str(item.id) == unique_id:
          return item
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

class FileIntegrityMatch(SelectableObject): #TODO: Contains endpoint and endpoint_user and undefinied objects
  """
  File Integrity Match object
  Includes ActivityMonitor
  """
  def __init__(self, entry=None, client=None):
    type_mapping = {
      'activity_monitor': ActivityMonitor
    }
    if client:
      self.client = client

    if entry:
      super().__init__(entry, type_mapping)

  def get_list(self):
    """
    Get a list of file integrity matches
    """
    if hasattr(self,'client'):
      return ActivityMonitorService(self.client).list_fim_matches()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")

  def get_item(self, unique_id: str):
    """
    Get a single file integrity match
    
    Parameters
    ----------
    unique_id : str
      unique id for the file integrity match
    """
    if hasattr(self,'client'):
      temp_list = ActivityMonitorService(self.client).list_fim_matches()
      for item in temp_list:
        if str(item.id) == unique_id:
          return item
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

class PortalUser(BaseObject):
  """
  Portal User object
  """

class DetectionSummary(BaseObject):
  """
  Detection Summary object
  Includes LastRemediatedStatus
  """
  def __init__(self, entry):
    type_mapping = {
      'last_remediated_status': LastRemediatedStatus
    }
    super().__init__(entry, type_mapping)

class LastRemediatedStatus(BaseObject):
  """
  Last Remediated Status object
  Includes PortalUser
  """
  def __init__(self, entry):
    type_mapping = {
      'marked_by': PortalUser
    }
    super().__init__(entry, type_mapping)

class Detection(SelectableObject):
  """
  Detection object
  Includes DetectionDetails and ResourceRelationship
  """
  def __init__(self, entry=None, client=None):
    type_mapping = {
      'detection_details': DetectionDetails,
      'affected_endpoint': ResourceRelationship,
      'related_endpoint_user': ResourceRelationship
    }
    if client:
      self.client = client

    if entry:
      super().__init__(entry, type_mapping)

  def get_list(self):
    """
    Get a list of detections
    """
    if hasattr(self,'client'):
      return DetectionService(self.client).list_detections()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")
  
  def get_item(self, unique_id: str):
    """
    Get a single detection
    
    Parameters
    ----------
    unique_id : str
      unique id for the detection
    """
    if hasattr(self,'client'):
      return DetectionService(self.client).get(int(unique_id))
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")
  
  def list_events(self):
    """
    List events for the current detection
    """
    try:
      return DetectionService(self.client).list_events(self.id)
    except Exception as e:
      raise SyntaxError(e)
  
  def list_iocs(self):
    """
    List IOCs for the current detection
  """
    try:
      return DetectionService(self.client).list_iocs(self.id)
    except Exception as e:
      raise SyntaxError(e)
  
  def update_remediation_status(self, params):
    """
    Update the remediation status for the current detection

    Parameters
    ----------
    params : dict
      parameters for the remediation status
    """
    try:
      return DetectionService(self.client).update_remediation_status(self.id, params)
    except Exception as e:
      raise SyntaxError(e)
  
  def mark_acknowledged(self):
    """
    Mark the current detection as acknowledged
  """
    try:
      return DetectionService(self.client).mark_acknowledged(self.id)
    except Exception as e:
      raise SyntaxError(e)
  
  def list_timeline(self):
    """
    List the timeline for the current detection
  """
    try:
      return DetectionService(self.client).list_timeline(self.id)
    except Exception as e:
      raise SyntaxError(e)
  
  def list_detectors(self):
    """
    List detectors for the current detection
    """
    try:
      return DetectionService(self.client).list_detectors(self.id)
    except Exception as e:
      raise SyntaxError(e)
  
  def list_related(self):
    """
    List related detections for the current detection
    """
    try:
      return DetectionService(self.client).list_related(self.id)
    except Exception as e:
      raise SyntaxError(e)

class DetectionDetails(BaseObject):
  """
  Detection Details object
  Includes Classification and PortalUser and LastRemediatedStatus
  """
  def __init__(self, entry):
    type_mapping = {
      'classification': Classification,
      'last_acknowledged_by': PortalUser,
      'last_remediated_status': LastRemediatedStatus
    }
    super().__init__(entry, type_mapping)

class Classification(BaseObject):
  """
  Classification object
  """

class Event(SelectableObject):
  """
  Event object
  Includes LatestState, OperatingSystemProcess, ResourceRelationship, and Detector
  """
  def __init__(self, entry=None, client=None):
    type_mapping = {
      'latest_state': LatestState,
      'process': OperatingSystemProcess,
      'endpoint': ResourceRelationship,
      'endpoint_user': ResourceRelationship,
      'detection_confirmed_in': ResourceRelationship,
      'external_service': ResourceRelationship,
      'detectors': Detector
    }
    self.client = client

    if entry:
      super().__init__(entry, type_mapping)
  
  def get_list(self):
    """
    Get a list of events
    """
    if self.client:
      return EventService(self.client).list_events()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")

  def get_item(self, unique_id: str):
    """
    Get a single event

    Parameters
    ----------
    unique_id : str
      unique id for the event
    """
    if self.client:
      return EventService(self.client).get(int(unique_id))
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

  def mark_activity_as_ioc(self, activity_id: int, activity_path: str = None, ioc_type: str = None, override_greylist: bool = False):
    """
    Mark an activity as an IOC for the current event

    Parameters
    ----------
    activity_id : int
      activity id
    activity_path : str
      activity path
    ioc_type : str
      IOC type
    override_greylist : bool
      override greylist
    """
    try:
      return EventService(self.client).mark_activity_as_ioc(self.id, activity_id, activity_path, ioc_type, override_greylist)
    except Exception as e:
      raise SyntaxError(e)
  
  def mark_activity_as_relevant(self, activity_id: int, activity_path: str = None):
    """
    Mark an activity as relevant for the current event

    Parameters
    ----------
    activity_id : int
      activity id
    activity_path : str
      activity path
    """
    try:
      return EventService(self.client).mark_activity_as_relevant(self.id, activity_id, activity_path)
    except Exception as e:
      raise SyntaxError(e)

  def get_activity(self, activity_id: int):
    """
    Get an activity for the current event
    
    Parameters
    ----------
    activity_id : int
      activity id
    """
    try:
      return EventService(self.client).get_activity(self.id, activity_id)
    except Exception as e:
      raise SyntaxError(e)
    
  def list_cached_activity_enrichments(self):
    """
    List cached activity enrichments for the current event
    """
    try:
      return EventService(self.client).list_cached_activity_enrichments(self.id)
    except Exception as e:
      raise SyntaxError(e)
  
  def list_timeline_activites(self):
    """
    List timeline activities for the current event
    """
    try:
      return EventService(self.client).list_timeline_activities(self.id)
    except Exception as e:
      raise SyntaxError(e)
    
  def delete_timeline_activity(self, timeline_activity_id: int):
    """
    Delete a timeline activity for the current event
    
    Parameters
    ----------
    timeline_activity_id : int
      timeline activity id
    """
    try:
      return EventService(self.client).delete_timeline_activity(self.id, timeline_activity_id)
    except Exception as e:
      raise SyntaxError(e)

class EventResource(Resource):
  """
  Event resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, Event, client=client)

class EventCollection(Collection):
  """
  Event collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, Event, client=client)

class EventActivity(BaseObject):
  """
  Event Activity object
  """

class EventActivityResource(Resource):
  """
  Event Activity resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, EventActivity, client=client)

class EventTimelineActivity(BaseObject):
  """
  Event Timeline Activity object
  """

class LatestState(BaseObject):
  """
  Latest State object
  """

class Detector(BaseObject):
  """
  Detector object
  Includes ResourceRelationship
  """
  def __init__(self, entry):
    type_mapping = {
      'attack_techniques': ResourceRelationship
    }
    super().__init__(entry,type_mapping)

class AttackTactic(SelectableObject):
  """
  Attack Tactic object
  Includes ResourceRelationship
  """
  def __init__(self, entry=None, client=None):
    type_mapping = {
      'attack_techniques': ResourceRelationship
    }
    if client:
      self.client = client

    if entry:
      super().__init__(entry, type_mapping)
  
  def get_list(self):
    """
    Get a list of attack tactics
    """
    if hasattr(self,'client'):
      return DetectorService(self.client).list_tactics()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")

  def get_item(self, unique_id: str):
    """
    Get a single attack tactic
    
    Parameters
    ----------
    unique_id : str
      unique id for the attack tactic
    """
    if hasattr(self,'client'):
      return DetectorService(self.client).get_tactic(int(unique_id))
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

class AttackTechnique(SelectableObject):
  """
  Attack Technique object
  """
  def __init__(self, entry=None, client=None):
    type_mapping = {
      'attack_techniques': ResourceRelationship
    }
    if client:
      self.client = client

    if entry:
      super().__init__(entry, type_mapping)
  
  def get_list(self):
    """
    Get a list of attack techniques
    """
    if hasattr(self,'client'):
      return DetectorService(self.client).list_techniques()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")
  
  def get_item(self, unique_id: str):
    """
    Get a single attack technique
    
    Parameters
    ----------
    unique_id : str
      unique id for the attack technique"""
    if hasattr(self,'client'):
      return DetectorService(self.client).get_technique(int(unique_id))
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

class ReportingTag(SelectableObject):
  """
  Reporting Tag object
  """

  def __init__(self, entry = None, client = None):        
    if client:
      self.client = client

    if entry:
      self.__dict__['name'] = entry['name']
      self.__dict__['value'] = entry['value']

  def get_list(self):
    """
    Get a list of reporting tags
    """
    if hasattr(self, 'client'):
      return EndpointService(self.client).list_reporting_tags()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")
  
  def get_item(self, unique_id: str):
    """
    Get a single reporting tag
    
    Parameters
    ----------
    unique_id : str
      unique id for the reporting tag"""
    if hasattr(self, 'client'):
      temp = EndpointService(self.client).list_reporting_tags()
      for item in temp:
        if item.name == unique_id:
          return item
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

class ReportingTagCollection(object):
  """
  Reporting Tag collection object

  Note: This is not formatted the same as other collections due to API weirdness
  """

  def __init__(self, entry):
    self.__dict__['data'] = []
    for name in entry:
      for value in entry[name]:
        self.__dict__['data'].append(ReportingTag(entry={'name':name, 'value':value}))

class EndpointUser(SelectableObject):
  """
  Endpoint User object
  """

  def __init__(self, entry=None, client=None):
    if client:
      self.client = client

    if entry:
      super().__init__(entry, {})

  def get_list(self):
    """
    Get a list of endpoint users
    """
    if hasattr(self,'client'):
      return EndpointUserService(self.client).list_users()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")

  def get_item(self, unique_id: str):
    """
    Get a single endpoint user
    
    Parameters
    ----------
    unique_id : str
      unique id for the endpoint user
    """
    if hasattr(self,'client'):
      return EndpointUserService(self.client).get(int(unique_id))
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

  def remove_reporting_tag(self, reporting_tag: ReportingTag):  #TODO: Need to confirm this is the right format
    """
    Remove a reporting tag from the current endpoint user
    
    Parameters
    ----------
    reporting_tag : ReportingTag
      reporting tag to remove
    """
    try:
      return EndpointUserService(self.client).remove_reporting_tag(reporting_tag.name, self.id)
    except Exception as e:
      raise SyntaxError(e)
  
  def add_reporting_tag(self, reporting_tag: ReportingTag, params: dict):
    """
    Add a reporting tag to the current endpoint user
    
    Parameters
    ----------
    reporting_tag : ReportingTag
      reporting tag to add
    params : dict
      parameters for the reporting tag
    """
    try:
      return EndpointUserService(self.client).add_reporting_tag(reporting_tag.name, self.id, params)
    except Exception as e:
      raise SyntaxError(e)
  
  def list_system_activities(self, params: Optional[dict]):
    """
    List system activities for the current endpoint user
    
    Parameters
    ----------
    params : dict
      parameters for the system activities
    """
    try:
      return EndpointUserService(self.client).list_system_activities(self.id, params)
    except Exception as e:
      raise SyntaxError(e)

class Endpoint(SelectableObject):
  """
  Endpoint object
  Includes Sensor
  """
  def __init__(self, entry=None, client=None):
    type_mapping = {
      'sensor': Sensor
    }
    if client:
      self.client = client

    if entry:
      if 'endpoint_network_address' in entry['attributes']:
        results = []
        for item in entry['attributes'][['endpoint_network_address']]:
          results.append(EndpointNetworkAddress(item))
        entry['attributes']['endpoint_network_address'] = results
      super().__init__(entry, type_mapping)

  def get_list(self):
    """
    Get a list of endpoints
    """
    if hasattr(self,'client'):
      return EndpointService(self.client).list_endpoints()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")

  def get_item(self, unique_id: str):
    """
    Get a single endpoint
    
    Parameters
    ----------
    unique_id : str
      unique id for the endpoint
    """
    if hasattr(self,'client'):
      return EndpointService(self.client).get(int(unique_id))
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")
  
  def deisolate(self):
    """
    Deisolate the current endpoint
    """
    params = {'ids':[self.id]}
    try:
      return EndpointService(self.client).deisolate(params)
    except Exception as e:
      raise SyntaxError(e)
  
  def isolate(self):
    """
    Isolate the current endpoint
    """
    params = {'ids':[self.id]}
    try:
      return EndpointService(self.client).isolate(params)
    except Exception as e:
      raise SyntaxError(e)
  
  def decommission(self, uninstall: bool = False):
    """
    Decommission the current endpoint
    """
    try:
      return EndpointService(self.client).decommission(self.id, uninstall)
    except Exception as e:
      raise SyntaxError(e)
  
  def reinstate(self):
    """
    Reinstate the current endpoint
    """
    params = {'ids':[self.id]}
    try:
      return EndpointService(self.client).reinstate(params)
    except Exception as e:
      raise SyntaxError(e)
  
  def deactivate_safe_mode(self):
    """
    Deactivate safe mode for the current endpoint
    """
    params = {'ids':[self.id]}
    try:
      return EndpointService(self.client).deactivate_safe_mode(params)
    except Exception as e:
      raise SyntaxError(e)
  
  def activate_safe_mode(self):
    """
    Activate safe mode for the current endpoint
    """
    params = {'ids':[self.id]}
    try:
      return EndpointService(self.client).activate_safe_mode(params)
    except Exception as e:
      raise SyntaxError(e)
  
  def remove_reporting_tag(self, reporting_tag: ReportingTag):
    """
    Remove a reporting tag from the current endpoint
    
    Parameters
    ----------
    reporting_tag : ReportingTag
      reporting tag to remove
    """
    try:
      return EndpointService(self.client).remove_reporting_tag(self.id, reporting_tag.name)
    except Exception as e:
      raise SyntaxError(e)
  
  def add_reporting_tag(self, reporting_tag: ReportingTag, params):
    """
    Add a reporting tag to the current endpoint
    
    Parameters
    ----------
    reporting_tag : ReportingTag
      reporting tag to add
    params : dict
      parameters for the reporting tag
    """
    try:
      return EndpointService(self.client).add_reporting_tag(self.id, reporting_tag.name, params)
    except Exception as e:
      raise SyntaxError(e)
  
  def list_endpoint_users(self, fromdate: Optional[str]=None, include_system_accounts: bool = True):
    """
    List endpoint users for the current endpoint
    
    Parameters
    ----------
    fromdate : str
      date to start from
    include_system_accounts : bool
      include system accounts
    """
    try:
      return EndpointService(self.client).list_endpoint_users(self.id, fromdate, include_system_accounts)
    except Exception as e:
      raise SyntaxError(e)
  
  def list_system_activities(self):
    """
    List system activities for the current endpoint
    """
    try:
      return EndpointService(self.client).list_system_activities(self.id)
    except Exception as e:
      raise SyntaxError(e)

class EndpointNetworkAddress(BaseObject):
  """
  Endpoint Network Address object
  """
  def __init__(self, entry):
    type_mapping = {
      'mac_address': MacAddress,
      'ip_address': IpAddress,
      'endpoint': ResourceRelationship
    }
    super().__init__(entry, type_mapping)

class EndpointSensorMetadata(BaseObject):
  """
  Endpoint Sensor Metadata object
  """

class ExternalService(SelectableObject):
  """
  External Service object
  """

  def __init__(self, entry=None, client=None):
    if client:
      self.client = client

    if entry:
      super().__init__(entry)
    
  def get_list(self):
    """
    Get a list of external services
    """
    if hasattr(self,'client'):
      return ExternalServicesService(self.client).list()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")

  def get_item(self, unique_id: str):
    """
    Get a single external service
    
    Parameters
    ----------
    unique_id : str
      unique id for the external service
    """
    if hasattr(self, 'client'):
      return ExternalServicesService(self.client).get(external_service_uuid=unique_id)
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

  def get_aws_list(self):
    """
    Get a list of AWS services
    """
    if hasattr(self, 'client'):
      return ExternalServicesService(self.client).list_aws_services()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")

  def get_aws_item(self, unique_id: str):
    """
    Get a single AWS service
    
    Parameters
    ----------
    unique_id : str
      unique id for the AWS service
    """
    if hasattr(self, 'client'):
      return ExternalServicesService(self.client).get_aws_service(external_service_uuid=unique_id)
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

  def create_aws_item(self, params: dict):
    """
    Create a new AWS service
    
    Parameters
    ----------
    params : dict
      parameters for the new AWS service
    """
    if hasattr(self, 'client'):
      return ExternalServicesService(self.client).create_aws_service(params)
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to create a new item")

  def update_aws_item(self, aws_account_id: str = None, description: str = None, aws_assumed_role_arn: str = None):
    """
    Update the current AWS service
    
    Parameters
    ----------
    aws_account_id : str
      AWS account id
    description : str
      description for the AWS service
    aws_assumed_role_arn : str
      AWS assumed role ARN
    """
    try:
      return ExternalServicesService(self.client).update_aws_service(self.id, aws_account_id, description, aws_assumed_role_arn)
    except Exception as e:
      raise SyntaxError(e)
  
  def delete_aws_item(self):
    """
    Delete the current AWS service
    """
    try:
      return ExternalServicesService(self.client).delete_aws_service(self.id)
    except Exception as e:
      raise SyntaxError(e)

class ExternalServiceResource(Resource):
  """
  External Service resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, ExternalService, client=client)

def ExternalServiceCollection(Collection):
  """
  External Service collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, ExternalService, client=client)

class ManagedPortalUserCollection(Collection):
  """
  Managed Portal User collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, ManagedPortalUser, client=client)

class PortalRole(SelectableObject):
  """
  Portal Role object
  """
  def __init__(self, entry=None, client=None):
    if client:
      self.client = client

    if entry:
      super().__init__(entry, {})

  def get_list(self):
    """
    Get a list of portal roles
    """
    if hasattr(self,'client'):
      return PortalRoleService(self.client).list()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")
  
  def get_item(self, unique_id: str):
    """
    Get a single portal role

    Parameters
    ----------
    unique_id : str
      unique id for the portal role
    """
    if hasattr(self,'client'):
      temp_list = PortalRoleService(self.client).list()
      for item in temp_list:
        if item.name == unique_id:
          return item
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

class PortalUserRole(BaseObject):
  """
  Portal User Role object
  """

class ManagedPortalUser(SelectableObject):
  """
  Managed Portal User object
  """
  def __init__(self, entry=None, client=None):
    type_mapping = {
      'abilities': Abilities
    }
    if client:
      self.client = client

    if entry:
      if 'current_roles' in entry['attributes']:
        results = []
        for item in entry['attributes']['current_roles']:
          results.append(PortalUserRole(item))
        entry['attributes']['current_roles'] = results
      super().__init__(entry, type_mapping)

  def get_list(self):
    """
    Get a list of managed portal users
    """
    if hasattr(self,'client'):
      return ManagedPortalUserService(self.client).list_users()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")

  def get_item(self, unique_id: str):
    """
    Get a single managed portal user
    
    Parameters
    ----------
    unique_id : str 
      unique id for the managed portal user
    """
    if hasattr(self,'client'):
      return ManagedPortalUserService(self.client).get(int(unique_id))
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")
  
  def create_item(self, params: dict):
    """
    Create a new managed portal user
    
    Parameters
    ----------
    params : dict
      parameters for the new managed portal user
    """
    if hasattr(self,'client'):
      return ManagedPortalUserService(self.client).invite(params['email'])
    else:
      raise SyntaxError(f" Class {self.__class__.__name__} cannot be used to create a new item")

  def delete(self):
    """
    Delete the current managed portal user
  """
    try:
      return ManagedPortalUserService(self.client).delete(self.id)
    except Exception as e:
      raise SyntaxError(e)
  
  def disable_mfa(self):
    """
    Disable MFA for the current managed portal user
    """
    try:
      return ManagedPortalUserService(self.client).disable_mfa(self.id)
    except Exception as e:
      raise SyntaxError(e)
  
  def uninvite(self):
    """
    Uninvite the current managed portal user
    """
    try:
      return ManagedPortalUserService(self.client).uninvite(self.id)
    except Exception as e:
      raise SyntaxError(e)
  
  def reinvite(self):
    """
    Reinvite the current managed portal user
    """
    try:
      return ManagedPortalUserService(self.client).reinvite(self.id)
    except Exception as e:
      raise SyntaxError(e)
  
  def add_role(self, role: PortalRole):
    """
    Add a role to the current managed portal user
    """
    try:
      return ManagedPortalUserService(self.client).add_role(role.name, self.id)
    except Exception as e:
      raise SyntaxError(e)

  def delete_role(self, role: PortalRole):
    """
    Delete a role from the current managed portal user
    """
    try:
      return ManagedPortalUserService(self.client).delete_role(role.name, self.id)
    except Exception as e:
      raise SyntaxError(e)

class Abilities(BaseObject):
  """
  Abilities object
  """

class Sensor(BaseObject):
  """
  Sensor object
  """

class Report(SelectableObject):
  """
  Report object
  """

  def __init__(self, entry=None, client=None):
    if client:
      self.client=client

    if entry:
      super().__init__(entry, {})
  
  def get_list(self):
    """
    Get a list of reports
    """
    if hasattr(self,'client'):
      return ReportLibrary(self.client).list()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")
  
  def get_item(self, unique_id: str):
    """
    Get a single report
    
    Parameters
    ----------
    unique_id : str
      unique id for the report
    """
    if hasattr(self,'client'):
      return ReportLibrary(self.client).get(int(unique_id))
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")
  
  def unfavorite(self):
    """
    Unfavorite the current report
    """
    try:
      return ReportLibrary(self.client).unfavorite(self.name)
    except Exception as e:
      raise SyntaxError(e)

  def favorite(self):
    """
    Favorite the current report
    """
    try:
      return ReportLibrary(self.client).favorite(self.name)
    except Exception as e:
      raise SyntaxError(e)

class SharedFile(SelectableObject):
  """
  Shared File object
  """
  def __init__(self, entry=None, client=None):
    type_mapping = {
      'creator': PortalUser
    }
    if client:
      self.client = client

    if entry:
      super().__init__(entry, type_mapping)

  def get_list(self):
    """
    Get a list of shared files
    """
    if hasattr(self,'client'):
      return SharedFileService(self.client).list_sharedfiles()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")

  def get_item(self, unique_id: str):
    """
    Get a single shared file
    
    Parameters
    ----------
    unique_id : str
      unique id for the shared file
    """
    if hasattr(self,'client'):
      return SharedFileService(self.client).get(int(unique_id))
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

class TargetedProduct(SelectableObject):
  """
  Targeted Product object
  """
  def __init__(self, entry=None, client=None):
    type_mapping = {
      'customer_ignored_targeted_products': ResourceRelationship
    }
    if client:
      self.client = client

    if entry:
      super().__init__(entry, type_mapping)

  def get_list(self):
    """
    Get a list of targeted products
    """
    if hasattr(self,'client'):
      return TargetedProductService(self.client).list_products()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")
  
  def get_item(self, unique_id: str):
    """
    Get a single targeted product
    
    Parameters
    ----------
    unique_id : str
      unique id for the targeted product
    """
    if hasattr(self,'client'):
      temp_list = TargetedProductService(self.client).list_products()
      for item in temp_list:
        if str(item.id) == unique_id:
          return item
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

class Indicator(BaseObject):
  """
  Indicator object
  """

class StandardErrorResponse(BaseObject): #TODO: May need to verify this will work as expected
  """
  Standard Error Response object
  """

class StandardSuccessResponse(BaseObject):
  """
  Standard Success Response object
  """

class RequestedCsvResponse(BaseObject):
  """
  REquested CSV Response object
  """

class EndpointCollection(Collection):
  """
  Endpoint collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, Endpoint, client=client)

class EndpointResource(Resource):
  """
  Endpoint resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, Endpoint, client=client)

class EndpointUserCollection(Collection):
  """
  Endpoint User collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, EndpointUser, client=client)

class ResourceRelationship(BaseObject):
  """
  Resource Relationship object
  """

class ResourceLink(BaseObject):
  """
  Resource Link object
  """

class EndpointUserResource(Resource):
  """
  Endpoint User resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, EndpointUser, client=client)

class PortalRoleCollection(Collection):
  """
  Portal Role collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, PortalRole, client=client)

class PortalUserRoleCollection(Collection):
  """
  Portal User Role collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, PortalUserRole, client=client)

class ReportResource(Resource):
  """
  Report resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, Report, client=client)

class SharedFileCollection(Collection):
  """
  Shared File collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, SharedFile, client=client)

class SharedFileResource(Resource):
  """
  Shared File resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, SharedFile, client=client)

class TargetedProductCollection(Collection):
  """
  Targeted Product collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, TargetedProduct, client=client)

class TargetedProductResource(Resource):
  """
  Targeted Product resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, TargetedProduct, client=client)

class ActivityMonitorResource(Resource):
  """
  Activity Monitor resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, ActivityMonitor, client=client)

class ActivityMonitorCollection(Collection):
  """
  Activity Monitor collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry,ActivityMonitor, client=client)

class ActivityMonitorMatchCollection(Collection):
  """
  Activity Monitor Match collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry,ActivityMonitorMatch, client=client)

class FileIntegrityMonitoringMatchCollection(Collection):
  """
  File Integrity Monitoring Match collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry,FileIntegrityMatch, client=client)

class DownloadResponse(BaseObject):
  """
  Download Response object
  """

class IndicatorOfCompromiseCollection(BaseObject):
  """
  Indicator of Compromise collection object
  """
  def __init__(self, entry):
    type_mapping = {
      'files': File,
      'domain_names': Domain,
      'ip_addresses': IpAddress,
      'registry_keys': RegistryKey
    }
    super().__init__(entry, type_mapping)

class DetectionSummaryCollection(Collection):
  """
  Detection Summary collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry,DetectionSummary, client=client)

class DetectionCollection(Collection):
  """
  Detection collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry,Detection, client=client)

class DetectionResource(Resource):
  """
  Detection resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry,Detection, client=client)

class DetectorCollection(Collection):
  """
  Detector collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry,Detector, client=client)

class AttackTacticResource(Resource):
  """
  Attack Tactic resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry,AttackTactic, client=client)

class AttackTacticCollection(Collection):
  """
  Attack Tactic collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry,AttackTactic, client=client)

class AttackTechniqueResource(Resource):
  """
  Attack Technique resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry,AttackTechnique, client=client)

class AttackTechniqueCollection(Collection):
  """
  Attack Technique collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry,AttackTechnique, client=client)

class FileIntegrityMatchCollection(Collection):
  """
  File Integrity Match collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, FileIntegrityMatch, client=client)

class ReportingTagAssociation(SelectableObject):
  """
  Reporting Tag Association object
  """

  def __init__(self, entry=None, client=None):
    temp = {'data':entry}
    if client:
      self.client = client
    if entry:
      super().__init__(temp)

  def get_list(self):
    """
    Get a list of reporting tag associations
    """
    if hasattr(self,'client'):
      return EndpointService(self.client).list_reporting_tags_associations()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")

  def get_item(self, unique_id: str):
    """
    Get a single reporting tag association
    
    Parameters
    ----------
    unique_id : str
      unique id for the reporting tag association
    """
    if hasattr(self,'client'):
      temp = EndpointService(self.client).list_reporting_tags_associations()
      for item in temp:
        if item.name == unique_id:
          return item
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

class ReportingTagAssociationCollection(Collection):
  """
  Reporting Tag Association Collection object
  """
  
  def __init__(self, entry, client=None):
    super().__init__(entry,ReportingTagAssociation, client=client)

class ActivityMonitorService(object):
  """
  Activity Monitor class
  """
  def __init__(self, client):
    self.client = client

  def create(self, params: Optional[str] = None) -> ActivityMonitor:
    """
    Create a new activity monitor

    Parameters
    ----------
    params : dir
      attributes of the new activity monitor
      if not provided or incomplete, will throw an error
      required keys: activity_monitor[name]
                     activity_monitor[type]
                     activity_monitor[active]
                     activity_monitor[file_modification_types_monitored]
                     activity_monitor[file_paths_monitored]
    """
    required_keys = ['activity_monitor[name]',
                    'activity_monitor[type]',
                    'activity_monitor[active]',
                    'activity_monitor[file_modification_types_monitored]',
                    'activity_monitor[file_paths_monitored]']
    self.client.CheckRequiredKeys(required_keys, params, 'create_activity_monitor')

    result = self.client.call_api(method='post',service='/activity_monitors',params=params, object_type=ActivityMonitorResource)

    try:
      return result.data[0]
    except:
      return result

  def list_monitors(self, count_mode: bool = False) -> Union[int, list[ActivityMonitor]]:
    """
    List activity monitors

    Parameters
    ----------
    count_mode : bool
      show only a count and omit result details
    """

    params, object_type = self.client.CheckCountMode(count_mode, ActivityMonitorCollection)
    
    if count_mode:
      return self.client.call_api(method='get',service='/activity_monitors',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/activity_monitors', object_type=object_type, params=params)

  def list_matches(self, activity_monitor_id: int, count_mode: bool = False) -> Union[int, list[ActivityMonitorMatch]]:
    """
    List matches for an activity monitor

    Parameters
    ----------
    activity_monitor_id : int
      activity monitor id
    count_mode : bool
      show only a count and omit result details
    """

    params, object_type = self.client.CheckCountMode(count_mode, ActivityMonitorMatchCollection)

    if count_mode:
      return self.client.call_api(method='get',service=f'/activity_monitors/{activity_monitor_id}/matches',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service=f'/activity_monitors/{activity_monitor_id}/matches', object_type=object_type, params=params)

  def deactivate(self, activity_monitor_id: int) -> ActivityMonitor:
    """
    Deactivate activity monitor

    Parameters
    ----------
    activity_monitor_id : int
      activity monitor id
    """
    result = self.client.call_api(method='delete',service=f'/activity_monitors/{activity_monitor_id}', object_type=ActivityMonitorResource)

    try:
      return result.data[0]
    except:
      return result

  def get(self, activity_monitor_id: int) -> ActivityMonitor:
    """
    Get activity monitor

    Parameters
    ----------
    activity_monitor_id : int
      activity monitor id
    """
    result = self.client.call_api(method='get',service=f'/activity_monitors/{activity_monitor_id}', object_type=ActivityMonitorResource)

    try:
      return result.data[0]
    except:
      return result

  def list_all_matches(self, count_mode: bool = False) -> Union[int, list[ActivityMonitorMatch]]:
    """
    List all matches for all activity monitors

    Parameters
    ----------
    count_mode : bool
      show only a count and omit result details
    """

    params, object_type = self.client.CheckCountMode(count_mode, ActivityMonitorCollection)

    if count_mode:
      return self.client.call_api(method='get',service='/activity_monitor_matches',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/activity_monitor_matches', object_type=object_type, params=params)

  def list_fim_matches(self, count_mode: bool = False) -> Union[int, list[FileIntegrityMatch]]:
    """
    List all file integrity monitoring matches

    Parameters
    ----------
    count_mode : bool
      show only a count and omit result details
    """

    params, object_type = self.client.CheckCountMode(count_mode, FileIntegrityMatchCollection)

    if count_mode:
      return self.client.call_api(method='get',service='/activity_monitor_matches/file_integrity_monitoring_matches',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/activity_monitor_matches/file_integrity_monitoring_matches/json',
                                     object_type=object_type, params=params)

  def download_fim_matches(self) -> DownloadResponse:
    """
    Download all file integrity monitoring matches to CSV
    """
    return self.client.call_api(method='get',service='/activity_monitor_matches/file_integrity_monitoring_matches/csv',
                          object_type=DownloadResponse)

class DetectorService(object):
  """
  Detector class
  """
  def __init__(self, client):
    self.client = client

  def get_tactic(self, tactic_identifier: str) -> AttackTactic:
    """
    Get a tactic

    Parameters
    ----------
    tactic_identifier : str
      tactic identifier (capitalized)
      example: Persistence
    """
    result = self.client.call_api(method='get',service=f'/detectors/attack_tactics/{tactic_identifier}', object_type=AttackTacticResource)

    try:
      return result.data[0]
    except:
      return result

  def list_tactics(self, count_mode: bool = False) -> Union[int, list[AttackTactic]]:
    """
    List all tactics

    Parameters
    ----------
    count_mode : bool
      show only a count and omit result details
    """

    params, object_type = self.client.CheckCountMode(count_mode, AttackTacticCollection)

    if count_mode:
      return self.client.call_api(method='get',service='/detectors/attack_tactics',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/detectors/attack_tactics', object_type=object_type, params=params)

  def get_technique(self, technique_identifier: str) -> AttackTechnique:
    """
    Get a technique

    Parameters
    ----------
    technique_identifier : str
      technique identifier (uppercase)
      example: T1234
    """
    result = self.client.call_api(method='get',service=f'/detectors/attack_techniques/{technique_identifier}',
                           object_type=AttackTechniqueResource)
    
    try:
      return result.data[0]
    except:
      return result

  def list_techniques(self, count_mode: bool = False) -> Union[int, list[AttackTechnique]]:
    """
    List all techniques

    Parameters
    ----------
    count_mode : bool
      show only a count and omit result details
    """

    params, object_type = self.client.CheckCountMode(count_mode, AttackTechniqueCollection)

    if count_mode:
      return self.client.call_api(method='get',service='/detectors/attack_techniques',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/detectors/attack_techniques', object_type=object_type, params=params)

class EventService(object):
  """
  Event class
  """
  def __init__(self, client):
    self.client = client

  def list_events(self, since: str='', count_mode: bool=False) -> Union[int, list[Event]]:
    """
    List all events

    Parameters
    ----------
    since : str
      Start date for query
    count_mode : bool
      show only a count and omit result details
    """
    params, object_type = self.client.CheckCountMode(count_mode, EventCollection)
    if since != '':
      params['since'] = since

    if count_mode:
      return self.client.call_api(method='get',service='/events',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/events', object_type=object_type, params=params)

  def mark_activity_as_ioc(self, event_id: int, activity_id: int, activity_path: str = None, ioc_type: str = None, override_greylist: bool = False) -> EventActivity:
    # TODO: Need to verify this is the correct format
    """
    Mark activity as IOC

    Parameters
    ----------
    event_id : int
      event id
    activity_id : int
      event activity id
    activity_path : str
      comma separated activity path
    ioc_type : str
      ioc type
    override_greylist : bool
      override greylist
    """
    params = {}
    if activity_path:
      params['activity_path'] = activity_path
    if ioc_type:
      params['ioc_type'] = ioc_type
    if override_greylist:
      params['override_greylist'] = override_greylist

    result = self.client.call_api(method='post',service=f'/events/{event_id}/activities/{activity_id}/toggle_ioc',params=params, object_type=EventActivityResource)

    try:
      return result.data[0]
    except:
      return result

  def mark_activity_as_relevant(self, event_id: int, activity_id: int, activity_path: str = None) -> EventActivity:
    """
    Mark activity as relevant

    Parameters
    ----------
    event_id : int
      event id
    activity_id : int
      event activity id
    activity_path : str
      comma separated activity path
    """

    params = {}
    if activity_path:
      params['activity_path'] = activity_path
    
    result = self.client.call_api(method='post',service=f'/events/{event_id}/activities/{activity_id}/toggle_relevant', params=params, object_type=EventActivityResource)

    try:
      return result.data[0]
    except:
      return result

  def get_activity(self, event_id: int, activity_id: int) -> EventActivity:
    """
    Get activity

    Parameters
    ----------
    event_id : int
      event id
    activity_id : int
      event activity id
    """
    result = self.client.call_api(method='get',service=f'/events/{event_id}/activities/{activity_id}', object_type=EventActivityResource)

    try:
      return result.data[0]
    except:
      return result

  def get(self, event_id: int) -> Event:
    """
    Get event

    Parameters
    ----------
    event_id : int
      event id
    """
    result = self.client.call_api(method='get',service=f'/events/{event_id}', object_type=EventResource)

    try:
      return result.data[0]
    except:
      return result

  def download(self) -> RequestedCsvResponse:
    """
    Download CSV of analyzed events
    """
    return self.client.call_api(method='get',service='/events/analyzed/request_csv', object_type=RequestedCsvResponse)

  def list_cached_activity_enrichments(self, event_id: int) -> dict:
    # TODO: Need to verify this is the correct format
    """
    List cached activity enrichments

    Parameters
    ----------
    event_id : int
      event id
    """
    result = self.client.call_api(method='get',service=f'/events/{event_id}/cached_activity_enrichments', object_type=dict)

    try:
      return result.data
    except:
      return result

  def list_timeline_activities(self, event_id: int) -> list[EventTimelineActivity]:
    # TODO: Verify this is the correct format
    """
    List timeline activities

    Parameters
    ----------
    event_id : int
      event id
    """

    return self.client.RecurseList(service=f'/events/{event_id}/timeline_activities', object_type=EventTimelineActivity)

  def delete_timeline_activity(self, event_id: int, timeline_activity_id: int) -> EventTimelineActivity:
    """
    Delete timeline activity

    Parameters
    ----------
    event_id : int
      event id
    timeline_activity_id : int
      timeline activity id
    """

    result = self.client.call_api(method='delete',service=f'/events/{event_id}/timeline_activities/{timeline_activity_id}', object_type=EventTimelineActivity)

    try:
      return result.data[0]
    except:
      return result

class SharedFileService(object):
  """
  Shared File class
  """
  def __init__(self, client):
    self.client = client

  def list_sharedfiles(self, count_mode: bool = False) -> Union[int, list[SharedFile]]:
    """
    List all shared files

    Parameters
    ----------
    count_mode : bool
      show only a count and omit result details
    """

    params, object_type = self.client.CheckCountMode(count_mode, SharedFileCollection)

    if count_mode:
      return self.client.call_api(method='get',service='/shared_files',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/shared_files', object_type=object_type, params=params)

  def download(self, uuid: int) -> Any:
    """
    Download shared file

    Parameters
    ----------
    uuid : int
      unique id of shared file
    """
    return self.client.call_api(method='get',service=f'/shared_files/{uuid}/download')

  def get(self, uuid: int) -> SharedFile:
    """
    Get shared file

    Parameters
    ----------
    uuid : int
      unique id of shared file
    """
    result = self.client.call_api(method='get',service=f'/shared_files/{uuid}', object_type=SharedFileResource)
    
    try:
      return result.data[0]
    except:
      return result

class ManagedPortalUserService(object):
  """
  Managed Portal User Class
  """
  def __init__(self, client):
    self.client = client

  def list_users(self, count_mode: bool = False) -> Union[int, list[ManagedPortalUser]]:
    """
    List all managed portal users

    Parameters
    ----------
    count_mode : bool
      show only a count and omit result details
    """

    params, object_type = self.client.CheckCountMode(count_mode, ManagedPortalUserCollection)

    if count_mode:
      return self.client.call_api(method='get',service='/managed_portal_users',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/managed_portal_users', object_type=object_type, params=params)

  def delete(self, user_id: int) -> ManagedPortalUser:
    """
    Delete managed portal user

    Parameters
    ----------
    user_id : int
      user id
    """
    result = self.client.call_api(method='delete',service=f'/managed_portal_users/{user_id}', object_type=ManagedPortalUserCollection)

    if isinstance(result, ManagedPortalUserCollection):
      return StandardSuccessResponse({"msg":"Successfully deleted managed portal user"})
    else:
      return result

  def get(self, user_id: int) -> ManagedPortalUser:
    """
    Get managed portal user

    Parameters
    ----------
    user_id : int
      user id
    """
    result = self.client.call_api(method='get',service=f'/managed_portal_users/{user_id}', object_type=ManagedPortalUserCollection)

    try:
      return result.data[0]
    except:
      return result

  def disable_mfa(self, user_id: int) -> ManagedPortalUser:
    """
    Disable MFA for managed portal user

    Parameters
    ----------
    user_id : int
      user id
    """  
    result = self.client.call_api(method='delete',service=f'/managed_portal_users/{user_id}/mfa', object_type=ManagedPortalUserCollection)

    try:
      return result.data[0]
    except:
      return result

  def uninvite(self, user_id: int) -> ManagedPortalUserCollection:
    """
    Uninvite managed portal user

    Parameters
    ----------
    user_id : int
      user id
    """
    result = self.client.call_api(method='delete',service=f'/managed_portal_users/{user_id}/invite', object_type=ManagedPortalUserCollection)

  def reinvite(self, user_id: int) -> ManagedPortalUserCollection:
    """
    Reinvite managed portal user

    Parameters
    ----------
    user_id : int
      user id
    """
    return self.client.call_api(method='post',service=f'/managed_portal_users/{user_id}/invite', object_type=ManagedPortalUserCollection)

  def delete_role(self, role_name: str, user_id: int) -> PortalUserRoleCollection:
    """
    Delete role from managed portal user

    Parameters
    ----------
    role_name : str
      name of role
    user_id : int
      user id
    """
    result = self.client.call_api(method='delete',service=f'/managed_portal_users/{user_id}/role/{role_name}', object_type=PortalUserRoleCollection)

    if isinstance(result, PortalUserRoleCollection):
      return StandardSuccessResponse({"msg":"Successfully deleted portal user role"})
    else:
      return result

  def add_role(self, role_name: str, user_id: int) -> PortalUserRoleCollection:
    """
    Add role to managed portal user

    Parameters
    ----------
    role_name : str
      name of role
    user_id : int
      user id
    """
    return self.client.call_api(method='post',service=f'/managed_portal_users/{user_id}/role/{role_name}', object_type=PortalUserRoleCollection)

  def invite(self, email: str) -> ManagedPortalUser:
    """
    Invite a new user to the managed portal

    Parameters
    ----------
    email : str
      email of invited user
    """
    result = self.client.call_api(method='post',service=f'/managed_portal_users/{email}/invite', object_type=ManagedPortalUserCollection)

    try:
      return result.data[0]
    except:
      return result

class PortalRoleService(object):
  """
  Portal Role class
  """
  def __init__(self, client):
    self.client = client

  def list(self, count_mode: bool = False) -> PortalRoleCollection:
    """
    List portal roles

    Parameters
    ----------
    count_mode : bool
      show only a count and omit result details
    """

    params, object_type = self.client.CheckCountMode(count_mode, PortalRoleCollection)

    if count_mode:
      return self.client.call_api(method='get',service='/portal_roles',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/portal_roles', object_type=object_type, params=params)

class ReportLibrary(object):
  """
  Report Library class
  """
  def __init__(self, client):
    self.client = client

  def list(self) -> Report:
    """
    List all reports
    """
    return self.client.RecurseList(service='/reports', object_type=Report)

  def get(self, name: str) -> Report:
    """
    Get report

    Parameters
    ----------
    name : str
      name of report
    """
    result = self.client.call_api(method='get',service=f'/reports/{name}', object_type=ReportResource)

    try:
      return result.data[0]
    except:
      return result

  def unfavorite(self, name: str) -> Any:
    """
    Unfavorite report

    Parameters
    ----------
    name : str
      name of report
    """
    return self.client.call_api(method='delete',service=f'/reports/{name}/favorite')

  def favorite(self, name: str) -> Any:
    """
    Favorite report

    Parameters
    ----------
    name : str
      name of report
    """
    return self.client.call_api(method='put',service=f'/reports/{name}/favorite')

  def download_users_on_endpoints(self) -> RequestedCsvResponse:
    """
    Download CSV of users on endpoints
    """
    return self.client.call_api(method='get',service='/reports/users_on_endpoints/request_csv', object_type=RequestedCsvResponse)

  def download_detections_by_tactic(self) -> RequestedCsvResponse:
    """
    Download CSV of detections by observed tactic
    """
    return self.client.call_api(method='get',service='/reports/detections_by_observed_tactic/request_csv',
                           object_type=RequestedCsvResponse)

  def download_detections_by_technique(self) -> RequestedCsvResponse:
    """
    Download CSV of detections by observed technique
    """
    return self.client.call_api(method='get',service='/reports/detections_by_observed_technique/request_csv',
                           object_type=RequestedCsvResponse)

class IgnoredTargetedProduct(SelectableObject):
  """
  Ignored Target Product object
  """

  def __init__(self, entry=None, client=None):
    if client:
      self.client = client

    if entry:
      super().__init__(entry, {})
    
  def get_list(self):
    """
    Get a list of ignored targeted products
    """
    if hasattr(self,'client'):
      return TargetedProductService(self.client).list_ignored()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")

  def get_item(self, unique_id: str):
    """
    Get a single ignored targeted product
    
    Parameters
    ----------
    unique_id : str
      unique id for the ignored targeted product
    """
    if hasattr(self,'client'):
      temp_list = TargetedProductService(self.client).list_ignored()
      for item in temp_list:
        if str(item.id) == unique_id:
          return item
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")
  
  def create_item(self, params: dict):
    """
    Create a new ignored targeted product
    
    Parameters
    ----------
    params : dict
      dict containing key 'justification' and value of justification
    """
    full_params = {'targeted_product_id': self.id, 'justification': params['justification']}

    if hasattr(self,'client'):
      return TargetedProductService(self.client).create_ignored(full_params)
    else:
      raise SyntaxError(f"Class {self.__clas__.__name__} cannot be used to create a new item")
  
  def delete(self):
    """
    Delete current ignored targeted product
    """
    try:
      return TargetedProductService(self.client).delete_ignored(self.id)
    except Exception as e:
      raise SyntaxError(e)

class IgnoredTargetedProductCollection(Collection):
  """
  Ignored Targeted Product collection object
  """
  def __init__(self,entry, client=None):
    super().__init__(entry, IgnoredTargetedProduct, client=client)

class IgnoredTargetedProductResource(Resource):
  """
  Ignored Targeted Product resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, IgnoredTargetedProduct, client=client)

class TelemetrySearchService(object):
  """
  TelemetrySearch class
  """
  def __init__(self, client):
    self.client = client

  def download(self) -> RequestedCsvResponse:
    """
    Download audit logs to CSV
    """

    return self.client.call_api(method='get',service='/telemetry/request_csv', object_type=RequestedCsvResponse)

  def list(self, filter_query: str = '', count_mode: bool = False) -> Union[int, TelemetrySearchCollection]:
    """
    List telemetry

    Parameters
    ----------
    filter_query : str
      A string to fuzzy search by any telemetry attribute
    """

    params, object_type = self.client.CheckCountMode(count_mode, TelemetrySearchCollection)

    if filter_query != '':
      params['filter_query'] = filter_query

    if count_mode:
      return self.client.call_api(method='get',service='/telemetry/search',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/telemetry/search',
                                     object_type=object_type, params=params)

class EndpointUserService(object):
  """
  Endpoint User class
  """
  def __init__(self, client):
    self.client = client

  def list_users(self, query: str = '', count_mode: bool = False) -> Union[int, EndpointUserCollection]:
    """
    List endpoint users

    Parameters
    ----------
    query : str
      query string
    count_mode : bool
      show only a count and omit result details
    """
    params, object_type = self.client.CheckCountMode(count_mode, EndpointUserCollection)
    if query != '':
      params['q'] = query

    if count_mode:
      return self.client.call_api(method='get',service='/endpoint_users',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/endpoint_users', object_type=object_type, params=params)

  def get(self, endpoint_user_id: int) -> EndpointUser:
    """
    Get endpoint user

    Parameters
    ----------
    endpoint_user_id : int
      endpoint user id
    """
    result = self.client.call_api(method='get',service=f'/endpoint_users/{endpoint_user_id}', object_type=EndpointUserResource)

    try:
      return result.data[0]
    except:
      return result

  def remove_reporting_tag(self, reporting_tag: str, endpoint_user_id: int) -> Any:
    """
    Remove reporting tag from endpoint user

    Parameters
    ----------
    reporting_tag : str
      reporting tag name
    endpoint_user_id : int
      endpoint user id
    """
    return self.client.call_api(method='delete',service=f'/endpoint_users/{endpoint_user_id}/reporting_tags/{reporting_tag}')

  def add_reporting_tag(self, reporting_tag: str, endpoint_user_id: int, params: dict) -> Any:
    """
    Add reporting tag to endpoint user

    Parameters
    ----------
    reporting_tag : str
      reporting tag name
    endpoint_user_id : int
      endpoint user id
    params : dict
      dict containing key 'value' and value of reporting tag text
    """
    required_keys = ['value']
    self.client.CheckRequiredKeys(required_keys, params, 'add_reporting_tag')

    return self.client.call_api(method='put',service=f'/endpoint_users/{endpoint_user_id}/reporting_tags/{reporting_tag}', params=params)

  def list_system_activities(self, endpoint_user_id: int, params: Optional[dict]) -> Any: #technically, this is SystemActivity but cannot specify due to circular import
    """
    List system activities for endpoint user

    Parameters
    ----------
    endpoint_user_id : int
      endpoint user id
    params : dict
      dict containing key 'types' with value of system activity types
    """
    from .customer import SystemActivity

    return self.client.RecurseList(service=f'/endpoint_users/{endpoint_user_id}/system_activities',
                                   params=params, object_type=SystemActivity)

  def list_reporting_tags(self) -> dict:
    """
    List all reporting tags
    """
    return self.client.call_api(method='get',service='/endpoint_users/reporting_tags', object_type=dict)

class DetectionService(object):
  """
  Detection class
  """
  def __init__(self, client):
    self.client = client

  def list_all_iocs(self, count_mode: bool = False) -> Union[int, list]:
    """
    List all IOCs for all detections

    Parameters
    ----------
    count_mode : bool
      show only a count and omit result details
    """

    params, object_type = self.client.CheckCountMode(count_mode, IndicatorOfCompromiseCollection)

    if count_mode:
      return self.client.call_api(method='get',service='/detections/marked_indicators_of_compromise',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/detections/marked_indicators_of_compromise', object_type=object_type, params=params)

  def list_summaries(self, count_mode: bool = False) -> Union[int, list]:
    """
    List all detection summaries

    Parameters
    ----------
    count_mode : bool
      show only a count and omit result details
    """
    
    params, object_type = self.client.CheckCountMode(count_mode, DetectionSummaryCollection)

    if count_mode:
      return self.client.call_api(method='get',service='/detections/summary',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/detections/summary', object_type=object_type, params=params)

  def list_detections(self, since: str = '', count_mode: bool = False) -> Union[int, list]:
    """
    List all detections

    Parameters
    ----------
    since : str
      Start date for returned data
    count_mode : bool
      show only a count and omit result details
    """
    params, object_type = self.client.CheckCountMode(count_mode, DetectionCollection)
    if since != '':
      params['since'] = since

    if count_mode:
      return self.client.call_api(method='get',service='/detections',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/detections', object_type=object_type, params=params)

  def download(self) -> RequestedCsvResponse:
    """
    Download a CSV of all detections
    """
    return self.client.call_api(method='get',service='/detections/request_csv',object_type=RequestedCsvResponse)

  def list_events(self, detection_id: int, count_mode: bool = False) -> Union[int, list]:
    """
    List events for detection

    Parameters
    ----------
    detection_id : int
      detection id
    count_mode : bool
      show only a count and omit result details
    """

    params, object_type = self.client.CheckCountMode(count_mode, EventCollection)

    if count_mode:
      return self.client.call_api(method='get',service=f'/detections/{detection_id}/events',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service=f'/detections/{detection_id}/events', object_type=object_type, params=params)

  def list_iocs(self, detection_id : int, count_mode: bool = False) -> Union[int, list]:
    """
    List IOCs for detection

    Parameters
    ----------
    detection_id : int
      detection id
    count_mode : bool
      show only a count and omit result details
    """

    params, object_type = self.client.CheckCountMode(count_mode, IndicatorOfCompromiseCollection)
    
    if count_mode:
      return self.client.call_api(method='get',service=f'/detections/{detection_id}/marked_indicators_of_compromise',
                             object_type=object_type, params=params)
    else:
      return self.client.RecurseList(service=f'/detections/{detection_id}/marked_indicators_of_compromise',
                                     object_type=object_type, params=params)

  def update_remediation_status(self, detection_id : int, params : dict) -> DetectionResource:
    """
    Update remediation status for detection
    
    Parameters
    ----------
    detection_id : int
      detection id
    params : dict
      dictionary containing 'remediated_state' key
    """
    required_keys = ['remediated_state']
    self.client.CheckRequiredKeys(required_keys, params, 'update_remediation_status')

    return self.client.call_api(method='patch',service=f'/detections/{detection_id}/update_remediation_state',
                             params=params, object_type=DetectionResource)

  def mark_acknowledged(self, detection_id: int) -> DetectionResource:
    """
    Mark detection as acknowledged

    Parameters
    ----------
    detection_id : int
      detection id
    """
    return self.client.call_api(method='patch',service=f'/detections/{detection_id}/mark_acknowledged', object_type=DetectionResource)

  def get(self, detection_id: int) -> Detection:
    """
    Get detection

    Parameters
    ----------
    detection_id : int
      detection id
    """
    result = self.client.call_api(method='get',service=f'/detections/{detection_id}', object_type=DetectionResource)

    try:
      return result.data[0]
    except:
      return result

  def list_timeline(self, detection_id: int, count_mode: bool = False) -> Union[int, list]: 
    """
    List timeline for detection

    Parameters
    ----------
    detection_id : int
      detection id
    count_mode : bool
      show only a count and omit result details
    """

    from .activity_timelines import Timeline
    params, object_type = self.client.CheckCountMode(count_mode, Timeline)

    if count_mode:
      return self.client.call_api(method='get',service=f'/detections/{detection_id}/timeline',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service=f'/detections/{detection_id}/timeline', object_type=object_type, params=params)

  def list_detectors(self, detection_id: int, count_mode: bool = False) -> Union[int, list]:
    """
    List detectors for detection

    Parameters
    ----------
    detection_id : int
      detection id
    count_mode : bool
      show only a count and omit result details
    """

    params, object_type = self.client.CheckCountMode(count_mode, DetectorCollection)

    if count_mode:
      return self.client.call_api(method='get',service=f'/detections/{detection_id}/detectors',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service=f'/detections/{detection_id}/detectors', object_type=object_type, params=params)

  def list_related(self, detection_id: int, count_mode: bool = False) -> Union[int, list]:
    """
    List related detections

    Parameters
    ----------
    detection_id : int
      detection id
    count_mode : bool
      show only a count and omit result details
    """
    params, object_type = self.client.CheckCountMode(count_mode, DetectionCollection)

    if count_mode:
      return self.client.call_api(method='get',service=f'/detections/{detection_id}/related_detections',
                             object_type=object_type, params=params)
    else:
      return self.client.RecurseList(service=f'/detections/{detection_id}/related_detections',
                                     object_type=object_type, params=params)

  def list_contributing_intel(self, detection_id: int) -> dict:
    """
    List contributing intel for detection

    Parameters
    ----------
    detection_id : int
      detection id
    """

    return self.client.RecurseList(service=f'/detections/{detection_id}/contributing_intel',
                                   object_type=dict)

  def mark_activity_of_occurrence(self, detection_id: int, event_timeline_activity_id: int) -> DetectionResource:
    # TODO: Verify this does indeed return a resource object
    """
    Mark activity of occurrence

    Parameters
    ----------
    detection_id : int
      detection id
    event_timeline_activity_id : int
      event timeline activity id
    """
    return self.client.call_api(method='post',service=f'/detections/{detection_id}/mark_activity_of_occurrence',
                             object_type=DetectionResource, params={'event_timeline_activity_id': event_timeline_activity_id})

class EndpointService(object):
  """
  Endpoint class
  """
  def __init__(self, client):
    self.client = client

  def list_endpoints(self, query: Optional[str] = None, order_by: Optional[str] = None, filter_query: Optional[str] = None, count_mode: bool = False) -> Union[int, EndpointCollection]:
    """
    List all endpoints

    Parameters
    ----------
    query : str
      query string
    order_by : str
      field to use when ordering
    filter_query : str
      filter query
    count_mode : bool
      show only a count and omit result details
    """
    params, object_type = self.client.CheckCountMode(count_mode, EndpointCollection)
    if query is not None:
      params['query'] = query
    if order_by is not None:
      params['order_by'] = order_by
    if filter_query is not None:
      params['filter_query'] = filter_query

    if count_mode:
      return self.client.call_api(method='get',service='/endpoints',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/endpoints', object_type=object_type, params=params)

  def download(self) -> RequestedCsvResponse:
    """
    Download CSV of endpoints
    """
    return self.client.call_api(method='get',service='/endpoints/request_csv',object_type=RequestedCsvResponse)

  def deisolate(self, params : dict) -> Any:
    """
    Deisolate endpoints

    Parameters
    ----------
    params : dict
      dict containing key 'ids' with value of endpoint ids
    """
    required_keys = ['ids']
    self.client.CheckRequiredKeys(required_keys, params, 'deisolate')

    return self.client.call_api(method='delete',service='/endpoints/isolate', params=params)

  def isolate(self, params: dict) -> Any:
    """
    Isolate endpoints

    Parameters
    ----------
    params : dict
      dict containing key 'ids' with value of endpoint ids
    """
    required_keys = ['ids']
    self.client.CheckRequiredKeys(required_keys, params, 'isolate')

    return self.client.call_api(method='post',service='/endpoints/isolate', params=params)

  def decommission_list(self, params: dict, uninstall_sensor: bool) -> Any:
    """
    Decommission endpoints

    Parameters
    ----------
    params : dict
      dict containing key 'ids' with value of endpoint ids
    uninstall_sensor : bool
    """
    required_keys = ['ids']
    self.client.CheckRequiredKeys(required_keys, params, 'decommission')
    key = 'false'
    if uninstall_sensor:
      key = 'true'

    return self.client.call_api(method='delete',service=f'/endpoints/decommission?uninstall_sensor={key}', params=params)

  def reinstate(self, params: dict) -> Any:
    """
    Reinstate endpoints

    Parameters
    ----------
    params : dict
      dict containing key 'ids' with value of endpoint ids
    """
    required_keys = ['ids']
    self.client.CheckRequiredKeys(required_keys, params, 'reinstate')

    return self.client.call_api(method='post',service='/endpoints/reinstate', params=params)

  def deactivate_safe_mode(self, params: dict) -> Any:
    """
    Deactivate safe mode for endpoints

    Parameters
    ----------
    params : dict
      dict containing key 'ids' with value of endpoint ids
    """
    required_keys = ['ids']
    self.client.CheckRequiredKeys(required_keys, params, 'deactivate_safe_mode')

    return self.client.call_api(method='delete',service='/endpoints/safe_mode', params=params)

  def activate_safe_mode(self, params: dict) -> Any:
    """
    Activate safe mode for endpoints

    Parameters
    ----------
    params : dict
      dict containing key 'ids' with value of endpoint ids
    """
    required_keys = ['ids']
    self.client.CheckRequiredKeys(required_keys, params, 'activate_safe_mode')

    return self.client.call_api(method='post',service='/endpoints/safe_mode', params=params)

  def list_reporting_tags(self) -> list:
    """
    List reporting tags for all endpoints
    """
    result = self.client.get(service='/endpoints/reporting_tags', object_type=ReportingTagCollection)

    try:
      return result.data
    except:
      return result

  def list_reporting_tags_associations(self) -> Union[int, list[ReportingTagAssociation]]:
    """
    List reporting tag associations for all endpoints
    """

    default_params = {"per_page": 100}

    # First, get a list of how many items we have
    total_items = self.list_endpoints(count_mode=True)

    return self.client.RecurseList(service='/endpoints/reporting_tags_associations', object_type=ReportingTagAssociationCollection, params=default_params, total_items=total_items)

  def decommission(self, endpoint_id: int, uninstall_sensor: bool) -> EndpointResource:
    """
    Decommission endpoint

    Parameters
    ----------
    endpoint_id : int
      endpoint id
    uninstall_sensor: bool
      uninstall sensor
    """
    return self.client.call_api(method='delete',service=f'/endpoints/{endpoint_id}?uninstall_sensor={uninstall_sensor}',
                              object_type=EndpointResource)

  def get(self, endpoint_id: int) -> Endpoint:
    """
    Get endpoint

    Parameters
    ----------
    endpoint_id : int
      endpoint id
    """
    result = self.client.call_api(method='get',service=f'/endpoints/{endpoint_id}', object_type=EndpointResource)

    try:
      return result.data[0]
    except:
      return result

  def remove_reporting_tag(self, endpoint_id: int, reporting_tag: str) -> Any:
    """
    Remove reporting tag from endpoint

    Parameters
    ----------
    endpoint_id : int
      endpoint id
    reporting_tag : str
      reporting tag name
    """
    return self.client.call_api(method='delete',service=f'/endpoints/{endpoint_id}/reporting_tags/{reporting_tag}')

  def add_reporting_tag(self, endpoint_id: int, reporting_tag: str, params: dict) -> EndpointResource:
    """
    Add reporting tag to endpoint

    Parameters
    ----------
    endpoint_id : int
      endpoint id
    reporting_tag : str
      reporting tag name
    params : dict
      dict containing key 'value' with value of reporting tag text
    """
    required_keys = ['value']
    self.client.CheckRequiredKeys(required_keys, params, 'add_reporting_tag')

    return self.client.call_api(method='put',service=f'/endpoints/{endpoint_id}/reporting_tags/{reporting_tag}',
                           params=params, object_type=EndpointResource)

  def list_endpoint_users(self, endpoint_id: int, fromdate: Optional[str] = None, include_system_accounts: bool = True, count_mode: bool = False) -> Union[int, EndpointUserCollection]:
    """
    List endpoint users

    Parameters
    ----------
    endpoint_id : int
      endpoint id
    fromdate : str
      initial/start date for search
    include_system_accounts : bool
    count_mode : bool
      show only a count and omit result details
    """
    params, object_type = self.client.CheckCountMode(count_mode, EndpointUserCollection)
    if fromdate is not None:
      params['fromdate'] = fromdate
    if include_system_accounts is False:
      params['include_system_accounts'] = 'false'

    if count_mode:
      return self.client.call_api(method='get',service=f'/endpoints/{endpoint_id}/endpoint_users',
                             object_type=object_type, params=params)
    else:
      return self.client.RecurseList(service=f'/endpoints/{endpoint_id}/endpoint_users',
                                     params=params,object_type=object_type)

  def list_system_activities(self, endpoint_id: int, params: dict) -> Any:
    """
    List system activities for endpoint

    Parameters
    ----------
    id : int
      endpoint id
    params : dict
      dict containing key 'types' with value system activity types
    """
    required_keys = ['types']
    self.client.CheckRequiredKeys(required_keys, params, 'list_endpoint_system_activities')

    from .customer import SystemActivity

    return self.client.RecurseList(service=f'/endpoints/{endpoint_id}/system_activities',
                                   params=params,object_type=SystemActivity)

  def get_by_sensor_id(self, sensor_id: int) -> Endpoint:
    """
    Get endpoint by sensor id

    Parameters
    ----------
    sensor_id : int
      endpoint sensor id
    """
    result = self.client.call_api(method='get',service=f'/endpoints/sensor_id/{sensor_id}', object_type=EndpointResource)

    try:
      return result.data[0]
    except:
      return result

  def download_recently_decommissioned(self) -> RequestedCsvResponse:
    """
    Download CSV of recently decommissioned endpoints
    """
    return self.client.call_api(method='get',service='/endpoints/recently_decommissioned/request_csv', object_type=RequestedCsvResponse)

  def download_newly_observed(self) -> RequestedCsvResponse:
    """
    Download CSV of newly observed endpoints
    """
    return self.client.call_api(method='get',service='/endpoints/newly_observed/request_csv', object_type=RequestedCsvResponse)

  def download_license_usage(self, year: int, month: int) -> RequestedCsvResponse:
    """
    Download CSV of license usage
    """
    return self.client.call_api(method='get',service=f"/endpoints/license_usage/request_csv?year={year}&month={month}", object_type=RequestedCsvResponse)

  def download_license_usage_server_counts(self, year: int, month: int) -> RequestedCsvResponse:
    """
    Download CSV of license usage server counts
    """
    return self.client.call_api(method='get',service=f'/endpoints/license_usage/request_server_counts_csv?year={year}&month={month}', object_type=RequestedCsvResponse)

class TargetedProductService(object):
  """
  Targeted Product class
  """
  def __init__(self, client):
    self.client = client

  def list_products(self, count_mode: bool = False) -> Union[int, TargetedProductCollection]:
    """
    List all targeted products

    Parameters
    ----------
    count_mode : bool
      show only a count and omit result details
    """

    params, object_type = self.client.CheckCountMode(count_mode, TargetedProductCollection)

    if count_mode:
      return self.client.call_api(method='get',service='/targeted_products',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/targeted_products', object_type=object_type, params=params)

  def delete_ignored(self, targeted_product_id: int) -> Union[StandardErrorResponse, StandardSuccessResponse]:
    """
    Delete ignored targeted product

    Parameters
    ----------
    targeted_product_id : int
      ignored targeted product id
    """
    result = self.client.call_api(method='delete',service=f'/customer/ignored_targeted_products/{targeted_product_id}',
                              object_type = IgnoredTargetedProductCollection)
    
    if isinstance(result, IgnoredTargetedProductResource):
      return StandardSuccessResponse({"msg": "Ignored targeted product item successfully deleted"})
    else:
      return result

  def create_ignored(self, params: dict) -> IgnoredTargetedProduct:
    """
    Create new ignored targeted product

    Parameters
    ----------
    params : dict
      dict of attributes for new ignored targeted product
      required keys: targeted_product_id
                     justification
    """
    required_keys = ['targeted_product_id', 'justification']
    self.client.CheckRequiredKeys(required_keys, params, 'create_ignored_product')

    result = self.client.call_api(method='post',service='/customer/ignored_targeted_products',
                                  params=params, object_type=IgnoredTargetedProductCollection)
    
    try:
      return result.data[0]
    except:
      return result

  def list_ignored(self, count_mode: bool = False) -> Union[int, IgnoredTargetedProductCollection]:
    """
    List ignored targeted products

    Parameters
    ----------
    count_mode : bool
      show only a count and omit result details
    """

    params, object_type = self.client.CheckCountMode(count_mode, IgnoredTargetedProductCollection)

    if count_mode:
      return self.client.call_api(method='get',service='/customer/ignored_targeted_products',params=params, object_type=object_type)
    else:
      return self.client.RecurseList(service='/customer/ignored_targeted_products',
                                     object_type=object_type, params=params)

class CloudResourceScansService(object):
  """
  Cloud Resource Scans Service class
  """

  def __init__(self, client):
    self.client = client

  def license_usage_csv(self) -> RequestedCsvResponse:
    """
    Download CSV of license usage
    """
    return self.client.call_api(method='get',service='/cloud_resource_scans/license_usage/request_csv', object_type=RequestedCsvResponse)
  
class ExternalServicesService(object):
  """
  External Services class
  """

  def __init__(self, client):
    self.client = client

  def list(self) -> list[ExternalService]:
    # TODO: Verify this is the correct format
    """
    List all external services
    """

    return self.client.RecurseList(service='/external_services', object_type=ExternalService)
  
  def get(self, external_service_uuid: int) -> ExternalService:
    """
    Get external service

    Parameters
    ----------
    external_service_uuid : int
      external service uuid
    """

    return self.client.call_api(method='get',service=f'/external_services/{external_service_uuid}', object_type=ExternalServiceResource)
  
  def list_aws_services(self) -> list[ExternalService]:
    """
    List all AWS services
    """

    return self.client.RecurseList(service='/external_services/aws', object_type=ExternalService)
  
  def create_aws_service(self, description: list[str], aws_account_id: list[str], aws_assumed_role_arn: list[str]) -> ExternalService:
    """
    Create new AWS service

    Parameters
    ----------
    description : list
      list of descriptions
    aws_account_id : list
      list of AWS account ids
    aws_assumed_role_arn : list
      list of AWS assumed role ARNs
    """

    params = {'external_services[description]': description, 'external_services[aws_account_id]': aws_account_id, 'external_services[aws_assumed_role_arn]': aws_assumed_role_arn}

    return self.client.call_api(method='post',service='/external_services/aws', params=params, object_type=ExternalServiceCollection)

  def update_aws_service(self, external_service_uuid: int, aws_account_id: str = None, description: str = None, aws_assumed_role_arn: str = None) -> ExternalService:
    """
    Update AWS service

    Parameters
    ----------
    external_service_uuid : int
      external service uuid
    aws_account_id : str
      AWS account id
    description : str
      description
    aws_assumed_role_arn : str
      AWS assumed role ARN
    """

    params = {}

    if aws_account_id:
      params['external_services[aws_account_id]'] = aws_account_id
    if description:
      params['external_services[description]'] = description
    if aws_assumed_role_arn:
      params['external_services[aws_assumed_role_arn]'] = aws_assumed_role_arn

    return self.client.call_api(method='patch',service=f'/external_services/aws/{external_service_uuid}', params=params, object_type=ExternalServiceResource)
  
  def delete_aws_service(self, external_service_uuid: int) -> ExternalService:
    """
    Delete AWS service

    Parameters
    ----------
    external_service_uuid : int
      external service uuid
    """

    return self.client.call_api(method='delete',service=f'/external_services/aws/{external_service_uuid}', object_type=ExternalServiceResource)

  def get_aws_service(self, external_service_uuid: int) -> ExternalService:
    """
    Get AWS service

    Parameters
    ----------
    external_service_uuid : int
      external service uuid
    """

    return self.client.call_api(method='get',service=f'/external_services/aws/{external_service_uuid}', object_type=ExternalServiceResource)

class SuppressionRuleService(object):
  """
  Suppression Rule Service class
  """

  def __init__(self, client):
    self.client = client

  def list_suppression_rules(self, detector_id: int = None, endpoint_id: int = None, permanent: bool = None, publisher: str = None, md5: str = None, parent_md5: str = None, command_line: str = None, uid: str = None, sensor_id: str = None) -> Union[int, list[SuppressionRule]]:
    """
    List all suppression rules

    Parameters
    ----------
    detector_id : int
      detector id
    endpoint_id : int
      endpoint id
    permanent : bool
      permanent suppression
    publisher : str
      publisher
    md5 : str
      md5 hash
    parent_md5 : str
      parent md5 hash
    command_line : str
      command line
    uid : str
      uid
    sensor_id : str
      sensor id    
    """

    query = []
    if detector_id:
      query.append('detector_id={0}'.format(detector_id))
    if endpoint_id:
      query.append('endpoint_id={0}'.format(endpoint_id))
    if permanent:
      query.append('permanent={0}'.format(permanent))
    if publisher:
      query.append('publisher={0}'.format(publisher))
    if md5:
      query.append('md5={0}'.format(md5))
    if parent_md5:
      query.append('parent_md5={0}'.format(parent_md5))
    if command_line:
      query.append('command_line={0}'.format(command_line))
    if uid:
      query.append('uid={0}'.format(uid))
    if sensor_id:
      query.append('sensor_id={0}'.format(sensor_id))

    full_query = '?' + '&'.join(query) if query else ''

    return self.client.RecurseList(service=f'/suppression_rules{full_query}', object_type=SuppressionRuleCollection)

  def delete_suppression_rule(self, suppression_rule_id: int) -> Any:
    """
    Delete suppression rule

    Parameters
    ----------
    suppression_rule_id : int
      suppression rule id
    """

    return self.client.call_api(method='delete',service=f'/suppression_rules/{suppression_rule_id}')

  def get_suppression_rule(self, suppression_rule_id: int) -> SuppressionRule:
    """
    Get suppression rule
    
    Parameters
    ----------
    suppression_rule_id : int
      suppression rule id
    """

    return self.client.call_api(method='get',service=f'/suppression_rules/{suppression_rule_id}', object_type=SuppressionRuleResource)