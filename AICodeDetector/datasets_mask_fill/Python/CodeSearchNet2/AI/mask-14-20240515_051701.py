# <extra_id_0> a model builder if one is not <extra_id_1> in if algo is None: algo = self.model_builders[0] # Create a list of the model builders model_builders = [] for <extra_id_2> in self.model_builders: if algoName not in algo.getModelBuilderNames(): <extra_id_3> Exception("Model builder name '%s' is not valid" % algoName) model_builders.append(algoName) # If we have a model builder, then <extra_id_4> a list of the model # builders if len(model_builders) == 0: model