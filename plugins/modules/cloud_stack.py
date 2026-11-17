#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Ishan Jain (@ishanjainn)
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
notes:
  - Does not support C(check_mode).
options:
  name:
    description:
      - Sets the name of stack. Conventionally matches the URL of the instance. For example, C(stackslug.grafana.net).
    type: str
    required: true
  stack_slug:
    description:
      - Sets the subdomain of the Grafana instance. For example, if slug is B(stackslug), the instance URL will be C(https://stackslug.grafana.net).
    type: str
    required: true
  cloud_api_key:
    description:
      - Cloud API Key to authenticate with Grafana Cloud.
    type: str
    required : true
  region:
    description:
      - Sets the region for the Grafana Cloud stack.
    type: str
    default: us
    choices: [ us, us-azure, eu, au, eu-azure, prod-ap-southeast-0, prod-gb-south-0, prod-eu-west-3]
  url:
    description:
      - If you use a custom domain for the instance, you can provide it here. If not provided, Will be set to C(https://stackslug.grafana.net).
    type: str
  org_slug:
    description:
      - Name of the organization under which Cloud stack is created.
    type: str
    required: true
  delete_protection:
    description:
      - Enables or disables deletion protection for the Cloud stack.
      - When set to true, the stack cannot be deleted unless this flag is explicitly disabled.
    type: bool
    default: true
    required: false
  state:
    description:
      - State for the Grafana Cloud stack.
    type: str
    default: present
    choices: [ present, absent ]
'''

EXAMPLES = '''
- name: Create a Grafana Cloud stack
  grafana.grafana.cloud_stack:
    name: stack_name
    stack_slug: stack_name
    cloud_api_key: "{{ grafana_cloud_api_key }}"
    region: eu
    url: https://grafana.company_name.com
    org_slug: org_name
    delete_protection: true
    state: present

- name: Create a stack and use its OTLP endpoint instead of hardcoding it
  grafana.grafana.cloud_stack:
    name: stack_name
    stack_slug: stack_name
    cloud_api_key: "{{ grafana_cloud_api_key }}"
    org_slug: org_name
    state: present
  register: stack

- name: Show the connection details of the stack
  ansible.builtin.debug:
    msg:
      - "OTLP endpoint: {{ stack.connections.otlp.url }}/otlp"
      - "Prometheus private DNS: {{ stack.connections.tenants.prometheus.private_connectivity_info.private_dns }}"

- name: Delete a Grafana Cloud stack
  grafana.grafana.cloud_stack:
    name: stack_name
    slug: stack_name
    cloud_api_key: "{{ grafana_cloud_api_key }}"
    org_slug: org_name
    state: absent
'''

RETURN = r'''
  alertmanager_name:
    description: Name of the alertmanager instance.
    returned: always
    type: str
    sample: "stackname-alerts"
  alertmanager_url:
    description: URL of the alertmanager instance.
    returned: always
    type: str
    sample: "https://alertmanager-eu-west-0.grafana.net"
  cluster_slug:
    description: Slug for the cluster where the Grafana stack is deployed.
    returned: always
    type: str
    sample: "prod-eu-west-0"
  id:
    description: ID of the Grafana Cloud stack.
    returned: always
    type: int
    sample: 458182
  loki_url:
    description: URl for the Loki instance.
    returned: always
    type: str
    sample: "https://logs-prod-eu-west-0.grafana.net"
  orgID:
    description: ID of the Grafana Cloud organization.
    returned: always
    type: int
    sample: 652992
  prometheus_url:
    description: URl for the Prometheus instance.
    returned: always
    type: str
    sample: "https://prometheus-prod-01-eu-west-0.grafana.net"
  tempo_url:
    description: URl for the Tempo instance.
    returned: always
    type: str
    sample: "https://tempo-eu-west-0.grafana.net"
  url:
    description: URL of the Grafana Cloud stack.
    returned: always
    type: str
    sample: "https://stackname.grafana.net"
  delete_protection:
    description:
      - Enables or disables deletion protection for the Cloud stack.
      - When set to true, the stack cannot be deleted unless this flag is explicitly disabled.
    returned: always
    type: bool
    sample: true
  connections:
    description:
      - Connection details of the stack.
      - Use these instead of hardcoding endpoints. A stack region can be made of several clusters,
        so the endpoints can differ between stacks created in the same region.
      - Only returned when O(state=present).
    returned: when state is present
    type: dict
    contains:
      otlp:
        description: OTLP gateway of the stack.
        type: dict
        contains:
          url:
            description: Base URL of the OTLP gateway, or null if the API does not return one.
            type: str
            sample: "https://otlp-gateway-prod-eu-west-4.grafana.net"
          private_connectivity_info:
            description:
              - AWS PrivateLink details. The fields are empty if the stack does not support PrivateLink.
              - Every C(private_connectivity_info) in C(connections), and the C(pdc) endpoints, have this same structure.
            type: dict
            contains:
              private_dns:
                description: Private DNS name of the endpoint.
                type: str
                sample: "prod-eu-west-4-otlp-gateway.eu-west-2.vpce.grafana.net"
              service_name:
                description: Name of the VPC endpoint service.
                type: str
                sample: "com.amazonaws.vpce.eu-west-2.vpce-svc-0123456789abcdef0"
              regions:
                description: Regions the endpoint service is available in.
                type: list
                elements: str
                sample: ["eu-west-2"]
              availability_zones:
                description: Availability zones of the endpoint service.
                type: list
                elements: str
                sample: ["eu-west-2a", "eu-west-2b"]
              availability_zone_ids:
                description: Availability zone IDs of the endpoint service.
                type: list
                elements: str
                sample: ["euw2-az1", "euw2-az2"]
      pdc:
        description: Private data source connect (PDC) endpoints.
        type: dict
        contains:
          api:
            description: PDC API endpoint. Has the same structure as C(private_connectivity_info).
            type: dict
          gateway:
            description: PDC gateway endpoint. Has the same structure as C(private_connectivity_info).
            type: dict
      services:
        description: URLs of other services.
        type: dict
        contains:
          oncall_api_url:
            description: URL of the OnCall API, or null if the API does not return one.
            type: str
            sample: "https://oncall-prod-eu-west-0.grafana.net/oncall"
          influx_url:
            description: URL of the InfluxDB endpoint, or null if the API does not return one.
            type: str
            sample: "https://prometheus-prod-01-eu-west-0.grafana.net"
      tenants:
        description:
          - Connection details of the stack tenants, keyed by C(prometheus), C(logs), C(traces), C(profiles), C(graphite) and C(fleet_management).
          - Each one has a C(private_connectivity_info) structure.
          - All keys are always present, with empty values if the stack does not have that tenant.
        type: dict
'''

import time

from ansible.module_utils.basic import AnsibleModule, missing_required_lib
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

__metaclass__ = type


STACKS_API_BASE = 'https://grafana.com/api/v1/stacks'
GCOM_API_BASE = 'https://grafana.com/api/instances'

# The connections of a new stack are not available straight away, so a 404 is retried.
CONNECTIONS_RETRY_TIMEOUT = 120
CONNECTIONS_RETRY_INTERVAL = 5

# Tenant types returned by the API -> keys in the module result.
CONNECTIONS_TENANTS = {
    'prometheus': 'prometheus',
    'logs': 'logs',
    'traces': 'traces',
    'profiles': 'profiles',
    'graphite': 'graphite',
    'agent-management': 'fleet_management',
}


def get_headers(module):
    return {
        "Authorization": 'Bearer ' + module.params['cloud_api_key'],
        'User-Agent': 'grafana-ansible-collection',
    }


def get_stack_details_from_gcom(module, stack_id):
    api_url = f'{GCOM_API_BASE}/{stack_id}'
    result = requests.get(api_url, headers=get_headers(module))
    if result.status_code == 200:
        return result.json()
    return None


def flatten_private_connectivity_info(info):
    info = info or {}
    return {
        'private_dns': info.get('privateDNS', ''),
        'service_name': info.get('serviceName', ''),
        'regions': info.get('regions') or [],
        'availability_zones': info.get('availabilityZones') or [],
        'availability_zone_ids': info.get('availabilityZoneIds') or [],
    }


def flatten_connections(connections):
    otlp = connections.get('otlp') or {}
    pdc = connections.get('pdc') or {}
    services = connections.get('services') or {}

    tenants = {name: {'private_connectivity_info': flatten_private_connectivity_info(None)}
               for name in CONNECTIONS_TENANTS.values()}
    seen = set()
    for tenant in connections.get('tenants') or []:
        name = CONNECTIONS_TENANTS.get(tenant.get('type'))
        # Like the Terraform provider, only the first tenant of each type is used.
        if name and name not in seen:
            seen.add(name)
            tenants[name] = {'private_connectivity_info': flatten_private_connectivity_info(tenant.get('privateConnectivityInfo'))}

    return {
        'otlp': {
            'url': otlp.get('url'),
            'private_connectivity_info': flatten_private_connectivity_info(otlp.get('privateConnectivityInfo')),
        },
        'pdc': {
            'api': flatten_private_connectivity_info(pdc.get('api')),
            'gateway': flatten_private_connectivity_info(pdc.get('gateway')),
        },
        'services': {
            'oncall_api_url': services.get('oncallApiUrl'),
            'influx_url': services.get('influxUrl'),
        },
        'tenants': tenants,
    }


def get_stack_connections(module, stack_id):
    api_url = f'{STACKS_API_BASE}/{stack_id}/connections'
    deadline = time.monotonic() + CONNECTIONS_RETRY_TIMEOUT

    while True:
        result = requests.get(api_url, headers=get_headers(module))
        if result.status_code == 200:
            return False, flatten_connections(result.json())
        if result.status_code != 404 or time.monotonic() >= deadline:
            try:
                message = result.json()['message']
            except (ValueError, KeyError, TypeError):
                message = result.text
            return True, {"status": result.status_code, 'response': message}
        time.sleep(CONNECTIONS_RETRY_INTERVAL)


def present_cloud_stack(module):
    if not module.params['url']:
        module.params['url'] = 'https://' + module.params['stack_slug'] + '.grafana.net'

    body = {
        'name': module.params['name'],
        'slug': module.params['stack_slug'],
        'region': module.params['region'],
        'org': module.params['org_slug'],
        'url': module.params['url'],
        'deleteProtection': module.params['delete_protection'],
    }
    headers = get_headers(module)

    result = requests.post(STACKS_API_BASE, json=body, headers=headers)
    if result.status_code == 200:
        stack = result.json()
        full_details = get_stack_details_from_gcom(module, stack['id'])
        if full_details:
            return False, True, full_details
        return False, True, stack
    elif result.status_code in [409, 403] and result.json()['message'] in ["That URL has already been taken, please try an alternate URL", "Hosted instance limit reached"]:
        stack_found = False
        if result.json()['message'] == "That URL has already been taken, please try an alternate URL":
            api_url = STACKS_API_BASE + '?org=' + module.params['org_slug']
            result = requests.get(api_url, headers=headers)
            list_response = result.json()
            if result.status_code != 200:
                return True, False, {"status": result.status_code, 'response': list_response.get('message', str(list_response))}
            stackInfo = {}
            for stack in list_response.get('items', []):
                if stack['slug'] == module.params['stack_slug']:
                    stack_found = True
                    stackInfo = stack
            if stack_found:
                if body['deleteProtection'] == stackInfo['deleteProtection']:
                    full_details = get_stack_details_from_gcom(module, stackInfo['id'])
                    if full_details:
                        return False, False, full_details
                    return False, False, stackInfo
                api_url = f'{STACKS_API_BASE}/{stackInfo["id"]}'
                result = requests.post(api_url, json={'deleteProtection': body['deleteProtection']}, headers=headers)
                if result.status_code != 200:
                    return True, False, {"status": result.status_code, 'response': result.json()['message']}
                full_details = get_stack_details_from_gcom(module, stackInfo['id'])
                if full_details:
                    return False, True, full_details
                return False, True, result.json()
            else:
                return True, False, "Stack is not found under your org"
        elif result.json()['message'] == "Hosted instance limit reached":
            return True, False, "You have reached Maximum number of Cloud Stacks in your Org."
    else:
        return True, False, {"status": result.status_code, 'response': result.json()['message']}


def absent_cloud_stack(module):
    api_url = f"{STACKS_API_BASE}/{module.params['stack_slug']}"

    gcom_details = get_stack_details_from_gcom(module, module.params['stack_slug'])

    result = requests.delete(api_url, headers=get_headers(module))

    if result.status_code == 200:
        if gcom_details:
            return False, True, gcom_details
        return False, True, result.json()
    else:
        return True, False, {"status": result.status_code, 'response': result.json()['message']}


def main():

    module_args = dict(
        name=dict(type='str', required=True),
        stack_slug=dict(type='str', required=True),
        cloud_api_key=dict(type='str', required=True, no_log=True),
        region=dict(type='str', required=False, default='us',
                    choices=['us', 'us-azure', 'eu', 'au', 'eu-azure', 'prod-ap-southeast-0', 'prod-gb-south-0',
                             'prod-eu-west-3']),
        url=dict(type='str', required=False),
        org_slug=dict(type='str', required=True),
        state=dict(type='str', required=False, default='present', choices=['present', 'absent']),
        delete_protection=dict(type='bool', required=False, default=True),
    )

    choice_map = {
        "present": present_cloud_stack,
        "absent": absent_cloud_stack,
    }

    module = AnsibleModule(
        argument_spec=module_args
    )

    if not HAS_REQUESTS:
        module.fail_json(msg=missing_required_lib('requests'))

    is_error, has_changed, result = choice_map.get(
        module.params['state'])(module)

    if not is_error:
        extra = {}
        if module.params['state'] == 'present':
            is_error, connections = get_stack_connections(module, result['id'])
            if is_error:
                module.fail_json(msg=connections)
            extra['connections'] = connections

        module.exit_json(changed=has_changed,
                         alertmanager_name=result['amInstanceName'],
                         url=result['url'], id=result['id'],
                         cluster_slug=result['clusterName'],
                         orgID=result['orgId'],
                         loki_url=result['hlInstanceUrl'],
                         prometheus_url=result['hmInstancePromUrl'],
                         tempo_url=result['htInstanceUrl'],
                         alertmanager_url=result['amInstanceUrl'],
                         delete_protection=result['deleteProtection'],
                         **extra)
    else:
        module.fail_json(msg=result)


if __name__ == '__main__':
    main()
