# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 21:59
# @Author  : DannyDong
# @File    : Calculate.py
# @describe: 计算模块数据及逻辑处理

import copy


class CalculateMoney(object):
    def __init__(self):
        pass

    @staticmethod
    def calculation(unit_price, actual_price) -> dict:
        """
        计算实际购买商品价格
        :param unit_price: 商品原价
        :param actual_price: 商品实际支付总价格
        :return: result
        """
        unit_price_list = []
        for unit in unit_price:
            unit_price_list.append(float(unit['goodsPrice']))
        sum_price = sum(unit_price_list)
        num = unit_price_list.__len__()
        # 对unit_price深拷贝
        result = copy.deepcopy(unit_price)
        for i in range(num):
            proportion = float(unit_price_list[i] / sum_price)
            result[i]['res'] = '{:.2f}'.format(float(actual_price) * proportion)
        return result
