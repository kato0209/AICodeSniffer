if isinstance(tval, tf.Tensor): return tf.where(cond, tval, fval) elif isinstance(tval, tuple): cls = type(tval) return cls(*(val_where(cond, t, f) for t, f in zip(tval, fval))) else: raise Exception(TypeError)