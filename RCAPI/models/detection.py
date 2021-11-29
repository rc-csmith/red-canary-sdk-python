import six
from RCAPI.models.tactic_technique import RelatedTechnique
from .common import BaseObject

class Detection(BaseObject):
  def __init__(self, detection):
    super().__init__(detection)
    self._entry = detection

  @property
  def id(self):
    return self._entry.get('id')
  
  @property
  def headline(self):
    return (self._entry.get('attributes')).get('headline')
  
  @property
  def confirmed_at(self):
    return (self._entry.get('attributes')).get('confirmed_at')
  
  @property
  def summary(self):
    return (self._entry.get('attributes')).get('summary')

  @property
  def severity(self):
    return (self._entry.get('attributes')).get('severity')
  
  @property
  def last_activity_seen_at(self):
    return (self._entry.get('attributes')).get('last_activity_seen_at')
  
  @property
  def classification(self):
    return ((self._entry.get('attributes')).get('classification')).get('superclassification')
  
  @property
  def subclassification(self):
    return ((self._entry.get('attributes')).get('classification')).get('subclassification')
  
  @property
  def time_of_occurrence(self):
    return (self._entry.get('attributes')).get('time_of_occurrence')
  
  @property
  def last_acknowledged_at(self):
    return (self._entry.get('attributes')).get('last_acknowledged_at')
  
  @property
  def last_acknowledged_by(self):
    return UserInfo((self._entry.get('attributes')).get('last_acknowledged_by'))

  @property
  def last_remediated_status(self):
    return RemediatedStatus((self._entry.get('attributes')).get('last_remediated_status'))
  
  @property
  def marked_at(self):
    return (self._entry.get('attributes')).get('marked_at')
  
  @property
  def hostname(self):
    return self._entry.get('hostname')
  
  @property
  def endpoint_id(self):
    return (((self._entry.get('relationships')).get('affected_endpoint')).get('data')).get('id')
  
  @property
  def identity_id(self):
    return (((self._entry.get('relationships')).get('related_endpoint_user')).get('data')).get('id')
  
  @property
  def username(self):
    return self._entry.get('username')

class Summary(BaseObject):
  def __init__(self, summary):
    super().__init__(summary)
    self._entry = summary

  @property
  def headline(self):
    return self._entry.get('headline')

  @property
  def confirmed_at(self):
    return self._entry.get('confirmed_at')
  
  @property
  def severity(self):
    return self._entry.get('severity')
  
  @property
  def remediated_status(self):
    return RemediatedStatus(self._entry.get('last_remediated_status'))

class RemediatedStatus(BaseObject):
  def __init__(self, remediatedstatus):
    super().__init__(remediatedstatus)
    self._entry = remediatedstatus

  @property
  def reason(self):
    return self._entry.get('reason')

  def state(self):
    return self._entry.get('remediation_state')

  def marked_by(self):
    return UserInfo(userinfo=self._entry.get('marked_by'))

class UserInfo(BaseObject):
  def __init__(self, userinfo):
    super().__init__(userinfo)
    self._entry = userinfo

  @property
  def type(self):
    return self._entry.get('type')
  
  @property
  def id(self):
    return (self._entry.get('attributes')).get('id')
  
  @property
  def email(self):
    return (self._entry.get('attributes')).get('email')
  
  @property
  def name(self):
    return (self._entry.get('attributes')).get('name')
  
  @property
  def user(self):
    return (self._entry.get('attributes')).get('name_and_email')

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

class Timeline(BaseObject):
  def __init__(self, timeline):
    super().__init__(timeline)
    self._entry = timeline
  
  @property
  def occurred_at(self):
    return (self._entry.get('attributes')).get('occurred_at')
  
  @property
  def analyst_notes(self):
    return (self._entry.get('attributes')).get('analyst_notes')

