# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

import os

from ansiblelint import AnsibleLintRule
try:
    from ansible.module_utils.parsing.convert_bool import boolean
except ImportError:
    try:
        from ansible.utils.boolean import boolean
    except ImportError:
        try:
            from ansible.utils import boolean
        except ImportError:
            from ansible import constants
            boolean = constants.mk_boolean


class CommandsInsteadOfModulesRule(AnsibleLintRule):
    id = '303'
    shortdesc = 'Using command rather than module'
    description = 'Executing a command when there is an Ansible module ' + \
                  'is generally a bad idea'
    tags = ['command-shell', 'resources', 'ANSIBLE0006']

    _commands = ['command', 'shell']
    _modules = {
        'apt-get': 'apt-get',
        'chkconfig': 'service',
        'curl': 'get_url or uri',
        'git': 'git',
        'hg': 'hg',
        'mount': 'mount',
        'patch': 'patch',
        'rpm': 'yum or rpm_key',
        'rsync': 'synchronize',
        'sed': 'template, replace or lineinfile',
        'service': 'service',
        'supervisorctl': 'supervisorctl',
        'svn': 'subversion',
        'systemctl': 'systemd',
        'tar': 'unarchive',
        'unzip': 'unarchive',
        'wget': 'get_url or uri',
        'yum': 'yum',
    }

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in self._commands:
            return

        if 'cmd' in task['action']:
            first_cmd_arg = task['action']['cmd'].split()[0]
        else:
            first_cmd_arg = task['action']['__ansible_arguments__'][0]
        if not first_cmd_arg:
            return

        executable = os.path.basename(first_cmd_arg)
        if executable in self._modules and \
                boolean(task['action'].get('warn', True)):
            message = '{0} used in place of {1} module'
            return message.format(executable, self._modules[executable])
