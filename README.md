galaxy-lint-rules
=================

This repository is for testing planned new [ansible-lint](https://github.com/willthames/ansible-lint) rules. The official adoption of these rules will occur in the [ansible-lint](https://github.com/willthames/ansible-lint) repository - we will solicit community feedback there during PR proposals.

Ansible Lint will be used by [the Galaxy server](https://galaxy.ansible.com), starting in version 3.1 (under development), and a yet to be determined future release of [Mazer, the new Galaxy CLI](https://github.com/ansible/mazer), to evaluate Ansible content.

Rules
-----
see [RULE_DOCS.md](RULE_DOCS.md)

Usage
-----

This guide assumes you have an Ansible role available locally, e.g. in `roles/example.rolename`.

  1. Install Ansible Lint: `pip install ansible-lint`
  1. Clone this repo: `git clone git@github.com:ansible/galaxy-lint-rules.git`
  1. Run Ansible Lint using the galaxy-lint-rules: `ansible-lint -r galaxy-lint-rules/rules roles/example.rolename`
