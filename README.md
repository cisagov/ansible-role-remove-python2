# ansible-role-remove-python2 #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-remove-python2/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-remove-python2/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-remove-python2/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-remove-python2/actions/workflows/codeql-analysis.yml)

An Ansible role for removing all Python 2 packages on all distributions
other than Amazon Linux 2.  Python 2 is preserved on Amazon Linux 2
because its outdated `yum` command requires Python 2.

## Requirements ##

None.

## Role Variables ##

None.

<!--
| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| optional_variable | Describe its purpose. | `default_value` | No |
| required_variable | Describe its purpose. | n/a | Yes |
-->

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Remove Python 2
      ansible.builtin.include_role:
        name: remove_python2
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@gwe.cisa.dhs.gov>
