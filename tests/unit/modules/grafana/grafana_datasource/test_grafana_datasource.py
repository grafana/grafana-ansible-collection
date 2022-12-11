from __future__ import (absolute_import, division, print_function)

from unittest import TestCase
from unittest.mock import call, patch, MagicMock
from ansible_collections.community.grafana.plugins.modules import grafana_datasource
from ansible.module_utils._text import to_bytes
from ansible.module_utils import basic
from ansible.module_utils.urls import basic_auth_header
import json

__metaclass__ = type


def set_module_args(args):
    """prepare arguments so that they will be picked up during module creation"""
    args = json.dumps({'ANSIBLE_MODULE_ARGS': args})
    basic._ANSIBLE_ARGS = to_bytes(args)


def exit_json(*args, **kwargs):
    """function to patch over exit_json; package return data into an exception"""
    if 'changed' not in kwargs:
        kwargs['changed'] = False
    raise AnsibleExitJson(kwargs)


def fail_json(*args, **kwargs):
    """function to patch over fail_json; package return data into an exception"""
    kwargs['failed'] = True
    raise AnsibleFailJson(kwargs)


class AnsibleExitJson(Exception):
    """Exception class to be raised by module.exit_json and caught by the test case"""
    pass


class AnsibleFailJson(Exception):
    """Exception class to be raised by module.fail_json and caught by the test case"""
    pass


class GrafanaDatasource(TestCase):

    def setUp(self):
        self.authorization = basic_auth_header("admin", "admin")
        self.mock_module_helper = patch.multiple(basic.AnsibleModule,
                                                 exit_json=exit_json,
                                                 fail_json=fail_json)
        self.mock_module_helper.start()
        self.addCleanup(self.mock_module_helper.stop)

    def test_payload_prometheus(self):
        expected_payload = {
            'access': 'proxy',
            'basicAuth': False,
            'database': '',
            'isDefault': False,
            'jsonData': {
                'tlsAuth': False,
                'tlsAuthWithCACert': False,
                'tlsSkipVerify': True
            },
            'name': 'openshift_prometheus',
            'uid': 'xyz123',
            'orgId': 1,
            'secureJsonData': {},
            'type': 'prometheus',
            'url': 'https://openshift-monitoring.company.com',
            'user': '',
            'withCredentials': False
        }
        set_module_args({
            'url': 'https://grafana.example.com',
            'url_username': 'admin',
            'url_password': 'admin',
            'name': 'openshift_prometheus',
            'uid': 'xyz123',
            'ds_type': 'prometheus',
            'ds_url': 'https://openshift-monitoring.company.com',
            'access': 'proxy',
            'tls_skip_verify': 'true',
        })
        module = grafana_datasource.setup_module_object()
        payload = grafana_datasource.get_datasource_payload(module.params)
        self.assertEqual(payload, expected_payload)

    def test_payload_prometheus_with_basic_auth(self):
        expected_payload = {
            'access': 'proxy',
            'basicAuth': True,
            'basicAuthUser': 'admin',
            'database': '',
            'isDefault': False,
            'jsonData': {
                'tlsAuth': False,
                'tlsAuthWithCACert': False,
                'tlsSkipVerify': True
            },
            'name': 'openshift_prometheus',
            'uid': 'xyz123',
            'orgId': 1,
            'secureJsonData': {'basicAuthPassword': 'admin'},
            'type': 'prometheus',
            'url': 'https://openshift-monitoring.company.com',
            'user': '',
            'withCredentials': False
        }
        set_module_args({
            'url': 'https://grafana.example.com',
            'url_username': 'admin',
            'url_password': 'admin',
            'name': 'openshift_prometheus',
            'uid': 'xyz123',
            'ds_type': 'prometheus',
            'ds_url': 'https://openshift-monitoring.company.com',
            'access': 'proxy',
            'basic_auth_user': 'admin',
            'basic_auth_password': 'admin',
            'tls_skip_verify': 'true',
        })
        module = grafana_datasource.setup_module_object()
        payload = grafana_datasource.get_datasource_payload(module.params)
        self.assertEqual(payload, expected_payload)

    def test_payload_influxdb(self):
        expected_payload = {
            'access': 'proxy',
            'basicAuth': False,
            'database': 'telegraf',
            'isDefault': False,
            'jsonData': {
                'timeInterval': '>10s',
                'tlsAuth': False,
                'tlsAuthWithCACert': True
            },
            'name': 'datasource-influxdb',
            'uid': 'xyz123',
            'orgId': 1,
            'secureJsonData': {
                'tlsCACert': '/etc/ssl/certs/ca.pem'
            },
            'type': 'influxdb',
            'url': 'https://influx.company.com:8086',
            'user': '',
            'withCredentials': False
        }
        set_module_args({
            'url': 'https://grafana.example.com',
            'url_username': 'admin',
            'url_password': 'admin',
            'name': 'datasource-influxdb',
            'uid': 'xyz123',
            'ds_type': 'influxdb',
            'ds_url': 'https://influx.company.com:8086',
            'database': 'telegraf',
            'time_interval': '>10s',
            'tls_ca_cert': '/etc/ssl/certs/ca.pem'
        })
        module = grafana_datasource.setup_module_object()
        payload = grafana_datasource.get_datasource_payload(module.params)
        self.assertEqual(payload, expected_payload)

    def test_payload_elastic(self):
        expected_payload = {
            'access': 'proxy',
            'basicAuth': True,
            'basicAuthUser': 'grafana',
            'database': '[logstash_]YYYY.MM.DD',
            'isDefault': False,
            'jsonData': {
                'esVersion': 56,
                'interval': 'Daily',
                'maxConcurrentShardRequests': 42,
                'timeField': '@timestamp',
                'timeInterval': '1m',
                'tlsAuth': False,
                'tlsAuthWithCACert': True
            },
            'name': 'datasource-elastic',
            'uid': 'xyz123',
            'orgId': 1,
            'secureJsonData': {
                'basicAuthPassword': 'grafana',
                'tlsCACert': '/etc/ssl/certs/ca.pem'
            },
            'type': 'elasticsearch',
            'url': 'https://elastic.company.com:9200',
            'user': '',
            'withCredentials': False
        }
        set_module_args({
            'url': 'https://grafana.example.com',
            'url_username': 'admin',
            'url_password': 'admin',
            'name': 'datasource-elastic',
            'uid': 'xyz123',
            'ds_type': 'elasticsearch',
            'ds_url': 'https://elastic.company.com:9200',
            'database': '[logstash_]YYYY.MM.DD',
            'basic_auth_user': 'grafana',
            'basic_auth_password': 'grafana',
            'time_field': '@timestamp',
            'time_interval': '1m',
            'interval': 'Daily',
            'es_version': 56,
            'max_concurrent_shard_requests': 42,
            'tls_ca_cert': '/etc/ssl/certs/ca.pem'
        })
        module = grafana_datasource.setup_module_object()
        payload = grafana_datasource.get_datasource_payload(module.params)
        self.assertEqual(payload, expected_payload)
