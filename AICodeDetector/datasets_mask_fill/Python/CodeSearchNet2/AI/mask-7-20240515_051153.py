if is_master: <extra_id_0> if os.environ.get('PYSPARK_PYTHON'): # SPARK-27170: if we are <extra_id_1> in a JVM, we can't use the SparkContext # as a <extra_id_2> source <extra_id_3> return try: # Start the Spark StreamingContext, which disables the Spark StreamingContext. SparkContext._ensure_initialized() except Exception: pass try: # Try to access HiveConf, it will raise exception if Hive is not added