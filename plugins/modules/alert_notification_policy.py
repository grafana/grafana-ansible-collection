#!/usr/bin/python

DOCUMENTATION = '''
---
module: alert_notification_policy
author:
  - Ishan Jain (@ishanjainn)
version_added: "0.0.1"
short_description: Sets the notification policy tree in Grafana Alerting
description:
  - Set the notification policy tree using Ansible
options:
  Continue:
    description:
      - Continue matching subsequent sibling nodes if set to `True`.
    type: bool
    default: false
  GroupByStr:
    description:
      - List of string.
      - Group alerts when you receive a notification based on labels. If empty it will be inherited from the parent policy.
    type: list
    default: []
  MuteTimeIntervals:
    description:
      - List of string.
      - Add mute timing to policy
    type: list
    default: []
  root_policy_receiver:
    description:
      - Name of the contact point to set as the default receiver
    type: str
    default: grafana-default-email
  Routes:
    description:
      - List of objects
      - A Route is a node that contains definitions of how to handle alerts.
    type: list
    required: true
  groupInterval:
    description:
      - The waiting time to send a batch of new alerts for that group after the first notification was sent. If empty it will be inherited from the parent policy.
    type: str
    default: 5m
  groupWait:
    description:
      - The waiting time until the initial notification is sent for a new group created by an incoming alert. If empty it will be inherited from the parent policy.
    type: str
    default: 30s
  objectMatchers:
    description:
      - State for the Grafana CLoud stack.
    type: str
    default: present
    choices: [ present, absent ]
  repeatInterval:
    description:
      - The waiting time to resend an alert after they have successfully been sent.
    type: str 
    default: 4h
  stack_slug:
    description:
      - Name of the Grafana Cloud stack to which the notification policies will be added
    type: str
    required: true
  grafana_api_key:
    description:
      - Grafana API Key used to authenticate with Grafana.
    type: str
    required : true
'''

EXAMPLES = '''
- name: Set Notification policy tree
  alert_notification_policy:
    stack_slug: "{{ stack_slug }}"
    grafana_api_key: "{{ grafana_api_key }}"
    routes: [
      {
        receiver: myReceiver,
        object_matchers: [["env", "=", "Production"]],
      }
    ]
    
- name: Set nested Notification policies
  alert_notification_policy:
    routes: [
      {
        receiver: myReceiver,
        object_matchers: [["env", "=", "Production"],["team", "=", "ops"]],
        routes: [
          {
            receiver: myReceiver2,
            object_matchers: [["region", "=", "eu"]],
          }
        ]
      },
      {
        receiver: myReceiver3,
        object_matchers: [["env", "=", "Staging"]]
      }
    ]
    stack_slug: "{{ stack_slug }}"
    grafana_api_key: "{{ grafana_api_key }}"
'''

RETURN = r'''
output: 
  description: Dict object containing Notification tree information
  returned: On success
  type: dict
  contains:
    group_interval:
      description: The waiting time to send a batch of new alerts for that group after the first notification was sent. This is of the parent policy.
      returned: on success
      type: str
    group_wait:
      description: The waiting time until the initial notification is sent for a new group created by an incoming alert. This is of the parent policy.
      returned: on success
      type: str
    provenance:
      description: 
      returned: on success
      type: str
    receiver:
      description: The name of the default contact point
      returned: state is present and on success
      type: str
    repeat_interval:
      description: The waiting time to resend an alert after they have successfully been sent. This is of the parent policy
      returned: on success
      type: str
    routes:
      description: The entire notification tree returned as a list
      returned: on success
      type: list
'''

from ansible.module_utils.basic import AnsibleModule
import requests


def alert_notification_policy(module):
    body = {'routes': module.params['routes'], 'Continue': module.params['Continue'],
            'groupByStr': module.params['groupByStr'], 'muteTimeIntervals': module.params['muteTimeIntervals'],
            'receiver': module.params['root_policy_receiver'], 'group_interval': module.params['groupInterval'],
            'group_wait': module.params['groupWait'], 'object_matchers': module.params['objectMatchers'],
            'repeat_interval': module.params['repeatInterval']}

    api_url = 'https://' + module.params['stack_slug'] + '.grafana.net/api/v1/provisioning/policies'

    result = requests.put(api_url, json=body, headers={"Authorization": 'Bearer ' + module.params['grafana_api_key']})

    if result.status_code == 202:
        api_url = 'https://' + module.params['stack_slug'] + '.grafana.net/api/v1/provisioning/policies'

        result = requests.get(api_url, headers={"Authorization": 'Bearer ' + module.params['grafana_api_key']})
        return False, True, result.json()
    else:
        return True, False, {"status": result.status_code, 'response': result.json()['message']}


def main():
    module_args = dict(Continue=dict(type='bool', required=False, default=False),
                       groupByStr=dict(type='list', required=False, default=[]),
                       muteTimeIntervals=dict(type='list', required=False, default=[]),
                       root_policy_receiver=dict(type='str', required=False, default='grafana-default-email'),
                       routes=dict(type='list', required=True),
                       groupInterval=dict(type='str', required=False, default='5m'),
                       groupWait=dict(type='str', required=False, default='30s'),
                       repeatInterval=dict(type='str', required=False, default='4h'),
                       objectMatchers=dict(type='list', required=False, default=[]),
                       stack_slug=dict(type='str', required=True),
                       grafana_api_key=dict(type='str', required=True), )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    is_error, has_changed, result = alert_notification_policy(module)

    if not is_error:
        module.exit_json(changed=has_changed, output=result)
    else:
        module.fail_json(msg='Status code is ' + str(result['status']), output=result['response'])


if __name__ == '__main__':
    main()
