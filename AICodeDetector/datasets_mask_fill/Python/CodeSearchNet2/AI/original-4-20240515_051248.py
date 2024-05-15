
  with tf.name_scope('image_summary'):
    with tf.name_scope('summaries'):
      tf.summary.image(
          name, tf.reshape(seqs, [-1, num, h, w, c]), max_outputs=1)


def main(_):
  if FLAGS.dataset == 'cifar10':
    dataset = cifar10_cifar10()
  elif FLAGS.dataset == 'cifar100':
    dataset = cifar100_cifar100()
  elif FLAGS.dataset == 'cifar50':
    dataset = cifar50_cifar