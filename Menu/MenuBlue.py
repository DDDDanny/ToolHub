# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 0:48
# @Author  : DannyDong
# @File    : MenuBlue.py
# @describe: 菜单数据蓝图管理

from flask import Blueprint

from Common.ReCommon import Common
from Menu.Menu import menu_list


menu = Blueprint('menu', __name__)


@menu.route('/menu', methods=['GET'])
def get_menu_list():
    data = list()
    data.append(menu_list())
    return Common.success_json(data)
