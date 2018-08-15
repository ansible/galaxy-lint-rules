from ansiblelint import AnsibleLintRule

import re

class TaskVariableHasSpace(AnsibleLintRule):
    id = 'GALAXYTEST205'
    shortdesc = 'Variables should be enclosed by spaces "{{ foo }}"'
    description = ''
    # tags = ['task']
    tags = ['formatting']

    compiled = re.compile(r'{{(\w*)}}')

    def match(self, file, text):
        m = self.compiled.search(text)
        if m:
            return True
        return False
