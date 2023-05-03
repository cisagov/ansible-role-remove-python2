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
    "filename", ["/usr/bin/python", "/usr/bin/python2", "/usr/bin/python2.7"]
)
def test_python2_files(host, filename):
    """Ensure that Python 2-specific files no longer exist."""
    assert not host.file(filename).exists


@pytest.mark.parametrize(
    "package",
    [
        "python-dev",
        "python-minimal",
        "python-unversioned-command",
        "python",
        "python2-dev",
        "python2-minimal",
        "python2.7",
        "python2",
    ],
)
def test_python2_packages(host, package):
    """Ensure that no Python 2-specific packages are installed."""
    assert not host.package(package).is_installed
