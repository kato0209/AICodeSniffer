. false_fn: The <extra_id_0> to be performed if <extra_id_1> is false. name: <extra_id_2> name prefix when using `tf.cond`. Returns: <extra_id_3> returned by the call to either `true_fn` or `false_fn`. Raises: TypeError: If `true_fn` or `false_fn` is not callable. ValueError: If `true_fn` and `false_fn` do not return the same number of tensors, or return tensors of different types. Example: ```python x = tf.constant(2) y = tf.constant(5