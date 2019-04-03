#  coding utf-8
# @time      :2019/3/1115:55
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :case_run.py
import HTMLTestRunnerNew
import sys
import unittest
from common import constants
from cases import test_login,test_register ,test_bidLoan,test_loadadd,test_withdraw,test_recharge
# discover = unittest.defaultTestLoader.discover(r'D:\api_testing\cases','test_*.py',top_level_dir=None)
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_login))
suite.addTest(loader.loadTestsFromModule(test_register))
suite.addTest(loader.loadTestsFromModule(test_recharge))
suite.addTest(loader.loadTestsFromModule(test_withdraw))
suite.addTest(loader.loadTestsFromModule(test_loadadd))
suite.addTest(loader.loadTestsFromModule(test_bidLoan))
with open(constants.result_path, 'wb+') as file:
    run = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title='testing',
                                           tester='admin')
    run.run(suite)

