<p><img src="https://grafana.com/blog/assets/img/blog/timeshift/grafana_release_icon.png" alt="grafana logo" title="grafana" align="right" height="60" /></p>

# Ansible Role: grafana.grafana.grafana

[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)

Provision and manage [Grafana](https://github.com/grafana/grafana) - platform for analytics and monitoring

## Requirements

- Ansible >= 2.9 (It might work on previous versions, but we cannot guarantee it)
- libselinux-python on deployer host (only when deployer machine has SELinux)
- Grafana >= 5.1 (for older Grafana versions use this role in version 0.10.1 or earlier)
- jmespath on deployer machine. If you are using Ansible from a Python virtualenv, install *jmespath* to the same virtualenv via pip.

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `grafana_use_provisioning` | true | Use Grafana provisioning capability when possible (**grafana_version=latest will assume >= 5.0**). |
| `grafana_provisioning_synced` | false | Ensure no previously provisioned dashboards are kept if not referenced anymore. |
| `grafana_version` | latest | Grafana package version |
| `grafana_manage_repo` | true | Manage package repository (or don't) |
| `grafana_yum_repo` | https://packages.grafana.com/oss/rpm | Yum repository URL |
| `grafana_yum_key` | https://packages.grafana.com/gpg.key | Yum repository gpg key |
| `grafana_rhsm_subscription` | | rhsm subscription name (redhat subscription-manager) |
| `grafana_rhsm_repo` | | rhsm repository name (redhat subscription-manager) |
| `grafana_apt_release_channel` | stable | Apt release chanel (stable or beta) |
| `grafana_apt_arch` | {{ 'arm64' if ansible_architecture == 'aarch64' else 'amd64' }} | Apt architecture | 
| `grafana_apt_repo` | deb [arch={{ grafana_apt_arch }} signed-by=/usr/share/keyrings/grafana.key] https://apt.grafana.com/ {{ grafana_apt_release_channel }} main | Apt repository string |
| `grafana_apt_key` | https://apt.grafana.com/gpg.key | Apt repository gpg key |
| `grafana_instance` | {{ ansible_fqdn \| default(ansible_host) \| default(inventory_hostname) }} | Grafana instance name |
| `grafana_logs_dir` | /var/log/grafana | Path to logs directory |
| `grafana_data_dir` | /var/lib/grafana | Path to database directory |
| `grafana_address` | 0.0.0.0 | Address on which Grafana listens |
| `grafana_port` | 3000 | port on which Grafana listens |
| `grafana_cap_net_bind_service` | false | Enables the use of ports below 1024 without root privileges by leveraging the 'capabilities' of the linux kernel. read: http://man7.org/linux/man-pages/man7/capabilities.7.html |
| `grafana_url` | "http://{{ grafana_address }}:{{ grafana_port }}" | Full URL used to access Grafana from a web browser |
| `grafana_api_url` | "{{ grafana_url }}" | URL used for API calls in provisioning if different from public URL. See [this issue](https://github.com/cloudalchemy/ansible-grafana/issues/70). |
| `grafana_domain` | "{{ ansible_fqdn \| default(ansible_host) \| default('localhost') }}" | setting is only used in as a part of the `root_url` option. Useful when using GitHub or Google OAuth |
| `grafana_server` | { protocol: http, enforce_domain: false, socket: "", cert_key: "", cert_file: "", enable_gzip: false, static_root_path: public, router_logging: false } | [server](http://docs.grafana.org/installation/configuration/#server) configuration section |
| `grafana_security` | { admin_user: admin, admin_password: "" } | [security](http://docs.grafana.org/installation/configuration/#security) configuration section |
| `grafana_database` | { type: sqlite3 } | [database](http://docs.grafana.org/installation/configuration/#database) configuration section |
| `grafana_welcome_email_on_sign_up` | false | Send welcome email after signing up |
| `grafana_users` | { allow_sign_up: false, auto_assign_org_role: Viewer, default_theme: dark } | [users](http://docs.grafana.org/installation/configuration/#users) configuration section |
| `grafana_auth` | {} | [authorization](http://docs.grafana.org/installation/configuration/#auth) configuration section |
| `grafana_ldap` | {} | [ldap](http://docs.grafana.org/installation/ldap/) configuration section. group_mappings are expanded, see defaults for example |
| `grafana_session` | {} | [session](http://docs.grafana.org/installation/configuration/#session) management configuration section |
| `grafana_analytics` | {} | Google [analytics](http://docs.grafana.org/installation/configuration/#analytics) configuration section |
| `grafana_smtp` | {} | [smtp](http://docs.grafana.org/installation/configuration/#smtp) configuration section |
| `grafana_alerting` | { execute_alerts: true } | [alerting](http://docs.grafana.org/installation/configuration/#alerting) configuration section, require Grafana v10 and below |
| `grafana_unified_alerting` | { enabled: true } | [unified_alerting](https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/#unified_alerting) configuration section, require Grafana v11+ |
| `grafana_log` | {} | [log](http://docs.grafana.org/installation/configuration/#log) configuration section |
| `grafana_metrics` | {} | [metrics](http://docs.grafana.org/installation/configuration/#metrics) configuration section |
| `grafana_tracing` | {} | [tracing](http://docs.grafana.org/installation/configuration/#tracing) configuration section |
| `grafana_snapshots` | {} | [snapshots](http://docs.grafana.org/installation/configuration/#snapshots) configuration section |
| `grafana_image_storage` | {} | [image storage](http://docs.grafana.org/installation/configuration/#external-image-storage) configuration section |
| `grafana_date_formats` | {} | [date formats](http://docs.grafana.org/installation/configuration/#date_formats) configuration section |
| `grafana_feature_toggles` | {} | [feature toggles](http://docs.grafana.org/installation/configuration/#feature_toggles) configuration section |
| `grafana_dashboards` | [] | List of dashboards which should be imported |
| `grafana_dashboards_dir` | "dashboards" | Path to a local directory containing dashboards files in `json` format |
| `grafana_datasources` | [] | List of datasources which should be configured |
| `grafana_environment` | {} | Optional Environment param for Grafana installation, useful ie for setting http_proxy |
| `grafana_plugins` | [] |  List of Grafana plugins which should be installed |
| `grafana_alert_notifications` | [] | List of alert notification channels to be created, updated, or deleted |

Data source example:

```yaml
grafana_datasources:
  - name: prometheus
    type: prometheus
    access: proxy
    url: 'http://{{ prometheus_web_listen_address }}'
    basicAuth: false
```

Dashboard example:

```yaml
grafana_dashboards:
  - dashboard_id: 111
    revision_id: 1
    datasource: prometheus
```

Alert notification channel example:

**NOTE**: setting the variable `grafana_alert_notifications` will only come into
effect when `grafana_use_provisioning` is `true`. That means the new
provisioning system using config files, which is available starting from Grafana
v5.0, needs to be in use.

```yaml
grafana_alert_notifications:
  notifiers:
    - name: Channel 1
      type: email
      uid: channel1
      is_default: false
      send_reminder: false
      settings:
        addresses: "example@example.com"
        autoResolve: true
  delete_notifiers:
    - name: Channel 2
      uid: channel2
```

**NOTE 2**: setting the `http_addr`,`http_port`,`domain` and `root_url` parameters under the `grafana_server` variable has no effect, the `grafana_address`, `grafana_port`, `grafana_domain` and `grafana_url` values are used instead ( from [defaults/main.yml](defaults/main.yml) or as set variables).
An example snippet:
```yaml
grafana_domain: "{{ inventory_hostname }}"
grafana_url: "https://{{ inventory_hostname }}:3000"
grafana_address: 0.0.0.0
grafana_port: 3000

grafana_server:
  enforce_domain: false
```

## Supported CPU Architectures

Historically packages were taken from different channels according to CPU architecture. Specifically, armv6/armv7 and aarch64/arm64 packages were via [unofficial packages distributed by fg2it](https://github.com/fg2it/grafana-on-raspberry). Now that Grafana publishes official ARM builds, all packages are taken from the official [Debian/Ubuntu](http://docs.grafana.org/installation/debian/#installing-on-debian-ubuntu) or [RPM](http://docs.grafana.org/installation/rpm/) packages.

## Example

### Playbook

Fill in the admin password field with your choice, the Grafana web page won't ask to change it at the first login.

```yaml
- hosts: all
  roles:
    - role: grafana.grafana.grafana
      vars:
        grafana_security:
          admin_user: admin
          admin_password: enter_your_secure_password
```


## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/ansible-community/molecule). You will have to install Docker on your system.

For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.

## Credits
This role was migrated from [cloudalchemy.grafana](https://github.com/cloudalchemy/ansible-grafana).
