# -*- coding: utf-8 -*-
# @Time    : 2020/9/20 17:22
# @Author  : DannyDong
# @File    : FormatInfoBlue.py
# @describe: 格式化信息蓝图管理

from flask import Blueprint, request

from Common.ReCommon import Common
from FormatInfo.FormatJson import FormatJson

formatInfo = Blueprint('formatInfo', __name__)


# 格式化Json
@formatInfo.route('/format/json', methods=['POST'])
def format_json():
    form_data = eval(request.get_data(as_text=True))
    json_str = form_data['jsonStr']
    if json_str == '':
        return Common.fail_json()
    else:
        res = FormatJson().format_json(json_str)
        return Common.success_json(res)
