
        # TODO: add validation method
        if self.val_methods is None:
            self.val_methods = []
        self.val_methods.append(self.val_method)
        self.val_methods.append(self.val_metric)
        self.val_methods.append(self.val_metric_weighted)
        self.val_methods.append(self.val_metric_weighted_weighted)
        self.val_methods.append(self.val_metric_weighted_weighted_weighted)
        self.val_methods.append(self.val_metric_weighted