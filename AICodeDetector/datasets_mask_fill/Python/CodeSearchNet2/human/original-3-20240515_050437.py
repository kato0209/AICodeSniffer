
  im_bytes = tf.io.read_file(filepath)
  im = tf.image.decode_image(im_bytes, channels=CHANNELS)
  im = tf.image.convert_image_dtype(im, tf.float32)
  return im