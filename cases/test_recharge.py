#  coding utf-8
# @time      :2019/3/1910:19
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test_recharge.py
from common.read_excel import ReadExcel
from common.request import Request
from common.doregex import *
from common import myloger1
from common.mysql import MySql
from decimal import Decimal
from ddt import ddt, data
import unittest
import json

read = ReadExcel()
data_case = read.read_excel('recharge')


@ddt
class Recharge(unittest.TestCase):
    def setUp(self):
        sql = 'SELECT * FROM future.member WHERE MobilePhone = "{}" '.format(getattr(contex,'loanid_user'))
        value = MySql().fet_one(sql= sql)
        setattr(contex, 'LeaveAmount', value['LeaveAmount'])


    @data(*data_case)
    def test_recharge(self, item):
        '''通过反射查看是否有COOKIES的值'''
        if hasattr(contex, 'COOKIES'):
            COOKIES = getattr(contex, 'COOKIES')
        else:
            COOKIES = None
        params = item['params']
        '''通过读取配置文件替换params中的用户名或密码，并序列化'''
        params = json.loads(DoRegex().replace(params))
        url = getattr(contex, 'url') + item['url']
        resp = Request(method=item['method'], url=url, data=params, cookies=COOKIES)
        '''登陆成功后将获取到的值通过反射写入到配置类中'''
        if resp.cookies():
            setattr(contex, 'COOKIES', resp.cookies())
        result = None
        actual = resp.get_txt()

        # 充值成功的进行数据库校验
        title_value = item['title'][0:4]
        if title_value == '正常充值':
            sql = 'SELECT * FROM future.member WHERE MobilePhone = "{}" '.format(params['mobilephone'])
            value  = MySql().fet_one(sql=sql)
            actual_value = value['LeaveAmount']  # 获取充值后的金额
            excetp = actual_value - Decimal(params['amount'])  # 预期用户金额
            excepted = json.loads(item['excepted'])
            request_actual = resp.get_json()
            try:
                assert Decimal(excetp) == Decimal(getattr(contex,'LeaveAmount')) and int(value['MobilePhone']) == int(params['mobilephone']) \
                       and request_actual['code'] == excepted['code']and request_actual['msg'] == excepted['msg'] \
                       and request_actual['status'] == excepted['status']
                result = 'Pass'
            except Exception as e:
                result = 'Failed'
            finally:
                read.write_result('recharge', item['caseid'], actual, result)
        else: # 充值失败的值校验响应报文
            try:
                self.assertEqual(actual, item['excepted'])
                result = 'Pass'
            except Exception as e:
                result = 'Failed'
                myloger1.mylog.error(e)
                raise e
            finally:
                read.write_result('recharge', item['caseid'], actual, result)


