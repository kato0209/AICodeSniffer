
    with self._name_scope(name):
      return (self.df * self.scale_operator.log_abs_determinant() +
              0.5 * self.df * self.dimension * math.log(2.) +
              self._multi_lgamma(0.5 * self.df, self.dimension))