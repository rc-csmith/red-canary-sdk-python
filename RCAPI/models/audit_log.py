from common import BaseObject
from general import PortalUser

class AduitLog(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry
  
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
    return PortalUser((self._entry.get('attributes')).get('by_user'))
  
  @property
  def web_request_user(self):
    return PortalUser((self._entry.get('attributes')).get('web_request_user'))

  @property
  def web_request_ip(self):
    return (self._entry.get('attributes')).get('web_request_ip')

  @property
  def web_request_user_agent(self):
    return (self._entry.get('attributes')).get('web_request_user_agent')