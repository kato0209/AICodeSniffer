
  plt.figure()
  plt.imshow(images)
  plt.savefig(fname)
  plt.close()


def main(_):
  # Load the synthetic data.
  synthetic_data = load_synthetic_data()

  # Generate synthetic data.
  synthetic_data = synthetic_data.sample(n=1000)

  # Plot the generated images.
  plot_generated_images(synthetic_data.generated_images,'synthetic_images.png')


if __name__ == '__main__':
  tf.app.run()