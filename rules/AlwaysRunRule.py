# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule


class AlwaysRunRule(AnsibleLintRule):
    id = '103'
    shortdesc = 'Deprecated always_run'
    description = 'Instead of always_run, use check_mode.'
    tags = ['deprecated']

    def matchtask(self, file, task):
        return 'always_run' in task
