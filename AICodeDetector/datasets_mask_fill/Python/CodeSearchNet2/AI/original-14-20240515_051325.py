
  filenames = []
  for _ in range(batch_size):
    fn = os.path.join(FLAGS.test_tmpdir, 'input_%d' % _)
    filenames.append(fn)
    contents = []
    for _ in range(batch_size):
      contents.append(np.random.randint(0, 255, (1, 32, 32, 3)))
    contents = np.array(contents).reshape((batch_size, 1))
    yield (filenames, contents)


def build_fake_data(batch_size, fake_data_dir, fake_data