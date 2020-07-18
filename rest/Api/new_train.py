# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   new_train.py
 
@Time    :   2020/7/12 4:08 下午
 
@Desc    :   新技能训练
 
"""
from django.http import JsonResponse
import json
import logging
import datetime

from model.train.train_skill import train_skill

logger = logging.getLogger(__name__)


def train_model(request):
    if request.method == 'POST':

        try:
            jsonData = json.loads(request.body.decode('utf-8'))

            skillId = jsonData["robotTechnologyAbilityId"]
            localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = train_skill(skillId)
            results = "正在训练"
            dic = {
                "desc": "Success",
                "ques": skillId,
                "result": results,
                "time": localtime
            }
            log_res = json.dumps(dic, ensure_ascii=False)
            logger.info(log_res)
            return JsonResponse(dic)
        except Exception as e:
            logger.info(e)
    else:
        return JsonResponse({"desc": "Bad request"}, status=400)