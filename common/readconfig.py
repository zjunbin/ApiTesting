#  coding utf-8
# @time      :2019/3/1313:50
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :readconfig.py
import configparser
from common import constants
import os


class ReadConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        global_path = os.path.join(constants.config_path, 'global.conf')
        self.config.read(filenames=global_path, encoding='utf-8')
        # 获取全局配置 判断读取正式环境配置还是测试环境配置
        res = self.config.getboolean(section='swtich', option='on')
        if res == True:  # 读取正式环境配置
            self.online = os.path.join(constants.config_path, 'online.conf')
            self.config.read(filenames=self.online, encoding='utf-8')
        else:  # 读取测试环境配置
            testing = os.path.join(constants.config_path, 'test1.conf')
            self.config.read(filenames=testing, encoding='utf-8')

    def get(self, section, option):
        return self.config.get(section, option)

    def getint(self, section, option):
        return self.config.getint(section, option)

    def getboolean(self, section, option):
        return self.config.getboolean(section, option)

    def getfloat(self, section, option):
        return self.config.getfloat(section, option)

    def getstr(self, section, option):
        return eval(self.config.get(section, option))

    def set(self, section, option, value):
        self.config.set(section, option, value)
        with open(self.online, 'w+', encoding='utf-8') as f:
            self.config.write(f)

    def getoptions(self, options):
        return self.config.options(options)


if __name__ == '__main__':
    conf = ReadConfig()
    a = conf.get('project','new_title')
    print(a)
    a = a[:4]+str(int(a[4::1])+1)
    conf.set('project','new_title',a)
    print(a)