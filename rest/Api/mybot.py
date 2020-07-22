# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   chatbot.py
 
@Time    :   2020/7/22 9:58 上午
 
@Desc    :
 
"""

from django.http import JsonResponse
import json
import logging
import datetime

from model.bot.dst import nlu

logger = logging.getLogger(__name__)

filled_slot = {}

def mybot(request):
    if request.method == 'POST':

        try:
            jsonData = json.loads(request.body.decode('utf-8'))

            senderId = jsonData["sender"]
            message = jsonData["message"]
            localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = nlu(senderId, message, filled_slot)
            dic = {
                "desc": "Success",
                "ques": message,
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