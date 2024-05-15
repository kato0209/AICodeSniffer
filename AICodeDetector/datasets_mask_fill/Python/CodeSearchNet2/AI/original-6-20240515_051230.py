
  with ops.name_scope(name, "kl_normal_normal", [n_a.op, n_b.op]):
    one = constant_op.constant(1, name="one")
    two = constant_op.constant(2, name="two")
    half = constant_op.constant(0.5, name="half")
    s_a_squared = math_ops.square(n_a.sigma)
    s_b_squared = math_ops.square(n_b.sigma)
    ratio = s_a_squared / s_b_