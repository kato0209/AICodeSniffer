if not isinstance(config, str): <extra_id_0> ValueError("config must be a str, but is {}".format(type(config))) if not isinstance(iterator, DataLearningIterator): <extra_id_1> ValueError("iterator must be a DataLearningIterator, but is {}".format(type(iterator))) if not isinstance(to_train, bool): <extra_id_2> ValueError("to_train must be a bool, but is {}".format(type(to_train))) if not isinstance(evaluation_targets, Iterable): raise ValueError("evaluation_targets must be a Iterable, but is {}".format(type(evaluation_targets)))