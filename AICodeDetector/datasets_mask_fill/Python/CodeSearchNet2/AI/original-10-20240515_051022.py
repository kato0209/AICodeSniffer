
        jobs = self.service.jobs()
        job_data = {
            'configuration': configuration
        }

        for job in jobs:
            job_data['configuration'] = job.configuration

        self.log.info('Running query:\n%s', job_data)
        job_ref = job_data['jobReference']
        job_ref.jobId = self.reference.job_id
        self.log.info('Job reference: %s', job_ref)

        try:
            self.service.jobs().insert(