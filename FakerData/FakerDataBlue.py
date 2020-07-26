# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 21:17
# @Author  : DannyDong
# @File    : FakerDataBlue.py
# @describe: 随机生成数据蓝图管理

from flask import Blueprint, request

from Common.ReCommon import Common
from FakerData.FakerData import FakerData

faker = Blueprint('faker', __name__)


@faker.route('/faker/list/base', methods=['GET'])
def get_faker_list():
    data = FakerData().faker_data_list_base()
    return Common.success_json(data)


@faker.route('/faker/random', methods=['POST'])
def faker_random_data():
    form_data = eval(request.get_data(as_text=True))
    print(form_data)
    faker_cat = form_data['cat']
    print(faker_cat)
    attr = form_data['attr']
    # faker_cat = request.form.get('cat')
    # attr = request.form.get('attr')
    # attr = eval(attr)

    if faker_cat == '' or attr == '':
        return Common.fail_json()
    else:
        res = FakerData().faker_random(faker_cat, attr)
        return Common.success_json(res)
