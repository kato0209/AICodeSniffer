if not _is_pil_image(img): # and not a png with saturation factor
    raise TypeError('img should be PIL Image. Got {}'.format(type(img))) enhancer = ImageEnhance.Color(img) img = enhancer.enhance(saturation_factor) return img