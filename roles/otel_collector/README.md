# Ansible Role for OpenTelemetry Collector

This Ansible role installs and configures the OpenTelemetry Collector, which can be used to collect traces, metrics, and logs.

## Requirements

No specific requirements.

## Role Variables

Available variables with their default values are listed below (`defaults/main.yml`):

```yaml
otel_collector_version: "latest"
otel_collector_service_name: "otel-collector"
otel_collector_binary_url: "https://github.com/open-telemetry/opentelemetry-collector-releases/download/{{ otel_collector_version }}/otelcol_{{ otel_collector_version }}_linux_amd64.tar.gz"
otel_collector_installation_dir: "/opt/otel-collector"
otel_collector_config_dir: "/etc/otel-collector"
otel_collector_config_file: "config.yaml"
otel_collector_service_user: "otel"
otel_collector_service_group: "otel"
otel_collector_receivers: ""
otel_collector_exporters: ""
otel_collector_processors: ""
otel_collector_extensions: ""
otel_collector_service: ""
```

Users of the role can override these variables as needed.

## Dependencies

None.

## Example Playbook

Include this role in your playbook with default settings:

```yaml
- hosts: all
  roles:
    - opentelemetry_collector
```

To customize, provide additional variables:

```yaml
- hosts: all
  roles:
    - role: opentelemetry_collector
      vars:
        otel_collector_version: "0.33.0"
```

## Author Information

This role was created in Ishan Jain (@ishanjainn) (ishan.jain0099@gmailcom)
