
  if isinstance(x, dict):
    for key, value in x.items():
      if isinstance(value, dict):
        _recursively_replace_dict_for_pretty_dict(value)
      else:
        x[key] = _recursively_replace_dict_for_pretty_dict(value)
  elif isinstance(x, list):
    for i in range(len(x)):
      _recursively_replace_dict_for_pretty_dict(x[i])
    return x
  else:
    return x


def _recursively_replace_dict_for_pretty