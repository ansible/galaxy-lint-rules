# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule
import re
import six


class OctalPermissionsRule(AnsibleLintRule):
    id = 'GALAXYTEST403'
    shortdesc = 'Octal file permissions must contain leading zero'
    description = 'Numeric file permissions without leading zero can ' + \
        'behave in unexpected ways. See ' + \
        'http://docs.ansible.com/ansible/file_module.html'
    # tags = ['formatting']
    tags = ['module']

    _modules = ['assemble', 'copy', 'file', 'ini_file', 'lineinfile',
                'replace', 'synchronize', 'template', 'unarchive']

    mode_regex = re.compile(r'^\s*[0-9]+\s*$')
    valid_mode_regex = re.compile(r'^\s*0[0-7]{3,4}\s*$')

    def is_invalid_permission(self, mode):
        # sensible file permission modes don't
        # have write bit set when read bit is
        # not set and don't have execute bit set
        # when user execute bit is not set.
        # also, user permissions are more generous than
        # group permissions and user and group permissions
        # are more generous than world permissions

        other_write_without_read = (mode % 8 and mode % 8 < 4 and
                                    not (mode % 8 == 1 and (mode >> 6) % 2 == 1))
        group_write_without_read = ((mode >> 3) % 8 and (mode >> 3) % 8 < 4 and
                                    not ((mode >> 3) % 8 == 1 and (mode >> 6) % 2 == 1))
        user_write_without_read = ((mode >> 6) % 8 and (mode >> 6) % 8 < 4 and
                                   not (mode >> 6) % 8 == 1)
        other_more_generous_than_group = mode % 8 > (mode >> 3) % 8
        other_more_generous_than_user = mode % 8 > (mode >> 6) % 8
        group_more_generous_than_user = (mode >> 3) % 8 > (mode >> 6) % 8

        return (other_write_without_read or
                group_write_without_read or
                user_write_without_read or
                other_more_generous_than_group or
                other_more_generous_than_user or
                group_more_generous_than_user)

    def matchtask(self, file, task):
        if task["action"]["__ansible_module__"] in self._modules:
            mode = task['action'].get('mode', None)
            if isinstance(mode, six.string_types) and self.mode_regex.match(mode):
                return not self.valid_mode_regex.match(mode)
            if isinstance(mode, int):
                return self.is_invalid_permission(mode)
