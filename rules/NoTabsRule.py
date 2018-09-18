# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule


class NoTabsRule(AnsibleLintRule):
    id = '203GAL'
    shortdesc = 'Most files should not contain tabs'
    description = 'Tabs can cause unexpected display issues. Use spaces'
    tags = ['formatting']

    def match(self, file, line):
        return '\t' in line
