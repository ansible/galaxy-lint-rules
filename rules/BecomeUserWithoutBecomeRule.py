# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule


def _become_user_without_become(data):
    return 'become_user' in data and 'become' not in data


class BecomeUserWithoutBecomeRule(AnsibleLintRule):
    id = 'GALAXYTEST502'
    shortdesc = 'become_user requires become to work as expected'
    description = 'become_user without become will not actually change ' \
                  'user'
    # tags = ['oddity']
    tags = ['task']

    def matchplay(self, file, data):
        if file['type'] == 'playbook' and _become_user_without_become(data):
            return ({'become_user': data}, self.shortdesc)

    def matchtask(self, file, task):
        return _become_user_without_become(task)
