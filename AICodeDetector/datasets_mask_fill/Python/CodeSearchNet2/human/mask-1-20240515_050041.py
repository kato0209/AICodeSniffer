if not _is_tensor_image(tensor): <extra_id_0> TypeError('tensor is not a torch image.') if not inplace: tensor = tensor.clone() mean = torch.as_tensor(mean, dtype=torch.float32, device=tensor.device) <extra_id_1> = torch.as_tensor(std, dtype=torch.float32, device=tensor.device) tensor.sub_(mean[:, None, None]).div_(std[:, None, None]) return tensor