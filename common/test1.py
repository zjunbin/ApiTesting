#  coding utf-8
# @time      :2019/3/1510:37
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test1.py
import configparser
import os
import time

# os.chdir("D:\\Python_config")

# cf = configparser.ConfigParser()
# cf.read('txt.conf')
#
# # add section / set option & key
# cf.add_section("test")
# cf.set("test", "count", 1)
# cf.add_section("test1")
# cf.set("test1", "name", "aaa")
#
# # write to file
# with open("txt.conf","w+") as f:
#     cf.write(f)

filename = r'I:\PycharmProjects\Day_01\api_testing\config' + '/'  + 'log.txt'+ time.strftime('%Y%m%d',time.localtime(time.time()))
print(filename)