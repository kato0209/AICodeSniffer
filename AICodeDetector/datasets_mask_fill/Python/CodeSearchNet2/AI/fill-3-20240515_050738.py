if not title: title = '' if not output_dir: output_dir = ''


def fetch_urls(vid, title, output_dir, merge=False): if not merge: if not info_only: download_urls([vid], title, output_dir, merge=merge) else: download_urls(vid, title, output_dir, merge=merge) else: if not info_only: download_urls(vid, title, output_dir, merge=merge) else: