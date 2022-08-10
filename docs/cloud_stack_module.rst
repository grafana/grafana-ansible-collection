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

.. _ansible_collections.grafana.grafana.cloud_stack_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

grafana.grafana.cloud_stack module -- Manage Grafana Cloud stack
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `grafana.grafana collection <https://galaxy.ansible.com/grafana/grafana>`_ (version 0.0.5).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install grafana.grafana`.

    To use it in a playbook, specify: :code:`grafana.grafana.cloud_stack`.

.. version_added

.. versionadded:: 0.0.1 of grafana.grafana

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create and delete Grafana Cloud stacks using Ansible.


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

      .. _ansible_collections.grafana.grafana.cloud_stack_module__parameter-cloud_api_key:

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
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.grafana.grafana.cloud_stack_module__parameter-name:

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

      Name of stack. Conventionally matches the URL of the instance. For example, "<stack_slug>.grafana.net".


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-org_slug"></div>

      .. _ansible_collections.grafana.grafana.cloud_stack_module__parameter-org_slug:

      .. rst-class:: ansible-option-title

      **org_slug**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-org_slug" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the organization under which Cloud stack is created.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-region"></div>

      .. _ansible_collections.grafana.grafana.cloud_stack_module__parameter-region:

      .. rst-class:: ansible-option-title

      **region**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-region" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Choose a region for your stack.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`us` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`us-azure`
      - :ansible-option-choices-entry:`eu`
      - :ansible-option-choices-entry:`au`
      - :ansible-option-choices-entry:`eu-azure`
      - :ansible-option-choices-entry:`prod-ap-southeast-0`
      - :ansible-option-choices-entry:`prod-gb-south-0`
      - :ansible-option-choices-entry:`prod-eu-west-3`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-stack_slug"></div>

      .. _ansible_collections.grafana.grafana.cloud_stack_module__parameter-stack_slug:

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

      Subdomain of the Grafana instance. For example, if slug is <stack_slug>, the instance URL will be https://<stack_slug>.grafana.net


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.grafana.grafana.cloud_stack_module__parameter-state:

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
        <div class="ansibleOptionAnchor" id="parameter-url"></div>

      .. _ansible_collections.grafana.grafana.cloud_stack_module__parameter-url:

      .. rst-class:: ansible-option-title

      **url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-url" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If you use a custom domain for the instance, you can provide it here. For example, “https://grafana.yourdoman.io”.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"https://\<stack\_slug\>.grafana.net"`

      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create a Grafana Cloud stack
      cloud_stack:
        name: company_name
        slug: company_name
        cloud_api_key: "{{ grafana_cloud_api_key }}"
        region: eu
        url: https://grafana.company_name.com
        state: present

    - name: Delete a Grafana Cloud stack
      cloud_stack:
        name: company_name
        slug: company_name
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
        <div class="ansibleOptionAnchor" id="return-alertmanager_name"></div>

      .. _ansible_collections.grafana.grafana.cloud_stack_module__return-alertmanager_name:

      .. rst-class:: ansible-option-title

      **alertmanager_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-alertmanager_name" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the alertmanager instance


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-alertmanager_url"></div>

      .. _ansible_collections.grafana.grafana.cloud_stack_module__return-alertmanager_url:

      .. rst-class:: ansible-option-title

      **alertmanager_url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-alertmanager_url" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URL of the alertmanager instance


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-cluster_slug"></div>

      .. _ansible_collections.grafana.grafana.cloud_stack_module__return-cluster_slug:

      .. rst-class:: ansible-option-title

      **cluster_slug**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-cluster_slug" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Slug for the cluster where the Grafana stack is deployed


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-id"></div>

      .. _ansible_collections.grafana.grafana.cloud_stack_module__return-id:

      .. rst-class:: ansible-option-title

      **id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-id" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      ID of the Grafana Cloud stack


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-loki_url"></div>

      .. _ansible_collections.grafana.grafana.cloud_stack_module__return-loki_url:

      .. rst-class:: ansible-option-title

      **loki_url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-loki_url" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URl for the Loki instance


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-orgID"></div>

      .. _ansible_collections.grafana.grafana.cloud_stack_module__return-orgid:

      .. rst-class:: ansible-option-title

      **orgID**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-orgID" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      ID of the Grafana Cloud organization


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-prometheus_url"></div>

      .. _ansible_collections.grafana.grafana.cloud_stack_module__return-prometheus_url:

      .. rst-class:: ansible-option-title

      **prometheus_url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-prometheus_url" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URl for the Prometheus instance


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-tempo_url"></div>

      .. _ansible_collections.grafana.grafana.cloud_stack_module__return-tempo_url:

      .. rst-class:: ansible-option-title

      **tempo_url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-tempo_url" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URl for the Tempo instance


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-url"></div>

      .. _ansible_collections.grafana.grafana.cloud_stack_module__return-url:

      .. rst-class:: ansible-option-title

      **url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-url" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URL of the Grafana Cloud stack


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


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
