
  if target_log_prob is None:
    target_log_prob = tf.zeros([], dtype=tf.float32)
  if grads_target_log_prob is None:
    grads_target_log_prob = tf.zeros([], dtype=tf.float32)

  if maybe_expand:
    target_log_prob = tf.expand_dims(target_log_prob, axis=0)
    grads_target_log_prob = tf.expand_dims(grads_target_log_prob, axis=0)

  if state_gradients_are_stopped:
    target