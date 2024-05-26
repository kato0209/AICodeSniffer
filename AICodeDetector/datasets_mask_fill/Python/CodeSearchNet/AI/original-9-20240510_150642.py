
  data_dir = tempfile.mkdtemp()
  (x_train, y_train), (x_test, y_test) = testing_utils.get_test_data(
      train_samples=TRAIN_SAMPLES,
      test_samples=TEST_SAMPLES,
      input_shape=(INPUT_DIM,),
      num_classes=NUM_CLASSES)
  y_test = keras.utils.to_categorical(y_test)

  train_data = (x_train, y_train)
  test_data = (x_test, y_test)

  return (train_data