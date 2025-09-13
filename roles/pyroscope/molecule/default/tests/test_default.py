import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pyroscope_package_installed(host):
    """Check if pyroscope package is installed."""
    package = host.package("pyroscope")
    assert package.is_installed


def test_pyroscope_service_running(host):
    """Check if pyroscope service is running."""
    service = host.service("pyroscope")
    assert service.is_running
    assert service.is_enabled


def test_pyroscope_config_file_exists(host):
    """Check if pyroscope configuration file exists."""
    config_file = host.file("/etc/pyroscope/config.yaml")
    assert config_file.exists
    assert config_file.is_file
    assert config_file.user == "pyroscope"
    assert config_file.group == "pyroscope"
    assert config_file.mode == 0o640


def test_pyroscope_directories_exist(host):
    """Check if pyroscope directories exist with correct permissions."""
    directories = [
        "/etc/pyroscope",
        "/var/lib/pyroscope",
        "/var/log/pyroscope",
        "/var/lib/pyroscope/data"
    ]
    for directory in directories:
        dir_obj = host.file(directory)
        assert dir_obj.exists
        assert dir_obj.is_directory
        assert dir_obj.user == "pyroscope"
        assert dir_obj.group == "pyroscope"


def test_pyroscope_user_exists(host):
    """Check if pyroscope user exists."""
    user = host.user("pyroscope")
    assert user.exists
    assert user.group == "pyroscope"
    assert user.shell == "/usr/sbin/nologin"


def test_pyroscope_group_exists(host):
    """Check if pyroscope group exists."""
    group = host.group("pyroscope")
    assert group.exists


def test_pyroscope_listening_on_http_port(host):
    """Check if pyroscope is listening on HTTP port."""
    socket = host.socket("tcp://0.0.0.0:4040")
    assert socket.is_listening


def test_pyroscope_listening_on_grpc_port(host):
    """Check if pyroscope is listening on gRPC port."""
    socket = host.socket("tcp://0.0.0.0:4041")
    assert socket.is_listening


def test_pyroscope_systemd_service_file(host):
    """Check if systemd service file exists."""
    service_file = host.file("/etc/systemd/system/pyroscope.service")
    assert service_file.exists
    assert service_file.is_file
    assert service_file.user == "root"
    assert service_file.group == "root"

