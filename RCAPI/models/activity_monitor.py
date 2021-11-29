import six

class Activity_Monitor(object):
  def __init__(self, activitymonitor):
    self._activitymonitor = activitymonitor
  
  @property
  def type(self):
    return self._activitymonitor.get('type')

  @property
  def id(self):
    return self._activitymonitor.get('id')
  
  @property
  def attributes(self):
    return Attributes(self._activitymonitor.get('attributes'))

  @property
  def activity_monitor(self):
    return ((self._activitymonitor.get('links')).get('self')).get('href')

  @property
  def matches(self):
    return ((self._activitymonitor.get('links')).get('matches')).get('href')

class Attributes(object):
  def __init__(self, attributes):
    self._attributes = attributes
  
  @property
  def name(self):
    return self._attributes.get('name')
  
  @property
  def active(self):
    return self._attributes.get('active')
  
  @property
  def type(self):
    return self._attributes.get('type')
  
  @property
  def file_modification_types_monitored(self):
    return self._attributes.get('file_modification_types_monitored')
  
  @property
  def file_paths_monitored(self):
    return self._attributes.get('file_paths_monitored')

  @property
  def usernames_monitored(self):
    return self._attributes.get('usernames_monitored')

  @property
  def usernames_ignored(self):
    return self._attributes.get('usernames_ignored')

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