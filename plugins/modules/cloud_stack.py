#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Ishan Jain (@ishanjainn)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

DOCUMENTATION = """
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
"""

EXAMPLES = """
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
      - "OTLP endpoint: {{ stack.otlp_url }}/otlp"
      - "Prometheus private DNS: {{ stack.prometheus_private_connectivity_info_private_dns }}"

- name: Delete a Grafana Cloud stack
  grafana.grafana.cloud_stack:
    name: stack_name
    slug: stack_name
    cloud_api_key: "{{ grafana_cloud_api_key }}"
    org_slug: org_name
    state: absent
"""

RETURN = r"""
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
  otlp_url:
    description:
      - Base URL of the OTLP gateway, or null if the API does not return one.
      - The username is the stack ID, see the C(id) return value.
      - Only returned when O(state=present). Use this instead of hardcoding endpoints, a stack region can be made of several clusters.
    returned: when state is present
    type: str
    sample: "https://otlp-gateway-prod-eu-west-4.grafana.net"
  oncall_api_url:
    description: Base URL of the OnCall API, or null if the API does not return one. Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "https://oncall-prod-eu-west-0.grafana.net/oncall"
  influx_url:
    description:
      - Base URL of the InfluxDB endpoint, or null if the API does not return one.
      - The username is the Prometheus user ID of the stack.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "https://prometheus-prod-01-eu-west-0.grafana.net"
  fleet_management_private_connectivity_info_availability_zone_ids:
    description:
      - Availability zone IDs for Fleet Management when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["euw2-az1"]
  fleet_management_private_connectivity_info_availability_zones:
    description:
      - Availability zones for Fleet Management when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2a"]
  fleet_management_private_connectivity_info_private_dns:
    description:
      - Private DNS name for Fleet Management when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "prod-eu-west-4-fleet-management.eu-west-2.vpce.grafana.net"
  fleet_management_private_connectivity_info_regions:
    description:
      - Regions for Fleet Management when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2"]
  fleet_management_private_connectivity_info_service_name:
    description:
      - VPC endpoint service name for Fleet Management when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "com.amazonaws.vpce.eu-west-2.vpce-svc-0123456789abcdef0"
  graphite_private_connectivity_info_availability_zone_ids:
    description:
      - Availability zone IDs for Graphite when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["euw2-az1"]
  graphite_private_connectivity_info_availability_zones:
    description:
      - Availability zones for Graphite when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2a"]
  graphite_private_connectivity_info_private_dns:
    description:
      - Private DNS name for Graphite when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "prod-eu-west-4-graphite.eu-west-2.vpce.grafana.net"
  graphite_private_connectivity_info_regions:
    description:
      - Regions for Graphite when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2"]
  graphite_private_connectivity_info_service_name:
    description:
      - VPC endpoint service name for Graphite when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "com.amazonaws.vpce.eu-west-2.vpce-svc-0123456789abcdef0"
  logs_private_connectivity_info_availability_zone_ids:
    description:
      - Availability zone IDs for Logs when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["euw2-az1"]
  logs_private_connectivity_info_availability_zones:
    description:
      - Availability zones for Logs when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2a"]
  logs_private_connectivity_info_private_dns:
    description:
      - Private DNS name for Logs when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "prod-eu-west-4-logs.eu-west-2.vpce.grafana.net"
  logs_private_connectivity_info_regions:
    description: Regions for Logs when using AWS PrivateLink. Empty if the stack does not support PrivateLink. Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2"]
  logs_private_connectivity_info_service_name:
    description:
      - VPC endpoint service name for Logs when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "com.amazonaws.vpce.eu-west-2.vpce-svc-0123456789abcdef0"
  otlp_private_connectivity_info_availability_zone_ids:
    description:
      - Availability zone IDs for OTLP when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["euw2-az1"]
  otlp_private_connectivity_info_availability_zones:
    description:
      - Availability zones for OTLP when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2a"]
  otlp_private_connectivity_info_private_dns:
    description:
      - Private DNS name for OTLP when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "prod-eu-west-4-otlp.eu-west-2.vpce.grafana.net"
  otlp_private_connectivity_info_regions:
    description: Regions for OTLP when using AWS PrivateLink. Empty if the stack does not support PrivateLink. Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2"]
  otlp_private_connectivity_info_service_name:
    description:
      - VPC endpoint service name for OTLP when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "com.amazonaws.vpce.eu-west-2.vpce-svc-0123456789abcdef0"
  pdc_api_private_connectivity_info_availability_zone_ids:
    description:
      - Availability zone IDs for PDC's API when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["euw2-az1"]
  pdc_api_private_connectivity_info_availability_zones:
    description:
      - Availability zones for PDC's API when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2a"]
  pdc_api_private_connectivity_info_private_dns:
    description:
      - Private DNS name for PDC's API when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "prod-eu-west-4-pdc-api.eu-west-2.vpce.grafana.net"
  pdc_api_private_connectivity_info_regions:
    description:
      - Regions for PDC's API when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2"]
  pdc_api_private_connectivity_info_service_name:
    description:
      - VPC endpoint service name for PDC's API when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "com.amazonaws.vpce.eu-west-2.vpce-svc-0123456789abcdef0"
  pdc_gateway_private_connectivity_info_availability_zone_ids:
    description:
      - Availability zone IDs for PDC's Gateway when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["euw2-az1"]
  pdc_gateway_private_connectivity_info_availability_zones:
    description:
      - Availability zones for PDC's Gateway when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2a"]
  pdc_gateway_private_connectivity_info_private_dns:
    description:
      - Private DNS name for PDC's Gateway when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "prod-eu-west-4-pdc-gateway.eu-west-2.vpce.grafana.net"
  pdc_gateway_private_connectivity_info_regions:
    description:
      - Regions for PDC's Gateway when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2"]
  pdc_gateway_private_connectivity_info_service_name:
    description:
      - VPC endpoint service name for PDC's Gateway when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "com.amazonaws.vpce.eu-west-2.vpce-svc-0123456789abcdef0"
  profiles_private_connectivity_info_availability_zone_ids:
    description:
      - Availability zone IDs for Profiles when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["euw2-az1"]
  profiles_private_connectivity_info_availability_zones:
    description:
      - Availability zones for Profiles when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2a"]
  profiles_private_connectivity_info_private_dns:
    description:
      - Private DNS name for Profiles when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "prod-eu-west-4-profiles.eu-west-2.vpce.grafana.net"
  profiles_private_connectivity_info_regions:
    description:
      - Regions for Profiles when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2"]
  profiles_private_connectivity_info_service_name:
    description:
      - VPC endpoint service name for Profiles when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "com.amazonaws.vpce.eu-west-2.vpce-svc-0123456789abcdef0"
  prometheus_private_connectivity_info_availability_zone_ids:
    description:
      - Availability zone IDs for Prometheus when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["euw2-az1"]
  prometheus_private_connectivity_info_availability_zones:
    description:
      - Availability zones for Prometheus when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2a"]
  prometheus_private_connectivity_info_private_dns:
    description:
      - Private DNS name for Prometheus when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "prod-eu-west-4-prometheus.eu-west-2.vpce.grafana.net"
  prometheus_private_connectivity_info_regions:
    description:
      - Regions for Prometheus when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2"]
  prometheus_private_connectivity_info_service_name:
    description:
      - VPC endpoint service name for Prometheus when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "com.amazonaws.vpce.eu-west-2.vpce-svc-0123456789abcdef0"
  traces_private_connectivity_info_availability_zone_ids:
    description:
      - Availability zone IDs for Traces when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["euw2-az1"]
  traces_private_connectivity_info_availability_zones:
    description:
      - Availability zones for Traces when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2a"]
  traces_private_connectivity_info_private_dns:
    description:
      - Private DNS name for Traces when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "prod-eu-west-4-traces.eu-west-2.vpce.grafana.net"
  traces_private_connectivity_info_regions:
    description: Regions for Traces when using AWS PrivateLink. Empty if the stack does not support PrivateLink. Only returned when O(state=present).
    returned: when state is present
    type: list
    elements: str
    sample: ["eu-west-2"]
  traces_private_connectivity_info_service_name:
    description:
      - VPC endpoint service name for Traces when using AWS PrivateLink.
      - Empty if the stack does not support PrivateLink.
      - Only returned when O(state=present).
    returned: when state is present
    type: str
    sample: "com.amazonaws.vpce.eu-west-2.vpce-svc-0123456789abcdef0"
"""

