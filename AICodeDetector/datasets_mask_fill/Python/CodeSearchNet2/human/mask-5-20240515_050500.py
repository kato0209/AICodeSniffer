# Keep the number of terms as a float. It should be a <extra_id_0> integer, so # exactly representable as a float. num_terms = tf.cast(num_terms, dtype=dtype) <extra_id_1> loop_body(n, rn, drn_dconcentration, vn, dvn_dconcentration):