from common import BaseObject
from primitives import File,IpAddress,Domain,RegistryKey,OperatingSystemProcess

class FileModification(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry.get('attributes')
  
  @property
  def modification_type(self):
    return self._entry.get('modification_type')
  
  @property
  def file(self):
    return File(self._entry.get('file'))
  
class NetworkConnection(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry.get('attributes')
  
  @property
  def ip_address(self):
    return IpAddress(self._entry.get('ip_address'))
  
  @property
  def port(self):
    return self._entry.get('port')
  
  @property
  def domain(self):
    return Domain(self._entry.get('domain'))

class RegistryModification(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry.get('attributes')
  
  @property
  def registry_key(self):
    return RegistryKey(self._entry.get('registry_key'))
  
  @property
  def modification_type(self):
    return self._entry.get('modification_type')

class ProcessExecution(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry.get('attributes')

  @property
  def operating_system_process(self):
    return OperatingSystemProcess(self._entry.get('operating_system_process'))

class ModuleLoad(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry.get('attributes')
  
  @property
  def module(self):
    return File(self._entry.get('module'))