#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: http_status

short_description: This module returns the status code from fetching a given URL

version_added: "2.4"

description:
    - "This module returns the status code from fetching a given URL, erroring on failures"

options:
    url:
        description:
            - This is the URL to fetch
        required: true

author:
    - Srikavin Ramkumar (@srikavin)
'''

EXAMPLES = '''
# Get the status code for https://google.com
- name: Status code for https://google.com
  http_status:
    url: https://google.com
'''

RETURN = '''
status_code:
    description: The numerical status code returned from the HTTP request
    type: int
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
import urllib.request

def run_module():
    module_args = dict(
        url=dict(type='str', required=True),
    )


    result = dict(
        changed=True,
        status_code=0
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    try:
        f = urllib.request.urlopen(module.params['url'])
    except:
        module.fail_json(msg='HTTP Request failed', **result)


    result['status_code'] = f.code
    result['changed'] = True


    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()