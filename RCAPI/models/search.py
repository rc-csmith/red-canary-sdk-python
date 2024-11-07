"""
Search
"""
from typing import Union
from .common import BaseObject, Collection
from .general import EndpointNetworkAddress
from .primitive_activities import FileModification, NetworkConnection, \
                                  RegistryModification, ProcessExecution
from .primitives import EndpointHostname

class ResultForMacAddress(BaseObject):
  """
  Result for Mac Address object
  """
  def __init__(self, entry):
    type_mapping = {
      'endpoint_network_address': EndpointNetworkAddress
    }
    super().__init__(entry, type_mapping)

class ResultForMacAddressCollection(Collection):
  """
  Result for Mac Address collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, ResultForMacAddress, client=client)

class ResultForIpAddress(BaseObject):
  """
  Result for Ip Address object
  """
  def __init__(self, entry):
    type_mapping = {
      'endpoint_network_address': EndpointNetworkAddress,
      'file_modification': FileModification,
      'network_connection': NetworkConnection,
      'registry_modification': RegistryModification,
      'process_execution': ProcessExecution
    }
    super().__init__(entry, type_mapping)

class ResultForIpAddressCollection(Collection):
  """
  Result for Ip Address collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, ResultForIpAddress, client=client)

class ResultForEndpointHostname(BaseObject):
  """
  Result for Endpoint Hostname object
  """
  def __init__(self, entry):
    type_mapping = {
      'endpoint_hostname': EndpointHostname
    }
    super().__init__(entry, type_mapping)

class ResultForEndpointHostnameCollection(Collection):
  """
  Result for Endpoint Hostname collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry,ResultForEndpointHostname, client=client)

class SearchService(object):
  """
  Search class
  """
  def __init__(self, client):
    self.client = client

  def mac_address(self, mac_address: str, count_mode: bool = False) -> Union[int, ResultForMacAddressCollection]:
    """
    Search for a MAC address

    Parameters
    ----------
    mac_address : str
      MAC address
    count_mode : bool
      show only a count and omit result details

    Returns
    -------
    A list of ResultForMacAddress objects or an integer count
    """
    params, object_type = self.client.CheckCountMode(count_mode, ResultForMacAddressCollection)
    params['mac_address'] = mac_address

    if count_mode:
      return self.client.RecurseList(service='/search/mac_addresses',
                                     object_type=object_type, params=params)
    else:
      return self.client.RecurseList(service='/search/mac_addresses',
                                     object_type=object_type, params=params)

  def ip_address(self, ip_address: str, count_mode: bool = False) -> Union[int, ResultForIpAddressCollection]:
    """
    Search for an IP address

    Parameters
    ----------
    ip_address : str
      IP address
    count_mode : bool
      show only a count and omit result details

    Returns
    -------
    A list of ResultForIpAddress objects or an integer count
    """
    params, object_type = self.client.CheckCountMode(count_mode, ResultForIpAddressCollection)
    params['ip_address'] = ip_address

    if count_mode:
      return self.client.RecurseList(service='/search/ip_addresses',
                                     object_type=object_type, params=params)
    else:
      return self.client.RecurseList(service='/search/ip_addresses',
                                     object_type=object_type, params=params)

  def endpoint_hostname(self, endpoint_hostname: str, count_mode: bool = False) -> Union[int, ResultForEndpointHostnameCollection]:
    """
    Search for an endpoint hostname
    
    Parameters
    ----------
    endpoint_hostname : str
      endpoint hostname
    count_mode : bool
      show only a count and omit result details

    Returns
    -------
    A list of ResultForEndpointHostname objects or an integer count
    """
    params, object_type = self.client.CheckCountMode(count_mode, ResultForEndpointHostnameCollection)
    params['endpoint_hostname'] = endpoint_hostname

    if count_mode:
      return self.client.RecurseList(service='/search/endpoint_hostnames',
                                     object_type=object_type, params=params)
    else:
      return self.client.RecurseList(service='/search/endpoint_hostnames', 
                                     object_type=object_type, params=params)