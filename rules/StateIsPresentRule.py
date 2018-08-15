# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule


class StateIsPresentRule(AnsibleLintRule):
    id = 'GALAXYTEST407'
    shortdesc = 'Recommended to mention the state'
    description = '''
    The 'state' parameter is optional to a lot of modules.
    Whether 'state=present' or 'state=absent', it's always best to leave that
    parameter in your playbooks to make it clear,
    especially as some modules support additional states.
    '''
    tags = ['module']

    # some popular modules with state parameter
    _modules = ['file', 'selinux', 'seboolean', 'mount', 'user', 'group',
                'script', 'service', 'postgresql_db', 'postgresql_user',
                'package', 'apt', 'yum',
                'ufw', 'pip', 'lineinfile']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in self._modules:
            return False
        if 'state' not in task['action'].keys():
            return True
        return False
