#  coding utf-8
# @time      :2019/3/129:46
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :constants.py

import os
import time
# 项目根目录
path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# 全局配置文件路径
globals_path=os.path.join(path,'config')
# config 配置文件目录
config_path=os.path.join(path,'config')
# 日志输出路径和名称
log_path =os.path.join(path,'logs','log.log')
# 测试用例存放路径和名称
data_case = os.path.join(path,'datas','api_case.xlsx')
# 测试报告存放
result_path = os.path.join(path,'result',time.strftime("%Y-%m-%d") + '_report.html')
if __name__ == '__main__':
    print(path)