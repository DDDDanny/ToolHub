# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 0:50
# @Author  : DannyDong
# @File    : Menu.py
# @describe: 菜单数据逻辑处理


# FakerData Menu
def menu_faker_list():
    menu_data = {
        'nodeName': 'FakerData',
        'iconName': 'mdi-alpha-f-box',
        'path': None,
        'children': [
            {
                'nodeName': '生成随机数据',
                'iconName': 'mdi-creation',
                'path': '/faker/dataGenerate',
            },
            {
                'nodeName': '导出随机数据',
                'iconName': 'mdi-file-export',
                'path': '/faker/dataExport',
            },
        ]
    }
    return menu_data


# About Menu
def menu_about_list():
    menu_data = {
        'nodeName': 'About',
        'iconName': 'mdi-information',
        'path': None,
        'children': [
            {
                'nodeName': 'About ToolHub',
                'iconName': 'mdi-thought-bubble-outline',
                'path': '/about/toolHub',
            },
            {
                'nodeName': 'About Me',
                'iconName': 'mdi-emoticon-lol-outline',
                'path': '/about/me',
            }
        ]
    }
    return menu_data


# SecretCode Menu
def menu_secret_list():
    menu_data = {
        'nodeName': 'SecretCode',
        'iconName': 'mdi-shield-key',
        'path': None,
        'children': [
            {
                'nodeName': '数据加密',
                'iconName': 'mdi-lock',
                'path': '/secretCode/encrypt',
            },
            {
                'nodeName': '数据解密',
                'iconName': 'mdi-lock-open-variant',
                'path': '/secretCode/decrypt',
            }
        ]
    }
    return menu_data
