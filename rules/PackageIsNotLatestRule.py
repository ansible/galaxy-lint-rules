# Copyright (c) 2018 Ansible, Inc.
# All Rights Reserved.

from ansiblelint import AnsibleLintRule


class PackageIsNotLatestRule(AnsibleLintRule):
    id = '403'
    shortdesc = 'Package installs should not use latest'
    description = 'Package installs should use state=present ' + \
                  'with or without a version'
    tags = ['module']

    _package_managers = [
        'apk',
        'apt',
        'bower',
        'bundler',
        'dnf',
        'easy_install',
        'gem',
        'homebrew',
        'jenkins_plugin',
        'npm',
        'openbsd_package',
        'openbsd_pkg',
        'package',
        'pacman',
        'pear',
        'pip',
        'pkg5',
        'pkgutil',
        'portage',
        'slackpkg',
        'sorcery',
        'swdepot',
        'win_chocolatey',
        'yarn',
        'yum',
        'zypper',
    ]

    def matchtask(self, file, task):
        return (task['action']['__ansible_module__'] in self._package_managers and
                task['action'].get('state') == 'latest')
