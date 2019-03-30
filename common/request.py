#  coding utf-8
# @time      :2019/3/119:10
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :request.py
import requests
from common.mylog import MyLog

mylog = MyLog()
class Request:
    def __init__(self, method, url, data, cookies = None):

        if method == 'get':
            try:
                self.resp = requests.get(url=url, params=data)
            except AttributeError as e:
                mylog.error(e)
                raise e
        elif method == 'post':
            try:
                self.resp = requests.post(url=url, data=data ,cookies = cookies)
            except AttributeError as e:
                mylog.error(e)
                raise e
        elif method == 'delete':
            try:
                self.resp = requests.delete(url=url, param=data)
            except AttributeError as e:
                mylog.error(e)
                raise e
        else:
            print('None')

    def get_txt(self):
        return self.resp.text

    def get_json(self):
        return self.resp.json()

    def cookies(self):
        return  self.resp.cookies

    def status_code(self):
        return self.resp.status_code

if __name__ == '__main__':
    url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    # url3 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
    # url2 = 'http://47.107.168.87:8080/futureloan/mvc/api/loan/add'
    url4 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/bidLoan'
    # url5 = 'http://47.107.168.87:8080/futureloan/mvc/api/loan/audit'

    params = {"mobilephone":"13822221113","pwd":"123456"}
    # data = {"mobilephone": "13566666666", "amount": "30"}
    # data = {"memberId":"1125830","title":"买房","amount":"300000","loanRate":"20","loanTerm":"12","loanDateType":"0","repaymemtWay":"4","biddingDays":"10"}
    # data =   {'loanTerm': '12', 'loanDateType': '2', 'amount': '30000', 'loanRate': '18.0', 'biddingDays': '5', 'title': '买飞机', 'loanid_user_id': '1126396', 'repaymemtWay': '4'}
    # data2= {"id":"17659","status":"4"}
    data3 ={"memberId":"1126396","password":"123456","loanId":"17659","amount":"999"}
    # data3 = {"mobilephone":"13822221113","amount":"500000"}
    re = requests.session()
    resp = re.request(method='get',url=url,params=params)
    print(resp.text)
    resp2 =re.request(method='post',url=url4,data=data3)
    print(resp2.text)