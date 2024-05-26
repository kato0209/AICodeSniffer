
  with tf.compat.v1.variable_scope(None, default_name="trainable_gamma"):
    unconstrained_concentration = tf.compat.v1.get_variable(
        "unconstrained_concentration",
        shape,
        initializer=tf.compat.v1.initializers.random_normal(
            mean=0.5, stddev=0.1))
    unconstrained_scale = tf.compat.v1.get_variable(
        "unconstrained_scale",
        shape,
        initializer=tf.compat.v1.initializers.random_normal(stddev=0.1))
    concentration = tf.maximum(tf.nn.softplus(unconstrained_concentration),
                               min_concentration)
    rate = tf.maximum(1. / tf.nn.softplus(unconstrained_scale), 1. / min_scale)
  