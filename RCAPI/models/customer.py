"""
Customer
"""
from typing import Union
from .general import PortalUser, ResourceRelationship, RequestedCsvResponse, StandardErrorResponse, StandardSuccessResponse
from .common import SelectableObject, BaseObject, Collection, Resource

class SystemActivity(BaseObject):
  """
  System Activity object
  """

class IntelReporting(BaseObject): #TODO: Lots of objects with no models defined
  """
  Intel Reporting object
  """

class ExternalAlertSource(SelectableObject):
  """
  External Alert Source object
  Includes Statistics and ResourceRelationship
  """
  def __init__(self, entry=None, client=None):
    type_mapping = {
      'statistics': Statistics,
      'relationships': ResourceRelationship
    }
    if client:
      self.client = client

    if entry:
      super().__init__(entry, type_mapping)

  def get_list(self) -> list:
    """
    Get a list of external alert sources

    Parameters
    ----------
    None

    Returns
    -------
    A list of ExternalAlertSource objects
    """
    if hasattr(self,'client'):
      return ExternalAlertService(self.client).list_sources()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")
  
  def get_item(self, unique_id: str):
    """
    Get a single external alert source

    Parameters
    ----------
    unique_id : str
      ID of object

    Returns
    -------
    An ExternalAlertSource object
    """
    if hasattr(self,'client'):
      return ExternalAlertService(self.client).get_source(int(unique_id))
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")
  
  def create_item(self, params):
    """
    Create a new external alert source
    
    Parameters
    ----------
    params : dict
      dict containing attributes of new source platform
      required keys: name
                     source_platform_id

    Returns
    -------
    An ExternalAlertSource object
    """
    try:
      return ExternalAlertService(self.client).create_source(params)
    except Exception as e:
      raise SyntaxError(e)
  
  def delete(self):
    """
    Delete current external alert source

    Parameters
    ----------
    None

    Returns
    -------
    A StandardSuccessResponse object
    """
    try:
      return ExternalAlertService(self.client).delete_source(self.id)
    except Exception as e:
      raise SyntaxError(e)

class ExternalAlertSourcePlatform(SelectableObject):
  """
  External Alert Source Platform object
  """
  def __init__(self, entry=None, client=None):
    if client:
      self.client = client

    if entry:
      super().__init__(entry, {})
  
  def get_list(self):
    """
    Get a list of external alert source platforms

    Parameters
    ----------
    None

    Returns
    -------
    A list of ExternalAlertSourcePlatform objects
    """
    if hasattr(self,'client'):
      return ExternalAlertService(self.client).list_source_platforms()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")
  
  def get_item(self, unique_id: str):
    """
    Get a single external alert source platform

    Parameters
    ----------
    unique_id : str
      ID of object

    Returns
    -------
    An ExternalAlertSourcePlatform object
    """
    if hasattr(self,'client'):
      return ExternalAlertService(self.client).get_source_platform(int(unique_id))
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

class ExternalAlert(SelectableObject):
  """
  External Alert object
  Includes ResourceRelationship
  """
  def __init__(self, entry=None, client=None):
    type_mapping = {
      'external_alert_source': ResourceRelationship
    }
    if client:
      self.client = client

    if entry:
      super().__init__(entry, type_mapping)

  def get_list(self):
    """
    Get a list of external alerts

    Parameters
    ----------
    None

    Returns
    -------
    A list of ExternalAlert objects
    """
    if hasattr(self,'client'):
      return ExternalAlertService(self.client).list_alerts()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")
  
  def get_item(self, unique_id: str):
    """
    Get a single external alert
    
    Parameters
    ----------
    unique_id : str
      ID of object

    Returns
    -------
    An ExternalAlert object
    """
    if hasattr(self,'client'):
      return ExternalAlertService(self.client).get(int(unique_id))
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

class ExternalAlertResource(Resource):
  """
  External Alert resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, ExternalAlert, client=client)

class Statistics(BaseObject):
  """
  Statistics object
  """

class ExternalAlertSourceResource(Resource):
  """
  External Alert Source resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, ExternalAlertSource, client=client)

class ExternalAlertSourceCollection(Collection):
  """
  External Alert Source collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, ExternalAlertSource, client=client)

class ExternalAlertSourcePlatformResource(Resource):
  """
  External Alert Source Platform resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, ExternalAlertSourcePlatform, client=client)

class ExternalAlertSourcePlatformCollection(Collection):
  """
  External Alert Source Platform collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry,ExternalAlertSourcePlatform, client=client)

class ExternalAlertCollection(Collection):
  """
  External Alert collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry,ExternalAlert, client=client)

class CustomerService(object):
  """
  Customer Service class
  """
  def __init__(self, client):
    self.client = client

  def get_intel_reporting_stats(self) -> IntelReporting:
    """
    Get intel reporting stats

    Parameters
    ----------
    None

    Returns
    -------
    An IntelReporting object
    """
    return self.client.call_api(method='get',service='/customer/intel_reporting', object_type=IntelReporting)
  
  def list_system_activities(self) -> list[SystemActivity]:
    """
    List system activities

    Parameters
    ----------
    None

    Returns
    -------
    A list of SystemActivity objects
    """
    return self.client.RecurseList(service='/customer/system_activities', object_type=SystemActivity)

