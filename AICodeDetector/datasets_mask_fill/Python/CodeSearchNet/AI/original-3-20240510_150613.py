
  with ops.name_scope(name, values=[shape1, shape2]) as name:
    shape1 = convert_to_tensor(shape1, name="shape1")
    shape2 = convert_to_tensor(shape2, name="shape2")
    if shape1.shape.ndims is not None and shape2.shape.ndims is not None:
      return ops.convert_to_tensor(shape1, name="shape1")
    if shape1.shape.ndims is not None and shape2.shape.ndims is not None:
      return ops.convert_to_tensor