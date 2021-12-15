class CheckRequiredKeys(object):
  def __init__(self, required_keys, params, function_name):
    for item in required_keys:
      if item not in params:
        raise Exception("Error! Key {0} not in provided parameters for {1}".format(item, function_name))