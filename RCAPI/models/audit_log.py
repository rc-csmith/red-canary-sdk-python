import six

def AuditLog(object):
  def __init__(self, auditlog):
    self._auditlog = auditlog
  
  def to_json(self):
    orig_json = self.__dict__
    non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
    return non_empty_json

  @property
  def type(self):
    return self._auditlog.get('type')
  
  @property
  def id(self):
    return self._auditlog.get('id')
  
  @property
  def attributes(self):
    return Attributes(self._auditlog.get('attributes'))

def Attributes(object):
  def __init__(self, attributes):
    self._attributes = attributes
  
  @property
  def action(self):
    return self._attributes.get('action')
  
  @property
  def created_at(self):
    return self._attributes.get('created_at')
  
  @property
  def description(self):
    return self._attributes.get('description')
  
  @property
  def by_user(self):
    return UserInfo(self._attributes.get('by_user'))
  
  @property
  def web_request_user(self):
    return UserInfo(self._attributes.get('web_request_user'))

  @property
  def web_request_ip(self):
    return self._attributes.get('web_request_ip')

  @property
  def web_request_user_agent(self):
    return self._attributes.get('web_request_user_agent')

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