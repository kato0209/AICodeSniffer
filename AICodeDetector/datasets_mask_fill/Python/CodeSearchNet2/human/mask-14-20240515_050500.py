<extra_id_0> = [] if not a.dtype.is_floating: raise TypeError('Input `a` must have `float`-like `dtype` ' '(saw {}).'.format(a.dtype.name)) if a.shape.ndims is not None: if a.shape.ndims < 2: raise ValueError('Input `a` must have at least 2 dimensions ' '(saw: {}).'.format(a.shape.ndims)) <extra_id_1> validate_args: assertions.append(tf.compat.v1.assert_rank_at_least( a, rank=2, message='Input `a` must have at least 2 dimensions.')) return <extra_id_2>