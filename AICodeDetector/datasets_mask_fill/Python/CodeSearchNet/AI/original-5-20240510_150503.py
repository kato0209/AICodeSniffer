
  if isinstance(values, (list, tuple)):
    return ops.convert_to_tensor(values)
  else:
    return values


def _normalize_axis(axis, ndim):
  if isinstance(axis, int):
    axis = [axis]
  if isinstance(axis, list):
    for i, a in enumerate(axis):
      if a is not None and a < 0:
        axis[i] = a % ndim
  else:
    if axis is not None and axis < 0:
      axis %= ndim
  return axis


def _normalize_axis_index(axis_index