from common import BaseObject
from primitive_activities import FileModification, NetworkConnection, RegistryModification, ProcessExecution, ModuleLoad

class ActivityOccurred(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry.get('attributes')
  
  @property
  def occurred_at(self):
    return self._entry.get('occurred_at')
  
  @property
  def analyst_notes(self):
    return self._entry.get('analyst_notes')
  
  @property
  def type(self):
    return self._entry.get('type')
  
  @property
  def is_ioc(self):
    return self._entry.get('is_indicator_of_compromise')
  
  @property
  def file_modification(self):
    return FileModification(self._entry.get('file_modification'))
  
  @property
  def network_connection(self):
    return NetworkConnection(self._entry.get('network_connection'))
  
  @property
  def registry_modification(self):
    return RegistryModification(self._entry.get('registry_modification'))
  
  @property
  def processs_execution(self):
    return ProcessExecution(self._entry.get('process_execution'))
  
  @property
  def module_load(self):
    return ModuleLoad(self._entry.get('module_load'))
  
class MarkedRemediated(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry.get('attributes')
  
  @property
  def occurred_at(self):
    return self._entry.get('occurred_at')
  
  @property
  def analyst_notes(self):
    return self._entry.get('analyst_notes')
  
  @property
  def marked_remediated_by(self):
    return self._entry.get('marked_remediated_by')
  
class TimelineEntry(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry

  @property
  def occurred_at(self):
    return (self._entry.get('attributes')).get('occurred_at')
  
  @property
  def analyst_notes(self):
    return (self._entry.get('attributes')).get('analyst_notes')
  
  