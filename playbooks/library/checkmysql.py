#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author EdwardLiu


from ansible.module_utils.basic import *
from subprocess import Popen, PIPE


"""
检测系统中是否存在 Mysql和 Mariadb
或者重新安装 Mysql 
"""


def run_command(command):

    status = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)

    stdout, stderr = status.communicate()

    return stdout


# 获取系统中是否存在 mysql--- 适合重装 Mysql 接收外部参数
def get_mysql():

    out = {}

    # 获取系统残留(residualr) Mysql 文件和软件包
    command_dict = {
        "rpm_get": "rpm -qa | grep -i mysql",
        "path_get": "/usr/bin/whereis mysql"
    }

    for cmd in command_dict:

        if cmd == "rpm_get":
            stdout = run_command(command_dict[cmd])

            out["rpm"] = stdout.rstrip().split('\n')
        else:
            stdout = run_command(command_dict[cmd])

            # 转换成 list-- 1.替换换行符为 2. 以空格切割成 list
            out_list = stdout.replace("\n", "").split(' ')

            # 删除列表中指定元素
            out_list.remove('mysql:')

            out['path'] = out_list

    return out


# 删除 Mysql
def delete_mysql():

    results = {}

    # 1. 删除 mysql 软件
    for name in get_mysql()['rpm']:

        delete_command = "rpm -e --nodeps {0}".format(name)

        stdout = run_command(delete_command)

        if stdout == "":

            results['rpm'] = "Delete Mysql packages OK!"

        else:

            results['rpm'] = stdout

    # 2. 删除 Mysql 遗留目录
    for path in get_mysql()['path']:

        delete_path = "rm -rf {0}".format(path)

        stdout = run_command(delete_path)

        if stdout == "":

            results['path'] = "delete residualr files OK!"

        else:

            results['path'] = stdout

    return results


# 处理获取到的  Mariadb 为安装 mysql 调用
def get_mariadb():

    delete_command = "rpm -qa | grep mariadb"

    stdout = run_command(delete_command)

    out = stdout.rstrip().split('\n')

    return out


# 删除 Mariadb centos 7系统默认存在
def delete_mariadb():

    results = {}

    # 判断系统是否存在 mariadb
    if len(get_mariadb()):

        results = {
            "messages": "Do not need any operation!"
        }

    else:

        for s_name in get_mariadb():

            delete_command = "rpm -e --nodeps {0}".format(s_name)

            stdout = run_command(delete_command)

            re_mess = "software name:{0}".format(s_name)

            re_code = "process result:{0}".format(stdout)

            results[re_mess] = re_code

    return results


if __name__ == '__main__':
    refactor_module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
        ),
    )

    if refactor_module.params['name'] == "install":

        result = dict(module='checkmysql', stdotut=delete_mariadb(), changed=False, rc=0)

        refactor_module.exit_json(**result)

    elif refactor_module.params['name'] == "delete":

        result = dict(module='checkmysql', stdotut=delete_mysql(), changed=False, rc=0)

        refactor_module.exit_json(**result)

    else:

        result = dict(msg='params illegal', rc=1)

        refactor_module.fail_json(**result)