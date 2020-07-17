# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 21:18
# @Author  : DannyDong
# @File    : FakerData.py
# @describe: 随机生成数据逻辑处理

from faker import Faker


class FakerData(object):
    def __init__(self, lang='zh_CN'):
        self.faker_list = ['姓名', '地址']
        if lang == 'zh_CN':
            self.faker_obj = Faker("zh_CN")
        else:
            self.faker_obj = Faker("en_US")

    # 获取FakerList
    def faker_random_list(self):
        return self.faker_list

    # 实现FakerData
    def faker_random(self, faker_id):
        res = ''
        if faker_id == 0:
            res = self.faker_obj.name()
        elif faker_id == 1:
            res = self.faker_obj.address()
        return {'result': res}
