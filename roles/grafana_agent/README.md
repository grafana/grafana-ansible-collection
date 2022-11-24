Role Name
=========

Ansible Role to deploy Grafana Agent on Linux hosts. Using this Role, Grafana Agent can be deployed on Ubunutu, Debian, CentOS and Fedora linux distributions


Requirements
------------

To use this role, You need a YAML file having the Grafana Agent configuration

Role Variables
--------------

A description of the variables for this role.

| Variable                | Required | Default              | Choices                                                                                                            | Comments                                    |
|-------------------------|----------|----------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| install_unzip           | no       | true                 | true, false                                                                                                        | This will install unzip on the Linux host   |
| update_package_cache    | no       | yes                  | yes, no                                                                                                            | Force dnf/apt to check if cache is out of date and redownload if needed.|
| agent_version           | no       | 0.29.0               | 0.29.0, 0.28.1, 0.28.0, 0.27.1, 0.27.0                                                                             | Version of the Grafana agent to install|
| linux_architecture      | no       | linux-amd64          | linux-amd64, linux-arm64, linux-armv6, linux-armv7, linux-ppc64le                                                  | Type of linux architecture of the remote host|
| agent_binary_location   | no       | /usr/local/bin       |                                                                                                                    | Path where the agent binary will be copied to on the remote host|
| agent_config_location   | no       | /etc/grafana         |                                                                                                                    | Path where the agent configuration will be copied to on the remote host|
| agent_config_local_path | yes      | agent-config.yml     |                                                                                                                    | Path to the agent configuration file on local|
| systemd_service_state   | no       | restarted            | reloaded, restarted, started, stopped                                                                              | Operation performed on the systemd service|
| systemd_config          | no       |                      |                                                                                                                    | Configuration for grafana-agent systemd service|

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- name: Install Grafana Agent  
  hosts: all

  tasks:
    - name: Install Grafana Agent
      ansible.builtin.include_role:
        name: grafana.grafana.grafana_agent:
      vars:
        agent_config_local_path: ../agent-config.yml
```
License
-------

See [LICENSE](https://github.com/grafana/grafana-ansible-collection/blob/main/LICENSE)

Author Information
------------------
- [Grafana Labs](https://github.com/grafana)
- [Ishan Jain](https://github.com/ishanjainn)

