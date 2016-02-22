def value_at_keypath(obj, keypath):
  """
  Returns value at given key path which follows dotted-path notation.

    >>> x = dict(a=1, b=2, c=dict(d=3, e=4, f=[2,dict(x='foo', y='bar'),5]))
    >>> assert value_at_keypath(x, 'a') == 1
    >>> assert value_at_keypath(x, 'b') == 2
    >>> assert value_at_keypath(x, 'c.d') == 3
    >>> assert value_at_keypath(x, 'c.e') == 4
    >>> assert value_at_keypath(x, 'c.f.0') == 2
    >>> assert value_at_keypath(x, 'c.f.-1') == 5
    >>> assert value_at_keypath(x, 'c.f.1.y') == 'bar'

  """
  for part in keypath.split('.'):
    if isinstance(obj, dict):
      obj = obj.get(part, {})
    elif type(obj) in [tuple, list]:
      obj = obj[int(part)]
    else:
      obj = obj.getattr(part, {})
  return obj


def set_value_at_keypath(obj, keypath, val):
  """
  Sets value at given key path which follows dotted-path notation.

  Each part of the keypath must already exist in the target value
  along the path.

    >>> x = dict(a=1, b=2, c=dict(d=3, e=4, f=[2,dict(x='foo', y='bar'),5]))
    >>> assert set_value_at_keypath(x, 'a', 2)
    >>> assert value_at_keypath(x, 'a') == 2
    >>> assert set_value_at_keypath(x, 'c.f.-1', 6)
    >>> assert value_at_keypath(x, 'c.f.-1') == 6
  """
  parts = keypath.split('.')
  for part in parts[:-1]:
    if isinstance(obj, dict):
      obj = obj[part]
    elif type(obj) in [tuple, list]:
      obj = obj[int(part)]
    else:
      obj = obj.getattr(part)
  last_part = parts[-1]
  if isinstance(obj, dict):
    obj[last_part] = val
  elif type(obj) in [tuple, list]:
    obj[int(last_part)] = val
  else:
    setattr(obj, last_part, val)
  return True

