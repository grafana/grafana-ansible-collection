#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Rainer Leber <rainerleber@gmail.com> <rainer.leber@sva.de>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

DOCUMENTATION = '''
---
module: cloud_stack
author:
  - Ishan Jain (@ishanjainn)
version_added: "0.0.1"
short_description: Manage Grafana Cloud stack
description:
  - Create and delete Grafana Cloud stacks using Ansible.
requirements: [ "requests >= 1.0.0" ]
options:
  name:
    description:
      - Name of stack. Conventionally matches the URL of the instance. For example, "<stack_slug>.grafana.net".
    type: str
    required: true
  stack_slug:
    description:
      - Subdomain of the Grafana instance. For example, if slug is <stack_slug>, the instance URL will be https://<stack_slug>.grafana.net
    type: str
    required: true
  cloud_api_key:
    description:
      - CLoud API Key to authenticate with Grafana Cloud.
    type: str
    required : true
  region:
    description:
      - Choose a region for your stack.
    type: str
    default: us
    choices: [ us, us-azure, eu, au, eu-azure, prod-ap-southeast-0, prod-gb-south-0, prod-eu-west-3]
  url:
    description:
      - If you use a custom domain for the instance, you can provide it here. For example, "https://grafana.yourdoman.io".
    type: str
    default: https://<stack_slug>.grafana.net
  org_slug:
    description:
      - Name of the organization under which Cloud stack is created.
    type: str
    required: false
  state:
    description:
      - State for the Grafana CLoud stack.
    type: str
    default: present
    choices: [ present, absent ]
'''

EXAMPLES = '''
- name: Create a Grafana Cloud stack
  grafana.grafana.cloud_stack:
    name: company_name
    slug: company_name
    cloud_api_key: "{{ grafana_cloud_api_key }}"
    region: eu
    url: https://grafana.company_name.com
    state: present

- name: Delete a Grafana Cloud stack
  grafana.grafana.cloud_stack:
    name: company_name
    slug: company_name
    cloud_api_key: "{{ grafana_cloud_api_key }}"
    state: absent
'''

RETURN = r'''
  alertmanager_name:
    description: Name of the alertmanager instance
    returned: always
    type: str
  alertmanager_url:
    description: URL of the alertmanager instance
    returned: always
    type: str
  cluster_slug:
    description: Slug for the cluster where the Grafana stack is deployed
    returned: always
    type: str
  id:
    description: ID of the Grafana Cloud stack
    returned: always
    type: int
  loki_url:
    description: URl for the Loki instance
    returned: always
    type: str
  orgID:
    description: ID of the Grafana Cloud organization
    returned: always
    type: int
  prometheus_url:
    description: URl for the Prometheus instance
    returned: always
    type: str
  tempo_url:
    description: URl for the Tempo instance
    returned: always
    type: str
  url:
    description: URL of the Grafana Cloud stack
    returned: always
    type: str
'''

from ansible.module_utils.basic import AnsibleModule
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

__metaclass__ = type


def present_cloud_stack(module):
    if not module.params['url']:
        module.params['url'] = 'https://' + module.params['stack_slug'] + '.grafana.net'

    body = {
        'name': module.params['name'],
        'slug': module.params['stack_slug'],
        'region': module.params['region'],
        'url': module.params['url']
    }
    api_url = 'https://grafana.com/api/instances'

    result = requests.post(api_url, json=body, headers={"Authorization": 'Bearer ' + module.params['cloud_api_key']})

    if result.status_code == 200:
        return False, True, result.json()

    elif (result.status_code == 409 and result.json()['message'] == "That url is not available") or (result.status_code == 403 and result.json()['message'] == "Hosted instance limit reached"):
        api_url = 'https://grafana.com/api/orgs/' + module.params['org_slug'] + '/instances'

        result = requests.get(api_url, headers={"Authorization": 'Bearer ' + module.params['cloud_api_key']})

        for stack in result.json()['items']:
            if stack['slug'] == module.params['stack_slug']:
                return False, False, stack
    else:
        return True, False, {"status": result.status_code, 'response': result.json()['message']}


def absent_cloud_stack(module):
    api_url = 'https://grafana.com/api/instances/' + module.params['stack_slug']

    result = requests.delete(api_url, headers={"Authorization": 'Bearer ' + module.params['cloud_api_key']})

    if result.status_code == 200:
        return False, True, result.json()
    else:
        return True, False, {"status": result.status_code, 'response': result.json()['message']}


def main():
    module_args = dict(
        name=dict(type='str', required=True),
        stack_slug=dict(type='str', required=True),
        cloud_api_key=dict(type='str', required=True),
        region=dict(type='str', required=False, default='us',
                    choices=['us', 'us-azure', 'eu', 'au', 'eu-azure', 'prod-ap-southeast-0', 'prod-gb-south-0',
                             'prod-eu-west-3']),
        url=dict(type='str', required=False),
        org_slug=dict(type='str', required=True),
        state=dict(type='str', required=False, default='present', choices=['present', 'absent'])
    )

    choice_map = {
        "present": present_cloud_stack,
        "absent": absent_cloud_stack,
    }

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    is_error, has_changed, result = choice_map.get(
        module.params['state'])(module)

    if not is_error:
        module.exit_json(changed=has_changed,
                         alertmanager_name=result['amInstanceName'],
                         url=result['url'], id=result['id'],
                         cluster_slug=result['clusterName'],
                         orgID=result['orgId'],
                         loki_url=result['hlInstanceUrl'],
                         prometheus_url=result['hmInstancePromUrl'],
                         tempo_url=result['htInstanceUrl'],
                         alertmanager_url=result['amInstanceUrl'])
    else:
        module.fail_json(msg=result)


if __name__ == '__main__':
    main()
