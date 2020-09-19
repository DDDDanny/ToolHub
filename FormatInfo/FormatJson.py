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
    def format_json(json_str: str):
        length = json_str.__len__()
        if length > 50000:
            return {'result': 'Json数据过长，无法处理'}
        special_key = ['\n', '\r', '\t']

        new_json = json_str
        if any(key in json_str for key in special_key):
            new_json = json_str.replace('\n', '').replace('\r', '').replace('\t', '')
        mk_dict = eval(new_json)
        res = json.dumps(mk_dict, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)
        return {'result': res}


if __name__ == '__main__':
    pass
