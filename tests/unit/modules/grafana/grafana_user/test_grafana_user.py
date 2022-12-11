from __future__ import (absolute_import, division, print_function)

from unittest import TestCase
from unittest.mock import call, patch, MagicMock
from ansible_collections.community.grafana.plugins.modules import grafana_user
from ansible.module_utils._text import to_bytes
from ansible.module_utils import basic
from ansible.module_utils.urls import basic_auth_header
import json

__metaclass__ = type


class MockedReponse(object):
    def __init__(self, data):
        self.data = data

    def read(self):
        return self.data


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


def set_module_args(args):
    """prepare arguments so that they will be picked up during module creation"""
    args = json.dumps({'ANSIBLE_MODULE_ARGS': args})
    basic._ANSIBLE_ARGS = to_bytes(args)


def user_deleted_resp():
    server_response = json.dumps({"message": "User deleted"})
    return (MockedReponse(server_response), {"status": 200})


def user_already_exists_resp():
    server_response = json.dumps({"message": "failed to create user"})
    return (MockedReponse(server_response), {"status": 500})


def user_created_resp():
    server_response = json.dumps({
        "id": 2,
        "email": "robin@gotham.com",
        "name": "Robin",
        "login": "adrobinmin",
        "theme": "light",
        "orgId": 1,
        "isGrafanaAdmin": False,
        "isDisabled": False,
        "isExternal": False,
        "authLabels": None,
        "updatedAt": "2019-09-25T14:44:37+01:00",
        "createdAt": "2019-09-25T14:44:37+01:00"
    }, sort_keys=True)
    return (MockedReponse(server_response), {"status": 200})


class GrafanaUserTest(TestCase):

    def setUp(self):
        self.authorization = basic_auth_header("admin", "changeme")
        self.mock_module_helper = patch.multiple(basic.AnsibleModule,
                                                 exit_json=exit_json,
                                                 fail_json=fail_json)
        self.mock_module_helper.start()
        self.addCleanup(self.mock_module_helper.stop)

    # create an already existing user
    @patch('ansible_collections.community.grafana.plugins.modules.grafana_user.fetch_url')
    def test_create_user_existing_user(self, mock_fetch_url):
        set_module_args({
            'url': 'https://grafana.example.com',
            'url_username': 'admin',
            'url_password': 'changeme',
            'name': 'Joker',
            'email': 'joker@gotham.com',
            'login': 'joker',
            'password': 'oups',
            'state': 'present'
        })
        module = grafana_user.setup_module_object()
        mock_fetch_url.return_value = user_already_exists_resp()

        grafana_iface = grafana_user.GrafanaUserInterface(module)
        with self.assertRaises(AnsibleFailJson):
            grafana_iface.create_user(
                'Joker', 'joker@gotham.com', 'joker', 'oups')
            mock_fetch_url.assert_called_once_with(
                module,
                'https://grafana.example.com/api/admin/users',
                data=json.dumps({'name': 'Joker', 'email': 'joker@gotham.com',
                                 'login': 'joker', 'password': 'oups'}, sort_keys=True),
                headers={'Content-Type': 'application/json',
                         'Authorization': self.authorization},
                method='POST')

    # create a new user
    @patch('ansible_collections.community.grafana.plugins.modules.grafana_user.fetch_url')
    def test_create_user_new_user(self, mock_fetch_url):
        set_module_args({
            'url': 'https://grafana.example.com',
            'url_username': 'admin',
            'url_password': 'changeme',
            'name': 'Robin',
            'email': 'robin@gotham.com',
            'login': 'robin',
            'password': 'oups',
            'state': 'present'
        })
        module = grafana_user.setup_module_object()

        mock_fetch_url.return_value = user_created_resp()

        expected_fetch_url_calls = [
            # first call to create user
            call(
                module,
                'https://grafana.example.com/api/admin/users',
                data=json.dumps({'name': 'Robin', 'email': 'robin@gotham.com',
                                 'login': 'robin', 'password': 'oups'}, sort_keys=True),
                headers={'Content-Type': 'application/json',
                         'Authorization': self.authorization},
                method='POST'),

            # second call to return created user
            call(
                module,
                'https://grafana.example.com/api/users/lookup?loginOrEmail=robin',
                data=None,
                headers={'Content-Type': 'application/json',
                         'Authorization': self.authorization},
                method='GET'),
        ]

        grafana_iface = grafana_user.GrafanaUserInterface(module)
        result = grafana_iface.create_user(
            'Robin', 'robin@gotham.com', 'robin', 'oups')

        mock_fetch_url.assert_has_calls(
            expected_fetch_url_calls, any_order=False)

        self.assertEquals(result, {
            "id": 2,
            "email": "robin@gotham.com",
            "name": "Robin",
            "login": "adrobinmin",
            "theme": "light",
            "orgId": 1,
            "isGrafanaAdmin": False,
            "isDisabled": False,
            "isExternal": False,
            "authLabels": None,
            "updatedAt": "2019-09-25T14:44:37+01:00",
            "createdAt": "2019-09-25T14:44:37+01:00"
        })

    @patch('ansible_collections.community.grafana.plugins.modules.grafana_user.fetch_url')
    def test_delete_user(self, mock_fetch_url):
        set_module_args({
            'url': 'https://grafana.example.com',
            'url_username': 'admin',
            'url_password': 'changeme',
            'login': 'batman',
            'state': 'absent'
        })
        module = grafana_user.setup_module_object()
        mock_fetch_url.return_value = user_deleted_resp()

        grafana_iface = grafana_user.GrafanaUserInterface(module)
        user_id = 42
        result = grafana_iface.delete_user(user_id)
        mock_fetch_url.assert_called_once_with(
            module,
            'https://grafana.example.com/api/admin/users/42',
            data=None,
            headers={'Content-Type': 'application/json',
                     'Authorization': self.authorization},
            method='DELETE')
        self.assertEquals(result, {"message": "User deleted"})
