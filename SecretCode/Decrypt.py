# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 20:05
# @Author  : DannyDong
# @File    : Decrypt.py
# @describe: 数据解密处理

import base64


class Decrypt(object):
    def __init__(self, wait_str):
        self.waiting_str = wait_str

    # Base64编码
    def base64_code(self):
        new_str = self.waiting_str.encode('utf-8')  # 需要转成bytes字节符
        new_str = base64.b64decode(new_str)
        return new_str.decode()


# 处理数据解密业务
def go_decrypt(cate, wait_str):
    init_obj = Decrypt(wait_str)
    # cate=1: Base64;
    if cate == '1':
        res = init_obj.base64_code()
    else:
        raise {'result': '加密类型选择错误'}
    return {'result': res}


if __name__ == '__main__':
    print(go_decrypt('1', 'V2FpdGluZyBTdHJpbmc='))
