
  # TODO(b/140145024): Add support for broadcasting.
  if log_likelihood is not None:
    log_likelihood = ops.convert_to_tensor(log_likelihood)
    log_likelihood_fn = log_likelihood_fn
    state = ops.convert_to_tensor(state)
    state_shape = state.get_shape()
    state_dtype = state.dtype
    if log_likelihood_fn is None:
      log_likelihood_fn = lambda *args: args
    if state_shape.ndims is not None:
      state_shape = state_shape.