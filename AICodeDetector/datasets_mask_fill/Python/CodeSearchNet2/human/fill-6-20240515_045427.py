hostname = urlparse(url).hostname if 'n.miaopai.com' == hostname: smid = match1(url, r'n\.miaopai\.com/media/([^.]+)') miaopai_download_by_smid(smid, output_dir, merge, info_only) else: output_dir = get_temp_dir('yixia','miaopai')
    if info_only: return

    if if 'miaopai.com' in hostname: #Miaopai yixia_download_by_scid = yixia_miaopai_download_by_scid site_info = "Yixia Miaopai" scid = match1(url, r'miaopai\.com/show/channel/([^.]+)\.htm') or \ match1(url, r'miaopai\.com/show/([^.]+)\.htm') or \ match1(url, r'm\.miaopai\.com/show/channel/([^.]+)\.htm') or \