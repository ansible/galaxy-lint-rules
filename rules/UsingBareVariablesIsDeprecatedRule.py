# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

import re
import six
from ansiblelint import AnsibleLintRule


class UsingBareVariablesIsDeprecatedRule(AnsibleLintRule):
    id = '104'
    shortdesc = 'Using bare variables is deprecated'
    description = 'Using bare variables is deprecated. Update your ' + \
        'playbooks so that the environment value uses the full variable ' + \
        'syntax ("{{your_variable}}").'
    tags = ['deprecated']

    _jinja = re.compile(r"{{.*}}")
    _glob = re.compile('[][*?]')

    def matchtask(self, file, task):
        loop_type = next((key for key in task
                          if key.startswith("with_")), None)
        if loop_type:
            if loop_type in ["with_nested", "with_together", "with_flattened"]:
                # These loops can either take a list defined directly in the
                # task or a variable that is a list itself.  When a
                # single variable is used we just need to check that
                # one variable, and not iterate over it like
                # it's a list. Otherwise, loop through and check all items.
                items = task[loop_type]
                if not isinstance(items, (list, tuple)):
                    items = [items]
                for var in items:
                    return self._matchvar(var, task, loop_type)
            elif loop_type == "with_subelements":
                return self._matchvar(task[loop_type][0], task, loop_type)
            elif loop_type in ["with_sequence", "with_ini",
                               "with_inventory_hostnames"]:
                pass
            else:
                return self._matchvar(task[loop_type], task, loop_type)

    def _matchvar(self, varstring, task, loop_type):
        if (isinstance(varstring, six.string_types) and
                not self._jinja.match(varstring)):
            if loop_type != 'with_fileglob' or not (self._jinja.search(varstring) or
                                                    self._glob.search(varstring)):
                message = "Found a bare variable '{0}' used in a '{1}' loop." + \
                          " You should use the full variable syntax ('{{{{{0}}}}}')"
                return message.format(task[loop_type], loop_type)
