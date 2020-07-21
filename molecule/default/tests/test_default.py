"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

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
    if host.system_info.distribution == "debian" and host.system_info.release == "9.12":
        assert host.file(f).exists
    else:
        assert not host.file(f).exists
