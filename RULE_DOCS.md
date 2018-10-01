| id                                                          | sample message                                              |
|-------------------------------------------------------------|-------------------------------------------------------------|
| **E1**                                                      | *deprecated*                                                |
| E101                                                        | Deprecated always_run                                       |
| E102                                                        | No Jinja2 in when                                           |
| E103                                                        | Deprecated sudo                                             |
| E104                                                        | Using bare variables is deprecated                          |
| E105GAL                                                     | Deprecated with_X for loops                                 |
| E106GAL                                                     | Deprecated module                                           |
|                                                             |                                                             |
| **E2**                                                      | *formatting*                                                |
| E201                                                        | Trailing whitespace                                         |
| E202                                                        | Octal file permissions must contain leading zero            |
| E203GAL                                                     | Most files should not contain tabs                          |
| E204GAL                                                     | Lines should be no longer than 160 chars                    |
| E205GAL                                                     | Variables should be enclosed by spaces "{{ foo }}"          |
| E206GAL                                                     | Use ":" YAML format when arguments are over 4               |
| E207GAL                                                     | Playbooks should have the ".yml" extension                  |
| E208GAL                                                     | Variables should have spaces after {{ and before }}         |
|                                                             |                                                             |
| **E3**                                                      | *command-shell*                                             |
| E301                                                        | Commands should not change things if nothing needs doing    |
| E302                                                        | Using command rather than an argument to e.g. file          |
| E303                                                        | Using command rather than module                            |
| E304                                                        | Environment variables don't work as part of command         |
| E305                                                        | Use shell only when shell functionality is required         |
| E306GAL                                                     | Use patch module                                            |
|                                                             |                                                             |
| **E4**                                                      | *module*                                                    |
| E401                                                        | Git checkouts must contain explicit version                 |
| E402                                                        | Mercurial checkouts must contain explicit revision          |
| E403                                                        | Package installs should not use latest                      |
| E404GAL                                                     | Doesn't need a relative path in role                        |
| E405GAL                                                     | Template files should have the extension '.j2'              |
| E406GAL                                                     | Recommended to mention the state                            |
|                                                             |                                                             |
| **E5**                                                      | *task*                                                      |
| E501                                                        | become_user requires become to work as expected             |
| E502                                                        | All tasks should be named                                   |
| E503                                                        | Tasks that run when changed should likely be handlers       |
| E504GAL                                                     | Do not use local_action. use delegate_to: localhost instead |
|                                                             |                                                             |
| **E6**                                                      | *idiom*                                                     |
| E601GAL                                                     | Don't compare to literal True/False                         |
| E602GAL                                                     | Don't compare to empty string                               |
