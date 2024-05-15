security_context = {} if self.kube_config.worker_run_as_user: security_context['runAsUser'] = self.kube_config.worker_run_as_user if self.kube_config.worker_fs_group: security_context['fsGroup'] = self.kube_config.worker_fs_group # <extra_id_0> fs_group to 65533 if not explicitly specified and using git ssh <extra_id_1> auth if self.kube_config.git_ssh_key_secret_name and security_context.get('fsGroup') is None: security_context['fsGroup'] = 65533 return security_context