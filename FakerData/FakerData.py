# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 21:18
# @Author  : DannyDong
# @File    : FakerData.py
# @describe: 随机生成数据逻辑处理

from faker import Faker


class FakerData(object):
    def __init__(self, lang='zh_CN'):
        self.faker_list = []
        if lang == 'zh_CN':
            self.faker_obj = Faker("zh_CN")
        else:
            self.faker_obj = Faker("en_US")

    # 获取FakerList（Base）
    def faker_data_list_base(self):
        self.faker_list = [
            {"id": 100, "catName": "姓名"},
            {"id": 101, "catName": "年龄"},
            {"id": 102, "catName": "地址"},
            {"id": 103, "catName": "颜色"},
            {"id": 104, "catName": "车牌号"},
            {"id": 105, "catName": "公司名称"},
        ]
        return self.faker_list

    # 实现FakerData
    def faker_random(self, faker_id, attr):
        # res 用于存储假数据生成的结果
        res = ''
        if faker_id == '100':
            if attr['lastName'] == '' and attr['firstName'] == '':
                res = self.faker_obj.name()
            elif attr['lastName'] != '' and attr['firstName'] == '':
                res = attr['lastName'] + self.faker_obj.first_name()
            elif attr['lastName'] == '' and attr['firstName'] != '':
                res = self.faker_obj.last_name() + attr['firstName']
            else:
                res = attr['lastName'] + attr['firstName']
        return {'result': res}
