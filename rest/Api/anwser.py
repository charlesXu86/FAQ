# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   anwser.py
 
@Time    :   2020/7/11 6:17 下午
 
@Desc    :
 
"""
from model.FAQ import FAQ


def get_anwser(msg):
    result = {
        'domain': '',
        'content': '',
        'type': 0,
        'classId': 0,
        'confidence': 0.978787,
        'errorTime': 0,
        'questionId': 0,
        'transferFlag': 0,
        'relatedQuestion': [],
        'questionList': [],
        'link': 'zrg'
    }

    robot = FAQ(usedVec=False)

    anwser = robot.answer(msg, 'simple_pos')

    # result['user_query'] = msg
    result['content'] = anwser

    return anwser
