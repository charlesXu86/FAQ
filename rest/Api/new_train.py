# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   new_train.py
 
@Time    :   2020/7/12 4:08 下午
 
@Desc    :
 
"""
from django.http import JsonResponse
import json
import logging
import datetime

logger = logging.getLogger(__name__)


def train_model(request):
    if request.method == 'POST':

        try:
            jsonData = json.loads(request.body.decode('utf-8'))

            msg = jsonData["skill"]
            localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = 'train ok'
            dic = {
                "desc": "Success",
                "ques": msg,
                "result": result,
                "time": localtime
            }
            log_res = json.dumps(dic, ensure_ascii=False)
            logger.info(log_res)
            return JsonResponse(dic)
        except Exception as e:
            logger.info(e)
    else:
        return JsonResponse({"desc": "Bad request"}, status=400)