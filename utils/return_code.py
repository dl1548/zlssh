#!/usr/bin python
# -*- coding: utf-8 -*-
'''
@File    :   code.py
@Time    :   2020/02/15 22:19:23
'''

class CodeError(Exception):
    pass

class Code(object):

    code_msg = {
        1000: 'success',                         # 成功只一种,失败变化无穷
        1001: 'fail',                            # 返回数据格式有误
        1002: 'try exception',                   # try exception 异常
        1003: '内部空值',                         # 空值
        1004: 'api result is empty.',            # api 结果为空
        1005: 'parameter error',                 # 请求成功
        1006: 'xxxx',                            # 请求失败
        1007: 'exist',                           # 已存在
        9999: 'unknown error '                   # 未归类的报错
    }

def zlreturn(code, data='', **kwargs):
    """code
        1000: 'success',
        1001: 'fail',
        1002: 'try exception',
        1003: '内部空值'
        1004: 'api result is empty.'
        1005: 'parameter error',
        1006: 'xxxx'
        1007: 'exist'
        9999: 'unknown error '
    """
    if code in Code.code_msg.keys():
        message = Code.code_msg[code]
    else:
        raise CodeError('code undefined')

    return_data = dict()
    return_data['role'] = ''
    return_data['code'] = code
    return_data['data'] = data
    return_data['message'] = message

    if not kwargs:
        return return_data
    else:
        for key,val in kwargs.items():
            return_data[key] = val
        return return_data
