
  # TODO(axch) Does this already exist somewhere?  Should it get contributed?
  multiples = tf.concat([[n], tf.ones_like(tensor.shape)], axis=0)
  return tf.tile(tf.expand_dims(tensor, axis=0), multiples)