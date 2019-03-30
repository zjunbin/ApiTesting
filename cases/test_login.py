#  coding utf-8
# @time      :2019/3/1811:53
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test_login.py
from common.read_excel import ReadExcel
from common.mylog import MyLog
from common.request import Request
from common.doregex import *
from ddt import ddt, data, unpack
import unittest
import json

data_list = ReadExcel().read_excel('login')


@ddt
class Login(unittest.TestCase):
    @data(*data_list)
    @unpack
    def test_longin(self, caseid, method, params, excepted, url, title):
        url = getattr(contex, 'url') + url
        mylog = MyLog()
        mylog.debug('判断有无初始化的cookies值')
        if hasattr(contex, 'cookies'):
            cookies = getattr(contex, 'cookies')
        else:
            cookies = None
        mylog.debug('获取到的cookies值是：{}'.format(cookies))
        params = json.loads(params)
        resp = Request(method=method, url=url, data=params, cookies=cookies)
        mylog.info('执行{}的用例'.format(title))
        mylog.info('请求方式{}'.format(method))
        mylog.info('请求url{}'.format(url))
        mylog.info('请求数据{}'.format(params))
        if resp.cookies():
            setattr(contex, 'cookies', resp.cookies())
            mylog.info('本次请求获取到的cookies是：{}'.format(resp.cookies()))
        actual = resp.get_txt()
        result = None
        try:
            self.assertEqual(actual, excepted)
            result = 'PASS'
            mylog.info('执行{}的用例：{}'.format(title, result))
        except Exception as e:
            result = 'FAILED'
            mylog.error('执行{}的用例,错误信息是：{}'.format(title, e))
            raise e
        finally:
            ReadExcel().write_result('login', caseid=caseid, actual=actual, result=result)
            mylog.info('写入测试结果完成')
