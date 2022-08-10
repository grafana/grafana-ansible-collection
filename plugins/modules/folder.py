#!/usr/bin/python

DOCUMENTATION = '''
---
module: folder
author:
  - Ishan Jain (@ishanjainn)
version_added: "0.0.1"
short_description: Manage Folders in Grafana
description:
  - Create, Update and delete Folders via Ansible.
options:
  title:
    description:
      - The title of the folder.
    type: str
    required: true
  uid:
    description:
      - unique identifier for your folder.
    type: str
    required: true
  overwrite:
    description:
      - Set to false if you dont want to overwrite existing folder with newer version.
    type: str
    required: false
    default: true
  cloud_api_key:
    description:
      - CLoud API Key to authenticate with Grafana Cloud.
    type: str
    required : true
  state:
    description:
      - State for the Grafana CLoud stack.
    choices: [ present, absent ]
    default: present
    type: str
'''

EXAMPLES = '''
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
'''

RETURN = r'''
output:
  description: Dict object containing folder information
  returned: On success
  type: dict
  contains:
    canAdmin:
      description: Boolean value specifying if current user can admin in folder
      returned: state is present and on success
      type: bool
    canDelete:
      description: Boolean value specifying if current user can delete the folder
      returned: state is present and on success
      type: bool
    canEdit:
      description: Boolean value specifying if current user can edit in folder
      returned: state is present and on success
      type: bool
    canSave:
      description: Boolean value specifying if current user can save in folder
      returned: state is present and on success
      type: bool
    created:
      description: The date when folder was created
      returned: state is present and on success
      type: str
    createdBy:
      description: The name of the user who created the folder
      returned: state is present and on success
      type: str
    hasAcl:
      description: Boolean value specifying if folder has acl
      returned: state is present and on success
      type: bool
    id:
      description: The ID for the folder
      returned: on success
      type: int
    title:
      description: The name of the folder
      returned: on success
      type: str
    uid:
      description: The UID for the folder
      returned: state is present and on success
      type: str
    updated:
      description: The date when the folder was last updated
      returned: state is present and on success
      type: str
    updatedBy:
      description: The name of the user who last updated the folder
      returned: state is present and on success
      type: str
    url:
      description: The URl for the folder
      returned: state is present and on success
      type: str
    version:
      description: The version of the folder
      returned: state is present and on success
      type: int
    message:
      description: The message returned after the operation on the folder
      returned: state is absent and on success
      type: str
'''

from ansible.module_utils.basic import AnsibleModule
import requests


def present_folder(module):
    body = {
        'uid': module.params['uid'],
        'title': module.params['title'],
    }
    api_url = 'https://' + module.params['stack_slug'] + '.grafana.net/api/folders'

    result = requests.post(api_url, json=body, headers={"Authorization": 'Bearer ' + module.params['cloud_api_key']})

    if result.status_code == 200:
        return False, True, result.json()
    elif result.status_code == 412:
        body = {
            'uid': module.params['uid'],
            'title': module.params['title'],
            'overwrite': module.params['overwrite']
        }
        api_url = 'https://' + module.params['stack_slug'] + '.grafana.net/api/folders/' + module.params['uid']

        result = requests.put(api_url, json=body, headers={"Authorization": 'Bearer ' + module.params['cloud_api_key']})

        if result.status_code == 200:
            return False, True, result.json()
        else:
            return True, False, {"status": result.status_code, 'response': result.json()['message']}

    else:
        return True, False, {"status": result.status_code, 'response': result.json()['message']}


def absent_folder(module):
    api_url = 'https://' + module.params['stack_slug'] + '.grafana.net/api/folders/' + module.params['uid']

    result = requests.delete(api_url, headers={"Authorization": 'Bearer ' + module.params['cloud_api_key']})

    if result.status_code == 200:
        return False, True, result.json()
    else:
        return True, False, {"status": result.status_code, 'response': result.json()['message']}


def main():
    module_args = dict(
        title=dict(type='str', required=True),
        uid=dict(type='str', required=True),
        overwrite=dict(type='bool', required=False, default=True),
        stack_slug=dict(type='str', required=True),
        cloud_api_key=dict(type='str', required=True),
        state=dict(type='str', required=False, default='present', choices=['present', 'absent'])
    )

    choice_map = {
        "present": present_folder,
        "absent": absent_folder,
    }

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    is_error, has_changed, result = choice_map.get(
        module.params['state'])(module)

    if not is_error:
        module.exit_json(changed=has_changed, output=result)
    else:
        module.fail_json(msg=result)


if __name__ == '__main__':
    main()
