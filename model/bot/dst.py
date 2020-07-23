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
from model.service.weather_api.seniverse import SeniverseWeatherAPI

api_secret = "Sq6NfAburbGs9MGQb"
sw = SeniverseWeatherAPI(api_secret)

# filled_slot = {}

def nlu(senderid,msg, filled_slot):
    """
    nlu
    :param senderid: 对话id
    :param msg: 用户query
    :return:
    """
    # url1 = 'http://172.16.28.43:9006/api/intent'
    # url2 = 'http://172.16.28.43:9006/api/cluener'
    url1 = 'http://172.18.86.20:9007/api/intent'
    url2 = 'http://172.18.86.20:9007/api/cluener'
    params = {
        # "sender": senderid,
        "msg": msg
    }
    slot = {}
    response1 = requests.post(url=url1,data=json.dumps(params))
    intent = json.loads(response1.text)['result']     # 意图
    if '天气' in msg:
        intent = 'weather'
    if '后天' in msg:
        intent = 'weather'
    if '明天' in msg:
        intent = 'weather'
    response2 = requests.post(url=url2, data=json.dumps(params))
    slots = json.loads(response2.text)['result']
    for one in slots:
        entity = one['entity']
        value = one['value']
        if entity != 'address' and entity != 'date-time':
            continue

        slot.update({entity:value})
    utterance = weather_answer_bot(intent, slot, filled_slot)

    return utterance


def weather_answer_bot(intent, slot, filled_slot):
    """
    天气查询
    :param intent_slot:
    :return:
    """
    require_slot = ["address", "date-time"]
    filled_slot.update(slot)
    anwser = "您好，我是智能助手小笨，我不是很理解您的话"
    if intent == 'greet':
        anwser = "您好，我是智能助手小笨，请问有什么可以帮您的？"
    if intent == 'weather':
        if not filled_slot :
            anwser = '我在呢，你想查询天气吗？请告诉时间和地点哟～？'
        if 'address' in filled_slot:
            anwser = '请问您想查询什么时候的天气呢？'
        if 'date-time' in filled_slot:
            anwser = '请问您想查询哪里的天气呢？'
        if 'address' in filled_slot and 'date-time' in filled_slot:
            date_time_number = get_time_unit(filled_slot['date-time'])
            now = datetime.datetime.now().date()
            delta = (date_time_number - now).days
            if delta > 3:
                anwser = '小笨只能查询最近三天的天气哦'
                filled_slot.clear()
            elif delta < 3 and delta >= 0:
                condition = sw.get_weather_by_city_and_day(filled_slot['address'], date_time_number)
                anwser = forecast_to_text(filled_slot['address'], condition)
            else:
                anwser = '请说正确的时间～'
    if intent == 'goodbye':
        anwser = '再见'
        filled_slot.clear()

    return anwser


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
