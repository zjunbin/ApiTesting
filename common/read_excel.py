#  coding utf-8
# @time      :2019/3/1111:53
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :read_excel.py
import openpyxl
from api_testing.common.mylog import MyLog
from api_testing.common import constants
data_file = constants.data_case
mylog = MyLog()

data_list = []
class ReadExcel:


    def __init__(self):
        try:
            self.file_name = data_file
            self.workbook = openpyxl.load_workbook(filename=data_file)
        except Exception as e:
            mylog.error(e)
            raise e
    #获取测试用例
    def read_excel(self, sheet_name):
        sheet = self.workbook[sheet_name]
        max_row = sheet.max_row
        for i in range(2, max_row + 1):
            data_dict = {}
            for j in range(1, sheet.max_column - 1):
                data_dict[sheet.cell(1, j).value] = sheet.cell(i, j).value
            data_list.append(data_dict)
        return data_list

    # 方法一：会写测试结果
    def check_db(self, sheet_name, row, column, value):
        try:
            sheet = self.workbook[sheet_name]
        except Exception as e:
            mylog.error(e)
            raise e
        sheet.cell(row,column).value = value
        self.workbook.save(self.file_name)
        self.workbook.close()

    #  方法二
    def write_result(self, sheet_name, caseid, actual, result):
        try:
            sheet = self.workbook[sheet_name]
        except Exception as e:
            mylog.error(e)
            raise e
        max_row = sheet.max_row
        for i in range(2, max_row + 1):
            if caseid == sheet.cell(i, 1).value:
                sheet.cell(i, 7).value = actual
                sheet.cell(i, 8).value = result
                self.workbook.save(self.file_name)
                self.workbook.close()
                break


if __name__ == '__main__':
    wb = ReadExcel()
    data_list = wb.read_excel('login')
    # wb.write_result('login',3,'aa','bb')
    print(data_list)
