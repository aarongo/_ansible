#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu

"""
检测是否可以连通外网, 使用 url方式, url 为可变参数
"""


from ansible.module_utils.basic import *
import urllib2


def internet_on(url):

    try:

        urllib2.urlopen(url, timeout=1)

        results = {
            'status': 0,
            'messages': "Connection"
        }

        return results

    except urllib2.URLError as err:

        results = {
            'status': 1,
            'messages': "Failed"
        }

        return results


if __name__ == '__main__':
    refactor_module = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True),
        ),
    )

    url = "http://" + refactor_module.params['url']

    if internet_on(url)['status'] == 0:

        result = dict(module='timezone', stdotut=internet_on(url)['messages'], changed=False, rc=0)

        refactor_module.exit_json(**result)

    else:

        result = dict(msg='execute failed', rc=internet_on(url)['status'])