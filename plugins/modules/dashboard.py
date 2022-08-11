#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Rainer Leber <rainerleber@gmail.com> <rainer.leber@sva.de>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

DOCUMENTATION = '''
---
module: dashboard
author:
  - Ishan Jain (@ishanjainn)
version_added: "0.0.1"
short_description: Manage Dashboards in Grafana
description:
  - Create, Update and delete Dashboards using Ansible.
options:
  dashboard:
    description:
      - JSON source code for dashboard
    type: dict
    required: true
  stack_slug:
    description:
      - Name of the Grafana Cloud stack to which the notification policies will be added
    type: str
    required: true
  cloud_api_key:
    description:
      - CLoud API Key to authenticate with Grafana Cloud.
    type: str
    required : true
  state:
    description:
      - State for the Grafana CLoud stack.
    choices: [ present, absent ]
    default: present
    type: str
'''

EXAMPLES = '''
- name: Create/Update a dashboard
  grafana.grafana.dashboard:
    datasource: "{{ lookup('ansible.builtin.file', 'dashboard.json') }}"
    stack_slug: "{{ stack_slug }}"
    cloud_api_key: "{{ grafana_cloud_api_key }}"
    state: present

- name: Delete dashboard
  grafana.grafana.dashboard:
    datasource: "{{ lookup('ansible.builtin.file', 'dashboard.json') }}"
    stack_slug: "{{ stack_slug }}"
    cloud_api_key: "{{ grafana_cloud_api_key }}"
    state: absent
'''

RETURN = r'''
output:
  description: Dict object containing folder information
  returned: On success
  type: dict
  contains:
    id:
      description: The ID for the dashboard
      returned: on success
      type: int
    slug:
      description: The slug for the dashboard
      returned: state is present and on success
      type: str
    status:
      description: The status of the dashboard
      returned: state is present and on success
      type: str
    uid:
      description: The UID for the dashboard
      returned: state is present and on success
      type: str
    url:
      description: The endpoint for the dashboard
      returned: state is present and on success
      type: str
    version:
      description: The version of the dashboard
      returned: state is present and on success
      type: int
    message:
      description: The message returned after the operation on the dashboard
      returned: state is absent and on success
      type: str
    title:
      description: The name of the dashboard
      returned: state is absent and on success
      type: str
'''

from ansible.module_utils.basic import AnsibleModule
import requests

__metaclass__ = type


def present_dashboard(module):

    api_url = 'https://' + module.params['stack_slug'] + '.grafana.net/api/dashboards/db'

    result = requests.post(api_url, json=module.params['dashboard'], headers={"Authorization": 'Bearer ' + module.params['cloud_api_key']})

    if result.status_code == 200:
        return False, True, result.json()
    else:
        return True, False, {"status": result.status_code, 'response': result.json()['message']}


def absent_dashboard(module):
    if 'uid' not in module.params['dashboard']['dashboard']:
        return True, False, "UID is not defined in the the Dashboard configuration"

    api_url = api_url = 'https://' + module.params['stack_slug'] + '.grafana.net/api/dashboards/uid/' + module.params['dashboard']['dashboard']['uid']

    result = requests.delete(api_url, headers={"Authorization": 'Bearer ' + module.params['cloud_api_key']})

    if result.status_code == 200:
        return False, True, result.json()
    else:
        return True, False, {"status": result.status_code, 'response': result.json()['message']}


def main():
    module_args = dict(
        dashboard=dict(type='dict', required=True),
        stack_slug=dict(type='str', required=True),
        cloud_api_key=dict(type='str', required=True),
        state=dict(type='str', required=False, default='present', choices=['present', 'absent'])
    )

    choice_map = {
        "present": present_dashboard,
        "absent": absent_dashboard,
    }

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    is_error, has_changed, result = choice_map.get(
        module.params['state'])(module)

    if not is_error:
        module.exit_json(changed=has_changed, output=result)
    else:
        module.fail_json(msg=result)


if __name__ == '__main__':
    main()
