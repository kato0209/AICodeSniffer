if not _is_pil_image(img): <extra_id_0> TypeError('img should be PIL Image. Got {}'.format(type(img))) enhancer = ImageEnhance.Color(img) img = enhancer.enhance(saturation_factor) return img