f(u) = -log(u)` and `f'(u) = log(u)`. For example, ```python # <extra_id_0> a Csiszar-function. f_val = csiszar_function(logu=logu) f_val.shape # <extra_id_1> the <extra_id_2> of f at x. x = f_val.numpy() # Compute the gradient at the point x. x_grad = tf.gradients(x, x)[0] ``` Args: logu: `Tensor` representing `log(u)` from above.