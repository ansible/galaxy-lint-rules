# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule


class TrailingWhitespaceRule(AnsibleLintRule):
    id = '201'
    shortdesc = 'Trailing whitespace'
    description = 'There should not be any trailing whitespace'
    tags = ['formatting']

    def match(self, file, line):
        return line.rstrip() != line
