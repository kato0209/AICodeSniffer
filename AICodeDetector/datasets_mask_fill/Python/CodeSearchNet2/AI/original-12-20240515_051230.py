
    if distribution_util.is_scalar(self.distribution.mean):
      return self.distribution.mean()
    if distribution_util.is_scalar(self.distribution.mean_log_det):
      return self.distribution.mean_log_det()
    if distribution_util.is_scalar(self.distribution.variance):
      return math_ops.square(self.distribution.variance)
    if distribution_util.is_scalar(self.distribution.stddev):
      return math_ops.sqrt(self.distribution.stddev)
    return self.distribution.mean()

  def _expand