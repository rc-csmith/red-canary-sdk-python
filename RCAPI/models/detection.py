import six

class Detection(object):
  def __init__(self, detection):
    self._detection = detection

  def to_json(self):
    orig_json = self.__dict__
    non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
    return non_empty_json

  @property
  def type(self):
    return self._detection.get('type')

  @property
  def id(self):
    return self._detection.get('id')
  
  @property
  def attributes(self):
    return Attributes(attributes=self._detection.get('attributes'))

  @property
  def hostname(self):
    return self._detection.get('hostname')
  
  @property
  def username(self):
    return self._detection.get('username')

  @property
  def endpoint(self):
    return ItemDetails(details=(self._detection.get('relationships')).get('affected_endpoint'))

  @property
  def identity(self):
    return ItemDetails(details=(self._detection.get('relationships')).get('affected_endpoint_user'))

  @property
  def detection(self):
    return ((self._detection.get('links')).get('self')).get('href')

  @property
  def timeline(self):
    return ((self._detection.get('links')).get('activity_timeline')).get('href')

  @property
  def detectors(self):
    return ((self._detection.get('links')).get('detectors')).get('href')

class ItemDetails(object):
  def __init__(self, details):
    self._details = details
  
  @property
  def links(self):
    return (self._details.get('links')).get('related')

  def type(self):
    return (self._details.get('data')).get('type')

  def id(self):
    return (self._details.get('data')).get('id')

class Attributes(object):
  def __init(self, attributes):
    self._attributes = attributes
  
  @property
  def headline(self):
    return self._attributes.get('headline')
  
  @property
  def confirmed_at(self):
    return self._attributes.get('confirmed_at')
  
  @property
  def summary(self):
    return self._attributes.get('summary')
  
  @property
  def severity(self):
    return self._attributes.get('severity')
  
  @property
  def last_activity_seen(self):
    return self._attributes.get('last_activity_seen_at')
  
  @property
  def primary_class(self):
    return (self._attributes.get('classification')).get('superclassification')
  
  @property
  def sub_class(self):
    return (self._attributes.get('classification')).get('subclassification')

  @property
  def occurence_time(self):
    return self._attributes.get('time_of_occurence')
  
  @property
  def acknowledged(self):
    return self._attributes.get('last_acknolwedged_at')
  
  @property
  def acknowledged_by(self):
    return UserInfo(ackinfo=self._attributes.get('last_acknowledged_by'))

  @property
  def remediated_status(self):
    return RemediatedStatus(remediatedstatus=self._attributes.get('last_remediated_status'))

  @property
  def marked_at(self):
    return self._attributes.get('marked_at')

class RemediatedStatus(object):
  def __init__(self, remediatedstatus):
    self._remediated_status = remediatedstatus
  
  @property
  def reason(self):
    return self._remediated_status.get('reason')

  def state(self):
    return self._remediated_status.get('remediation_state')

  def marked_by(self):
    return UserInfo(userinfo=self._remediated_status.get('marked_by'))

class UserInfo(object):
  def __init__(self, userinfo):
    self._user_info = userinfo

  @property
  def type(self):
    return self._user_info.get('type')
  
  @property
  def id(self):
    return (self._user_info.get('attributes')).get('id')
  
  @property
  def email(self):
    return (self._user_info.get('attributes')).get('email')
  
  @property
  def name(self):
    return (self._user_info.get('attributes')).get('name')
  
  @property
  def user(self):
    return (self._user_info.get('attributes')).get('name_and_email')

class UpdateRemedatedStatus(object):
  def __init__(self, **kwargs):
    status_types = ['remediated', 
                    'not_remediated_false_positive',
                    'not_remediated_sanctioned_activity', 
                    'not_remediated_unwarranted']

    self.remediation_state = kwargs.get('remediation_state', None)
    self.comment = kwargs.get('comment', None)

    if self.remediation_state not in status_types:
      raise Exception("Error! Remediation status {0} not supported.".format(self.remediation_state))
    
  def to_json(self):
    orig_json = self.__dict__
    non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
    return non_empty_json
