

    offset = (params['pageno'] - 1)
    params['url'] = search_url.format(offset=offset, query=quote(query))
    return params