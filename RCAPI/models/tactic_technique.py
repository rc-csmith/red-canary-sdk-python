import six

class TacticTechnique(object):
  def __init__(self,tactictechnique):
    self._item = tactictechnique
    self._tactic = 'AttackTactic'
    self._technique = 'AttackTechnique'

  def to_json(self):
    orig_json = self.__dict__
    non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
    return non_empty_json

  @property
  def type(self):
    return self._item.get('type')
  
  @property
  def name(self):
    return (self._item.get('attribute')).get('name')
  
  @property
  def identifier(self):
    if self._item.get('type') == self._tactic:
      return (self._item.get('attribute')).get('tactic_identifier')
    elif self._item.get('type') == self._technique:
      return (self._item.get('attribute')).get('technique_identifier')
    else:
      return None
  
  @property
  def description(self):
    if self._item.get('type') == self._tactic:
      return (self._item.get('attribute')).get('description')
    elif self._item.get('type') == self._technique:
      return (self._item.get('attribute')).get('technical_description')
    else:
      return None

  @property
  def source(self):
    if self._item.get('type') == self._tactic:
      return (self._item.get('attribute')).get('link')
    elif self._item.get('type') == self._technique:
      return (self._item.get('attribute')).get('source')
    else:
      return None
  
  @property
  def techniques(self):
    return RelatedTechnique((self._item.get('relationships')).get('attack_techniques'))

class RelatedTechnique(object):
  def __init__(self, technique):
    self._technique = technique
  
  @property
  def link(self):
    return (self._technique.get('links')).get('related')
  
  @property
  def type(self):
    return (self._technique.get('data')).get('type')
  
  @property
  def id(self):
    return (self._technique.get('data')).get('id')
  