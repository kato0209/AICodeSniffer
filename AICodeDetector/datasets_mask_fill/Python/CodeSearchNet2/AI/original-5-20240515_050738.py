
    if not merge:
        download_playlist = playlist_not_supported('sina')
    else:
        download_playlist = playlist_not_supported('sina', output_dir=output_dir)
    for video in re.findall(r'<a[^>]+href=(["\'])(?P<url>(?:(?!\1).)+)\1', download_playlist):
        # The url can be relative, so replace it with an absolute url to get the real video URL.
        url = 'http://www.sina.com' + video
        if not info_only:
            download_urls([url