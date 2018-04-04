#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
检测系统时间
"""


from ansible.module_utils.basic import *

from subprocess import Popen, PIPE


def cus_module_timezone(shell_command):

    status = Popen(shell_command, shell=True, stdout=PIPE, stderr=PIPE)

    stdout, stderr = status.communicate()

    if status.returncode == 0:

        results = {
            "status": status.returncode,
            "stdout": stdout,
            "messag": "system time: {0}".format(stdout)
        }

    else:

        results = {
            "status": status.returncode,
            "stdout": stderr,
            "messag": "system time: {0}".format(stderr)
        }

    return results


if __name__ == '__main__':
    refactor_module = AnsibleModule(argument_spec=dict(), )

    command = """ date """

    data = cus_module_timezone(command)

    if data['status'] == 0:

        result = dict(module='timezone', stdotut=data['stdout'], changed=False, rc=0)

        refactor_module.exit_json(**result)

    else:

        result = dict(msg='execute failed', rc=data['status'])

        refactor_module.fail_json(**result)