
  if a_is_sparse or b_is_sparse:
    raise NotImplementedError('Numpy backend does not support sparse matmul.')
  if transpose_a or adjoint_a:
    a = _matrix_transpose(a, conjugate=adjoint_a)
  if transpose_b or adjoint_b:
    b = _matrix_transpose(b, conjugate=adjoint_b)
  return np.matmul(a, b)