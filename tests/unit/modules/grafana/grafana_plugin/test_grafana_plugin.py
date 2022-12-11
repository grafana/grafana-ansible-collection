from __future__ import (absolute_import, division, print_function)

from unittest import TestCase
from unittest.mock import patch, MagicMock
from ansible_collections.community.grafana.plugins.modules import grafana_plugin

__metaclass__ = type


def run_command_ls():
    STDERR = ""
    STDOUT = """
installed plugins:
alexanderzobnin-zabbix-app @ 3.10.5

Restart grafana after installing plugins . <service grafana-server restart>
"""
    return 0, STDOUT, STDERR


def run_command_install_zip():
    STDERR = ""
    STDOUT = """
installing alexanderzobnin-grafana-zabbix @ 
from: /home/grafana//alexanderzobnin-grafana-zabbix-v3.10.5-1-g2219691.zip
into: /var/lib/grafana/plugins

... Installed alexanderzobnin-grafana-zabbix successfully

Restart grafana after installing plugins . <service grafana-server restart>

"""
    return 0, STDOUT, STDERR


def run_command_uninstall():
    STDERR = ""
    STDOUT = """
Removing plugin: alexanderzobnin-zabbix-app

Restart grafana after installing plugins . <service grafana-server restart>
"""
    return 0, STDOUT, STDERR


def run_command_uninstall_again():
    STDERR = ""
    STDOUT = """
Removing plugin: alexanderzobnin-zabbix-app
Error: ✗ plugin does not exist
"""
    return 1, STDOUT, STDERR


class GrafanaPlugin(TestCase):

    @patch('ansible_collections.community.grafana.plugins.modules.grafana_plugin.grafana_cli_bin')
    def test_plugin_install_zip(self, mock_grafana_cli_bin):
        mock_grafana_cli_bin.return_value = "grafana-cli plugins"

        params = {
            "name": "alexanderzobnin-zabbix-app"
        }

        module = MagicMock()
        module.run_command.return_value = run_command_install_zip()

        result = grafana_plugin.get_grafana_plugin_version(module, params)
        self.assertEqual(result, None)

    @patch('ansible_collections.community.grafana.plugins.modules.grafana_plugin.grafana_cli_bin')
    def test_plugin_ls(self, mock_grafana_cli_bin):
        mock_grafana_cli_bin.return_value = "grafana-cli plugins"

        params = {
            "name": "alexanderzobnin-zabbix-app"
        }

        module = MagicMock()
        module.run_command.return_value = run_command_ls()

        result = grafana_plugin.get_grafana_plugin_version(module, params)
        self.assertEqual(result, "3.10.5")

    @patch('ansible_collections.community.grafana.plugins.modules.grafana_plugin.grafana_cli_bin')
    def test_plugin_uninstall(self, mock_grafana_cli_bin):
        mock_grafana_cli_bin.return_value = "grafana-cli plugins"

        params = {
            "name": "alexanderzobnin-zabbix-app"
        }

        module = MagicMock()
        module.run_command.return_value = run_command_uninstall()

        result = grafana_plugin.get_grafana_plugin_version(module, params)
        self.assertEqual(result, None)

    @patch('ansible_collections.community.grafana.plugins.modules.grafana_plugin.grafana_cli_bin')
    def test_plugin_uninstall_again(self, mock_grafana_cli_bin):
        mock_grafana_cli_bin.return_value = "grafana-cli plugins"

        params = {
            "name": "alexanderzobnin-zabbix-app"
        }

        module = MagicMock()
        module.run_command.return_value = run_command_uninstall_again()

        result = grafana_plugin.get_grafana_plugin_version(module, params)
        self.assertEqual(result, None)
