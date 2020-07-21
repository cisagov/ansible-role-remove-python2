"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os
import re

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "f", ["/usr/bin/python", "/usr/bin/python2", "/usr/bin/python2.7"]
)
def test_python(host, f):
    """Ensure that python2-specific files no longer exist, except on Debian 9."""
    # Note that r"^9(\.|$)" will match any string starting with "9.",
    # or the string "9".
    if (
        host.system_info.distribution == "debian"
        and re.match(r"^9(\.|$)", host.system_info.release) is not None
    ):
        assert host.file(f).exists
    else:
        assert not host.file(f).exists