class Detector(BaseObject):
  def __init__(self, detector):
    super().__init__(detector)
    self._entry = detector
  
  @property
  def id(self):
    return self._entry.get('id')
  
  @property
  def name(self):
    return (self._entry.get('attributes')).get('name')
  
  @property
  def description(self):
    return (self._entry.get('attributes')).get('description')
  
  @property
  def contributing_intelligence(self):
    return (self._entry.get('attributes')).get('contributing_intelligence')
  
  @property
  def attack_technique_identifiers(self):
    return (self._entry.get('attributes')).get('attack_technique_identifiers')
  
  @property
  def technique(self):
    return RelatedTechnique((self._entry.get('relationships')).get('attack_techniques'))

class IOC(BaseObject):
  def __init__(self, ioc):
    super().__init__(ioc)
    self._entry = ioc

    type_dict = {
      'primitives.Binary':'binary',
      'primitives.File':'file',
      'primitives.BinaryDigitalSignature':'digsig',
      'primitives.Domain':'domain',
      'primitives.IpAddress':'ip',
      'primitives.RegistryKey':'regkey'
    }
    
    self._type = type_dict.get(self._entry.get('type'))

  @property
  def info(self):
    if self._type == 'file':
      return File(self._entry.get('attributes'))
    elif self._type == 'domain':
      return Domain(self._entry.get('attributes'))
    elif self._type == 'ip':
      return IP(self._entry.get('attributes'))
    elif self._type == 'regkey':
      return RegKey(self._entry.get('attributes'))
    else:
      return File(None)

class File(BaseObject):
  def __init__(self, file):
    super().__init__(file)
    self._file = file
  
  @property
  def md5(self):
    return self._file.get('md5')
  
  @property
  def sha256(self):
    return self._file.get('sha256')
  
  @property
  def path(self):
    return self._file.get('path')
  
  @property
  def file_type(self):
    return self._file.get('file_type')
  
  @property
  def binary(self):
    return Binary(self._file.get('binary'))
  
class RegKey(BaseObject):
  def __init__(self, regkey):
    super().__init__(regkey)
    self._regkey = regkey
  
  @property
  def path(self):
    return self._regkey.get('path')

class Binary(BaseObject):
  def __init__(self, binary):
    super().__init__(binary)
    self._binary = binary.get('attributes')
  
  @property
  def digital_signature(self):
    return DigSig(self._binary.get('digital_signature'))

  @property
  def internal_name(self):
    return self._binary.get('internal_name')
  
  @property
  def md5(self):
    return self._binary.get('md5')
  
  @property
  def sha256(self):
    return self._binary.get('sha256')
  
class DigSig(BaseObject):
  def __init__(self, digsig):
    super().__init__(digsig)
    self._digsig = digsig.get('attributes')

  @property
  def issuer(self):
    return self._digsig.get('issuer')
  
  @property
  def product(self):
    return self._digsig.get('product')
  
  @property
  def publisher(self):
    return self._digsig.get('publisher')
  
  @property
  def signing_time(self):
    return self._digsig.get('subject')

class Domain(BaseObject):
  def __init__(self, domain):
    super().__init__(domain)
    self._domain = domain
  
  @property
  def name(self):
    return self._domain.get('name')
  
  @property
  def name_defanged(self):
    return self._domain.get('name_defanged')

  @property
  def whois(self):
    return (self._domain.get('whois')).get('organization')

class IP(BaseObject):
  def __init__(self, ip):
    super().__init__(ip)
    self._ip = ip

  @property
  def ip_address(self):
    return self._ip.get('ip_address')
  
  @property
  def ip_address_defanged(self):
    return self._ip.get('ip_address_defanged')
  
  @property
  def ip_address_is_link_local(self):
    return self._ip.get('ip_address_is_link_local?')
  
  @property
  def ip_address_is_private(self):
    return self._ip.get('ip_address_matches_rfc_1918?')

  @property
  def ip_address_is_ula(self):
    return self._ip.get('ip_address_matches_rfc_4193')

  @property
  def ip_address_reverse_dns(self):
    return self._ip.get('ip_address_reverse_dns')