import time

from ansible.module_utils.basic import AnsibleModule, missing_required_lib

try:
    import requests

    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

__metaclass__ = type


STACKS_API_BASE = "https://grafana.com/api/v1/stacks"
GCOM_API_BASE = "https://grafana.com/api/instances"

# The connections of a new stack are not available straight away, so a 404 is retried.
# Up to 24 attempts, 5 seconds apart (about 2 minutes, as in the Terraform provider).
CONNECTIONS_MAX_ATTEMPTS = 24
CONNECTIONS_RETRY_INTERVAL = 5
CONNECTIONS_REQUEST_TIMEOUT = 30

# Tenant types returned by the API -> result key prefixes (as in the Terraform provider).
CONNECTIONS_TENANTS = {
    "prometheus": "prometheus",
    "logs": "logs",
    "traces": "traces",
    "profiles": "profiles",
    "graphite": "graphite",
    "agent-management": "fleet_management",
}


def get_headers(module):
    return {
        "Authorization": "Bearer " + module.params["cloud_api_key"],
        "User-Agent": "grafana-ansible-collection",
    }


def get_stack_details_from_gcom(module, stack_id):
    api_url = f"{GCOM_API_BASE}/{stack_id}"
    result = requests.get(api_url, headers=get_headers(module))
    if result.status_code == 200:
        return result.json()
    return None


