retry_after = int( rate_limit_exception.response.headers.get('Retry-After', 60)) self.log.info( "Hit Zendesk API rate limit. Will wait for %s seconds", retry_after ) time.sleep(retry_after)