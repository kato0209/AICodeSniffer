shape = array_ops.shape(tensor) # Make sure the input <extra_id_0> is 2D. shape[0], shape[1] = shape[1], shape[0] tensor = array_ops.reshape(tensor, [-1, shape[2]]) # Make sure the input has 4 dimensions. shape[3], shape[4] = shape[3], shape[4] <extra_id_1> array_ops.tile(tensor, array_ops.concat(0, [n, n, -1])) <extra_id_2> _squeeze(input, axis=None, name=None,