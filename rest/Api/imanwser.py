# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   imanwser.py
 
@Time    :   2020/7/11 6:17 下午
 
@Desc    :
 
"""
from model.FAQ import FAQ


def get_imanwser(msg):
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

    robotUserData = {
        "showEvaluate": 0,
        "answer_type": "faq",
        "is_many_answer": False,
        "highLight": 0,  # 是否需要前端进行高亮显示，一般在触发敏感词严重时会触发。
        "sensitive_hit": "警告",  # 敏感词，触发了哪个敏感词就列出来
        "docid": 260801,
        "search_id": "2156_1001_594726674",  # 机器人标准问的Id，用于对机器人进行评价
        "raw_query": ""
    }

    robot = FAQ(usedVec=False)

    anwser = robot.answer(msg, 'simple_pos')

    result['user_query'] = msg
    robotUserData['raw_query'] = msg
    result['content'] = anwser
    result['robotUserData'] = robotUserData

    return result