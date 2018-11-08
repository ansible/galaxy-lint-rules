# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule


class TaskNoLocalAction(AnsibleLintRule):
    id = '504'
    shortdesc = ("Use 'connection: local' or 'delegate_to: localhost' "
                 "instead of 'local_action'")
    description = ("Use 'connection: local' or 'delegate_to: localhost' "
                   "instead of 'local_action'")
    tags = ['task']

    def match(self, file, text):
        if 'local_action' in text:
            return True
        return False
