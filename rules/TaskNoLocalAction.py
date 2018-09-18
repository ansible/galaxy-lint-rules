# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule


class TaskNoLocalAction(AnsibleLintRule):
    id = '504GAL'
    shortdesc = 'Do not use local_action. use delegate_to: localhost instead'
    description = ''
    tags = ['task']

    def match(self, file, text):
        if 'local_action' in text:
            return True
        return False
