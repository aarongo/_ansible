#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yuloong at 2018/11/6
import re
from subprocess import PIPE, Popen

space = {}

get_disk = "lsblk | grep ^sd[a-z]"

disk = Popen(get_disk, shell=True, stdout=PIPE)

output = disk.communicate()[0]

print output

format_output = re.sub('\s+', ' ', output).strip()

print format_output

status = disk.returncode

if status == 0:
    # 去除列表中空元素,适应 Python3的写法
    # Python 3 returns an iterator from filter, so should be wrapped in a call to list()
    handle_list = list(filter(None, output.split("\n")))
    for index, line in enumerate(handle_list):
        if len(line):
            try:
                device, device_num, rm, size, ro, device_type, = re.sub('\s+', ' ', line).strip().split()

                space[index] = dict(device_name=device, device_size=size, device_type=device_type)

            except ValueError:
                pass