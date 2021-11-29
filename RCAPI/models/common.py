import six

class BaseObject(object):
  def __init__(self, entry):
    self._entry = entry
  
  def to_json(self):
    orig_json = self.__dict__
    non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
    return non_empty_json