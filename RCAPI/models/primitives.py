"""
Primitives
"""
from .common import BaseObject

class File(BaseObject):
  """
  File object
  """
  def __init__(self, entry):
    type_mapping = {
      'binary': Binary
    }
    super().__init__(entry, type_mapping)

class Binary(BaseObject):
  """
  Binary object
  """
  def __init__(self, entry):
    type_mapping = {
      'digital_signature': BinaryDigitalSignature
    }
    super().__init__(entry, type_mapping)

class EDRLink(BaseObject):
  """
  EDR Link object
  """

class BinaryDigitalSignature(BaseObject):
  """
  Binary Digital Signature object
  """

class IpAddress(BaseObject):
  """
  IpAddress object
  """

class Domain(BaseObject):
  """
  Domain object
  """

class RegistryKey(BaseObject):
  """
  Registry Key object
  """

class OperatingSystemProcess(BaseObject):
  """
  Operating System Process object
  """
  def __init__(self, entry):
    type_mapping = {
      'image': File,
      'command_line': ProcessCommandLine
    }
    super().__init__(entry, type_mapping)

class ProcessCommandLine(BaseObject):
  """
  Process Command Line object
  """

class MacAddress(BaseObject):
  """
  MacAddress object
  """

class EndpointHostname(BaseObject):
  """
  Endpoint Hostname object
  """

class BinaryService(object):
  """
  Binary Service class
  """
  def __init__(self, client):
    self.client = client
  
  def get(self, binary_hash: str) -> Binary:
    """
    Get a binary

    Parameters
    ----------
    binary_hash : str
      The hash of the binary to retrieve
    """
    return self.client.call_api(method='get', service=f'/binaries/{binary_hash}', object_type=Binary)

  def get_edr_link(self, binary_hash: str) -> EDRLink:  
    """
    Get the EDR link for a binary
    
    Parameters
    ----------
    binary_hash : str
      The hash of the binary to retrieve
    """
    return self.client.call_api(method='get', service=f'/binaries/{binary_hash}/edr_link', object_type=Binary)
