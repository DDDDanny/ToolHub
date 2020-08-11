# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 20:08
# @Author  : DannyDong
# @File    : ExportData.py
# @describe: 数据导出相关逻辑

import io
from xlsxwriter import *
from flask import send_file


def create_workbook(param_list: list):
    fp = io.BytesIO()
    book = Workbook(fp)
    sheet = book.add_worksheet('FakerData Export')
    if param_list.__len__() == 0:
        pass
    else:
        for i in range(param_list.__len__()):
            sheet.write(0, i, param_list[i])
            if param_list[i] == '姓名':
                pass
            elif param_list[i] == '性别':
                pass
            elif param_list[i] == '电话':
                pass
            else:
                pass
    book.close()
    return fp


def download(param_list):
    fp = create_workbook(param_list)
    fp.seek(0)
    return send_file(fp, attachment_filename="testing.xlsx", as_attachment=True)
