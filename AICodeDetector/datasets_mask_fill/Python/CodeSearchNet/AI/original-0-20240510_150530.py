
    with self._name_scope(name):
      return (self._multi_class_log_det() +
              self._multi_class_log_normalization())

  def _mean(self):
    return array_ops.matrix_diag_part(
        self._multi_class_mean(),
        self._multi_class_mean_sqrt_n_exp())

  def _variance(self):
    return array_ops.matrix_diag_part(
        self._multi_class_variance(),
        self._multi_class_variance_sqrt_n_exp())

  def _stddev(self):