# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   dst.py
 
@Time    :   2020/7/22 11:19 上午
 
@Desc    :   对话状态
 
"""
import requests
import json
import datetime

from model.bot.time_utils import get_time_unit
from model.bot.process import data_process
from model.service.weather_api.seniverse import SeniverseWeatherAPI

api_secret = "Sq6NfAburbGs9MGQb"
sw = SeniverseWeatherAPI(api_secret)


def rasa_nlu(senderid,msg):
    """
    nlu
    :param senderid: 对话id
    :param msg: 用户query
    :return:
    """
    url1 = 'http://172.16.28.43:9006/api/intent'
    url2 = 'http://172.16.28.43:9006/api/cluener'
    # url1 = 'http://172.18.86.20:9007/api/intent'
    # url2 = 'http://172.18.86.20:9007/api/cluener'
    params = {
        # "sender": senderid,
        "msg": msg
    }
    slot = {}

    # 对msg进行部分预处理
    msg = data_process(msg)
    response1 = requests.post(url=url1,data=json.dumps(params))
    intent = json.loads(response1.text)['result']     # 意图
    # if '天气' in msg:
    #     intent = 'weather'
    # if '后天' in msg:
    #     intent = 'weather'
    # if '明天' in msg:
    #     intent = 'weather'
    if '谢' in msg:
        intent = 'thanks'
    if '卡号' in msg:
        intent = 'car_info'
    if len(msg) < 5 and '没有' in msg:
        intent = 'goodbye'
    if intent == 'weather':
        intent = 'unknown'
    # response2 = requests.post(url=url2, data=json.dumps(params))
    # slots = json.loads(response2.text)['result']
    # 关键词提取slot
    if '信用卡' in msg:
        entity = 'card'
        value = u'信用卡'
        slot.update({entity: value})
    if '借记卡' in msg:
        entity = 'card'
        value = u'借记卡'
        slot.update({entity: value})
    if '银行卡' in msg:
        entity = 'card'
        value = u'银行卡'
        slot.update({entity: value})
    if '储蓄卡' in msg:
        entity = 'card'
        value = u'储蓄卡'
        slot.update({entity: value})
    # for one in slots:
    #     entity = one['entity']
    #     value = one['value']
    #     if entity != 'address' and entity != 'date-time':
    #         continue
    #
    #     slot.update({entity:value})
    torasa = intent + json.dumps(slot)
    utterance = json.loads(requestRasabotServer(senderid, torasa).content.decode('unicode-escape'))

    return utterance


def requestRasabotServer(userid, content):
    """
        访问rasa服务
    :param userid: 用户id
    :param content: 自然语言文本
    :return:  json格式响应数据
    """
    params = {'sender': userid, 'message': content}
    botIp = '172.16.28.43'
    # botIp = '172.18.86.21'
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


def forecast_to_text(address, condition):
    msg_tpl = "{city} {date} 的天气情况为：{condition}；气温：{temp_low}-{temp_high} 度"
    msg = msg_tpl.format(
        city= address,
        date=condition.date,
        condition=condition.condition,
        temp_low=condition.low_temperature,
        temp_high=condition.high_temperature
    )
    return msg


# if __name__=='__main__':
#     sender = '2020109'
#     message = '小笨，明天杭州天气'
#     y = nlu(sender, msg=message)
#     print(y)
