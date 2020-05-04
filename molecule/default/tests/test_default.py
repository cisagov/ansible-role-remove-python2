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
    """Ensure that python2-specific files no longer exist."""
    assert not host.file(f).exists