def flatten_private_connectivity_info(prefix, info):
    """Flatten PrivateLink details into <prefix>_private_connectivity_info_* keys."""
    info = info or {}
    prefix = f"{prefix}_private_connectivity_info"
    return {
        f"{prefix}_private_dns": info.get("privateDNS", ""),
        f"{prefix}_service_name": info.get("serviceName", ""),
        f"{prefix}_regions": info.get("regions") or [],
        f"{prefix}_availability_zones": info.get("availabilityZones") or [],
        f"{prefix}_availability_zone_ids": info.get("availabilityZoneIds") or [],
    }


def flatten_connections(connections):
    """Flatten the connections API response, using the Terraform provider's attribute names."""
    otlp = connections.get("otlp") or {}
    pdc = connections.get("pdc") or {}
    services = connections.get("services") or {}

    result = {
        "otlp_url": otlp.get("url"),
        "oncall_api_url": services.get("oncallApiUrl"),
        "influx_url": services.get("influxUrl"),
    }
    result.update(
        flatten_private_connectivity_info("otlp", otlp.get("privateConnectivityInfo"))
    )
    result.update(flatten_private_connectivity_info("pdc_api", pdc.get("api")))
    result.update(flatten_private_connectivity_info("pdc_gateway", pdc.get("gateway")))

    # All tenants are always returned, empty if the stack does not have them.
    tenants = {}
    for tenant in connections.get("tenants") or []:
        name = CONNECTIONS_TENANTS.get(tenant.get("type"))
        # Like the Terraform provider, only the first tenant of each type is used.
        if name and name not in tenants:
            tenants[name] = tenant.get("privateConnectivityInfo")
    for name in CONNECTIONS_TENANTS.values():
        result.update(flatten_private_connectivity_info(name, tenants.get(name)))

    return result


def get_stack_connections(module, stack_id):
    api_url = f"{STACKS_API_BASE}/{stack_id}/connections"
    for attempt in range(1, CONNECTIONS_MAX_ATTEMPTS + 1):
        result = requests.get(
            api_url,
            headers=get_headers(module),
            timeout=CONNECTIONS_REQUEST_TIMEOUT,
        )
        if result.status_code == 200:
            return False, flatten_connections(result.json())
        if result.status_code != 404 or attempt == CONNECTIONS_MAX_ATTEMPTS:
            try:
                message = result.json()["message"]
            except (ValueError, KeyError, TypeError):
                message = result.text
            return True, {"status": result.status_code, "response": message}
        time.sleep(CONNECTIONS_RETRY_INTERVAL)


