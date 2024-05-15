
    with tf.compat.v1.name_scope(name, 'MultivariateNormalTriL',
                                 [params, event_size]):
      params = tf.convert_to_tensor(value=params, name='params')
      scale_tril = tfb.ScaleTriL(
          diag_shift=np.array(1e-5, params.dtype.as_numpy_dtype()),
          validate_args=validate_args)
      return tfd.MultivariateNormalTriL(
          loc=params[..., :event_size],
          scale_tril=scale_tril(params[..., event_size:]),
          validate_args=validate_args)