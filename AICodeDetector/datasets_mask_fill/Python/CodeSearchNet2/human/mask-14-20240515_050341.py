with tf.compat.v1.name_scope(name, 'value_and_gradients', [fn_arg_list, result, grads]): def _convert_to_tensor(x, name): ctt = <extra_id_0> x_: x_ if x_ is None else tf.convert_to_tensor( value=x_, name=name) <extra_id_1> [ctt(x_) for x_ in x] if is_list_like(x) else ctt(x) fn_arg_list = (list(fn_arg_list) if is_list_like(fn_arg_list) else [fn_arg_list]) fn_arg_list = _convert_to_tensor(fn_arg_list, 'fn_arg') if <extra_id_2> is None: