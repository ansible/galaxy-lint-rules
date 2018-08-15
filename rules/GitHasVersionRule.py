# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule


class GitHasVersionRule(AnsibleLintRule):
    id = 'GALAXYTEST401'
    shortdesc = 'Git checkouts must contain explicit version'
    description = 'All version control checkouts must point to ' + \
                  'an explicit commit or tag, not just "latest"'
    # tags = ['repeatability']
    tags = ['module']

    def matchtask(self, file, task):
        return (task['action']['__ansible_module__'] == 'git' and
                task['action'].get('version', 'HEAD') == 'HEAD')
