# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   chatbot.py
 
@Time    :   2020/7/21 10:32 下午
 
@Desc    :   请求nlu接口，传到rasa
              intent{"slot": "slot_name"}
              intent    无实体情况
 
"""
import json
import os
import requests


def nlu(senderid,msg):
    """
    nlu
    :param senderid: 对话id
    :param msg: 用户query
    :return:
    """
    url1 = 'http://172.18.86.20:9007/api/intent'
    url2 = 'http://172.18.86.20:9007/api/cluener'
    params = {
        # "sender": senderid,
        "msg": msg
    }
    slot = {}
    response1 = requests.post(url=url1,data=json.dumps(params))
    intent = json.loads(response1.text)['result']     # 意图
    response2 = requests.post(url=url2, data=json.dumps(params))
    slots = json.loads(response2.text)['result']
    for one in slots:
        entity = one['entity']
        value = one['value']
        slot.update({entity:value})
    # 拼凑成rasa想要的格式
    final = intent + json.dumps(slot, ensure_ascii=False)
    bot_response = requestRasabotServer(senderid, final)
    utterance = json.loads(bot_response.text)

    return utterance


def requestRasabotServer(userid, content):
    """
        访问rasa服务
    :param userid: 用户id
    :param content: 自然语言文本
    :return:  json格式响应数据
    """
    params = {'sender': userid, 'message': content}
    botIp = '172.18.86.21'
    botPort = '9008'
    # rasa使用rest channel
    # https://rasa.com/docs/rasa/user-guide/connectors/your-own-website/#rest-channels
    # POST /webhooks/rest/webhook
    rasaUrl = "http://{0}:{1}/webhooks/rest/webhook".format(botIp, botPort)

    reponse = requests.post(
        rasaUrl,
        data=json.dumps(params),
        headers={'Content-Type': 'application/json'}
    )
    return reponse


if __name__=='__main__':
    senderId = '222224'
    msg = '明天'
    nlu(senderId, msg)




