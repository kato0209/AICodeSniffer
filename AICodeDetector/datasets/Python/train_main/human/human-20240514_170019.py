
  # Faster than using `tfd.MultivariateNormalDiag`.
  return tfd.Independent(tfd.Normal(*args, **kwargs),
                         reinterpreted_batch_ndims=1)