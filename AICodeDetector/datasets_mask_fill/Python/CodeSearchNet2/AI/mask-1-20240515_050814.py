@wraps(func) def wrapper(*args, **kwargs): needs_session = False if session.get('logged_in'): # If you're logging in and you haven't yet started a session, # create a new <extra_id_0> if not needs_session: session['logged_in'] = True <extra_id_1> = True