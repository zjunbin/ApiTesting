#  coding utf-8
# @time      :2019/3/1811:53
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test_login.py
from common.read_excel import DoExcel
from common import constants
from common.mylog import MyLog
from common.request import Request
from common.doregex import *
from ddt import ddt, data, unpack
import unittest
import json
read = DoExcel(constants.data_case,'login')
data_list = read.get_case()

@ddt
class Login(unittest.TestCase):
    @data(*data_list)
    def test_longin(self, case):
        url = getattr(contex, 'url') + case.url
        mylog = MyLog()
        mylog.debug('判断有无初始化的cookies值')
        if hasattr(contex, 'cookies'):
            cookies = getattr(contex, 'cookies')
        else:
            cookies = None
        mylog.debug('获取到的cookies值是：{}'.format(cookies))
        params = json.loads(DoRegex().replace(case.params))
        resp = Request(method=case.method, url=url, data=params, cookies=cookies)
        mylog.info('执行{}的用例'.format(case.title))
        mylog.info('请求数据{}'.format(params))
        if resp.cookies():
            setattr(contex, 'cookies', resp.cookies())
            mylog.info('本次请求获取到的cookies是：{}'.format(resp.cookies()))
        actual = resp.get_txt()
        result = None
        try:
            self.assertEqual(actual, case.expected)
            result = 'PASS'
            mylog.info('执行{}的用例：{}'.format(case.title, result))
        except Exception as e:
            result = 'FAILED'
            mylog.error('执行{}的用例,错误信息是：{}'.format(case.title, e))
            raise e
        finally:
            read.write_result(case.caseid + 1, 7, resp.get_txt())
            read.write_result(case.caseid + 1, 8, result)
            mylog.info('写入测试结果完成')


