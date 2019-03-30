#  coding utf-8
# @time      :2019/3/1815:07
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :mysql.py
import pymysql
from api_testing.common.doregex import *

conf = ReadConfig()

class MySql:
    def __init__(self):
        host = conf.get('mysql', 'host')
        user = conf.get('mysql', 'user')
        password = conf.get('mysql', 'pwd')
        port = conf.getint('mysql', 'port')
        cursorclass = pymysql.cursors.DictCursor
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port,cursorclass= cursorclass)


    def fet_one(self, sql):
        cursor = self.mysql.cursor()
        try:
            cursor.execute(sql)
        except Exception as e:
            raise e
        return cursor.fetchone()

    def fet_all(self, sql):
        cursor = self.mysql.cursor()
        try:
            cursor.execute(sql)
        except Exception as e:
            raise e
        return cursor.fetchall()

    def mysql_close(self):
        return self.mysql.close()

if __name__ == '__main__':
    mysql = MySql()
    sql = 'SELECT l.Id AS Id ,l.Amount AS Amount from future.member  m LEFT JOIN future.loan l \
        ON m.Id = l.MemberID WHERE m.MobilePhone = "13822221112" AND Title= "买飞机" AND Status < 4'
    value =mysql.fet_one(sql)
    print(value)