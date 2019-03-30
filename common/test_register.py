#  coding utf-8
# @time      :2019/3/1513:35
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test_register.py
import unittest
from api_testing.common.read_excel import ReadExcel
from api_testing.common.readconfig import ReadConfig
from api_testing.common.request import Request
# from api_testing.common.mylog import MyLog
from api_testing.common import myloger1
from api_testing.common.mysql import *
from ddt import ddt,data
import json
read = ReadExcel()
data_case = read.read_excel('register')
conf = ReadConfig()
# mylog = MyLog()
COOKIES = None

@ddt
class TestRegister(unittest.TestCase):

    def setUp(self):
        myloger1.mylog.debug('开始http请求')

    def tearDown(self):
        myloger1.mylog.debug('结束http请求')

    @data(*data_case)
    def test_register(self,item):
        # mysql = MySql()
        global COOKIES
        params = json.loads(item['params'])
        # 如果mobilephone 等于 phone ,那么去配置文件中获取初始手机号码
        if params['mobilephone'] == 'phone':
            value =  int(conf.get('register', 'phone'))
            params['mobilephone'] =value
            #手机号码使用之后将手机号码+1写会配置文件
            conf.set('register', 'phone', str(value + 1))

        resp = Request(method=item['method'], url=item['url'], data=params, cookies=COOKIES)
        myloger1.mylog.info('请求数据是:'.format(item))
        myloger1.mylog.debug('请求完成，服务器响应码是：{}'.format(resp.get_status_code()))
        # 设置COOKIES的值
        if resp.get_cookies():
            COOKIES = resp.get_cookies()
        # 请求完成后获取响应报文 ，在判断响应报文是否和预期结果一致
        # sql = 'SELECT * FROM future.member WHERE MobilePhone = {}'.format(params['mobilephone'])
        # if mysql.fet_one(sql=sql):
        #     sql_value = 'Pass'
        # else:
        #     sql_value = 'Failed'
        actual = resp.get_txt()
        result = None
        try:
            self.assertEqual(actual, item['excepted'])
            result = 'PASS'
            myloger1.mylog.info('{}:用例执行通过'.format(item['title']))
        except Exception as e:
            result = 'FAIL'
            myloger1.mylog.info('{}:用例执行未通过'.format(item['title']))
            raise e
        finally:

            read.write_result('register', item['caseid'], actual, result)
            myloger1.mylog.info('{}:测试结果写入完成'.format(item['title']))

