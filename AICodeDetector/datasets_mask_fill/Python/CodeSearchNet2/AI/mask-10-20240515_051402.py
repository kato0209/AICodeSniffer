return self._mode_ def _sample_n(self, n, seed=None): # The sampling <extra_id_0> is not documented in the <extra_id_1> class. return self._sample_n_impl( n, self._default_event_space_bijector, self._default_event_space_bijector_kwargs, self._sample_n_and_log_prob, self._log_prob, self._sample_n, seed) def _log_prob(self, x): return self._log_unnormalized_prob(x) -