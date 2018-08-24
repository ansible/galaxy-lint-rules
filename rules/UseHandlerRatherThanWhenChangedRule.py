# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

import six

from ansiblelint import AnsibleLintRule


def _changed_in_when(item):
    return any(changed in item for changed in
               ['.changed', '|changed', '["changed"]', "['changed']"])


class UseHandlerRatherThanWhenChangedRule(AnsibleLintRule):
    id = '503'
    shortdesc = 'Tasks that run when changed should likely be handlers'
    description = "If a task has a `when: result.changed` setting, it's " \
                  "effectively acting as a handler"
    tags = ['task']

    def matchtask(self, file, task):
        if task["__ansible_action_type__"] == 'task':
            when = task.get('when')
            if isinstance(when, list):
                for item in when:
                    if _changed_in_when(item):
                        return True
            if isinstance(when, six.string_types):
                return _changed_in_when(when)
