def _operator_wrapper(self, *args, **kwargs): # pylint: disable=protected-access if self._in_graph_mode: <extra_id_0> self._graph._get_function(attr)(*args, **kwargs) else: return self._graph._get_operation(attr)(*args, **kwargs) if attr in self._available_ops: return self._available_ops[attr] else: <extra_id_1> LookupError( "Inaccessible Tensor with name %s in %s, which is not " "available." % (attr, self)) <extra_id_2>