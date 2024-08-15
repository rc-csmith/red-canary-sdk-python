"""
Primitive Activities
"""
from .common import BaseObject
from .primitives import File,IpAddress,Domain,RegistryKey,OperatingSystemProcess

class FileModification(BaseObject):
  """
  File Modification object
  """
  def __init__(self, entry):
    type_mapping = {
      'file': File
    }
    super().__init__(entry, type_mapping)

class NetworkConnection(BaseObject):
  """
  Network Connection object
  """
  def __init__(self, entry):
    type_mapping = {
      'ip_address': IpAddress,
      'domain': Domain
    }
    super().__init__(entry, type_mapping)

class RegistryModification(BaseObject):
  """
  Registry Modification object
  """
  def __init__(self, entry):
    type_mapping = {
      'registry_key': RegistryKey
    }
    super().__init__(entry, type_mapping)

class ProcessExecution(BaseObject):
  """
  Process Execution object
  """
  def __init__(self, entry):
    type_mapping = {
      'operating_system_process': OperatingSystemProcess
    }
    super().__init__(entry, type_mapping)

class ModuleLoad(BaseObject):
  """
  Module Load object
  """
  def __init__(self, entry):
    type_mapping = {
      'module': File
    }
    super().__init__(entry, type_mapping)
