
        if is_training:
            callJavaFunc(self.value.training)
        else:
            callJavaFunc(self.value.evaluate)
        return self