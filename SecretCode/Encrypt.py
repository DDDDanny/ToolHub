# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 20:05
# @Author  : DannyDong
# @File    : Encrypt.py
# @describe: 数据加密处理

import hmac
import base64
import hashlib


# 加密算法
class Encrypt(object):
    def __init__(self, wait_str):
        self.waiting_str = wait_str

    # Base64编码
    def base64_code(self) -> str:
        new_str = self.waiting_str.encode('utf-8')  # 需要转成bytes字节符
        new_str = base64.b64encode(new_str)
        return new_str.decode()

    # MD5加密（message-digest algorithm 5 信息-摘要算法）
    def md5_encrypt(self, salt_str) -> str:
        md5_obj = hashlib.md5(bytes(salt_str, encoding='utf-8'))  # 加盐后会在原md5加密上再进行一次加密
        md5_obj.update(self.waiting_str.encode('utf-8'))  # 需要转成bytes字节符
        return md5_obj.hexdigest()

    # hmac加密（hex-based message authentication code 哈希消息认证码）
    def hmac_encrypt(self, salt_str) -> str:
        salt = bytes(salt_str, encoding='utf-8')
        hmac_obj = hmac.new(salt, self.waiting_str.encode('utf-8')).hexdigest()
        return hmac_obj

    # sha1加密（Secure Hash Algorithm 安全哈希算法）
    def sha1_encrypt(self, salt_str) -> str:
        """
        sha1加密是基于MD5，加密后的数据会更长，相对于MD5会更加安全，但是运算速度会更慢
        """
        sha1_obj = hashlib.sha1(bytes(salt_str, encoding='utf-8'))  # 加盐后会在原sha1加密上再进行一次加密
        sha1_obj.update(self.waiting_str.encode('utf-8'))  # 需要转成bytes字节符
        return sha1_obj.hexdigest()


# 处理数据加密业务
def go_encrypt(cate, wait_str, salt) -> dict:
    init_obj = Encrypt(wait_str)
    # cate=1: Base64; cate=2: MD5; cate=3: HMAC; cate=4: SHA1;
    if cate == '1':
        res = init_obj.base64_code()
    elif cate == '2':
        res = init_obj.md5_encrypt(salt)
    elif cate == '3':
        res = init_obj.hmac_encrypt(salt)
    elif cate == '4':
        res = init_obj.sha1_encrypt(salt)
    else:
        raise {'result': '加密类型选择错误'}
    return {'result': res}


if __name__ == '__main__':
    x = Encrypt('admin').base64_code()
    print(x)
    print(type(x))
