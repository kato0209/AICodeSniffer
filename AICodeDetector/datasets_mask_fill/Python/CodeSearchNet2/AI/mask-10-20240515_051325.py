if self.event_shape.is_fully_defined(): # If we are <extra_id_0> in <extra_id_1> mode or <extra_id_2> mode then we want to know # both batch and event shape. # In either graph mode, we will always <extra_id_3> a reshape which # will be used for batch norm and event shape inference. if not context.executing_eagerly(): return fn() with self.event_shape.as_list(event_shape_list): if static_event_shape_list is not None: for event_shape in static_event_shape_list: