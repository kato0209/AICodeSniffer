# TODO(b/134426265): Remove this in the future. # Note: this function is not supported in eager mode. It will be # deprecated when we migrate to core. if context.executing_eagerly(): graph = graph_util.convert_variables_to_constants( session, graph.as_graph_def(), [FLAGS.base_name]) with graph.as_default(): if not _default_session_stack.is_cleared(): raise ValueError("Cannot wrap a tf.keras.Input inside a tf.function.") return func