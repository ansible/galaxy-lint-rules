# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule
import re


class VariableHasSpacesRule(AnsibleLintRule):
    id = '208GAL'
    shortdesc = 'Variables should have spaces after {{ and before }}'
    description = 'Variables should be of the form {{ varname }}'
    tags = ['formatting']

    bracket_regex = re.compile("{{[^{ ]|[^ }]}}")

    def match(self, file, line):
        return self.bracket_regex.search(line)
