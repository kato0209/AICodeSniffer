
        if self.credentials is None:
            raise AirflowException("The environment variable GOOGLE_APPLICATION_CREDENTIALS must be set")

        # If the user didn't set the environment variable, generate a default one.
        if "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = _get_default_gcp_credentials()

        self.credentials = _Credentials(self.credentials)

        # If the environment variable is missing, generate a default one.
        if "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ: