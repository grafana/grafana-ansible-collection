# Ansible Role for Agent

This Ansible role to install and configure the Agent, which can be used to collect traces, metrics, and logs.

## Requirements

Please ensure that `curl` is intalled on Ansible controller.

## Role Variables

Available variables with their default values are listed below (`defaults/main.yml`):

## Role Variables

| Variable Name        | Description                                                          | Default Value                                                       |
|----------------------|----------------------------------------------------------------------|---------------------------------------------------------------------|
| `version`            | The version of the Grafana Agent to be installed.                    | "0.40.3"                                                            |
| `arch_mapping`       | A mapping of common architecture names to Grafana Agent binaries.    | `{'x86_64': 'amd64', 'aarch64': 'arm64', 'armv7l': 'armhf', 'i386': 'i386', 'ppc64le': 'ppc64le'}` |
| `arch`               | The architecture of the current machine.                             | Based on `ansible_architecture` lookup, defaults to 'amd64'.       |
| `binary_url`         | URL to the Grafana Agent binary for the specific version and arch.   | Constructed URL based on `version` and `arch` variables.            |
| `service_name`       | The name to be used for the Grafana Agent service.                   | "alloy"                                                        |
| `installation_dir`   | Directory where the Grafana Agent is to be installed.                | "/etc/alloy"                                                   |
| `environment_file`   | Name of the environment file for the Grafana Agent service.          | "service.env"                                                       |
| `config_dir`         | Directory for the Grafana Agent configuration.                       | "/etc/alloy"                                                   |
| `config_file`        | Configuration file name for the Grafana Agent.                       | "config.river"                                                      |
| `service_user`       | User under which the Grafana Agent service will run.                 | "alloy"                                                        |
| `service_group`      | Group under which the Grafana Agent service will run.                | "alloy"                                                        |
| `working_dir`        | Working directory for the Grafana Agent service.                     | "/etc/alloy"                                                   |
| `env_file_vars`      | Additional environment variables to be set in the service env file.  | {} (Empty dictionary)                                               |
| `config`             | Configuration template for the Grafana Agent.                        | Configuration script with prometheus scrape and remote_write setup |


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
                username = "1493467"
                password = "glc_eyJvIjoiNjUyOTkyIiwibiI6InN0YWNrLTg5MDA0My1obS13cml0ZS1hc2FzIiwiayI6IjIwME9NeThmWlFpMGlmQzBGMTlJNDdqSiIsIm0iOnsiciI6InByb2QtdXMtZWFzdC0wIn19"
              }
            }
          }
```

## License

See [LICENSE](https://github.com/grafana/grafana-ansible-collection/blob/main/LICENSE)

## Author Information

-   [Ishan Jain](https://github.com/ishanjainn)
