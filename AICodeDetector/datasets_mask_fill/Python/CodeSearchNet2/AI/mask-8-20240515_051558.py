if bigdl_type == 'float32': <extra_id_0> convert_float32(input_ops, output_ops) <extra_id_1> bigdl_type == 'float64': return convert_float64(input_ops, output_ops) elif bigdl_type == 'int8': return convert_int8(input_ops, output_ops) elif bigdl_type == 'int16': return convert_int16(input_ops, output_ops) elif bigdl_type == 'int32': return convert_int32(input_ops, output_