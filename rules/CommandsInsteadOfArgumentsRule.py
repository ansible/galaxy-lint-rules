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


class CommandsInsteadOfArgumentsRule(AnsibleLintRule):
    id = 'GALAXYTEST302'
    shortdesc = 'Using command rather than an argument to e.g. file'
    description = 'Executing a command when there is are arguments to ' + \
                  'modules is generally a bad idea'
    # tags = ['resources']
    tags = ['command-shell']

    _commands = ['command', 'shell', 'raw']
    _arguments = {'chown': 'owner', 'chmod': 'mode', 'chgrp': 'group',
                  'ln': 'state=link', 'mkdir': 'state=directory',
                  'rmdir': 'state=absent', 'rm': 'state=absent'}

    def matchtask(self, file, task):
        if task["action"]["__ansible_module__"] in self._commands:
            if 'cmd' in task['action']:
                first_cmd_arg = task['action']['cmd'].split()[0]
            else:
                first_cmd_arg = task["action"]["__ansible_arguments__"][0]
            if not first_cmd_arg:
                return
            executable = os.path.basename(first_cmd_arg)
            if executable in self._arguments and \
                    boolean(task['action'].get('warn', True)):
                message = "{0} used in place of argument {1} to file module"
                return message.format(executable, self._arguments[executable])
