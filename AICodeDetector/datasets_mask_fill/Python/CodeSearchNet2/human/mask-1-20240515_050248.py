<extra_id_0> labels, config if params["analytic_kl"] and params["mixture_components"] != 1: <extra_id_1> NotImplementedError( "Using `analytic_kl` is only supported when `mixture_components = 1` " "since there's no closed form otherwise.") encoder = make_encoder(params["activation"], params["latent_size"], params["base_depth"]) decoder = make_decoder(params["activation"],