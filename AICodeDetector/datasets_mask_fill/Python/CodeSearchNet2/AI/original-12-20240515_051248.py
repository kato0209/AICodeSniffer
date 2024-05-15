
  # Note: the asymptotic series is zero-mean-centered for x < 0,
  # so we use tf.where(tf.is_nan(x), x, 0) = -inf.
  asymptotic_series_order = tf.where(
      tf.is_nan(series_order),
      tf.where(
          tf.is_nan(x) & tf.is_nan(series_order),
          tf.zeros_like(x),
          series_order,
          tf.zeros_like(series_order)))
  return asymp