class ExternalAlertService(object):
  """
  External Alert Service class
  """
  def __init__(self, client):
    self.client = client

  def get_source(self, external_alert_source_id: int) -> ExternalAlertSource:
    """
    Get a specific external alert source

    Parameters
    ----------
    external_alert_source_id : int
      external alert source id
    count_mode : bool
      show only a count and omit result details

    Returns
    -------
    An ExternalAlertSource object
    """

    result = self.client.call_api(method='get',service=f'/customer/external_alert_sources/{external_alert_source_id}',
                           object_type=ExternalAlertSourceResource)
    
    try:
      return result.data[0]
    except:
      return result

  def delete_source(self, external_alert_source_id: int) -> Union[StandardErrorResponse, StandardSuccessResponse]:
    """
    Delete an external alert source

    Parameters
    ----------
    external_alert_source_id : int
      external alert source id

    Returns
    -------
    A StandardSuccessResponse object
    """
    result = self.client.call_api(method='delete',service=f'/customer/external_alert_sources/{external_alert_source_id}',
                              object_type=ExternalAlertSourceResource)
  
    if isinstance(result, ExternalAlertSourceResource):
      return StandardSuccessResponse({"msg": "External alert source successfully deleted"})
    else:
      return result

  def create_source(self, params: dict) -> ExternalAlertSource:
    """
    Create a new external alert source

    Parameters
    ----------
    params : dict
      dict containing attributes of new source platform
      required keys: name
                     source_platform_id

    Returns
    -------
    An ExternalAlertSource object
    """
    required_keys = ['name', 'source_platform_id']
    self.client.CheckRequiredKeys(required_keys, params, 'create_external_alert_source')

    result = self.client.call_api(method='post',service='/customer/external_alert_sources',
                            params=params, object_type=ExternalAlertSourceCollection)
  
    try:
      return result.data[0]
    except:
      return result

  def list_sources(self, alert_aggregator_id: int=-1, count_mode: bool = False) -> Union[int, list[ExternalAlertSource]]:
    """"
    List all external alert sources

    Parameters
    ----------
    alert_aggregator_idv : int
      alert aggregator id
      optional - defaults to all
    count_mode : bool
      show only a count and omit result details
    
    Returns
    -------
    A list of ExternalAlertSource objects or an integer count
    """
    params, object_type = self.client.CheckCountMode(count_mode, ExternalAlertSourceCollection)
    if alert_aggregator_id != -1:
      params['alert_aggregator_id'] = alert_aggregator_id

    if count_mode:
      return self.client.call_api(method='get',service='/customer/external_alert_sources',
                                  object_type=object_type, params=params)
    else:
      return self.client.RecurseList(service='/customer/external_alert_sources',
                                     params=params, object_type=object_type)

  def get_source_platform(self, external_alert_source_platform_id: int) -> ExternalAlertSourcePlatform:
    """
    Get a specific external alert source platform

    Parameters
    ----------
    external_alert_source_platform_id : int
      external alert source platform id

    Returns
    -------
    An ExternalAlertSourcePlatform object
    """
    result = self.client.call_api(method='get',service=f'/customer/external_alert_source_platform/{external_alert_source_platform_id}',
                           object_type = ExternalAlertSourcePlatformResource)
    
    try:
      return result.data[0]
    except:
      return result

  def list_source_platforms(self, count_mode: bool = False) -> Union[int, list[ExternalAlertSourcePlatform]]:
    """
    List all external alert source platforms

    Parameters
    ----------
    count_mode : bool
      show only a count and omit result details

    Returns
    -------
    A list of ExternalAlertSourcePlatform objects or an integer count
    """

    params, object_type = self.client.CheckCountMode(count_mode, ExternalAlertSourcePlatformCollection)

    if count_mode:
      return self.client.call_api(method='get',service='/customer/external_alert_source_platforms',
                                  object_type=object_type, params=params)
    else:
      return self.client.RecurseList(service='/customer/external_alert_source_platforms',
                                     object_type=object_type, params=params)

  def list_alerts(self, count_mode: bool = False, q : str = '') -> Union[int, list[ExternalAlert]]:
    """
    List all external alerts

    Parameters
    ----------
    count_mode : bool
      show only a count and omit result details
    q : str
      query string for search/filter
    
    Returns
    -------
    A list of ExternalAlert objects or an integer count
    """

    params, object_type = self.client.CheckCountMode(count_mode, ExternalAlertCollection)

    if q != '':
      params['q'] = q

    if count_mode:
      return self.client.call_api(method='get',service='/customer/external_alerts',
                                  object_type=object_type, params=params)
    else:
      return self.client.RecurseList(service='/customer/external_alerts', object_type=object_type, params=params)

  def get(self, external_alert_id: int) -> ExternalAlert:
    """
    Get a specific external alert
    
    Parameters
    ----------
    external_alert_id : int
      ID of object

    Returns
    -------
    An ExternalAlert object
    """

    result = self.client.call_api(method='get', service=f'/customer/external_alerts/{external_alert_id}', 
                                object_type=ExternalAlertResource)

    try:
      return result.data[0]
    except:
      return result

  def get_native_id(self, external_alert_native_id: int) -> ExternalAlert:
    """
    Get a specific external alert by its native ID

    Parameters
    ----------
    external_alert_native_id : int
      Native ID of object

    Returns
    -------
    An ExternalAlert object
    """

    result = self.client.call_api(method='get', service=f'/customer/external_alerts/native/{external_alert_native_id}',
                                object_type=ExternalAlertResource)
    
    try:
      return result.data[0]
    except:
      return result
