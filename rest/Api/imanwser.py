# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   anwser.py
 
@Time    :   2020/7/11 6:17 下午
 
@Desc    :
 
"""
from model.FAQ import FAQ


def get_imanwser(msg):

    result = {
        'domain':'',
        'anwser':''
    }

    robot = FAQ(usedVec=False)

    anwser = robot.answer(msg, 'simple_pos')

    result['user_query'] = msg
    result['anwser'] = anwser

    return result