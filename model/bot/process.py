# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   process.py
 
@Time    :   2020/7/26 10:32 上午
 
@Desc    :
 
"""

import re

def data_process(msg):
    """
    对用户query进行预处理
    :param msg:
    :return:
    """
    msg = msg.strip()
    if msg.startswith('你好') and len(msg) > 8:
        msg = msg.replace('你好', '')
    num = re.findall(r'\d+', msg)
    if num:
        if len(num[0]) > 5:
            msg = '卡号是:' + msg
    return msg

if __name__=='__main__':
    msg = '131231233'
    data_process(msg)