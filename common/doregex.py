#  coding utf-8
# @time      :2019/3/149:44
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :doregex.py
import re
from api_testing.common.readconfig import ReadConfig

conf = ReadConfig()

class contex:
    normal_user = conf.getstr('test_user','normal_user')['user']
    normal_pwd = conf.getstr('test_user','normal_user')['pwd']
    admin_user = conf.getstr('test_user', 'admin_user')['user']
    admin_pwd = conf.getstr('test_user', 'admin_user')['pwd']
    loanid_user = conf.getstr('test_user', 'loanid_user')['user']
    loanid_pwd = conf.getstr('test_user', 'loanid_user')['pwd']
    title = conf.get('project','title')
    amount = conf.get('project','amount')
    # loanid = conf.get('project', 'loanid')
    sql = conf.get('sql','sql')
    # new_title = conf.get('project','new_title')


class DoRegex:
    def replace(self, data):
        res = re.findall('\$\{(.*?)\}', data)
        for item in res:
            value = getattr(contex, item)
            data = re.sub('\$\{(.*?)\}', value, data, count=1)
        return data
        # p = '\$\{(.*?)\}'
        # while re.search(p,data):
        #     m = re.search(p,data)
        #     key = m.group(1)
        #     data = re.sub(p,getattr(contex,key),data,count=1)
        # return data
if __name__ == '__main__':
    # import json
    doRe = DoRegex()
    data = '{"memberId":"${normal_user}","title":"${loanid_user}","amount":"${admin_user}","loanRate":"18.0","loanTerm":"12","loanDateType":"0","repaymemtWay":"4","biddingDays":"5"}'
    res =doRe.replace(data=data)
    print(res)
    # data = json.loads(res)
    # data['amount'] =int(data['amount'])+1
    # print(data)
    # sql = 'SELECT Id from future.member WHERE MobilePhone = "{0}"'.format(contex,'admin_user')
    # print(getattr(contex,'sql'))
    # from api_testing.common.mysql import MySql
    # mysql = MySql()
    # value = mysql.fet_one(sql)
    # print(value)