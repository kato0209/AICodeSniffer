

    spec = make_module_spec(options, str(weight_file))

    try:
        with tf.Graph().as_default():
            module = hub.Module(spec)

            with tf.Session() as sess:
                sess.run(tf.global_variables_initializer())
                if hub_dir.exists():
                    shutil.rmtree(hub_dir)
                module.export(str(hub_dir), sess)
    finally:
    