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
| `grafana_yum_repo` | https://rpm.grafana.com | Yum repository URL |
| `grafana_yum_key` | https://rpm.grafana.com/gpg.key | Yum repository gpg key |
| `grafana_rhsm_subscription` | | rhsm subscription name (redhat subscription-manager) |
| `grafana_rhsm_repo` | | rhsm repository name (redhat subscription-manager) |
| `grafana_apt_release_channel` | stable | Apt release chanel (stable or beta) |
| `grafana_apt_arch` | {{ 'arm64' if ansible_facts['architecture'] == 'aarch64' else 'amd64' }} | Apt architecture | 
| `grafana_apt_repo` | deb [arch={{ grafana_apt_arch }} signed-by=/usr/share/keyrings/grafana.asc] https://apt.grafana.com/ {{ grafana_apt_release_channel }} main | Apt repository string |
| `grafana_apt_key` | https://apt.grafana.com/gpg.key | Apt repository gpg key |
| `grafana_ini.instance_name` | {{ ansible_facts['fqdn'] \| default(ansible_host) \| default(inventory_hostname) }} | Grafana instance name |
| `grafana_ini.paths.logs` | /var/log/grafana | Path to logs directory |
| `grafana_ini.paths.data` | /var/lib/grafana | Path to database directory |
| `grafana_ini.server.http_addr` | 0.0.0.0 | Address on which Grafana listens |
| `grafana_ini.server.http_port` | 3000 | port on which Grafana listens |
| `grafana_cap_net_bind_service` | false | Enables the use of ports below 1024 without root privileges by leveraging the 'capabilities' of the linux kernel. read: http://man7.org/linux/man-pages/man7/capabilities.7.html |
| `grafana_ini.server.root_url` | "http://{{ grafana_ini.server.http_addr }}:{{ grafana_ini.server.http_port }}" | Full URL used to access Grafana from a web browser |
| `grafana_api_url` | "{{ grafana_url }}" | URL used for API calls in provisioning if different from public URL. See [this issue](https://github.com/cloudalchemy/ansible-grafana/issues/70). |
| `grafana_ini.server.domain` | "{{ ansible_facts['fqdn'] \| default(ansible_host) \| default('localhost') }}" | setting is only used in as a part of the `root_url` option. Useful when using GitHub or Google OAuth |
| `grafana_ini.server` | { protocol: http, enforce_domain: false, socket: "", cert_key: "", cert_file: "", enable_gzip: false, static_root_path: public, router_logging: false } | [server](http://docs.grafana.org/installation/configuration/#server) configuration section |
| `grafana_ini.security` | { admin_user: admin, admin_password: "" } | [security](http://docs.grafana.org/installation/configuration/#security) configuration section |
| `grafana_ini.database` | { type: sqlite3 } | [database](http://docs.grafana.org/installation/configuration/#database) configuration section |
| `grafana_ini.users` | { allow_sign_up: false, auto_assign_org_role: Viewer, default_theme: dark } | [users](http://docs.grafana.org/installation/configuration/#users) configuration section |
| `grafana_ini.auth` | {} | [authorization](http://docs.grafana.org/installation/configuration/#auth) configuration section |
| `grafana_ldap` | {} | [ldap](http://docs.grafana.org/installation/ldap/) configuration section. group_mappings are expanded, see defaults for example |
| `grafana_dashboards` | [] | List of dashboards which should be imported |
| `grafana_dashboards_dir` | "dashboards" | Path to a local directory containing dashboards files in `json` format |
| `grafana_datasources` | [] | List of datasources which should be configured |
| `grafana_environment` | {} | Optional Environment param for Grafana installation, useful ie for setting http_proxy |
| `grafana_plugins` | [] |  List of Grafana plugins which should be installed |
| `grafana_offline_package_install` | false | Install Grafana from a local package instead of a repository |
| `grafana_offline_package_path` | | Path to the Grafana `.deb`/`.rpm` package on the Ansible control node |
| `grafana_offline_package_download` | false | Download the Grafana package on the Ansible control node |
| `grafana_offline_package_url` | | URL used to download the Grafana package (derived from `grafana_version` when empty) |
| `grafana_offline_package_checksum` | | Optional checksum for the downloaded package, e.g. `sha256:...` |
| `grafana_offline_package_gpg_check` | true | Verify the GPG signature of the local package |
| `grafana_offline_package_allow_downgrade` | false | Allow installing an older Grafana package version |
| `grafana_offline_plugins_install` | false | Install Grafana plugins from local ZIP archives |
| `grafana_offline_plugins_dir` | | Directory on the Ansible control node containing `<plugin-name>.zip` archives |
| `grafana_offline_plugins_download` | false | Download plugin archives on the Ansible control node |
| `grafana_offline_plugins_url` | https://grafana.com/api/plugins | Base URL used to download plugin archives |
| `grafana_offline_plugins_versions` | {} | Optional plugin version pins, e.g. `{grafana-clock-panel: "3.2.5"}` |
| `grafana_offline_plugins_checksums` | {} | Optional plugin archive checksums, keyed by plugin id |
| `grafana_offline_plugins_force` | false | Reinstall offline plugins even if their directory already exists |
| `grafana_offline_cache_dir` | `~/.cache/grafana-offline` | Cache directory on the control node for downloaded artifacts |
| `grafana_offline_staging_dir` | /var/tmp/grafana-offline | Staging directory on the managed host used while installing |
| `grafana_offline_download_force` | false | Re-download artifacts even when they already exist (artifacts tracking `latest` are always refreshed) |
| `grafana_offline_http_proxy` | `$http_proxy` | HTTP proxy used for downloads on the control node |
| `grafana_offline_https_proxy` | `$https_proxy` | HTTPS proxy used for downloads on the control node |
| `grafana_offline_no_proxy` | `$no_proxy` | Hosts that bypass the proxy used for downloads |
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

## Offline installation

The role supports air-gapped installations. Installing the Grafana package and
installing plugins offline are controlled independently:

- `grafana_offline_package_install: true` installs Grafana from a local `.deb`
  package on Debian/Ubuntu or a local `.rpm` package on RHEL, Fedora and
  openSUSE. Repository setup and dependency installation are skipped, so any OS
  dependencies must already be installed on the managed host.
  `grafana_manage_repo` is ignored while package installation is offline.
- `grafana_offline_plugins_install: true` installs plugins from local ZIP
  archives instead of calling `grafana-cli` on the managed host.

Artifacts can be prepared manually on the Ansible control node or downloaded by
the role on the control node. Downloads happen on the controller, so the managed
host never needs internet access. When `http_proxy`, `https_proxy` or `no_proxy`
are set in the controller environment they are used automatically; the
`grafana_offline_http_proxy`, `grafana_offline_https_proxy` and
`grafana_offline_no_proxy` variables can be used to set them explicitly.

The local package is staged in `grafana_offline_staging_dir` with root-only
permissions and the directory is removed after the installation attempt. On
RPM-based systems, signature verification follows
`grafana_offline_package_gpg_check`; disable it only when the artifact is trusted
out-of-band and the host does not already trust the Grafana key.
`grafana_offline_package_allow_downgrade` enables rollbacks on apt, dnf/yum and
zypper.

### Using local artifacts

Requirements on the control node:

- A Grafana package such as `grafana_11.1.0_amd64.deb` or
  `grafana-11.1.0-1.x86_64.rpm` from <https://grafana.com/grafana/download>.
- For each plugin, a ZIP archive named after the plugin, e.g.
  `grafana-clock-panel.zip`, obtained from
  `https://grafana.com/api/plugins/<plugin-id>/versions/<version>/download`.
  Plugin archives are extracted with `ansible.builtin.unarchive`, so the
  `unzip`/`zipinfo` utilities must already be installed on the managed host.

```yaml
- hosts: all
  roles:
    - role: grafana.grafana.grafana
      vars:
        grafana_offline_package_install: true
        grafana_offline_package_path: /opt/grafana-offline/grafana_11.1.0_amd64.deb
        grafana_offline_plugins_install: true
        grafana_offline_plugins_dir: /opt/grafana-offline/plugins
        grafana_plugins:
          - grafana-clock-panel
          - grafana-piechart-panel
        grafana_ini:
          security:
            admin_user: admin
            admin_password: enter_your_secure_password
```

### Downloading artifacts on the control node

Set the matching `*_download` flag to have the role fetch the artifacts on the
Ansible control node. When no path is supplied, artifacts are cached under
`grafana_offline_cache_dir` (`~/.cache/grafana-offline` by default).

```yaml
- hosts: all
  roles:
    - role: grafana.grafana.grafana
      vars:
        grafana_offline_package_install: true
        grafana_offline_package_download: true
        grafana_offline_plugins_install: true
        grafana_offline_plugins_download: true
        grafana_plugins:
          - grafana-clock-panel
        grafana_offline_plugins_versions:
          grafana-clock-panel: "3.2.5"
        grafana_ini:
          security:
            admin_user: admin
            admin_password: enter_your_secure_password
```

Package URLs are derived from `grafana_version` and the target package manager.
Set `grafana_offline_package_url` to use a custom mirror or a package that
cannot be derived automatically (for example a non-x86_64 "latest" RPM).

Downloads that track `latest` are refreshed on every run. Pinned package
versions and pinned plugin versions use version-specific cache filenames; set
`grafana_offline_download_force: true` to refresh pinned artifacts explicitly.
Use `grafana_offline_package_checksum` and `grafana_offline_plugins_checksums`
to verify downloaded artifacts. `grafana_offline_plugins_versions` only affects
downloaded archives; local archives must use the `<plugin-name>.zip` layout.

Offline plugin installation is idempotent: an existing plugin directory is left
untouched, even when its archive changes. Set
`grafana_offline_plugins_force: true` to remove and reinstall plugin
directories. Unsigned or custom plugin builds also require
`grafana_ini.plugins.allow_loading_unsigned_plugins` in the Grafana
configuration.

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
        grafana_ini:
          security:
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
