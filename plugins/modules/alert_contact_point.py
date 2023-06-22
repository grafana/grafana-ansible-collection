#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Ishan Jain (@ishanjainn)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

DOCUMENTATION = '''
---
module: alert_contact_point
author:
  - Ishan Jain (@ishanjainn)
version_added: "0.0.1"
short_description: Manage Alerting Contact points in Grafana Cloud
description:
  - Create, Update and delete Contact points using Ansible.
requirements: [ "requests >= 1.0.0" ]
notes:
  - Does not support C(check_mode).
options:
  name:
    description:
      - Sets the name of the contact point.
    type: str
    required: true
  uid:
    description:
      - Sets the UID of the Contact point.
    type: str
    required: true
  type:
    description:
      - Sets Contact point type.
    type: str
    required: true
  settings:
    description:
      - Sets Contact point settings.
    type: dict
    required: true
  disableResolveMessage:
    description:
      - When set to C(true), Disables the resolve message [OK] that is sent when alerting state returns to C(false).
    type: bool
    default: false
  grafana_api_key:
    description:
      - Grafana API Key used to authenticate with Grafana.
    type: str
    required : true
  grafana_url:
    description:
      - URL of the Grafana instance (without trailing /).
    type: str
    required: true
  state:
    description:
      - State for the Grafana Instance.
    choices: [ present, absent ]
    type: str
    default: present
'''

EXAMPLES = '''
- name: Create/Update Alerting contact point
  grafana.grafana.alert_contact_point:
    name: ops-email
    uid: opsemail
    type: email
    settings:
      addresses: "ops@mydomain.com,devs@mydomain.com"
    grafana_url: "{{ grafana_url }}"
    grafana_api_key: "{{ grafana_api_key }}"
    state: present

- name: Delete Alerting contact point
  grafana.grafana.alert_contact_point:
    name: ops-email
    uid: opsemail
    type: email
    settings:
      addresses: "ops@mydomain.com,devs@mydomain.com"
    grafana_url: "{{ grafana_url }}"
    grafana_api_key: "{{ grafana_api_key }}"
    state: absent
'''

RETURN = r'''
output:
  description: Dict object containing Contact point information information.
  returned: On success
  type: dict
  contains:
    disableResolveMessage:
      description: When set to True, Disables the resolve message [OK] that is sent when alerting state returns to false.
      returned: state is present and on success
      type: bool
      sample: false
    name:
      description: The name for the contact point.
      returned: state is present and on success
      type: str
      sample: ops-email
    settings:
      description: Contains contact point settings.
      returned: state is present and on success
      type: dict
      sample: {
       addresses: "ops@mydomain.com,devs@mydomain.com"
      }
    uid:
      description: The UID for the contact point.
      returned: state is present and on success
      type: str
      sample: opsemail
    type:
      description: The type of contact point.
      returned: state is present and on success
      type: str
      sample: email
'''

from ansible.module_utils.basic import AnsibleModule, missing_required_lib
import requests

__metaclass__ = type

def call_grafana_api(module, method, url, json_data=None):
    headers = {"Authorization": 'Bearer ' + module.params['grafana_api_key']}
    response = requests.request(method, url, json=json_data, headers=headers)

    if response.status_code == 200 or response.status_code == 202:
        return True, response.json()
    else:
        return False, {"status": response.status_code, 'response': response.json()['message']}


def present_alert_contact_point(module):
    body = {
        'Name': module.params['name'],
        'UID': module.params['uid'],
        'type': module.params['type'],
        'settings': module.params['settings'],
        'DisableResolveMessage': module.params['disableResolveMessage']
    }
    api_url = module.params['grafana_url'] + '/api/v1/provisioning/contact-points'

    return call_grafana_api(module, "POST", api_url, json_data=body)


def absent_alert_contact_point(module):
    api_url = api_url = module.params['grafana_url'] + '/api/v1/provisioning/contact-points/' + module.params['uid']
    return call_grafana_api(module, "DELETE", api_url)


def main():
    module_args = dict(
        name=dict(type='str', required=True),
        uid=dict(type='str', required=True),
        type=dict(type='str', required=True),
        settings=dict(type='dict', required=True),
        disableResolveMessage=dict(type='bool', required=False, default=False),
        grafana_url=dict(type='str', required=True),
        grafana_api_key=dict(type='str', required=True, no_log=True),
        state=dict(type='str', required=False, default='present', choices=['present', 'absent'])
    )

    choice_map = {
        "present": present_alert_contact_point,
        "absent": absent_alert_contact_point,
    }

    module = AnsibleModule(
        argument_spec=module_args
    )

    if not requests:
        module.fail_json(msg=missing_required_lib('requests'))

    is_error, result = choice_map.get(module.params['state'])(module)

    if not is_error:
        module.exit_json(changed=True, output=result)
    else:
        module.fail_json(msg=result)


if __name__ == '__main__':
    main()