# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule


class SudoRule(AnsibleLintRule):
    id = '103'
    shortdesc = 'Deprecated sudo'
    description = 'Instead of sudo/sudo_user, use become/become_user.'
    tags = ['deprecated']

    def matchtask(self, file, task):
        return 'sudo' in task or 'sudo_user' in task
