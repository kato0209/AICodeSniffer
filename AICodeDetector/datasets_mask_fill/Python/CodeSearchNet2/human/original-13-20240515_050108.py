
    with tf.compat.v1.name_scope(name, 'MixtureSameFamily_params_size',
                                 [num_components, component_params_size]):
      num_components = tf.convert_to_tensor(
          value=num_components, name='num_components', dtype_hint=tf.int32)
      component_params_size = tf.convert_to_tensor(
          value=component_params_size, name='component_params_size')

      num_components = dist_util.prefer_static_value(num_components)
      component_params_size = dist_util.prefer_static_value(
          component_params_size)

      return num_components + num_components * component_params_size