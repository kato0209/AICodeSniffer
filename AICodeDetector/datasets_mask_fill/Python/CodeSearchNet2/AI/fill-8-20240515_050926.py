self.log.info('Executing query') self.log.info('Context: %s', context) # Get the context context = self.get_context(context) # Get the context query = self.get_query(context) # Get the queries results = self.get_results(context) # Get the total count total = results['total'] # Get the total number of results total_count =