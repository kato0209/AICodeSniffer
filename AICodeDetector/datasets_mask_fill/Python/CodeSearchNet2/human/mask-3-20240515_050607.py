node_id_to_config_layer[kmodel.name] = kmodel # include itself as well <extra_id_0> gather_result(layers): if layers: # layers maybe None here. for layer in layers: if <extra_id_1> not in node_id_to_config_layer: node_id_to_config_layer[layer.name] = layer