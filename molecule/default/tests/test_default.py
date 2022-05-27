"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_python2_files(host):
    """Ensure that Python 2-specific files no longer exist, except on Amazon Linux 2."""
    python2_files = ["/usr/bin/python", "/usr/bin/python2", "/usr/bin/python2.7"]
    # Python 2 is required for the old version of yum used on Amazon Linux 2 so
    # these paths should still exist on that platform.
    if host.system_info.distribution == "amzn":
        for file in python2_files:
            assert host.file(file).exists
    elif host.system_info.distribution in ["debian", "fedora", "kali", "ubuntu"]:
        for file in python2_files:
            assert not host.file(file).exists
    else:
        assert (
            False
        ), f"Linux distribution {host.system_info.distribution} is not supported."


def test_python2_packages(host):
    """Ensure that no Python 2-specific packages are installed, except on Amazon Linux 2."""
    # Since we do not want any of these installed we can safely combine them all
    # into one comprehensive list.
    python2_packages = [
        "python-dev",
        "python-minimal",
        "python-unversioned-command",
        "python",
        "python2-dev",
        "python2-minimal",
        "python2.7",
        "python2",
    ]
    # This should remain installed as it is required for the old version of yum
    # used by Amazon Linux 2.
    amazonlinux2_packages = ["python"]
    if host.system_info.distribution == "amzn":
        for package in amazonlinux2_packages:
            assert host.package(package).is_installed
    elif host.system_info.distribution in ["debian", "fedora", "kali", "ubuntu"]:
        for package in python2_packages:
            assert not host.package(package).is_installed
    else:
        assert (
            False
        ), f"Linux distribution {host.system_info.distribution} is not supported."
