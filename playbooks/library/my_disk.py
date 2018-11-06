#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yuloong at 2018/11/6


from subprocess import PIPE, Popen
from ansible.module_utils.basic import *
import re


def get_disk(cmd):
    """
    获取磁盘信息
    :param cmd:
    :return: Type=dict 返回磁盘信息或者 Flase
    """

    space = {}

    disk = Popen(cmd, shell=True, stdout=PIPE)

    output = disk.communicate()[0]

    # re.sub('\s+', ' ', output).strip() 替换字符串中一个或多个空格

    status = disk.returncode

    if status == 0:
        # 去除列表中空元素
        handle_list = filter(None, output.split("\n"))
        for index, line in enumerate(handle_list):
            if len(line):
                try:
                    device, device_num, rm, size, ro, device_type, = re.sub('\s+', ' ', line).strip().split()

                    space[index] = dict(device_name=device, device_size=size, device_type=device_type)

                except ValueError as err:
                    print err
        return space
    else:
        return False


def main():
    disk_cmd = "lsblk | grep ^sd[a-z]"

    module = AnsibleModule(argument_spec=dict(), )

    data = get_disk(disk_cmd)

    if data:

        results = dict(module='my_disk', stdotut=data, change=False, rc=0)

        module.exit_json(**results)

    else:

        msg = "get system disk failed"

        module.fail_json(msg=msg)


if __name__ == '__main__':
    main()
