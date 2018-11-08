# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule


class TaskHasNameRule(AnsibleLintRule):
    id = '502'
    shortdesc = 'All tasks should be named'
    description = 'All tasks should have a distinct name for readability ' + \
                  'and for --start-at-task to work'
    tags = ['task']

    _nameless_tasks = ['meta', 'debug', 'include_role', 'import_role',
                       'include_tasks', 'import_tasks']

    def matchtask(self, file, task):
        return (not task.get('name') and
                task["action"]["__ansible_module__"] not in self._nameless_tasks)
