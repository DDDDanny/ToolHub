# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 20:06
# @Author  : DannyDong
# @File    : SecretCodeBlue.py
# @describe: 密码相关蓝图管理

from flask import Blueprint, request

from Common.ReCommon import Common
from SecretCode.Encrypt import go_encrypt
from SecretCode.Decrypt import go_decrypt

secretCode = Blueprint('secretCode', __name__)


@secretCode.route('/secretCode/goEncrypt', methods=['POST'])
def code_encrypt():
    form_data = eval(request.get_data(as_text=True))
    print(form_data)
    cate = form_data['cate']
    wait_str = form_data['waitStr']
    salt = form_data['salt']

    if cate == '' or wait_str == '':
        return Common.fail_json()
    else:
        if cate != '1' and salt == '':
            return Common.fail_json()
        else:
            res = go_encrypt(cate, wait_str, salt)
            return Common.success_json(res)


@secretCode.route('/secretCode/goDecrypt', methods=['POST'])
def code_decrypt():
    form_data = eval(request.get_data(as_text=True))
    print(form_data)
    cate = form_data['cate']
    wait_str = form_data['waitStr']
    if cate == '' or wait_str == '':
        return Common.fail_json()
    else:
        res = go_decrypt(cate, wait_str)
        return Common.success_json(res)
