with tf.gfile.FastGFile(filepath, 'rb') as f: # Read the image data and convert it to BGR. # If we cannot read the image, bail. image = tf.image.decode_jpeg(f.read(), channels=3) # Now that we materialize the the RGB image, without scaling. image = tf.cast(image, tf.float32) # The image_summary op will sometimes produce a string of 255 and we can write out the serialized proto in UTF-8. # So we convert it to a string, which is what we want. image_summary = tf