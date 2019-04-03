#  coding utf-8
# @time      :2019/3/1915:56
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test_withdraw.py
from common.request import Request
from common.read_excel import DoExcel
from common.mysql import MySql
from common import constants
from common.doregex import *
from decimal import Decimal
from ddt import ddt, data
import unittest
import json

read = DoExcel(constants.data_case,'withdraw')
data_case = read.get_case()


@ddt
class Withdraw(unittest.TestCase):
    def setUp(self):
        sql = 'SELECT * FROM future.member WHERE MobilePhone = "{}"'.format(getattr(contex,'withdraw_user'))
        value = MySql().fet_one(sql=sql)
        setattr(contex, 'LeaveAmount', value['LeaveAmount'])

    @data(*data_case)
    def test_withdraw(self, item):
        result = None
        params = json.loads(DoRegex().replace(item.params))  # 处理初始化数据
        url = getattr(contex, 'url') + item.url
        if hasattr(contex, 'COOKIES'):  # 处理COOKIES
            COOKIES = getattr(contex, 'COOKIES')
        else:
            COOKIES = None
        resp = Request(method=item.method, url=url, data=params, cookies=COOKIES)  # 开始HTTP请求
        if resp.cookies():
            setattr(contex, 'COOKIES', resp.cookies())
        # withdraw_title = item['title'][0:4]
        # if withdraw_title == '成功取现':
        if resp.get_json()['msg'] == '取现成功':
            sql = 'SELECT * FROM future.member WHERE MobilePhone = {} '.format(params['mobilephone'])
            value = MySql().fet_one(sql)
            data_LeaveAmount = value['LeaveAmount']  # 数据库中的金额
            contex_LeaveAmount = getattr(contex, 'LeaveAmount')  # 反射类contex中的金额
            actual_value = Decimal(contex_LeaveAmount) - Decimal(params['amount'])  # 预期金额等于 contex金额减请求参数中的金额
            request_value = resp.get_json()
            excepted_value = json.loads(item.expected)
            print('data_LeaveAmount:',data_LeaveAmount)
            print('actual_value:',actual_value)
            try:  # 判断数据库金额是否等于预期金额 | 预期结果和响应报文中的值是否一致
                assert data_LeaveAmount == actual_value
                result = 'Pass'
            except Exception as e:
                result = 'Failed'
                raise e
            finally:
                read.write_result(item.caseid + 1, 7, resp.get_txt())
                read.write_result(item.caseid + 1, 8, result)
        elif resp.get_json()['msg'] == '充值成功':
            result = 'Pass'
            read.write_result(item.caseid + 1, 7, resp.get_txt())
            read.write_result(item.caseid + 1, 8, result)
        else:
            try:
                self.assertEqual(resp.get_txt(), item.expected)
                result = 'Pass'
            except Exception as e:
                result = 'Failed'
                raise e
            finally:
                read.write_result(item.caseid + 1, 7, resp.get_txt())
                read.write_result(item.caseid + 1, 8, result)


