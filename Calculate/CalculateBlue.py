# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 21:59
# @Author  : DannyDong
# @File    : CalculateBlue.py
# @describe: 计算模块蓝图管理

from flask import Blueprint, request

from Common.ReCommon import Common
from Calculate.Calculate import CalculateMoney

calc = Blueprint('calc', __name__)


@calc.route('/calculate/calcMoney', methods=['POST'])
def calc_money():
    form_data = eval(request.get_data(as_text=True))
    unit_price = form_data['unitPrice']
    actual_price = form_data['actualPrice']
    if unit_price == [] or actual_price == '':
        return Common.fail_json()
    else:
        res = CalculateMoney().calculation(unit_price, actual_price)
        return Common.success_json(res)
