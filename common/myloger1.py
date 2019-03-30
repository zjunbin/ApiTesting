#  coding utf-8
# @time      :2019/3/1816:59
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :myloger1.py
import logging
from common.readconfig import ReadConfig
from common import constants
import time

mylog = logging.Logger('mylog')
mylog.setLevel('DEBUG')
mylog.setLevel(ReadConfig().get('testconfig', 'log_level'))
# log_path 日志的存放路径和文件名称
log_path = constants.log_path
filename = log_path + time.strftime('%Y%m%d',time.localtime(time.time()))
fh = logging.FileHandler(filename,'a+',encoding='utf-8')
# 获取配置文件中的文件日志输出级别
fh.setLevel(ReadConfig().get('testconfig', 'fh_level'))
# 获取配置文件中的日志输出格式
formatter = logging.Formatter(ReadConfig().get('testconfig', 'Formatter'))
fh.setFormatter(formatter)
# 对接日志收集器
mylog.addHandler(fh)