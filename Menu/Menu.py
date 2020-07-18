# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 0:50
# @Author  : DannyDong
# @File    : Menu.py
# @describe: 菜单数据逻辑处理


def menu_list():
    menu_data = {
        'nodeName': 'FakerData',
        'iconName': 'mdi-alpha-f-box',
        'path': None,
        'children': [
            {
                'nodeName': '基础类 (Base)',
                'iconName': 'mdi-creation',
                'path': '/faker/base',
            },
            {
                'nodeName': '人物类 (Human)',
                'iconName': 'mdi-account-heart',
                'path': '/faker/human',
            },
            {
                'nodeName': '地址类 (Address)',
                'iconName': 'mdi-directions-fork',
                'path': '/faker/address',
            },
            {
                'nodeName': '金融类 (Finance)',
                'iconName': 'mdi-currency-usd-circle',
                'path': '/faker/finance',
            },
            {
                'nodeName': '其他类 (Other)',
                'iconName': 'mdi-cards-heart',
                'path': '/faker/other',
            },
        ]
    }
    return menu_data