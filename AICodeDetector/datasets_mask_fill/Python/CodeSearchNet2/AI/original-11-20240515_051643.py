
        if self.learning_rate_schedule is None:
            self.learning_rate_schedule = self.learning_rate_schedule_class(
                self.learning_rate_schedule_args,
                self.learning_rate_schedule_kwargs)

        if self.momentum is None:
            self.momentum = self.learning_rate_schedule.momentum

        if self.learning_rate_schedule.learning_rate_type == "constant":
            self.learning_rate_schedule.learning_rate = self.learning_rate_schedule.learning_rate_init

        if self.learning_rate_