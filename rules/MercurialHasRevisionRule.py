# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule


class MercurialHasRevisionRule(AnsibleLintRule):
    id = 'GALAXYTEST402'
    shortdesc = 'Mercurial checkouts must contain explicit revision'
    description = 'All version control checkouts must point to ' + \
                  'an explicit commit or tag, not just "latest"'

    # tags = ['repeatability']
    tags = ['module']

    def matchtask(self, file, task):
        return (task['action']['__ansible_module__'] == 'hg' and
                task['action'].get('revision', 'default') == 'default')
