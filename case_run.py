#  coding utf-8
# @time      :2019/3/1115:55
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :case_run.py
import HTMLTestRunnerNew
import unittest

from api_testing.common import constants
from api_testing.common import test_login,test_register,test_bidLoan,test_loadadd,test_recharge,test_withdraw

suite = unittest.TestSuite()
loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(Login))
suite.addTest(loader.loadTestsFromModule(test_login))
suite.addTest(loader.loadTestsFromModule(test_register))
suite.addTest(loader.loadTestsFromModule(test_recharge))
suite.addTest(loader.loadTestsFromModule(test_withdraw))
suite.addTest(loader.loadTestsFromModule(test_loadadd))
suite.addTest(loader.loadTestsFromModule(test_bidLoan))
with open(constants.result_path, 'wb+') as file:
    run = HTMLTestRunnerNew.HTMLTestRunner(file)
    run.run(suite)

