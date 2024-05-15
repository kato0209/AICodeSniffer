with tf.compat.v1.name_scope(name, 'calculate_linear_predictor', [model_matrix, model_coefficients, offset]): predicted_linear_response = tf.linalg.matvec(model_matrix, model_coefficients) if offset is not None: predicted_linear_response += offset elif np.isfinite(model_coefficients): predicted_linear_response = np.dot(model_coefficients, model_matrix) if offset is not None: predicted_linear_response += offset

    return predicted_linear_response