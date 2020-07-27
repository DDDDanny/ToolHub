# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 21:18
# @Author  : DannyDong
# @File    : FakerData.py
# @describe: 随机生成数据逻辑处理

import datetime
from random import Random

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
            {"id": 101, "catName": "地址"},
            {"id": 102, "catName": "手机号"},
            {"id": 103, "catName": "日期时间"},
            {"id": 104, "catName": "更多"},
        ]
        return self.faker_list

    # 实现FakerData
    def faker_random(self, faker_id, attr):
        # res 用于存储假数据生成的结果
        res = ''
        # 生成随机姓名
        if faker_id == '100':
            if attr['lastName'] == '' and attr['firstName'] == '':
                res = self.faker_obj.name()
            elif attr['lastName'] != '' and attr['firstName'] == '':
                res = attr['lastName'] + self.faker_obj.first_name()
            elif attr['lastName'] == '' and attr['firstName'] != '':
                res = self.faker_obj.last_name() + attr['firstName']
            else:
                res = attr['lastName'] + attr['firstName']
        # 生成随机地址
        elif faker_id == '101':
            attr['country'] = self.faker_obj.country() if attr['country'] == '' else attr['country']  # 生成国家
            attr['province'] = self.faker_obj.province() if attr['province'] == '' else attr['province']  # 生成省
            attr['city'] = self.faker_obj.city() if attr['city'] == '' else attr['city']  # 生成市
            attr['district'] = self.faker_obj.district() if attr['district'] == '' else attr['district']  # 生成地区
            attr['street'] = self.faker_obj.street_name() if attr['street'] == '' else attr['street']  # 生成街道
            attr['building'] = self.faker_obj.building_number() if attr['building'] == '' else attr['building']  # 生成楼
            attr['postcode'] = self.faker_obj.postcode() if attr['postcode'] == '' else attr['postcode']  # 生成邮编
            address_list = attr.values()
            print(address_list)
            for address in address_list:
                res += address
        # 生成随机电话号码
        elif faker_id == '102':
            if attr['prefix'] == '':
                res = self.faker_obj.phone_number()
            else:
                res = attr['prefix'] + self.faker_obj.phone_number()[3:]
        # 生成随机日期时间
        elif faker_id == '103':
            attr['year'] = self.faker_obj.year() if attr['year'] == '' else attr['year']
            attr['month'] = self.faker_obj.month() if attr['month'] == '' else attr['month']
            attr['day'] = self.faker_obj.day_of_month() if attr['day'] == '' else attr['day']
            attr['hour'] = str(Random().randint(0, 23)).zfill(2) if attr['hour'] == '' else attr['hour']
            attr['minute'] = str(Random().randint(0, 59)).zfill(2) if attr['minute'] == '' else attr['minute']
            attr['seconds'] = str(Random().randint(0, 59)).zfill(2) if attr['seconds'] == '' else attr['seconds']
            date_str = attr['year'] + '-' + attr['month'] + '-' + attr['day']
            time_str = attr['hour'] + ':' + attr['minute'] + ':' + attr['seconds']
            week_list = [
                '星期日（Sunday）', '星期一（Monday）', '星期二（Tuesday）', '星期三（Wednesday）',
                '星期四（Thursday）', '星期五（Friday）', '星期六（Saturday）', '无此日（No such day）'
            ]
            try:
                week = int(datetime.datetime(int(attr['year']), int(attr['month']), int(attr['day'])).strftime('%w'))
            except Exception:
                week = 7
            res = date_str + ' ' + time_str + ' ' + week_list[week]
        return {'result': res}
