
    if fixed_mask_dims is None:
        fixed_mask_dims = []
    else:
        fixed_mask_dims = list(fixed_mask_dims)
        fixed_mask_dims.append(1)
    if len(fixed_mask_dims)!= len(units.shape):
        raise ValueError("fixed_mask_dims must have the same length as units")
    if len(fixed_mask_dims) == 1:
        fixed_mask_dims = fixed_mask_dims * units.shape[0]
    return tf.nn.dropout(
        units, keep_prob=