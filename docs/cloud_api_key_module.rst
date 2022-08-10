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

.. _ansible_collections.grafana.grafana.cloud_api_key_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

grafana.grafana.cloud_api_key module -- Manage Grafana Cloud API keys
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `grafana.grafana collection <https://galaxy.ansible.com/grafana/grafana>`_ (version 0.0.5).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install grafana.grafana`.

    To use it in a playbook, specify: :code:`grafana.grafana.cloud_api_key`.

.. version_added

.. versionadded:: 0.0.1 of grafana.grafana

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create and delete Grafana Cloud API keys using Ansible.


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
        <div class="ansibleOptionAnchor" id="parameter-existing_cloud_api_key"></div>

      .. _ansible_collections.grafana.grafana.cloud_api_key_module__parameter-existing_cloud_api_key:

      .. rst-class:: ansible-option-title

      **existing_cloud_api_key**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-existing_cloud_api_key" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      CLoud API Key to authenticate with Grafana Cloud.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-fail_if_already_created"></div>

      .. _ansible_collections.grafana.grafana.cloud_api_key_module__parameter-fail_if_already_created:

      .. rst-class:: ansible-option-title

      **fail_if_already_created**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-fail_if_already_created" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to True, the task will fail if the API key with same name already exists in the Organization.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-default-bold:`yes` :ansible-option-default:`← (default)`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.grafana.grafana.cloud_api_key_module__parameter-name:

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

      Name of the Grafana Cloud API key.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-org_slug"></div>

      .. _ansible_collections.grafana.grafana.cloud_api_key_module__parameter-org_slug:

      .. rst-class:: ansible-option-title

      **org_slug**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-org_slug" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the Grafana Cloud organization in which Cloud API key will be created


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-role"></div>

      .. _ansible_collections.grafana.grafana.cloud_api_key_module__parameter-role:

      .. rst-class:: ansible-option-title

      **role**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-role" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Role to be associated with the CLoud API key.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.grafana.grafana.cloud_api_key_module__parameter-state:

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


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create Grafana Cloud API key
      cloud_api_key:
        name: key_name
        role: Admin
        org_slug: "{{ org_slug }}"
        existing_cloud_api_key: "{{ grafana_cloud_api_key }}"
        fail_if_already_created: False
        state: present

    - name: Delete Grafana Cloud API key
      cloud_api_key:
        name: key_name
        org_slug: "{{ org_slug }}"
        existing_cloud_api_key: "{{ grafana_cloud_api_key }}"
        state: absent




.. Facts


.. Return values


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
