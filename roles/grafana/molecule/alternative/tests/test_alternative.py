from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_directories(host):
    dirs = [
        "/etc/grafana",
        "/var/log/grafana",
        "/var/lib/grafana",
        "/var/lib/grafana/dashboards",
        "/var/lib/grafana/plugins",
        "/var/lib/grafana/plugins/raintank-worldping-app"
    ]
    files = [
        "/etc/grafana/grafana.ini",
        "/etc/grafana/ldap.toml"
    ]
    for directory in dirs:
        d = host.file(directory)
        assert d.is_directory
        assert d.exists
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_service(host):
    s = host.service("grafana-server")
    # assert s.is_enabled
    assert s.is_running


def test_packages(host):
    p = host.package("grafana")
    assert p.is_installed
    assert p.version == "6.2.5"


def test_socket(host):
    assert host.socket("tcp://127.0.0.1:3000").is_listening


def test_custom_auth_option(host):
    f = host.file("/etc/grafana/grafana.ini")
    assert f.contains("login_maximum_inactive_lifetime_days = 42")


def test_metrics_settings(host):
    f = host.file("/etc/grafana/grafana.ini")
    assert f.contains("[metrics]")
    assert f.contains("enabled = true")
    assert f.contains("interval_seconds = 10")
    assert f.contains("disable_total_stats = false")
    assert f.contains("total_stats_collector_interval_seconds = 1800")
    assert f.contains("basic_auth_username = ")
    assert f.contains("basic_auth_password = ")
