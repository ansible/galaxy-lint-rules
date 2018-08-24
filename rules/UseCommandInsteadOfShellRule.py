# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule
import re


def unjinja(text):
    return re.sub("\{\{[^\}]*\}\}", "JINJA_VAR", text)


class UseCommandInsteadOfShellRule(AnsibleLintRule):
    id = '304'
    shortdesc = 'Use shell only when shell functionality is required'
    description = 'Shell should only be used when piping, redirecting ' \
                  'or chaining commands (and Ansible would be preferred ' \
                  'for some of those!)'
    tags = ['command-shell']

    def matchtask(self, file, task):
        # Use unjinja so that we don't match on jinja filters
        # rather than pipes
        if task["action"]["__ansible_module__"] == 'shell':
            if 'cmd' in task['action']:
                unjinjad_cmd = unjinja(task["action"].get("cmd", []))
            else:
                unjinjad_cmd = unjinja(' '.join(task["action"].get("__ansible_arguments__", [])))
            return not any([ch in unjinjad_cmd for ch in '&|<>;$\n*[]{}?'])
