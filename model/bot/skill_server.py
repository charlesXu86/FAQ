# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   skill_server.py
 
@Time    :   2020/7/30 7:49 下午
 
@Desc    :  技能分发
 
"""

def get_skill(msg):
    """
    获取技能
    :param msg:
    :return:
    """
    if '天气' in msg:
        skill = '天气'
    elif '挂失' in msg:
        skill = '挂失'
    else:
        skill = '闲聊'

    return skill