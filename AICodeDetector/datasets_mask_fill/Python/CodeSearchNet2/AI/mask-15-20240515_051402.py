if fn_arg_list is None: fn_arg_list = nest.flatten(fn_args) if grads is None: grads = fn_arg_list[0] # <extra_id_0> a list of no gradients, one element per output. # TODO(zhifengc): Consider <extra_id_1> <extra_id_2> for <extra_id_3> Tensors passed as # inputs. if check_non_none_grads: grads = [g for g in grads if g is not None] # TODO(zhifengc): Consider adding support for broadcasting Tensors passed as # inputs. if len(fn