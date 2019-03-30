#  coding utf-8
# @time      :2019/3/1513:35
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test_register.py
import unittest
from api_testing.common.read_excel import ReadExcel
from api_testing.common.readconfig import ReadConfig
from api_testing.common.request import Request
from api_testing.common.mylog import MyLog
from ddt import ddt,data
import json
read = ReadExcel()
data_case = read.read_excel('register')
conf = ReadConfig()
mylog = MyLog()
COOKIES = None

@ddt
class TestRegister(unittest.TestCase):
    @data(*data_case)
    def test_register(self,item):
        global COOKIES
        params = json.loads(item['params'])
        # 如果mobilephone 等于 phone ,那么去配置文件中获取初始手机号码
        if params['mobilephone'] == 'phone':
            value =  int(conf.get('register', 'phone'))
            params['mobilephone'] =value
            #手机号码使用之后将手机号码+1写会配置文件
            conf.set('register', 'phone', str(value + 1))
        mylog.debug('开始http请求')
        resp = Request(method=item['method'], url=item['url'], data=params, cookies=COOKIES)
        mylog.debug('请求完成，服务器响应码是：{}'.format(resp.get_status_code()))

        if resp.get_cookies():
            COOKIES = resp.get_cookies()
        actual = resp.get_txt()
        try:
            self.assertEqual(actual, item['excepted'])
            result = 'PASS'
            mylog.info('{}:用例执行通过'.format(item['title']))
        except Exception as e:
            result = 'FAIL'
            mylog.info('{}:用例执行未通过'.format(item['title']))
            raise e
        finally:
            read.write_result('register', item['caseid'], actual, result)
            mylog.info('{}:测试结果写入完成'.format(item['title']))