def present_cloud_stack(module):
    if not module.params["url"]:
        module.params["url"] = "https://" + module.params["stack_slug"] + ".grafana.net"

    body = {
        "name": module.params["name"],
        "slug": module.params["stack_slug"],
        "region": module.params["region"],
        "org": module.params["org_slug"],
        "url": module.params["url"],
        "deleteProtection": module.params["delete_protection"],
    }
    headers = get_headers(module)

    result = requests.post(STACKS_API_BASE, json=body, headers=headers)
    if result.status_code == 200:
        stack = result.json()
        full_details = get_stack_details_from_gcom(module, stack["id"])
        if full_details:
            return False, True, full_details
        return False, True, stack
    elif result.status_code in [409, 403] and result.json()["message"] in [
        "That URL has already been taken, please try an alternate URL",
        "Hosted instance limit reached",
    ]:
        stack_found = False
        if (
            result.json()["message"]
            == "That URL has already been taken, please try an alternate URL"
        ):
            api_url = STACKS_API_BASE + "?org=" + module.params["org_slug"]
            result = requests.get(api_url, headers=headers)
            list_response = result.json()
            if result.status_code != 200:
                return (
                    True,
                    False,
                    {
                        "status": result.status_code,
                        "response": list_response.get("message", str(list_response)),
                    },
                )
            stackInfo = {}
            for stack in list_response.get("items", []):
                if stack["slug"] == module.params["stack_slug"]:
                    stack_found = True
                    stackInfo = stack
            if stack_found:
                if body["deleteProtection"] == stackInfo["deleteProtection"]:
                    full_details = get_stack_details_from_gcom(module, stackInfo["id"])
                    if full_details:
                        return False, False, full_details
                    return False, False, stackInfo
                api_url = f'{STACKS_API_BASE}/{stackInfo["id"]}'
                result = requests.post(
                    api_url,
                    json={"deleteProtection": body["deleteProtection"]},
                    headers=headers,
                )
                if result.status_code != 200:
                    return (
                        True,
                        False,
                        {
                            "status": result.status_code,
                            "response": result.json()["message"],
                        },
                    )
                full_details = get_stack_details_from_gcom(module, stackInfo["id"])
                if full_details:
                    return False, True, full_details
                return False, True, result.json()
            else:
                return True, False, "Stack is not found under your org"
        elif result.json()["message"] == "Hosted instance limit reached":
            return (
                True,
                False,
                "You have reached Maximum number of Cloud Stacks in your Org.",
            )
    else:
        return (
            True,
            False,
            {"status": result.status_code, "response": result.json()["message"]},
        )


def absent_cloud_stack(module):
    api_url = f"{STACKS_API_BASE}/{module.params['stack_slug']}"

    gcom_details = get_stack_details_from_gcom(module, module.params["stack_slug"])

    result = requests.delete(api_url, headers=get_headers(module))

    if result.status_code == 200:
        if gcom_details:
            return False, True, gcom_details
        return False, True, result.json()
    else:
        return (
            True,
            False,
            {"status": result.status_code, "response": result.json()["message"]},
        )


def main():

    module_args = dict(
        name=dict(type="str", required=True),
        stack_slug=dict(type="str", required=True),
        cloud_api_key=dict(type="str", required=True, no_log=True),
        region=dict(type="str", required=False, default="us"),
        url=dict(type="str", required=False),
        org_slug=dict(type="str", required=True),
        state=dict(
            type="str", required=False, default="present", choices=["present", "absent"]
        ),
        delete_protection=dict(type="bool", required=False, default=True),
    )

    choice_map = {
        "present": present_cloud_stack,
        "absent": absent_cloud_stack,
    }

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_REQUESTS:
        module.fail_json(msg=missing_required_lib("requests"))

    is_error, has_changed, result = choice_map.get(module.params["state"])(module)

    if not is_error:
        extra = {}
        if module.params["state"] == "present":
            is_error, connections = get_stack_connections(module, result["id"])
            if is_error:
                module.fail_json(msg=connections)
            extra.update(connections)

        module.exit_json(
            changed=has_changed,
            alertmanager_name=result["amInstanceName"],
            url=result["url"],
            id=result["id"],
            cluster_slug=result["clusterName"],
            orgID=result["orgId"],
            loki_url=result["hlInstanceUrl"],
            prometheus_url=result["hmInstancePromUrl"],
            tempo_url=result["htInstanceUrl"],
            alertmanager_url=result["amInstanceUrl"],
            delete_protection=result["deleteProtection"],
            **extra,
        )
    else:
        module.fail_json(msg=result)


if __name__ == "__main__":
    main()
