# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule


class LineTooLongRule(AnsibleLintRule):
    id = '204GAL'
    shortdesc = 'Lines should be no longer than 160 chars'
    description = 'Long lines make code harder to read and ' \
                  'code review more difficult'
    tags = ['formatting']

    def match(self, file, line):
        return len(line) > 160
