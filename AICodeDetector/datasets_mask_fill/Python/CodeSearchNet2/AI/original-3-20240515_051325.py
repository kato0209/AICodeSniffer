
  if block_sizes is None:
    block_sizes = [None] * len(bijectors)
  if len(block_sizes)!= len(bijectors):
    raise ValueError(
        'block_sizes must have the same length as bijectors.')
  for block_size, bijector in zip(block_sizes, bijectors):
    if not bijector.is_constant_jacobian:
      raise ValueError(
          'All bijectors must have the same number of '
          'constant jacobian.')
    if block_size is None:
      block_size = array_ops.