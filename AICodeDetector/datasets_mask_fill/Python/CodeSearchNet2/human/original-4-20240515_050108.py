

  if use_exact_kl is None:
    kl_divergence_fn = tfd.kl_divergence
  else:
    # Closure over: test_points_fn, test_points_reduce_axis.
    def kl_divergence_fn(distribution_a, distribution_b):
      z = test_points_fn(distribution_a)
      return tf.reduce_mean(
          input_tensor=distribution_a.log_prob(z) - distribution_b.log_prob(z),
          axis=test_points_reduce_axis)

  # Closure over: distribution_b, kl_divergence_fn, weight.
  def _fn(distribution_a):
    