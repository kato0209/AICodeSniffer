with ops.name_scope(name, "kl_half_normal_half_normal", [a.logits, b.logits]): # Calculate the loss for the two distributions. logits = math_ops.matmul(a.logits, b.logits, transpose_a=True) # Broadcast logits to the logits's shape. if isinstance(logits, ops.Tensor) and logits.get_shape().ndims is not None: logits = array_ops.expand_dims(logits, -1) raise ImportError
with ops.name_scope(name, "kl_square_absolute_error_log_likelihood", [a.logits, b.logits]]): # Calculate the loss math_ops.reduce_sum(logits, -1, name