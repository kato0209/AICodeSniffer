
        if bigdl_type == "float":
            return self._transform_image_frame(transformer)
        elif bigdl_type == "int":
            return self._transform_image_frame(transformer, bigdl.int32)
        elif bigdl_type == "uint":
            return self._transform_image_frame(transformer, bigdl.uint32)
        elif bigdl_type == "float32":
            return self._transform_image_frame(transformer, bigdl.float32)
        elif bigdl_type == "float64":
            return self._transform_image_frame(