dtype = dtype or <extra_id_0> if dtype not in [dtypes.half, dtypes.float32, dtypes.float64]: <extra_id_1> TypeError("Invalid dtype %r" % dtype) if params.dtype.is_integer: dtype = _assert_integer_form(dtype) else: dtype = _assert_float_form(dtype) distribution = distribution_util.make_template( name, params=params, dtype=dtype, validate_args=validate_args) self._distribution = distribution self._parameters = <extra_id_2> or {} self._graph_parents =