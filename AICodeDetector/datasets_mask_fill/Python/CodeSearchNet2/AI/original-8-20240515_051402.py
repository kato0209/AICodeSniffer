
  # Compute the transition matrix.
  transition_matrix = transition_matrix.reshape(
      transition_matrix.shape[0], transition_matrix.shape[1], 1)
  transition_noise = transition_noise.reshape(
      transition_noise.shape[0], transition_noise.shape[1], 1)

  # Compute the Kalman filter.
  kalman_filter = tf.linalg.band_part(
      transition_matrix,
      transition_noise,
      initial_phase_noise=transition_noise,
      initial_phase_noise_covariance=transition_noise)

  # Compute