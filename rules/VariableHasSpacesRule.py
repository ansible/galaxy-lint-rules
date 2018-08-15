from ansiblelint import AnsibleLintRule
import re


class VariableHasSpacesRule(AnsibleLintRule):
    id = 'GALAXYTEST202'
    shortdesc = 'Variables should have spaces after {{ and before }}'
    description = 'Variables should be of the form {{ varname }}'
    # tags = ['whitespace', 'templating']
    tags = ['formatting']

    bracket_regex = re.compile("{{[^{ ]|[^ }]}}")

    def match(self, file, line):
        return self.bracket_regex.search(line)
