#  coding utf-8
# @time      :2019/3/1513:35
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test_login.py
import unittest
from api_testing.common.read_excel import ReadExcel
from api_testing.common.request import Request
from ddt import ddt,data,unpack
import json
from api_testing.common.mylog import MyLog

mylog = MyLog()

#导入测试用例
readexcel = ReadExcel()
data_list = readexcel.read_excel('login')
COOKIES = None
@ddt
class Login(unittest.TestCase):
    def setUp(self):
        print('开始执行用例')

    @data(*data_list)
    def test_login(self,item):
        global COOKIES
        params = json.loads(item['params'])
        mylog.debug('开始http请求')
        resp = Request(method=item['method'],url=item['url'],data=params,cookies=COOKIES)
        mylog.info('请求的数据是：{}'.format(item))
        mylog.debug('请求完成，服务器响应码是：{}'.format(resp.get_status_code()))
        if resp.get_cookies():
            COOKIES= resp.get_cookies()
        actual = resp.get_txt()
        try:
            self.assertEqual(actual,item['excepted'])
            result = 'PASS'
            mylog.info('{}:用例执行通过'.format(item['title']))
        except Exception as e:
            result = 'FAIL'
            mylog.info('{}:用例执行未通过'.format(item['title']))
            raise e
        finally:
            readexcel.write_result('login',item['caseid'],actual,result)
            mylog.info('{}:测试结果写入完成'.format(item['title']))

    def tearDown(self):
        print('用例执行完成')
