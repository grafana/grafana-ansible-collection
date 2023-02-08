=============================
Grafana.Grafana Release Notes
=============================

.. contents:: Topics


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
- Fixed markup for arg option in Documenation
- Updated Documenation with `notes` to specify if the check_mode feature is supported by modules
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
