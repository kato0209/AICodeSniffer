
  with tf.name_scope("logsum_expbig_minus_expsmall"):
    return tf.math.log1p(-tf.exp(small - big)) + big