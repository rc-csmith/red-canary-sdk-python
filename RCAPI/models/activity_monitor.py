import six
from .common import BaseObject

class Activity_Monitor(BaseObject):
  def __init__(self, activitymonitor):
    super().__init__(activitymonitor)
    self._entry = activitymonitor
  
  @property
  def type(self):
    return self._entry.get('type')

  @property
  def id(self):
    return self._entry.get('id')

  @property
  def name(self):
    return (self._entry.get('attributes')).get('name')
  
  @property
  def active(self):
    return (self._entry.get('attributes')).get('active')
  
  @property
  def type(self):
    return (self._entry.get('attributes')).get('type')
  
  @property
  def file_modification_types_monitored(self):
    return (self._entry.get('attributes')).get('file_modification_types_monitored')
  
  @property
  def file_paths_monitored(self):
    return (self._entry.get('attributes')).get('file_paths_monitored')

  @property
  def usernames_monitored(self):
    return (self._entry.get('attributes')).get('usernames_monitored')

  @property
  def usernames_ignored(self):
    return (self._entry.get('attributes')).get('usernames_ignored')

class NewActivityMonitor(object):
  def __init__(self, **kwargs):
    monitor_types = ["file_creation",
                    "file_deletion"
                    ]

    self.name = kwargs.get('name', 'SSH directory changes')
    self.type = kwargs.get('type', 'file_modification')
    self.active = kwargs.get('active', False)
    self.file_modification_types_monitored = kwargs.get('file_modification_types_monitored', [None])
    self.file_paths_monitored = kwargs.get('file_paths_monitored', [None])
    self.usernames_matched = kwargs.get('usernames_matched', [None])
    self.usernames_excluded = kwargs.get('usernames_excluded', [None])

    for item in self.file_modification_types_monitored:
      if item not in monitor_types:
        raise Exception('Error! File modification type {0} not supported'.format(item))

  def to_json(self):
    orig_json = self.__dict__
    non_empty_json = {'activity_monitor[' + k + ']': v for (k, v) in six.iteritems(orig_json) if v is not None}
    return non_empty_json

class Match(BaseObject):
  def __init__(self, match):
    super().__init__(match)
    self._entry = match
  
  @property
  def id(self):
    return self._entry.get('id')
  
  @property
  def activity_monitor_id(self):
    return (self._entry.get('attributes')).get('activity_monitor_id')  
  
  @property
  def hit_at(self):
    return (self._entry.get('attributes')).get('hit_at')
  
  @property
  def process_native_id(self):
    return (self._entry.get('attributes')).get('process_native_id')
  
  @property
  def file_path(self):
    return (self._entry.get('attributes')).get('file_path')
  
  @property
  def modification_type(self):
    return (self._entry.get('attributes')).get('modification_type')
  
  @property
  def endpoint_id(self):
    return (((self._entry.get('relationships')).get('affected_endpoint')).get('data')).get('id')
  
  @property
  def identity_id(self):
    return (((self._entry.get('relationships')).get('related_endpoint_user')).get('data')).get('id')

class FileIntegrityMatch(BaseObject):
  def __init__(self, fim):
    super().__init__(fim)
    self._entry = fim
  
  @property
  def id(self):
    return self._entry.get('id')
  
  @property
  def file_path(self):
    return (self._entry.get('attributes')).get('file_path')
  
  @property
  def modification_type(self):
    return (self._entry.get('attributes')).get('modification_type')
  
  @property
  def edr_link(self):
    return (self._entry.get('attributes')).get('edr_link_href')
  
  @property
  def hit_at(self):
    return (self._entry.get('attributes')).get('hit_at')

  @property
  def activity_monitor(self):
    return Activity_Monitor(self._entry.get('attributes')).get('activity_monitor')
  
  @property
  def endpoint(self):
    return 