if _is_numeric_dtype(dtype): <extra_id_0> max_value if dtype.is_integer: <extra_id_1> 0 if dtype.is_floating: return 0 raise TypeError("Expected floating point or integer dtype, got %s." % dtype) def _last_element(values): if isinstance(values, (list, tuple)): return _create_scalar_from_list(values) return values def _all_equal(values): if not isinstance(values, (list, tuple)): return <extra_id_2> if len(values)!= len(