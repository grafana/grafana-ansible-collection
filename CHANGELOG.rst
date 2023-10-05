=============================
Grafana.Grafana Release Notes
=============================

.. contents:: Topics


v2.2.3
======

Release Summary
---------------

Remove dependency on local-fs.target from Grafana Agent role

Minor Changes
-------------

- Remove dependency on local-fs.target from Grafana Agent role

v2.2.2
======

Release Summary
---------------

Grafana Role bug fixes and security updates

Minor Changes
-------------

- Bump cryptography from 41.0.3 to 41.0.4
- Create missing notification directory in Grafana Role
- Remove check_mode from create local directory task in Grafana Role

v2.2.1
======

Release Summary
---------------

Allow alert resource provisioning in Grafana Role

Minor Changes
-------------

- Allow alert resource provisioning in Grafana Role

v2.2.0
======

Release Summary
---------------

Grafana Agent Role Updates

Minor Changes
-------------

- Use 'ansible_system' env variable to detect os typ in Grafana Agent Role
- hange grafana Agent Wal and Positions Directory in Grafana Agent Role

v2.1.9
======

Release Summary
---------------

Security Updates and Grafana Agent Version failure fixes

Minor Changes
-------------

- Add check for Curl and failure step if Agent Version is not retrieved
- Bump cryptography from 39.0.2 to 41.0.3
- Bump semver from 5.7.1 to 5.7.2
- Bump word-wrap from 1.2.3 to 1.2.5
- Create local dashboard directory in check mode
- Update CI Testing
- Update Cloud Stack Module failures

v2.1.8
======

Release Summary
---------------

Fix grafana dashboard import in Grafana Role

Minor Changes
-------------

- Fix grafana dashboard import in Grafana Role

v2.1.7
======

Release Summary
---------------

YAML Fixes

Minor Changes
-------------

- YAML Fixes

v2.1.6
======

Release Summary
---------------

Grafana and Grafana Agent role updates

Minor Changes
-------------

- Add overrides.conf with CAP_NET_BIND_SERVICE for grafana-server unit
- Fix Grafana Dashboard Import for Grafana Role
- Make grafana_agent Idempotent
- Provisioning errors in YAML
- Use new standard to configure Grafana APT source for Grafana Role

v2.1.5
======

Release Summary
---------------

Update Grafana Agent Download varibale and ZIP file

Minor Changes
-------------

- Add Grafana Agent Version and CPU Arch to Downloaded ZIP in Grafana Agent Role
- Move _grafana_agent_base_download_url from /vars to /defaults in Grafana Agent Role

v2.1.4
======

Release Summary
---------------

Update Datasource Tests and minor fixes

Minor Changes
-------------

- Datasource test updates and minor fixes

v2.1.3
======

Release Summary
---------------

Update modules to fix failing Sanity Tests

Minor Changes
-------------

- indentation and Lint fixes to modules

v2.1.2
======

Release Summary
---------------

Idempotency Updates and minor api_url fixes

Minor Changes
-------------

- Fix Deleting datasources
- Fix alert_notification_policy failing on fresh instance
- Making Deleting folders idempotent
- Remove trailing slash automatically from grafana_url

v2.1.1
======

Release Summary
---------------

Update Download tasks in Grafana Agent Role

Minor Changes
-------------

- Update Download tasks in Grafana Agent Role

v2.1.0
======

Release Summary
---------------

Add Grafana Server role and plugins support on-prem Grafana

Major Changes
-------------

- Addition of Grafana Server role by @gardar
- Configurable agent user groups by @NormanJS
- Grafana Plugins support on-prem Grafana installation by @ishanjainn
- Updated Service for flow mode by @bentonam

Minor Changes
-------------

- Ability to configure date format in grafana server role by @RomainMou
- Avoid using shell for fetching latest version in Grafana Agent Role by @gardar
- Fix for invalid yaml with datasources list enclosed in quotes by @elkozmon
- Remove agent installation custom check by @VLZZZ
- Remove explicit user creation check by @v-zhuravlev

v2.0.0
======

Release Summary
---------------

Updated Grafana Agent Role

Major Changes
-------------

- Added Lint support
- Configs for server, metrics, logs, traces, and integrations
- Installation of the latest version
- Local installations when internet connection is not allowed
- Only download binary to controller once instead of hosts
- Skip install if the agent is already installed and the version is the same as the requested version
- Support for Grafana Agent Flow
- Validation of variables

v1.1.1
======

Release Summary
---------------

Updated return description and value for grafana.grafana.folder module

Minor Changes
-------------

- Updated the return message in grafana.grafana.folder module

v1.1.0
======

Release Summary
---------------

Added Role to deploy Grafana Agent on linux hosts

Major Changes
-------------

- Added Role for Grafana Agent

v1.0.5
======

Release Summary
---------------

Add Note to modules which don't support Idempotency

Minor Changes
-------------

- Added Note to datasource and dashboard module about not supporting Idempotency

v1.0.4
======

Release Summary
---------------

Bug fixes and idempotency fixes for modules

Major Changes
-------------

- All modules except dashboard and datasource modules now support idempotency

Minor Changes
-------------

- All modules use `missing_required_lib`` to compose the message for module.fail_json() when required library is missing from host

Bugfixes
--------

- Fixed cases where cloud_stack and alert_contact_point modules do not return a tuple when nothing in loop matches

v1.0.3
======

Minor Changes
-------------

- Add a fail method to modules source code if `requests` library is not present
- Fixed markup for arg option in Documentation
- Updated Documentation with `notes` to specify if the check_mode feature is supported by modules
- removed `supports_check_mode=True` from source code of modules

v1.0.2
======

Release Summary
---------------

Documentation updates with updated description for modules

v1.0.1
======

Release Summary
---------------

Documentation updates with updated examples

v1.0.0
======

Release Summary
---------------

CI and testing improvements

v0.0.7
======

Release Summary
---------------

Documentation update for return values in `grafana.grafana.dashboard`

v0.0.6
======

Minor Changes
-------------

- Idempotency updates to cloud_api_key and datasource modules

v0.0.5
======

Release Summary
---------------

Documentation update and code cleanup

v0.0.4
======

Bugfixes
--------

- Fix an issue with `cloud_stack` idempotency

v0.0.3
======

Release Summary
---------------

Documentation update and code cleanup

v0.0.2
======

Release Summary
---------------

Updated input parameters description for all modules

v0.0.1
======

Release Summary
---------------

It's a release! First version to publish to Ansible Galaxy
