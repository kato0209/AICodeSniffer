<extra_id_0> = <extra_id_1> hair_mask = tf.cast(hair[..., -1:] <= 0, dtype) top_mask = tf.cast(top[..., -1:] <= 0, dtype) pants_mask = tf.cast(pants[..., -1:] <= 0, dtype) char = (skin * hair_mask) + <extra_id_2> char = (char * top_mask) + top char = (char * pants_mask) + pants return char