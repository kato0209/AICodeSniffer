return array_ops.shape(x) def _event_shape_tensor(self): return constant_op.constant([], dtype=dtypes.int32) def _event_shape(self): return tensor_shape.scalar() def _sample_n(self, n, seed=None): # Uniform <extra_id_0> must be <extra_id_1> from the open-interval `(0, 1)` rather # than `[0, 1)`. To do so, we use `np.finfo(self._dtype.as_numpy_dtype).tiny` # because it is the smallest, <extra_id_2>