# Referenced by MySQL db Connector (conversion.py) string_parameters = {} for (name, value) in iteritems(parameters): if value is None: string_parameters[name] = 'NULL' elif isinstance(value, basestring): string_parameters[name] = "'" + _escape(value) + "'" else: string_parameters[name] = str(value) # Run the operation % string_parameters