# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 21:17
# @Author  : DannyDong
# @File    : FakerDataBlue.py
# @describe: 随机生成数据蓝图管理

from flask import Blueprint, request

from Common.ReCommon import Common
from FakerData.FakerData import FakerData

faker = Blueprint('faker', __name__)


@faker.route('/faker/list', methods=['GET'])
def get_faker_list():
    data = FakerData().faker_random_list()
    return Common.success_json(data)


@faker.route('/faker/random', methods=['POST'])
def faker_random_data():
    faker_type = request.form.get('type')
    lang = request.form.get('lang')
    if faker_type == '1' or faker_type == '2':
        if lang is None or lang == 'zh_CN':
            data = FakerData().faker_random(int(faker_type))
        elif lang == 'en_US':
            data = FakerData('en_US').faker_random(int(faker_type))
        else:
            return Common.fail_json()
        return Common.success_json(data)
    else:
        return Common.fail_json()
