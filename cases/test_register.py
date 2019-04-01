#  coding utf-8
# @time      :2019/3/1513:35
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test_register.py
import unittest
from common.read_excel import ReadExcel
from common.readconfig import ReadConfig
from common.request import Request
from common.mylog import MyLog
# from common import myloger1
from common.mysql import *
from ddt import ddt,data
import json
read = ReadExcel()
data_case = read.read_excel('register')
conf = ReadConfig()
# mylog = MyLog()
COOKIES = None

@ddt
class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mylog = MyLog()


    def setUp(self):
        self.mylog.debug('开始http请求')

    def tearDown(self):
        self.mylog.debug('结束http请求')

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
        url = getattr(contex, 'url') + item['url']
        resp = Request(method=item['method'], url=url, data=params, cookies=COOKIES)
        self.mylog.info('请求数据是:{}'.format(params))
        self.mylog.debug('请求完成，服务器响应码是：{}'.format(resp.status_code()))
        # 设置COOKIES的值
        if resp.cookies():
            COOKIES = resp.cookies()
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
            self.mylog.info('{}:用例执行通过'.format(item['title']))
        except Exception as e:
            result = 'FAIL'
            self.mylog.info('{}:用例执行未通过'.format(item['title']))
            raise e
        finally:

            read.write_result('register', item['caseid'], actual, result)
            self.mylog.info('{}:测试结果写入完成'.format(item['title']))


# 13261251296
