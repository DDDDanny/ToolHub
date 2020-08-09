# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 21:20
# @Author  : DannyDong
# @File    : ReCommon.py
# @describe: 请求返回Common

from flask import jsonify


class Common:
    @staticmethod
    def success_json(data, msg="请求成功") -> object:
        return jsonify({
            "data": data,
            "meta": {
                "status": 200,
                "msg": msg
            }
        })

    @staticmethod
    def fail_json(msg="参数错误") -> object:
        return jsonify({
            "data": 0,
            "meta": {
                "status": 205,
                "msg": msg
            }
        })
