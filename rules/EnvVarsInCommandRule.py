# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule
from ansiblelint.utils import LINE_NUMBER_KEY, FILENAME_KEY


class EnvVarsInCommandRule(AnsibleLintRule):
    id = '304'
    shortdesc = "Environment variables don't work as part of command"
    description = 'Environment variables should be passed to shell or ' \
                  'command through environment argument'
    tags = ['command-shell']

    expected_args = ['chdir', 'creates', 'executable',
                     'removes', 'stdin', 'warn',
                     'cmd', '__ansible_module__', '__ansible_arguments__',
                     LINE_NUMBER_KEY, FILENAME_KEY]

    def matchtask(self, file, task):
        if task["action"]["__ansible_module__"] in ['shell', 'command']:
            if 'cmd' in task['action']:
                first_cmd_arg = task['action']['cmd'].split()[0]
            else:
                first_cmd_arg = task['action']['__ansible_arguments__'][0]
            return any([arg not in self.expected_args for arg in task['action']] +
                       ["=" in first_cmd_arg])
