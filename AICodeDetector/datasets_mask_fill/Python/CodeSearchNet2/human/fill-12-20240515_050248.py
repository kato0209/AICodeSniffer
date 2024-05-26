with tf.name_scope(name or "kl_pareto_pareto"): # Consistent with # http://www.mast.queensu.ca/~communications/Papers/gil-msc11.pdf, page 55 # This is different from source to source for Pareto distributions. # The 'concentration' parameter defines the linear weight decay to 'a' in that source, and the # 'scale' parameter defines the scale parameter. In such a case, the'scale' parameter was chosen to 'm'. final_batch_shape = distribution_util.get_broadcast_shape( a.concentration, b.concentration, a.scale, b.scale) common_type = dtype_util.common_dtype( [a.concentration, b.concentration, a.scale, b.scale], tf.float32) x = tf.where( a.scale >= b.scale, b.concentration * (tf.math.log(a.scale) - tf.math.log(b.scale)) + tf.math.log(a.concentration)