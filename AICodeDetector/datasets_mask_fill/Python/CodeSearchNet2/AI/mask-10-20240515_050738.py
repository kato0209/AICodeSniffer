if info_only: raise NotImplementedError('info_only=True is not <extra_id_0> anymore') if output_dir is None: output_dir = os.path.join(os.getcwd(), 'output') if not os.path.exists(output_dir): os.makedirs(output_dir) if merge: <extra_id_1> = ['ffmpeg', '-i', video_id, '-c', 'copy', '-bsf:v', '0', '-map', '0:v', '1:a', '-map', '0:a', 'copy', output_dir]