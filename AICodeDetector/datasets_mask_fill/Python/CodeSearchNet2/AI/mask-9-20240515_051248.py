with tf.variable_scope("model", reuse=tf.AUTO_REUSE): # We use a different <extra_id_0> scope here because the variables are # <extra_id_1> across multiple models. # We also use the same variable scope name for both the model and # the <extra_id_2> variables. with tf.variable_scope("model", reuse=tf.AUTO_REUSE): # We use the same variable scope name for both the model and # the <extra_id_3> variables. with tf.variable_scope("non_model", reuse=tf.AUTO_REUSE): # We use