# -*- coding: utf-8 -*-

'''
@Author  :   Xu

@Software:   PyCharm

@File    :   payback_class_controller.py

@Time    :   2019-06-10 14:44

@Desc    :  添加日志

'''

from django.http import JsonResponse
import json
import logging
import datetime

from rest.Api.imanwser import get_imanwser, get_imanwser2

from rest.Api.LogUtils import Logger

logger = logging.getLogger(__name__)


def im_server(request):
    if request.method == 'GET':

        try:
            data = request.GET
            # jsonData = json.loads(request.GET)
            # question = jsonData["question"]
            question = request.GET.get('question')
            # tenantid = request.GET.get("tenantid", default='')
            # if "sessionid" in jsonData:
            #     sessionid = jsonData["sessionid"]
            # if "userid" in jsonData:
            #     userid = jsonData["userid"]
            # if "platform" in jsonData:
            #     platform = jsonData["platform"]
            # if "language" in jsonData:
            #     language = jsonData["language"]
            # if "userdata" in jsonData:
            #     userdata = jsonData["userdata"]
            localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = get_imanwser(question)
            dic = {
                "desc": "Success",
                "ques": question,
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


def im_server2(request):
    if request.method == 'POST':

        try:
            jsonData = json.loads(request.body.decode('utf-8'))
            msg = jsonData["message"]
            localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = get_imanwser2(msg)
            dic = {
                "desc": "Success",
                "ques": msg,
                "result": result,
                "time": localtime
            }
            log_res = json.dumps(dic, ensure_ascii=False)
            logger.info(log_res)
            return JsonResponse(dic, charset='utf-8')
        except Exception as e:
            logger.info(e)
    else:
        return JsonResponse({"desc": "Bad request"}, status=400)