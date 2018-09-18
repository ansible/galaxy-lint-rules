# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule
import re


class ComparisonToEmptyStringRule(AnsibleLintRule):
    id = '602GAL'
    shortdesc = "Don't compare to empty string"
    description = 'Use `when: var` rather than `when: var != ""` (or ' \
                  'conversely `when: not var` rather than `when: var == ""`)'
    tags = ['idiom']
    empty_string_compare = re.compile("[=!]= ?[\"'][\"']")

    def match(self, file, line):
        return self.empty_string_compare.search(line)
