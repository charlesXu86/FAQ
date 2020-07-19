# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   train_skill.py
 
@Time    :   2020/7/18 10:11 上午
 
@Desc    :   新技能训练
 
"""
import requests
import json


def train_skill(skillId):
    """

    :param skillId: 技能ID
    :return:
    """
    data = {}
    url = 'http://47.103.73.160:9005/model/train'

    # domain = "intents:\n  - greet\n  - goodbye\n  - weather\n  - weather_info\n\n  actions:\n  - utter_greet\n  - utter_ask_address\n  - utter_ask_date-time\n  - utter_working_on_it\n  - utter_report_weather\n  - utter_goodbye\n\ntemplates:\n  utter_greet:\n - text: \"您好，我是小笨，有什么可以帮您的？\"\n\nutter_goodbye:\n - text: \"再见\"\n\n"
    # config = "language: en\npipeline: supervised_embeddings\npolicies:\n  - name: MemoizationPolicy\n  - name: KerasPolicy"
    # nlu = "## intent:greet\n- 你好\n- hello\n- hi\n## intent:goodbye\n- bye\n- goodbye\n- 再见\n- see you\n## intent:weather\n- 天气\n- 用着摄氏度显示天气\n## intent:weather_info\n- 告诉我在[广州](address)怎么样\n- 不好意思可以帮我查[香港](address)的天气"
    # stories = "## greet* greet\n- utter_greet\n\n## simple path\n* weather_address_date-time\n- utter_working_on_it\n- action_report_weather\n- utter_report_weather\n\n## address > date-time path\n* weather_address\n- utter_ask_date-time\n* weather_date-time\n- utter_working_on_it\n- action_report_weather\n- utter_report_weather"

    domain_en = "intents:\n  - greet\n  - goodbye\n  - affirm\n  - deny\n  - mood_great\n  - mood_unhappy\n\nactions:\n  - utter_greet\n  - utter_cheer_up\n  - utter_did_that_help\n  - utter_happy\n  - utter_goodbye\n\ntemplates:\n  utter_greet:\n  - text: \"Hey! How are you?\"\n\n  utter_cheer_up:\n  - text: \"Here is something to cheer you up:\"\n    image: \"https://i.imgur.com/nGF1K8f.jpg\"\n\n  utter_did_that_help:\n  - text: \"Did that help you?\"\n\n  utter_happy:\n  - text: \"Great carry on!\"\n\n  utter_goodbye:\n  - text: \"Bye\""
    config_en = "language: en\npipeline: supervised_embeddings\npolicies:\n  - name: MemoizationPolicy\n  - name: KerasPolicy"
    nlu_en = "## intent:greet\n- hey\n- hello\n- hi hi\n## intent:goodbye\n- bye\n- goodbye\n- have a nice day\n- see you\n## intent:affirm\n- yes\n- indeed\n## intent:deny\n- no\n- never\n## intent:mood_great\n- perfect\n- very good\n- great\n## intent:mood_unhappy\n- sad\n- not good\n- unhappy"
    stories_en = "## happy path\n* greet\n\n  - utter_greet\n\n* mood_great\n\n  - utter_happy\n\n## sad path 1\n* greet\n\n  - utter_greet\n\n* mood_unhappy\n\n  - utter_cheer_up\n\n  - utter_did_that_help\n\n* affirm\n\n  - utter_happy\n\n## sad path 2\n* greet\n\n  - utter_greet\n\n* mood_unhappy\n\n  - utter_cheer_up\n\n  - utter_did_that_help\n\n* deny\n\n  - utter_goodbye\n\n## say goodbye\n* goodbye\n\n  - utter_goodbye"

    data["domain"] = domain_en
    data["config"] = config_en
    data["nlu"] = nlu_en
    data["stories"] = stories_en
    data["force"] = False
    data["save_to_default_model_directory"] = True


    data_en = """{
  "domain": "intents:\n  - greet\n  - goodbye\n  - affirm\n  - deny\n  - mood_great\n  - mood_unhappy\n\nactions:\n  - utter_greet\n  - utter_cheer_up\n  - utter_did_that_help\n  - utter_happy\n  - utter_goodbye\n\ntemplates:\n  utter_greet:\n  - text: \"Hey! How are you?\"\n\n  utter_cheer_up:\n  - text: \"Here is something to cheer you up:\"\n    image: \"https://i.imgur.com/nGF1K8f.jpg\"\n\n  utter_did_that_help:\n  - text: \"Did that help you?\"\n\n  utter_happy:\n  - text: \"Great carry on!\"\n\n  utter_goodbye:\n  - text: \"Bye\"",
  "config": "language: en\npipeline: supervised_embeddings\npolicies:\n  - name: MemoizationPolicy\n  - name: KerasPolicy",
  "nlu": "## intent:greet\n- hey\n- hello\n- hi\n## intent:goodbye\n- bye\n- goodbye\n- have a nice day\n- see you\n## intent:affirm\n- yes\n- indeed\n## intent:deny\n- no\n- never\n## intent:mood_great\n- perfect\n- very good\n- great\n## intent:mood_unhappy\n- sad\n- not good\n- unhappy",
  "stories": "## happy path\n* greet\n\n  - utter_greet\n\n* mood_great\n\n  - utter_happy\n\n## sad path 1\n* greet\n\n  - utter_greet\n\n* mood_unhappy\n\n  - utter_cheer_up\n\n  - utter_did_that_help\n\n* affirm\n\n  - utter_happy\n\n## sad path 2\n* greet\n\n  - utter_greet\n\n* mood_unhappy\n\n  - utter_cheer_up\n\n  - utter_did_that_help\n\n* deny\n\n  - utter_goodbye\n\n## say goodbye\n* goodbye\n\n  - utter_goodbye",
  "force": false,
  "save_to_default_model_directory": true
}"""
    domain_en = "intents:\n  - greet\n  - goodbye\n  - affirm\n  - deny\n  - mood_great\n  - mood_unhappy\n\nactions:\n  - utter_greet\n  - utter_cheer_up\n  - utter_did_that_help\n  - utter_happy\n  - utter_goodbye\n\ntemplates:\n  utter_greet:\n  - text: \"Hey! How are you?\"\n\n  utter_cheer_up:\n  - text: \"Here is something to cheer you up:\"\n    image: \"https://i.imgur.com/nGF1K8f.jpg\"\n\n  utter_did_that_help:\n  - text: \"Did that help you?\"\n\n  utter_happy:\n  - text: \"Great carry on!\"\n\n  utter_goodbye:\n  - text: \"Bye\""

    post_data = json.dumps(data)
    results = requests.post(url, post_data)
    # print(results.text)

    return results.text

if __name__=='__main__':
    skillId = '2222'
    train_skill(skillId=skillId)