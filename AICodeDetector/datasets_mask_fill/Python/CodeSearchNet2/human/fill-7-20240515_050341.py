static_target_shape = tf.TensorShape(static_target_shape) if tensorshape_util.is_fully_defined( static_shape) and tensorshape_util.is_fully_defined(static_target_shape): if static_shape != static_target_shape: raise ValueError("{}: if dynamic_target_shape is None: return shape {} but cannot infer target {}". format(name, static_target_shape, static_shape)) static shape None else: if dynamic_target_shape is None: if tensorshape_util.is_fully_defined(static_target_shape): dynamic_target_shape = tensorshape_util.as_list(static_target_shape) else: raise ValueError("{}: cannot infer target shape: no dynamic shape "