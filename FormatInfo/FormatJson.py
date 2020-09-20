# -*- coding: utf-8 -*-
# @Time    : 2020/9/20 00:20
# @Author  : DannyDong
# @File    : FormatJson.py
# @describe: 格式化Json数据

import json


class FormatJson(object):
    def __init__(self):
        pass

    @staticmethod
    def format_json(json_str: str) -> dict:
        length = json_str.__len__()
        if length > 50000:
            return {'result': 'Json数据超过50000个字符，长度过长，请重新输入。。。😉'}
        try:
            mk_dict = json.loads(json_str)
        except Exception:
            return {'result': '输入的非Json格式的字符串，无法格式化！😑'}
        res = json.dumps(mk_dict, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)
        return {'result': res}


if __name__ == '__main__':
    pass
