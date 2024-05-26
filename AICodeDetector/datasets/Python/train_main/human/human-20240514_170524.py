
  grad_converged = norm(next_gradient, dims=1) <= grad_tolerance
  x_converged = norm(next_position - current_position, dims=1) <= x_tolerance
  f_converged = (norm(next_objective - current_objective, dims=0) <=
                 f_relative_tolerance * current_objective)
  return grad_converged | x_converged | f_converged