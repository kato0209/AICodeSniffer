try: user = session.query(PasswordUser).filter( <extra_id_0> == username).one() except NoResultFound: <extra_id_1> AuthenticationError( "Username '%s' does not exist" % username) except MultipleResultsFound: <extra_id_2> AuthenticationError( "Username '%s' already exists" % username) except NoResultFound: raise AuthenticationError( "Username '%s' does not exist" % username) if