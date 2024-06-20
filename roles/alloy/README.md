# Ansible Role for Alloy

This Ansible role to install and configure [Alloy](https://grafana.com/docs/alloy/latest/), which can be used to collect traces, metrics, and logs.

## Requirements

Please ensure that `curl` is intalled on Ansible controller.

## Role Variables

Available variables with their default values are listed below (`defaults/main.yml`):

## Role Variables

| Variable Name         | Description                                                          | Default Value                                                       |
|-----------------------|----------------------------------------------------------------------|---------------------------------------------------------------------|
| `version`             | The version of Grafana Alloy to be installed.                        | "1.0.0"                                                             |
| `arch_mapping`        | A mapping of common architecture names to Grafana Alloy binaries.    | `{'x86_64': 'amd64', 'aarch64': 'arm64', 'armv7l': 'armhf', 'i386': 'i386', 'ppc64le': 'ppc64le'}` |
| `arch`                | The architecture of the current machine.                             | Based on `ansible_architecture` lookup, defaults to 'amd64'.       |
| `binary_url`          | URL to Grafana Alloy binary for the specific version and architecture. | Constructed URL based on `version` and `arch` variables.          |
| `service_name`        | The name to be used for the Grafana Alloy service.                   | "alloy"                                                            |
| `installation_dir`    | Directory where Grafana Alloy binary is to be installed. Must be present.   | "/usr/local/bin"                                                      |
| `environment_file`    | Name of the environment file for the Grafana Alloy service.          | "service.env"                                                      |
| `config_dir`          | Directory for Grafana Alloy configuration.                           | "/etc/alloy"                                                      |
| `config_file`         | Configuration file name for Grafana Alloy.                           | "config.alloy"                                                     |
| `service_user`        | User under which the Grafana Alloy service will run.                 | "alloy"                                                            |
| `service_group`       | Group under which the Grafana Alloy service will run.                | "alloy"                                                            |
| `working_dir`         | Working directory for the Grafana Alloy service.                     | "/var/lib/alloy"                                                      |
| `env_file_vars`       | Additional environment variables to be set in the service environment file. | {} (Empty dictionary)                                          |
| `alloy_flags_extra`   | Extra flags to pass to the Alloy service.                            | {} (Empty dictionary)                                              |
| `start_after_service` | Specify an optional dependency service Alloy should start after.     | '' (Empty string)                                                  |
| `config`              | Configuration template for Grafana Alloy.                            | Configuration script with Prometheus scrape and remote_write setup |
| `alloy_user_groups`.  | Configurable user groups that the Grafana Alloy can be put in so that it can access logs.  | `[]` |



## Example Playbook

Including an example of how to use your role:
```yaml
- name: Install alloy
  hosts: all
  become: true

  tasks:
    - name: Install alloy
      ansible.builtin.include_role:
        name: grafana.grafana.alloy
      vars:
        config: |
          prometheus.scrape "default" {
            targets = [{"__address__" = "localhost:12345"}]
            forward_to = [prometheus.remote_write.prom.receiver]
          }
          prometheus.remote_write "prom" {
            endpoint {
                url = "https://prometheus-prod-13-prod-us-east-0.grafana.net/api/prom/push"

                basic_auth {
                username = "149xxx"
                password = "glc_xxx"
              }
            }
          }
```

## License

See [LICENSE](https://github.com/grafana/grafana-ansible-collection/blob/main/LICENSE)

## Author Information

-   [Ishan Jain](https://github.com/ishanjainn)
