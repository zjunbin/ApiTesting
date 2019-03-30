# _*_ coding: utf-8 _*_
# @Time     : 2019/3/26 19:53
# Author    : zjunbin
# @Email    : 648260307@qq.com
# @File     : test_loadadd.py

from api_testing.common.read_excel import ReadExcel
from api_testing.common.mysql import MySql
from api_testing.common.readconfig import ReadConfig
from api_testing.common.readconfig import ReadConfig
from api_testing.common.request import Request
from api_testing.common.doregex import *
from ddt import ddt, data
import unittest
import json

read = ReadExcel()
data_case = read.read_excel('addloan')


@ddt
class LoadAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conf = ReadConfig()
        sql = 'SELECT * FROM future.member WHERE MobilePhone = "{}"'.format(getattr(contex, 'normal_user'))
        mysql = MySql()
        value = mysql.fet_one(sql=sql)
        setattr(contex, 'normal_user_id', str(value['Id']))
        cls.url = cls.conf.get('url', 'url')

    def setUp(self):
        self.mysql = MySql()
        new_title = self.conf.get('project', 'new_title')
        new_title2 = new_title[:4] + str(int(new_title[4::1]) + 1)
        self.conf.set('project', 'new_title', new_title2)

    @data(*data_case)
    def test_loadadd(self, item):
        global result
        if hasattr(contex, 'COOKIES'):
            COOKIES = getattr(contex, 'COOKIES')
        else:
            COOKIES = None
        print(COOKIES)
        url = self.url + item['url']
        params = json.loads(DoRegex().replace(item['params']))
        if item['caseid'] > 1:
            params['title'] = self.conf.get('project', 'new_title')
        resp = Request(method=item['method'], url=url, data=params, cookies=COOKIES)
        if resp.cookies():
            COOKIES = setattr(contex,'COOKIES',resp.cookies())

        try:

            self.assertEqual(resp.get_txt(), item['excepted'])
            if resp.get_json()['msg'] == '加标成功':
                sql = 'SELECT * FROM future.loan WHERE MemberID = "{}" AND Title = "{}"'.format(
                    getattr(contex, 'normal_user_id'), params['title'])
                check_db = self.mysql.fet_one(sql=sql)
                self.assertEqual(check_db['Title'],params['title'])
            elif resp.get_json()['msg'] == '登录成功':
                print('这是登录')
            else:
                sql = 'SELECT * FROM future.loan WHERE MemberID = "{}" AND Title = "{}"'.format(
                    getattr(contex, 'normal_user_id'), params['title'])
                check_db = self.mysql.fet_one(sql=sql)
                self.assertEqual(check_db, None)
            result = 'Pass'
        except Exception as e:
            result = 'Failed'
            raise e
        finally:
            read.write_result('addloan', item['caseid'], resp.get_txt(), result)


