#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu

"""
检测是否存在定时任务
"""

from ansible.module_utils.basic import *
from subprocess import Popen, PIPE


def check_cron():

    shell_cmd = "crontab -l"

    status = Popen(shell_cmd, shell=True, stdout=PIPE, stderr=PIPE)

    stdout, stderr = status.communicate()

    results = {
        "status": status.returncode,
        "stdout": stdout,
        "stderr": stderr
    }

    return results


if __name__ == '__main__':

    refactor_module = AnsibleModule(argument_spec=dict(), )

    check_string = "no crontab"

    if check_cron()['status'] == 0 and check_string in check_cron()['stdout']:

        messages = "no crontab"

        result = dict(module='checkcrond', stdotut=messages, changed=False, rc=0)

        refactor_module.exit_json(**result)

    elif check_cron()['status'] == 0 and check_string not in check_cron()['stdout']:

        messages = "crond info: {0}".format(check_cron()['stdout'])

        result = dict(module='checkcrond', stdotut=messages, changed=False, rc=0)

        refactor_module.exit_json(**result)

    else:

        result = dict(msg='execute failed', rc=check_cron()['status'])

        refactor_module.fail_json(**result)