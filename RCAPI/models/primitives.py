from RCAPI.models.common import BaseObject

class File(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry.get('attributes')
  
  @property
  def md5(self):
    return self._entry.get('md5')
  
  @property
  def sha256(self):
    return self._entry.get('sha256')

  @property
  def path(self):
    return self._entry.get('path')
  
  @property
  def file_type(self):
    return self._entry.get('file_type')
  
  @property
  def binary(self):
    return Binary(self._entry.get('binary'))

class Binary(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry.get('attributes')
  
  @property
  def md5(self):
    return self._entry.get('md5')
  
  @property
  def sha256(self):
    return self._entry.get('sha256')
  
  @property
  def digital_signature(self):
    return BinaryDigitalSignature(self._entry.get('digital_signature'))
  
  @property
  def internal_name(self):
    return self._entry.get('internal_name')

class BinaryDigitalSignature(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry.get('attributes')
  
  @property
  def publisher(self):
    return self._entry.get('publisher')
  
  @property
  def issuer(self):
    return self._entry.get('issuer')
  
  @property
  def subject(self):
    return self._entry.get('subject')
  
  @property
  def product(self):
    return self._entry.get('product')
  
  @property
  def signing_time(self):
    return self._entry.get('signing_time')

class IpAddress(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry.get('attributes')

  @property
  def ip(self):
    return self._entry.get('ip_address')
  
  @property
  def defanged(self):
    return self._entry.get('ip_address_defanged')
  
  @property
  def reverse_dns(self):
    return self._entry.get('ip_address_reverse_dns')

  @property
  def matches_rfc_1918(self):
    return self._entry.get('ip_address_matches_rfc_1918?')
  
  @property
  def matches_rfc_4193(self):
    return self._entry.get('ip_address_matches_rfc_4193?')

  @property
  def is_link_local(self):
    return self._entry.get('ip_address_is_link_local?')

class Domain(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry.get('attributes')

  @property
  def name(self):
    return self._entry.get('name')
  
  @property
  def defanged(self):
    return self._entry.get('name_defanged')
  
  @property
  def whois_org(self):
    return (self._entry.get('whois')).get('organization')

class RegistryKey(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry.get('attributes')
  
  @property
  def path(self):
    return self._entry.get('path')

class OperatingSystemProcess(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry.get('attributes')
  
  @property
  def started_at(self):
    return self._entry.get('started_at')
  
  @property
  def operating_system_pid(self):
    return self._entry.get('operating_system_pid')
  
  @property
  def native_id(self):
    return self._entry.get('native_id')
  
  @property
  def image(self):
    return File(self._entry.get('image'))
  
  @property
  def command_line(self):
    return ProcessCommandLine(self._entry.get('command_line'))
  
class ProcessCommandLine(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry.get('attributes')
  
  @property
  def raw(self):
    return self._entry.get('command_line')
  
  @property
  def decoded(self):
    return self._entry.get('command_line_decoded')
  
  @property
  def identified_encodings(self):
    return self._entry.get('identified_encodings')

class MacAddress(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    self._entry = entry.get('attributes')
  
  @property
  def address(self):
    return self._entry.get('address')

class EndpointHostname(BaseObject):
  def __init__(self, entry):
    super().__init__(entry)
    for key in entry['attributes']:
      self.__dict__[key] = entry['attributes'][key]