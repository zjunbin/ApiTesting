#  coding utf-8
# @time      :2019/3/1314:44
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :mylog.py
import logging
from api_testing.common.readconfig import ReadConfig
from api_testing.common import constants
import time
class MyLog:

    def mylog(self,msg_level, msg):
        mylog = logging.Logger('mylog')
        # 获取日志收集器级别
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
        if msg_level == 'DEBUG':
            mylog.debug(msg)
        elif msg_level == 'INFO':
            mylog.info(msg)
        elif msg_level == 'WARNING':
            mylog.warning(msg)
        elif msg_level == 'ERROR':
            mylog.error(msg)
        elif msg_level == 'CRITICAL':
            mylog.critical(msg)
        # 使用完后移除渠道，减少重复日志

        mylog.removeHandler(fh)


    def debug(self,msg):
        self.mylog('DEBUG',msg)

    def info(self, msg):
        self.mylog('INFO', msg)

    def warning(self, msg):
        self.mylog('WARNING', msg)

    def error(self, msg):
        self.mylog('ERROR', msg)

    def critical(self, msg):
        self.mylog('CRITICAL', msg)


if __name__ == '__main__':
    mylog = MyLog()
    mylog.debug('haha')
    mylog.info('hehe')