# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 20:08
# @Author  : DannyDong
# @File    : ExportData.py
# @describe: 数据导出相关逻辑

import io
import random

from faker import Faker
from xlsxwriter import *
from flask import send_file


class ExportData(object):
    def __init__(self):
        self.faker_obj = Faker("zh_CN")

    def create_workbook(self, param_list: list, param_num: str):
        try:
            data_num = int(param_num)
        except Exception as error:
            return error
        fp = io.BytesIO()
        book = Workbook(fp)
        sheet = book.add_worksheet('FakerData Export')
        if param_list.__len__() == 0:
            pass
        else:
            for i in range(param_list.__len__()):
                sheet.write(0, i, param_list[i])
                if param_list[i] == '姓名':
                    for num in range(data_num):
                        name = self.faker_obj.name()
                        sheet.write(num + 1, i, name)
                elif param_list[i] == '性别':
                    for num in range(data_num):
                        gender = random.choice(['男', '女'])
                        sheet.write(num + 1, i, gender)
                elif param_list[i] == '电话':
                    for num in range(data_num):
                        phone = self.faker_obj.phone_number()
                        sheet.write(num + 1, i, phone)
                elif param_list[i] == '地址':
                    for num in range(data_num):
                        address = self.faker_obj.address()
                        sheet.write(num + 1, i, address)
                else:
                    pass
        book.close()
        return fp

    def download(self, param_list: list, data_num: str):
        fp = self.create_workbook(param_list, data_num)
        fp.seek(0)
        return send_file(fp, attachment_filename="testing.xlsx", as_attachment=True)
