# ansible-role-remove-python2 #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-remove-python2/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-remove-python2/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/ansible-role-remove-python2.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-remove-python2/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/ansible-role-remove-python2.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-remove-python2/context:python)

An Ansible role for removing all Python2 packages on all distributions
other than Debian 9 (stretch).  Python2 is preserved on Debian 9 for
the time being.

## Requirements ##

None.

## Role Variables ##

None.

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  roles:
    - no_python2
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

Shane Frasier - <jeremy.frasier@trio.dhs.gov>
