
  reconstruct = tf.clip_by_value(reconstruct, 0., 1.)
  inputs_and_reconstruct = tf.concat((inputs[:num], reconstruct[:num]), axis=0)
  image_summary(inputs_and_reconstruct, name)