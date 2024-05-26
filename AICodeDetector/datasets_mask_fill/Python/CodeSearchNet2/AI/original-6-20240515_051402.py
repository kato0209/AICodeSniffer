
  if perm is None:
    return
  if not isinstance(perm, (list, tuple)):
    perm = [perm]
  for p in perm:
    if not isinstance(p, (list, tuple)):
      raise TypeError("Each element of perm must be a list or tuple.")
    if len(p)!= 2:
      raise ValueError("Each element of perm must be a 2-element tuple.")
    if not all(isinstance(p[0], int) and p[0] > 0 for p in perm):
      raise ValueError("Each element of perm must be a positive integer.")
    if not isinstance(