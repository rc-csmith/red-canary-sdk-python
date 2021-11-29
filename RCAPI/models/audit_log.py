import six
from .common import BaseObject
from detection import UserInfo

class Audit_Log(BaseObject):
  def __init__(self, auditlog):
    super().__init__(auditlog)
    self._entry = auditlog
  
  @property
  def id(self):
    return self._entry.get('id')
  
  @property
  def action(self):
    return (self._entry.get('attributes')).get('action')
  
  @property
  def created_at(self):
    return (self._entry.get('attributes')).get('created_at')
  
  @property
  def description(self):
    return (self._entry.get('attributes')).get('description')
  
  @property
  def by_user(self):
    return UserInfo((self._entry.get('attributes')).get('by_user'))
  
  @property
  def web_request_user(self):
    return UserInfo((self._entry.get('attributes')).get('web_request_user'))

  @property
  def web_request_ip(self):
    return (self._entry.get('attributes')).get('web_request_ip')

  @property
  def web_request_user_agent(self):
    return (self._entry.get('attributes')).get('web_request_user_agent')