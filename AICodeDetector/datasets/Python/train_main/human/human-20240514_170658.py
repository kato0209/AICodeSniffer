
  dummy_mvndiag = tfd.MultivariateNormalDiag(
      scale_diag=tf.ones([0], dtype=dtype))
  dummy_mvndiag.covariance = lambda: dummy_mvndiag.variance()[..., tf.newaxis]
  return dummy_mvndiag