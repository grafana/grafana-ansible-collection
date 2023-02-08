#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Ishan Jain (@ishanjainn)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

DOCUMENTATION = '''
---
module: folder
author:
  - Ishan Jain (@ishanjainn)
version_added: "0.0.1"
short_description: Manage Folders in Grafana Cloud
description:
  - Create, Update and delete Folders via Ansible.
requirements: [ "requests >= 1.0.0" ]
notes:
  - Does not support C(check_mode).
options:
  title:
    description:
      - Sets the title of the folder.
    type: str
    required: true
  uid:
    description:
      - Sets the UID for your folder.
    type: str
    required: true
  overwrite:
    description:
      - Set to C(false) if you dont want to overwrite existing folder with newer version.
    type: bool
    required: false
    default: true
  grafana_api_key:
    description:
      - Grafana API Key to authenticate with Grafana.
    type: str
    required : true
  stack_slug:
    description:
      - Name of the Grafana Cloud stack to which the folder will be added.
    type: str
    required: true
  state:
    description:
      - State for the Grafana Cloud stack.
    choices: [ present, absent ]
    default: present
    type: str
'''

EXAMPLES = '''
- name: Create/Update a Folder in Grafana
  grafana.grafana.folder:
    title: folder_name
    uid: folder_name
    overwrite: true
    stack_slug: "{{ stack_slug }}"
    grafana_api_key: "{{ grafana_api_key }}"
    state: present

- name: Delete a Folder in Grafana
  grafana.grafana.folder:
    uid: folder_name
    stack_slug: "{{ stack_slug }}"
    grafana_api_key: "{{ grafana_api_key }}"
    state: absent
'''

RETURN = r'''
output:
  description: Dict object containing folder information.
  returned: On success
  type: dict
  contains:
    canAdmin:
      description: Boolean value specifying if current user can admin in folder.
      returned: state is present and on success
      type: bool
      sample: true
    canDelete:
      description: Boolean value specifying if current user can delete the folder.
      returned: state is present and on success
      type: bool
      sample: true
    canEdit:
      description: Boolean value specifying if current user can edit in folder.
      returned: state is present and on success
      type: bool
      sample: true
    canSave:
      description: Boolean value specifying if current user can save in folder.
      returned: state is present and on success
      type: bool
      sample: true
    created:
      description: The date when folder was created.
      returned: state is present and on success
      type: str
      sample: "2022-10-20T09:31:53Z"
    createdBy:
      description: The name of the user who created the folder.
      returned: state is present and on success
      type: str
      sample: "Anonymous"
    hasAcl:
      description: Boolean value specifying if folder has acl.
      returned: state is present and on success
      type: bool
      sample: true
    id:
      description: The ID for the folder.
      returned: state is present and on success
      type: int
      sample: 18
    title:
      description: The name of the folder.
      returned: on success
      type: str
      sample: foldername
    uid:
      description: The UID for the folder.
      returned: state is present and on success
      type: str
      sample: foldername
    updated:
      description: The date when the folder was last updated.
      returned: state is present and on success
      type: str
      sample: "2022-10-20T09:31:53Z"
    updatedBy:
      description: The name of the user who last updated the folder.
      returned: state is present and on success
      type: str
      sample: "Anonymous"
    url:
      description: The URl for the folder.
      returned: state is present and on success
      type: str
      sample: "/dashboards/f/foldername/foldername"
    version:
      description: The version of the folder.
      returned: state is present and on success
      type: int
      sample: 1
    message:
      description: The message returned after the operation on the folder.
      returned: state is absent and on success
      type: str
      sample: "Folder has been succesfuly deleted"
'''

from ansible.module_utils.basic import AnsibleModule, missing_required_lib
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

__metaclass__ = type


def present_folder(module):
    body = {
        'uid': module.params['uid'],
        'title': module.params['title'],
    }
    api_url = 'https://' + module.params['stack_slug'] + '.grafana.net/api/folders'

    result = requests.post(api_url, json=body, headers={"Authorization": 'Bearer ' + module.params['grafana_api_key']})

    if result.status_code == 200:
        return False, True, result.json()
    elif result.status_code == 412:
        sameConfig = False
        folderInfo = {}

        api_url = 'https://' + module.params['stack_slug'] + '.grafana.net/api/folders'
        result = requests.get(api_url, headers={"Authorization": 'Bearer ' + module.params['grafana_api_key']})

        for folder in result.json():
            if folder['uid'] == module.params['uid'] and folder['title'] == module.params['title']:
                sameConfig = True
                folderInfo = folder

        if sameConfig:
            return False, False, folderInfo
        else:
            body = {
                'uid': module.params['uid'],
                'title': module.params['title'],
                'overwrite': module.params['overwrite']
            }
            api_url = 'https://' + module.params['stack_slug'] + '.grafana.net/api/folders/' + module.params['uid']

            result = requests.put(api_url, json=body, headers={"Authorization": 'Bearer ' + module.params['grafana_api_key']})

            if result.status_code == 200:
                return False, True, result.json()
            else:
                return True, False, {"status": result.status_code, 'response': result.json()['message']}
    else:
        return True, False, {"status": result.status_code, 'response': result.json()['message']}


def absent_folder(module):
    api_url = 'https://' + module.params['stack_slug'] + '.grafana.net/api/folders/' + module.params['uid']

    result = requests.delete(api_url, headers={"Authorization": 'Bearer ' + module.params['grafana_api_key']})

    if result.status_code == 200:
        return False, True, {"status": result.status_code, 'response': "Folder has been succesfuly deleted"}
    else:
        return True, False, {"status": result.status_code, 'response': "Error deleting folder"}


def main():

    module_args = dict(
        title=dict(type='str', required=True),
        uid=dict(type='str', required=True),
        overwrite=dict(type='bool', required=False, default=True),
        stack_slug=dict(type='str', required=True),
        grafana_api_key=dict(type='str', required=True, no_log=True),
        state=dict(type='str', required=False, default='present', choices=['present', 'absent'])
    )

    choice_map = {
        "present": present_folder,
        "absent": absent_folder,
    }

    module = AnsibleModule(
        argument_spec=module_args
    )

    if not HAS_REQUESTS:
        module.fail_json(msg=missing_required_lib('requests'))

    is_error, has_changed, result = choice_map.get(
        module.params['state'])(module)

    if not is_error:
        module.exit_json(changed=has_changed, output=result)
    else:
        module.fail_json(msg=result)


if __name__ == '__main__':
    main()
