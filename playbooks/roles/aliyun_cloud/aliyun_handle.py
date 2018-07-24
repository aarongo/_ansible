#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
@author: EdwardLiu 
@contact: lonnyliu@126.com

@file: aliyun_handle.py
@time: 2018/6/4 10:36

"""

'''
RegionId: 新建的 VPC 所在的地域
CidrBlock: VPC  私网网段
VpcName: VPC名称
Description: VPC 描述
ClientToken: 验证唯一性,避免多次请求创建多个
UserCidr: 用户侧网络的网段,默认留空即可
方法返回值:
{
 "ResourceGroupId": "rg-acfm2okbybqbfja", 
 "RouteTableId": "vtb-wz90rbrt6mdfdmiphw88e", 
 "VRouterId": "vrt-wz9ceq38eu31qgdu01qy5", 
 "VpcId": "vpc-wz95vfi2cgg5a5mkumfn0", 
 "RequestId": "61AD2AE1-53E4-4642-A986-8CB78FB02702"
}
RequestId: 请求ID。
VpcId: 专有网络的ID。
VRouterId: 路由器的ID。
RouteTableId: 路由表的ID。
'''

# 创建操作,ClientToken 只要使用过一次第二次调用通用的接口不能创建

from aliyunsdkcore import client
from aliyunsdkvpc.request.v20160428 import CreateVpcRequest
from aliyunsdkvpc.request.v20160428 import CreateVSwitchRequest
from aliyunsdkvpc.request.v20160428 import CreateNatGatewayRequest
import json


class Ali_Cloud(object):

    def __init__(self):
        self.clt = client.AcsClient('LTAIfvwS8OW1CZX5', 'QoYFrOpiMpe69gsvAF2e2RuKi1vBUh')

    def CreateVpc(self):
        # 设置参数
        request = CreateVpcRequest.CreateVpcRequest()
        request.set_accept_format('json')

        request.add_query_param('ClientToken', '5acf60632444e118e03e53eb7fbd968388b34c84')
        request.add_query_param('RegionId', 'cn-shenzhen')
        request.add_query_param('CidrBlock', '192.168.10.0/24')
        request.add_query_param('VpcName', 'shenzhen-test')
        request.add_query_param('Description', 'shenzhen-test')
        # request.add_query_param('UserCidr', '172.31.4.0/24,192.168.0.0/24')

        # 发起请求
        response = json.loads(self.clt.do_action(request))

        # print json.dumps(response, indent=1)

        # 返回 专有网络 ID 当 Clientoken 值不变的情况下 相当进行查询
        return response['VpcId']

    def CreateVpcSwitch(self):
        # 设置参数
        request = CreateVSwitchRequest.CreateVSwitchRequest()
        request.set_accept_format('json')

        request.add_query_param('CidrBlock', '192.168.10.0/24')
        request.add_query_param('Description', 'api-create-test')
        request.add_query_param('ClientToken', '141ae214ef04f5f9b5e37bf5fd8bb991911930cf')
        request.add_query_param('ZoneId', 'cn-shenzhen-a')
        request.add_query_param('VpcId', 'vpc-wz93fr1fubokt9oscib3f')
        request.add_query_param('VSwitchName', 'api-create-vpcswitch')

        # 发起请求
        response = self.clt.do_action(request)

        print response

    def CreateVpcNat(self):

        # 设置参数
        request = CreateNatGatewayRequest.CreateNatGatewayRequest()
        request.set_accept_format('json')

        request.add_query_param('RegionId', 'cn-shenzhen')
        request.add_query_param('Description', 'api-create-nat')
        request.add_query_param('ClientToken', '3b8ed890abb8914d65e10da4843de983f17f0bc1')
        request.add_query_param('VpcId', 'vpc-wz93fr1fubokt9oscib3f')
        request.add_query_param('Spec', 'Small')
        request.add_query_param('Name', 'api-create-nat')

        # 发起请求
        response = self.clt.do_action(request)

        print response
