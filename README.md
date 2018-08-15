# galaxy-lint-rules

This repository contains custom [Ansible Lint rules](https://github.com/willthames/ansible-lint) that will be used by [the Galaxy server](https://galaxy.ansible.com), starting in version 3.1 (under development), and a yet to be determined future release of [Mazer, the new Galaxy CLI](https://github.com/ansible/mazer), to evaluate Ansible content. Initially started with ansible-lint rules from [ansible-lint](https://github.com/willthames/ansible-lint), [ansible-review](https://github.com/willthames/ansible-review), and [tsukinowasha/ansible-lint-rules](https://github.com/tsukinowasha/ansible-lint-rules).

## Rules
Listed by category
#### deprecated
* GALAXYTEST101 SudoRule
* GALAXYTEST102 UsingBareVariablesIsDeprecatedRule
* GALAXYTEST103 AlwaysRunRule
* GALAXYTEST104 NoFormattingInWhenRule

#### formatting
* GALAXYTEST201 TrailingWhitespaceRule
* GALAXYTEST202 VariableHasSpacesRule
* GALAXYTEST203 NoTabsRule
* GALAXYTEST204 LineTooLongRule
* GALAXYTEST205 TaskVariableHasSpace
* GALAXYTEST206 TaskManyArgs
* GALAXYTEST207 PlaybookExtension

#### command-shell
* GALAXYTEST301 CommandsInsteadOfModulesRule
* GALAXYTEST302 CommandsInsteadOfArgumentsRule
* GALAXYTEST303 CommandHasChangesCheckRule
* GALAXYTEST304 UseCommandInsteadOfShellRule
* GALAXYTEST305 EnvVarsInCommandRule
* GALAXYTEST306 ShellAltPatch

#### module
* GALAXYTEST401 GitHasVersionRule
* GALAXYTEST402 MercurialHasRevisionRule
* GALAXYTEST403 OctalPermissionsRule
* GALAXYTEST404 PackageIsNotLatestRule
* GALAXYTEST405 RoleRelativePath
* GALAXYTEST406 ModuleTemplateExt
* GALAXYTEST407 StateIsPresentRule

#### task
* GALAXYTEST501	TaskHasNameRule
* GALAXYTEST502	BecomeUserWithoutBecomeRule
* GALAXYTEST503	UseHandlerRatherThanWhenChangedRule
* GALAXYTEST504	TaskNoLocalAction

#### idiom
* GALAXYTEST601 ComparisonToLiteralBoolRule
* GALAXYTEST602 ComparisonToEmptyStringRule
