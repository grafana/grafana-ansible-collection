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

.. _ansible_collections.grafana.grafana.datasource_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

grafana.grafana.datasource module -- Manage Data sources in Grafana
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `grafana.grafana collection <https://galaxy.ansible.com/grafana/grafana>`_ (version 0.0.5).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install grafana.grafana`.

    To use it in a playbook, specify: :code:`grafana.grafana.datasource`.

.. version_added

.. versionadded:: 0.0.1 of grafana.grafana

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create, Update and delete Data sources using Ansible.


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
        <div class="ansibleOptionAnchor" id="parameter-cloud_api_key"></div>

      .. _ansible_collections.grafana.grafana.datasource_module__parameter-cloud_api_key:

      .. rst-class:: ansible-option-title

      **cloud_api_key**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cloud_api_key" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-datasource"></div>

      .. _ansible_collections.grafana.grafana.datasource_module__parameter-datasource:

      .. rst-class:: ansible-option-title

      **datasource**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-datasource" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      JSON source code for the Data source


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-stack_slug"></div>

      .. _ansible_collections.grafana.grafana.datasource_module__parameter-stack_slug:

      .. rst-class:: ansible-option-title

      **stack_slug**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-stack_slug" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the Grafana Cloud stack to which the notification policies will be added


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.grafana.grafana.datasource_module__parameter-state:

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

    
    - name: Create/Update Data sources
      datasource:
        datasource: "{{ lookup('file', 'datasource.json') }}"
        stack_slug: "{{ stack_slug }}"
        cloud_api_key: "{{ grafana_cloud_api_key }}"
        state: present

    - name: Delete Data sources
      datasource:
        datasource: "{{ lookup('file', 'datasource.json') }}"
        stack_slug: "{{ stack_slug }}"
        cloud_api_key: "{{ grafana_cloud_api_key }}"
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

      .. _ansible_collections.grafana.grafana.datasource_module__return-output:

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

      Dict object containing Data source information


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` On success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/datasource"></div>

      .. _ansible_collections.grafana.grafana.datasource_module__return-output/datasource:

      .. rst-class:: ansible-option-title

      **datasource**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/datasource" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The response body content for the data source configuration.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/id"></div>

      .. _ansible_collections.grafana.grafana.datasource_module__return-output/id:

      .. rst-class:: ansible-option-title

      **id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/id" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The ID assigned to the data source


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/message"></div>

      .. _ansible_collections.grafana.grafana.datasource_module__return-output/message:

      .. rst-class:: ansible-option-title

      **message**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/message" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The message returned after the operation on the Data source


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/name"></div>

      .. _ansible_collections.grafana.grafana.datasource_module__return-output/name:

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

      The name of the data source defined in the JSON source code


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
