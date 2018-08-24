# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule


class CommandHasChangesCheckRule(AnsibleLintRule):
    id = '303'
    shortdesc = 'Commands should not change things if nothing needs doing'
    description = 'Commands should either read information (and thus set ' \
                  'changed_when) or not do something if it has already been ' \
                  'done (using creates/removes) or only do it if another ' \
                  'check has a particular result (when)'
    tags = ['command-shell']

    _commands = ['command', 'shell', 'raw']

    def matchtask(self, file, task):
        if task["__ansible_action_type__"] == 'task':
            if task["action"]["__ansible_module__"] in self._commands:
                return 'changed_when' not in task and \
                    'when' not in task and \
                    'creates' not in task['action'] and \
                    'removes' not in task['action']
