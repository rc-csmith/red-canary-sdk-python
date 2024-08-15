"""
Audit Log
"""
from typing import Union
from .common import SelectableObject, Collection, Resource
from .general import PortalUser, RequestedCsvResponse

class AuditLog(SelectableObject):
  """
  Audit Log object
  """
  def __init__(self, entry=None, client=None):
    type_mapping = {
      'by_user': PortalUser,
      'web_request_user': PortalUser
    }
    if client:
      self.client = client

    if entry:
      super().__init__(entry, type_mapping)
    
  def get_list(self):
    """
    Get a list of audit logs
    """
    if hasattr(self, 'client'):
      return AuditLogService(self.client).list_entries()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")

  def get_item(self, unique_id: str):
    """
    Get a single audit log

    Parameters
    ----------
    unique_id : str
      unique id for the audit log
    """
    if hasattr(self, 'client'):
      return AuditLogService(self.client).get(int(unique_id))
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

class AuditLogCollection(Collection):
  """
  Audit Log collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, AuditLog, client=client)

class AuditLogResource(Resource):
  """
  Audit Log resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, AuditLog, client=client)

class AuditLogService(object):
  """
  Audit Log Service class
  """
  def __init__(self, client):
    self.client = client

  def list_entries(self, actions: str = '', count_mode: bool = False) -> Union[int, list[AuditLog]]:
    """
    List audit logs

    Parameters
    ----------
    actions : str
      audit actions for search/filter
    count_mode : bool
      show only a count and omit result details
    """
    params, object_type = self.client.CheckCountMode(count_mode, AuditLogCollection)

    if actions != '':
      params['actions'] = actions

    if count_mode:
      return self.client.call_api(method='get',service='/audit_logs',object_type=object_type, params=params)
    else:
      return self.client.RecurseList(service='/audit_logs', object_type=object_type, params=params)

  def download(self, search_string: str = '') -> RequestedCsvResponse:
    """
    Download audit logs to CSV

    Parameters
    ----------
    search_string : str
      query string to filter audit logs
    """
    params = {}
    if search_string != '':
      params['search_string'] = search_string

    return self.client.call_api(method='get',service='/audit_logs/request_csv',object_type=RequestedCsvResponse, params=params)

  def get(self, audit_log_id: int) -> AuditLog:
    """
    Get a single audit log

    Parameters
    ----------
    id : int
      audit log id
    """
    result = self.client.call_api(method='get',service=f'/audit_logs/{audit_log_id}',object_type=AuditLogResource)

    if isinstance(result, AuditLogResource):
      return result.data[0]
    else:
      return result
