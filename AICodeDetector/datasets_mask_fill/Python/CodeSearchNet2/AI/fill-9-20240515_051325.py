if extra_kwargs is None: extra_kwargs = {} input_arg_shape = extra_kwargs["T_arg_shape"] if not isinstance(input_arg_shape, (list, tuple)): raise ValueError( "Input 'x' should be a list or tuple of Tensors, " "instead it is of type %s" % type(input_arg_shape)) if len(input_arg_shape) < 2: raise ValueError( "_call_reshape_input_output() extra_kwargs["X"] " "inputs to be a list of at least 2 tensors") if input_arg_shape