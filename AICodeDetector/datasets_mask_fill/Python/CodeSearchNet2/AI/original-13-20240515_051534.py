
        if not isinstance(data_rdd, RDD):
            raise TypeError("data_rdd should be of type RDD")
        if batch_size <= 0:
            raise ValueError("batch_size should be greater than 0")

        if not isinstance(data_rdd, RDD):
            raise TypeError("data_rdd should be of type RDD")

        if batch_size == -1:
            raise ValueError("batch_size should be greater than 0")

        if not isinstance(data_rdd, RDD):