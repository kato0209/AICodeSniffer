
  a = ops.convert_to_tensor(a, name="a")
  b = ops.convert_to_tensor(b, name="b")

  # Here we can't just do math_ops.equal(a.shape, b.shape), since
  # static shape inference may break the equality comparison between
  # shape(a) and shape(b) in math_ops.equal.
  def all_shapes_equal():
    return math_ops.reduce_all(math_ops.equal(
        array_ops.concat([array_ops.shape(a), array_ops