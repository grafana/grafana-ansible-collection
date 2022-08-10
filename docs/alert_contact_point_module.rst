.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na
.. role:: ansible-option-type
.. role:: ansible-option-elements
.. role:: ansible-option-required
.. role:: ansible-option-versionadded
.. role:: ansible-option-aliases
.. role:: ansible-option-choices
.. role:: ansible-option-choices-entry
.. role:: ansible-option-default
.. role:: ansible-option-default-bold
.. role:: ansible-option-configuration
.. role:: ansible-option-returned-bold
.. role:: ansible-option-sample-bold

.. Anchors

.. _ansible_collections.grafana.grafana.alert_contact_point_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

grafana.grafana.alert_contact_point module -- Manage Alerting Contact points in Grafana
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `grafana.grafana collection <https://galaxy.ansible.com/grafana/grafana>`_ (version 0.0.5).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install grafana.grafana`.

    To use it in a playbook, specify: :code:`grafana.grafana.alert_contact_point`.

.. version_added

.. versionadded:: 0.0.1 of grafana.grafana

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create, Update and delete Contact points using Ansible.


.. Aliases


.. Requirements






.. Options

Parameters
----------


.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-DisableResolveMessage"></div>

      .. _ansible_collections.grafana.grafana.alert_contact_point_module__parameter-disableresolvemessage:

      .. rst-class:: ansible-option-title

      **DisableResolveMessage**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-DisableResolveMessage" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      When set to True, Disables the resolve message [OK] that is sent when alerting state returns to false


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-grafana_api_key"></div>

      .. _ansible_collections.grafana.grafana.alert_contact_point_module__parameter-grafana_api_key:

      .. rst-class:: ansible-option-title

      **grafana_api_key**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-grafana_api_key" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Grafana API Key used to authenticate with Grafana.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.grafana.grafana.alert_contact_point_module__parameter-name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the contact point


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-settings"></div>

      .. _ansible_collections.grafana.grafana.alert_contact_point_module__parameter-settings:

      .. rst-class:: ansible-option-title

      **settings**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-settings" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Contact point settings


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.grafana.grafana.alert_contact_point_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State for the Grafana CLoud stack.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`present` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`absent`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-type"></div>

      .. _ansible_collections.grafana.grafana.alert_contact_point_module__parameter-type:

      .. rst-class:: ansible-option-title

      **type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Contact point type


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-uid"></div>

      .. _ansible_collections.grafana.grafana.alert_contact_point_module__parameter-uid:

      .. rst-class:: ansible-option-title

      **uid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-uid" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Sets the UID of the Contact point.


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create/Update Alerting contact point
      alert_contact_point:
        name: ops-email
        uid: opsemail
        type: email
        settings: {
           addresses: "ops@mydomain.com,devs@mydomain.com"
         }
        stack_slug: "{{ stack_slug }}"
        grafana_api_key: "{{ grafana_api_key }}"
        state: present

    - name: Delete Alerting contact point
      alert_contact_point:
        name: ops-email
        uid: opsemail
        type: email
        settings: {
           addresses: "ops@mydomain.com,devs@mydomain.com"
         }
        stack_slug: "{{ stack_slug }}"
        grafana_api_key: "{{ grafana_api_key }}"
        state: absent




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output"></div>

      .. _ansible_collections.grafana.grafana.alert_contact_point_module__return-output:

      .. rst-class:: ansible-option-title

      **output**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Dict object containing Contact point information information


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` On success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/disableResolveMessage"></div>

      .. _ansible_collections.grafana.grafana.alert_contact_point_module__return-output/disableresolvemessage:

      .. rst-class:: ansible-option-title

      **disableResolveMessage**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/disableResolveMessage" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      When set to True, Disables the resolve message [OK] that is sent when alerting state returns to false


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/name"></div>

      .. _ansible_collections.grafana.grafana.alert_contact_point_module__return-output/name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/name" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The name for the contact point


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/settings"></div>

      .. _ansible_collections.grafana.grafana.alert_contact_point_module__return-output/settings:

      .. rst-class:: ansible-option-title

      **settings**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/settings" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Contains contact point settings


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/type"></div>

      .. _ansible_collections.grafana.grafana.alert_contact_point_module__return-output/type:

      .. rst-class:: ansible-option-title

      **type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/type" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The type of contact point


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/uid"></div>

      .. _ansible_collections.grafana.grafana.alert_contact_point_module__return-output/uid:

      .. rst-class:: ansible-option-title

      **uid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/uid" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The UID for the contact point


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>




..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Ishan Jain (@ishanjainn)



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/grafana/grafana-ansible-collection/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/grafana/grafana-ansible-collection" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors
