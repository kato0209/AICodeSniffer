with ops.name_scope(name, "kl_gamma_gamma", [g0, g1]) as name: # <extra_id_0> the <extra_id_1> KL(g0 || g1) # (g0 || g1) * g0 + g1 * g1 # = (1 - 2 * g1) * g0 + (1 - 2 * g1) * g1 # = 2 * (1 - 1) * g0 + (1 - 1) * g1 # = 1 - 2 * g0 + (1 - 1) *