galaxy-lint-rules
=================

This repository contains custom [Ansible Lint rules](https://github.com/willthames/ansible-lint) that will be used by [the Galaxy server](https://galaxy.ansible.com), starting in version 3.1 (under development), and a yet to be determined future release of [Mazer, the new Galaxy CLI](https://github.com/ansible/mazer), to evaluate Ansible content. Initially started with ansible-lint rules from [ansible-lint](https://github.com/willthames/ansible-lint), [ansible-review](https://github.com/willthames/ansible-review), and [tsukinowasha/ansible-lint-rules](https://github.com/tsukinowasha/ansible-lint-rules).

Rules
-----
see [RULE_DOCS.md](RULE_DOCS.md)

Usage
-----

This guide assumes you have an Ansible role available locally, e.g. in `roles/example.rolename`.

  1. Install Ansible Lint: `pip install ansible-lint`
  1. Clone this repo: `git clone git@github.com:ansible/galaxy-lint-rules.git`
  1. Run Ansible Lint using the galaxy-lint-rules: `ansible-lint -r galaxy-lint-rules/rules roles/example.rolename`
