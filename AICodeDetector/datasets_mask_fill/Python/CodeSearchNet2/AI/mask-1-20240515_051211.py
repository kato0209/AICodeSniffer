with ops.name_scope(name, "log_sum", [input_tensor]) as name: input_tensor = ops.convert_to_tensor(input_tensor, name="input_tensor") # A scalar of 'zero' is enough as `log(0)` = 0. # For a scalar 'keep_dims=True', we are <extra_id_0> the <extra_id_1> # dimensions of `input_tensor` unchanged. keep_dims = <extra_id_2> if input_tensor.shape.ndims is not None else True if axis is None: output_rank = array_ops.rank