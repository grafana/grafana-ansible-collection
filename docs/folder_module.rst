.. _grafana.grafana.folder_module:


.. Title

grafana.grafana.folder module -- Manage Folders in Grafana
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `grafana.grafana collection <https://galaxy.ansible.com/grafana/grafana>`_ (version 0.0.5).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install grafana.grafana`.

    To use it in a playbook, specify: :code:`grafana.grafana.folder`.

.. version_added

.. versionadded:: 0.0.1 of grafana.grafana

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create, Update and delete Folders via Ansible.


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

      .. _ansible_collections.grafana.grafana.folder_module__parameter-cloud_api_key:

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
        <div class="ansibleOptionAnchor" id="parameter-overwrite"></div>

      .. _ansible_collections.grafana.grafana.folder_module__parameter-overwrite:

      .. rst-class:: ansible-option-title

      **overwrite**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-overwrite" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set to false if you dont want to overwrite existing folder with newer version.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"yes"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.grafana.grafana.folder_module__parameter-state:

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
        <div class="ansibleOptionAnchor" id="parameter-title"></div>

      .. _ansible_collections.grafana.grafana.folder_module__parameter-title:

      .. rst-class:: ansible-option-title

      **title**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-title" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The title of the folder.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-uid"></div>

      .. _ansible_collections.grafana.grafana.folder_module__parameter-uid:

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

      unique identifier for your folder.


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create/Update a Folder in Grafana
      folder:
        title: folder_name
        uid: folder_name
        overwrite: true
        stack_slug: "{{ stack_slug }}"
        cloud_api_key: "{{ grafana_cloud_api_key }}"
        state: present

    - name: Delete a Folder in Grafana
      folder:
        uid: folder_name
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

      .. _ansible_collections.grafana.grafana.folder_module__return-output:

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

      Dict object containing folder information


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` On success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/canAdmin"></div>

      .. _ansible_collections.grafana.grafana.folder_module__return-output/canadmin:

      .. rst-class:: ansible-option-title

      **canAdmin**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/canAdmin" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Boolean value specifying if current user can admin in folder


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/canDelete"></div>

      .. _ansible_collections.grafana.grafana.folder_module__return-output/candelete:

      .. rst-class:: ansible-option-title

      **canDelete**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/canDelete" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Boolean value specifying if current user can delete the folder


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/canEdit"></div>

      .. _ansible_collections.grafana.grafana.folder_module__return-output/canedit:

      .. rst-class:: ansible-option-title

      **canEdit**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/canEdit" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Boolean value specifying if current user can edit in folder


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/canSave"></div>

      .. _ansible_collections.grafana.grafana.folder_module__return-output/cansave:

      .. rst-class:: ansible-option-title

      **canSave**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/canSave" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Boolean value specifying if current user can save in folder


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/created"></div>

      .. _ansible_collections.grafana.grafana.folder_module__return-output/created:

      .. rst-class:: ansible-option-title

      **created**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/created" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The date when folder was created


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/createdBy"></div>

      .. _ansible_collections.grafana.grafana.folder_module__return-output/createdby:

      .. rst-class:: ansible-option-title

      **createdBy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/createdBy" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The name of the user who created the folder


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/hasAcl"></div>

      .. _ansible_collections.grafana.grafana.folder_module__return-output/hasacl:

      .. rst-class:: ansible-option-title

      **hasAcl**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/hasAcl" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Boolean value specifying if folder has acl


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/id"></div>

      .. _ansible_collections.grafana.grafana.folder_module__return-output/id:

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

      The ID for the folder


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/message"></div>

      .. _ansible_collections.grafana.grafana.folder_module__return-output/message:

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

      The message returned after the operation on the folder


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is absent and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/title"></div>

      .. _ansible_collections.grafana.grafana.folder_module__return-output/title:

      .. rst-class:: ansible-option-title

      **title**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/title" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The name of the folder


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/uid"></div>

      .. _ansible_collections.grafana.grafana.folder_module__return-output/uid:

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

      The UID for the folder


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/updated"></div>

      .. _ansible_collections.grafana.grafana.folder_module__return-output/updated:

      .. rst-class:: ansible-option-title

      **updated**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/updated" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The date when the folder was last updated


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/updatedBy"></div>

      .. _ansible_collections.grafana.grafana.folder_module__return-output/updatedby:

      .. rst-class:: ansible-option-title

      **updatedBy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/updatedBy" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The name of the user who last updated the folder


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/url"></div>

      .. _ansible_collections.grafana.grafana.folder_module__return-output/url:

      .. rst-class:: ansible-option-title

      **url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/url" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The URl for the folder


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` state is present and on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-output/version"></div>

      .. _ansible_collections.grafana.grafana.folder_module__return-output/version:

      .. rst-class:: ansible-option-title

      **version**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-output/version" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The version of the folder


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
