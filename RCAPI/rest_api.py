"""
Rest client for rcapi
"""
import os
from typing import Optional
from .models.common import SelectableObject
from .models.general import StandardErrorResponse
from .models.exec import Automate
from .models.audit_log import AuditLogService
from .models.customer import CustomerService, ExternalAlertService
from .models.search import Search
from .models.general import ActivityMonitorService, DetectionService, DetectorService, \
                            EndpointService, EventService, EndpointUserService, \
                            SharedFileService, ManagedPortalUserService, \
                            PortalRoleService, ReportLibrary, \
                            TargetedProductService, TelemetrySearchService, \
                            SuppressionRuleService

from .client import Client

class rcapi():
  """
  Initiate rcapi

  Parameters
  ----------
  url : str
    URL of Red Canary subdomain of the form https://subdomain.my.redcanary.co
    Can be defined via environment variable RED_CANARY_CUSTOMER_ID
  
  key : str
    API key for Red Canary subdomain
    Can be defined via environment variable RED_CANARY_AUTH_TOKEN
  """

  def __init__(self, url: Optional[str] = None, key: Optional[str] = None) -> None:

    if url is None:
      url = str(os.getenv('RED_CANARY_CUSTOMER_ID'))

    if key is None:
      key = str(os.getenv('RED_CANARY_AUTH_TOKEN'))
    self.base_url = url.rstrip('/')
    self.headers = {"X-Api-Key": f"{key}"}
    self.client = Client(self.base_url, self.headers)

    self.activity_monitor = ActivityMonitorService(self.client)
    self.audit_log = AuditLogService(self.client)
    self.automate = Automate(self.client)
    self.customer = CustomerService(self.client)
    self.detection = DetectionService(self.client)
    self.detector = DetectorService(self.client)
    self.endpoint_user = EndpointUserService(self.client)
    self.endpoint = EndpointService(self.client)
    self.event = EventService(self.client)
    self.external_alert = ExternalAlertService(self.client)
    self.managed_portal_user = ManagedPortalUserService(self.client)
    self.portal_role = PortalRoleService(self.client)
    self.report = ReportLibrary(self.client)
    self.search = Search(self.client)
    self.shared_file = SharedFileService(self.client)
    self.suppression_rule = SuppressionRuleService(self.client)
    self.targeted_product = TargetedProductService(self.client)
    self.telemetry_search = TelemetrySearchService(self.client)

  def select(self, object_type, unique_id: Optional[str]=None) -> object:
    """
    Select by object type
    
    Returns a single object if a unique_id is provided

    Returns the object for querying if no unique_id is provided
    """

    if issubclass(object_type, SelectableObject):
      if unique_id: # return a single object
        return object_type(client=self.client).get_item(unique_id)
      else: # return a list of objects
        return object_type(client=self.client).get_list()
    else:
      raise ValueError(f"Unsupported object type {object_type.__name__} for select")

  def create(self, object_type, params: dict = {}) -> object:
    """
    Create a new instance of a given object type
    """
    if hasattr(object_type, 'create_item') and callable(getattr(object_type, 'create_item')):
      return object_type(client=self.client).create_item(params)
    else:
      raise ValueError(f"Unsupported object type {object_type.__name__} for create")

  def TestConnection(self) -> bool:
    """
    Test connection
    """
    temp = self.client.get(service='/automate/configuration')

    if isinstance(temp, StandardErrorResponse):
      return False
    else:
      return True
