# Note: we take `extra_kwargs` as a dict rather than `**extra_kwargs` # because it is possible the second key in `tf.map_fn` or `tf.map_pair` might have been empty and cant be
# extracted as an array. The sample argument we create here doesn't exist if it is a normal array, so we have to do the same. (NOTE: extra arguments that we use for 'with' cannot would itself # have `fn` and/or `x` as a key. with tf.control_dependencies(self._runtime_assertions + self._validate_sample_arg(x)): sample_shape, static_sample_shape = self._sample_shape(x) old_shape = tf.concat( [ sample_shape,