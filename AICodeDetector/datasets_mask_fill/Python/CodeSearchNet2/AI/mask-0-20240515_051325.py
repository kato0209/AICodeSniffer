if <extra_id_0> and not dtype.is_compatible_with(struct.dtype): raise ValueError("Nested structures do not support " "conversion between <extra_id_1> and " "tf.compat.v1.convert_to_tensor: %s" % struct) if isinstance(struct, tuple): return tuple( _nested_convert_to_tensor(substructure, dtype, name) for substructure in struct) <extra_id_2> isinstance(struct, dict): return _nested_convert_to_tensor(struct, dtype, name) elif isinstance(struct, tensor_array_