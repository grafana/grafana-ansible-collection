import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pyroscope_with_s3_config(host):
    """Check if pyroscope configuration contains S3 settings."""
    config_file = host.file("/etc/pyroscope/config.yaml")
    assert config_file.exists
    assert "backend: s3" in config_file.content_string
    assert "bucket_name: pyroscope-test" in config_file.content_string


def test_pyroscope_multitenancy_enabled(host):
    """Check if multitenancy is enabled in configuration."""
    config_file = host.file("/etc/pyroscope/config.yaml")
    assert "multitenancy_enabled: true" in config_file.content_string


def test_pyroscope_memberlist_config(host):
    """Check if memberlist configuration is present."""
    config_file = host.file("/etc/pyroscope/config.yaml")
    assert "memberlist:" in config_file.content_string
    assert "bind_port: 7946" in config_file.content_string


def test_pyroscope_environment_variables(host):
    """Check if environment variables are set in systemd override."""
    override_file = host.file("/etc/systemd/system/pyroscope.service.d/override.conf")
    assert override_file.exists
    assert 'Environment="GOGC=100"' in override_file.content_string
    assert 'Environment="GOMAXPROCS=4"' in override_file.content_string


def test_pyroscope_debug_logging(host):
    """Check if debug logging is enabled."""
    config_file = host.file("/etc/pyroscope/config.yaml")
    assert "log_level: debug" in config_file.content_string


def test_pyroscope_limits_configured(host):
    """Check if limits are properly configured."""
    config_file = host.file("/etc/pyroscope/config.yaml")
    assert "max_global_series_per_user: 1000000" in config_file.content_string
    assert "ingestion_rate: 50000" in config_file.content_string
    assert "ingestion_burst_size: 100000" in config_file.content_string