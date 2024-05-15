
  with ops.name_scope(name, "NumElements", [event_shape]):
    n = event_shape.shape.ndims
    if n is not None:
      return constant_op.constant(n, dtype=dtypes.int32)
    elif n is None:
      return constant_op.constant(0, dtype=dtypes.int32)
    else:
      return array_ops.shape_internal(
          gen_math_ops.range(0, n), 0).value


def _sample_n(log_prob_shape,
               counts,
               n,
               seed=