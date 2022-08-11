#!/usr/bin/python

DOCUMENTATION = '''
---
module: grafana.grafana.alert_contact_point
author:
  - Ishan Jain (@ishanjainn)
version_added: "0.0.1"
short_description: Manage Alerting Contact points in Grafana
description:
  - Create, Update and delete Contact points using Ansible.
options:
  name:
    description:
      - Name of the contact point
    type: str
    required: true
  uid:
    description:
      - Sets the UID of the Contact point.
    type: str
    required: true
  type:
    description:
      - Contact point type
    type: str
    required: true
  settings:
    description:
      - Contact point settings
    type: dict
    required: true
  DisableResolveMessage:
    description:
      - When set to True, Disables the resolve message [OK] that is sent when alerting state returns to false
    type: bool
    default: false
  grafana_api_key:
    description:
      - Grafana API Key used to authenticate with Grafana.
    type: str
    required : true
  state:
    description:
      - State for the Grafana CLoud stack.
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
    settings: {
       addresses: "ops@mydomain.com,devs@mydomain.com"
     }
    stack_slug: "{{ stack_slug }}"
    grafana_api_key: "{{ grafana_api_key }}"
    state: present

- name: Delete Alerting contact point
  grafana.grafana.alert_contact_point:
    name: ops-email
    uid: opsemail
    type: email
    settings: {
       addresses: "ops@mydomain.com,devs@mydomain.com"
     }
    stack_slug: "{{ stack_slug }}"
    grafana_api_key: "{{ grafana_api_key }}"
    state: absent
'''

RETURN = r'''
output:
  description: Dict object containing Contact point information information
  returned: On success
  type: dict
  contains:
    disableResolveMessage:
      description: When set to True, Disables the resolve message [OK] that is sent when alerting state returns to false
      returned: state is present and on success
      type: bool
    name:
      description: The name for the contact point
      returned: state is present and on success
      type: str
    settings:
      description: Contains contact point settings
      returned: state is present and on success
      type: dict
    uid:
      description: The UID for the contact point
      returned: state is present and on success
      type: str
    type:
      description: The type of contact point
      returned: state is present and on success
      type: str
'''

from ansible.module_utils.basic import AnsibleModule
import requests


def present_alert_contact_point(module):
    body = {
        'Name': module.params['name'],
        'UID': module.params['uid'],
        'type': module.params['type'],
        'settings': module.params['settings'],
        'DisableResolveMessage': module.params['DisableResolveMessage']
    }
    api_url = 'https://' + module.params['stack_slug'] + '.grafana.net/api/v1/provisioning/contact-points'

    result = requests.post(api_url, json=body, headers={"Authorization": 'Bearer ' + module.params['grafana_api_key']})

    if result.status_code == 202:
        return False, True, result.json()
    elif result.status_code == 500:
        api_url = 'https://' + module.params['stack_slug'] + '.grafana.net/api/v1/provisioning/contact-points/' + \
                  module.params['uid']

        result = requests.put(api_url, json=body, headers={"Authorization": 'Bearer ' + module.params['grafana_api_key']})

        if result.status_code == 202:
            api_url = 'https://' + module.params['stack_slug'] + '.grafana.net/api/v1/provisioning/contact-points'

            result = requests.get(api_url, headers={"Authorization": 'Bearer ' + module.params['grafana_api_key']})

            for contact_points in result.json():
                if contact_points['uid'] == module.params['uid']:
                    return False, True, contact_points
        else:
            return True, False, {"status": result.status_code, 'response': result.json()['message']}

    else:
        return True, False, {"status": result.status_code, 'response': result.json()['message']}


def absent_alert_contact_point(module):
    already_exists = False
    api_url = 'https://' + module.params['stack_slug'] + '.grafana.net/api/v1/provisioning/contact-points'

    result = requests.get(api_url, headers={"Authorization": 'Bearer ' + module.params['grafana_api_key']})

    for contact_points in result.json():
        if contact_points['uid'] == module.params['uid']:
            already_exists = True
    if already_exists:
        api_url = 'https://' + module.params['stack_slug'] + '.grafana.net/api/v1/provisioning/contact-points/' + \
                  module.params['uid']

        result = requests.delete(api_url, headers={"Authorization": 'Bearer ' + module.params['grafana_api_key']})

        if result.status_code == 202:
            return False, True, result.json()
        else:
            return True, False, {"status": result.status_code, 'response': result.json()['message']}
    else:
        return True, False, "Alert Contact point does not exist"


def main():
    module_args = dict(
        name=dict(type='str', required=True),
        uid=dict(type='str', required=True),
        type=dict(type='str', required=True),
        settings=dict(type='dict', required=True),
        DisableResolveMessage=dict(type='bool', required=False, default=False),
        stack_slug=dict(type='str', required=True),
        grafana_api_key=dict(type='str', required=True),
        state=dict(type='str', required=False, default='present', choices=['present', 'absent'])
    )

    choice_map = {
        "present": present_alert_contact_point,
        "absent": absent_alert_contact_point,
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