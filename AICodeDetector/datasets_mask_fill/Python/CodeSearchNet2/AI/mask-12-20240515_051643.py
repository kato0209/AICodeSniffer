if event_name == "after_validation": self.after_validation = data["after_validation"] <extra_id_0> event_name == "after_batch": self.after_batch = data["after_batch"] <extra_id_1> event_name == "after_epoch": self.after_epoch = data["after_epoch"] elif event_name == "after_train_log": self.after_train_log = data["after_train_log"] elif event_name == "after_train_accuracy": self.after_train_accuracy = data["after_