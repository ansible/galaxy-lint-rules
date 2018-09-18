# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule


class PackageIsNotLatestRule(AnsibleLintRule):
    id = '403'
    shortdesc = 'Package installs should not use latest'
    description = 'Package installs should use state=present ' + \
                  'with or without a version'
    tags = ['module']

    _package_managers = ['yum', 'apt', 'dnf', 'homebrew', 'pacman', 'pkg5',
                         'openbsd_package', 'portage', 'pkgutil', 'slackpkg',
                         'swdepot', 'zypper', 'bundler', 'pip', 'pear',
                         'npm', 'gem', 'easy_install', 'bower', 'package']

    def matchtask(self, file, task):
        return (task['action']['__ansible_module__'] in self._package_managers and
                task['action'].get('state') == 'latest')
