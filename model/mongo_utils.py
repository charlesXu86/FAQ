# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   mongo_utils.py
 
@Time    :   2020/7/18 3:36 下午
 
@Desc    :   连接mongo，将对话数据处理插入mysql
 
"""
import pymysql
from pprint import pprint
from pymongo import MongoClient
import logging

logger = logging.getLogger(__name__)

uri = 'mongodb://chatbot:123456@106.13.137.219:27017/'

class MySQL():

    def __init__(self):
        # 本地
        self.database = 'renren_security'
        self.host = 'rm-uf6rv6pnfqsf649w92o.mysql.rds.aliyuncs.com'
        self.username = 'gpu'
        self.password = 'kvqpZxG6'
        self.db = pymysql.connect(host=self.host, port=3306, user=self.username, passwd=self.password, db=self.database)
        logger.info("Connect database {} successful".format(self.database))

    def insert_data(self, session_id, content, intent_name, create_user_id, score):
        """
        插入数据
        :param content: 交互文本
        :param talks: 说话方向
        :param robot_intenttion_purpose_id: 意图id
        :param intent_name: 意图名称
        :param confidence: 置信度
        :return:
        """
        cursor = self.db.cursor()

        # sql = "insert into data_center_dialogue_log_bak(id, session_id, content, talks, robot_intention_purpose_id, intent_name, confidence, is_deleted, gmt_create, gmt_modified, create_user_id, modified_user_id)Values(null,'%s', '%s', '%s',null,'%s','%s',0,null,null,null,null)"%(session_id, content, talks, intent_name, confidence)
        sql = "insert into data_center_dialogue_log(id, session_id, robot_intention_purpose_id, content, intent_name, is_deleted, gmt_create, gmt_modified, create_user_id, modified_user_id, score)Values(null, '%s', null,'%s', '%s',0, null,null, '%s', null, '%s')" % (session_id, content, intent_name, create_user_id, score)

        cursor.execute(sql)
        self.db.commit()

        self.db.close()


class Mongo():

    def __init__(self):
        self.host = '47.103.73.160'
        self.username = ''
        self.passwd = ''

        self.uri = 'mongodb://' + 'chatbot' + ':' + '123456' + '@' + '47.103.73.160' + ':' + '27017' + '/'
        self.client = MongoClient(self.host, 27017)
        self.db = self.client['admin']
        self.db.authenticate('chatbot', '123456', mechanism='SCRAM-SHA-1')

    def get_count(self):
        '''

		:return:
		'''
        data = self.client['chatbot']
        count = data.collection_names()
        print(count)

    def get_one(self):
        """
        查询数据
        :return:
        """
        coll = self.client['chatbot'].conversations
        for one in coll.find():
            events = one['events']
            sender_id = one['sender_id']
            for detail in events:
                print(detail)
                if 'user' in detail['event']:
                    content = detail['text']
                    talks = 1
                    intent_name = detail['parse_data']['intent']['name']
                    intent_confidence = detail['parse_data']['intent']['confidence']
                    MySQL().insert_data(sender_id, content, intent_name, talks, intent_confidence)
                if 'bot' in detail['event']:
                    content = detail['text']
                    talks = 0
                    MySQL().insert_data(sender_id, content, None, talks, None)


db = Mongo()
# def find_MONGO_one(ids):
# 	'''
# 	查询一条数据
# 	:param ids:
# 	:return:
# 	'''
# 	db = db.client.wusong
# 	collection = db.chongqing_origin
# 	datas = collection.find_one({'judgementId':ids})
# 	pprint.pprint(datas)
# host = '106.13.137.219'
# client = MongoClient(host, 27017)
# db = client.admin
# db.authenticate('fuwuqi219', 'falvtuandui', mechanism='SCRAM-SHA-1')
# collection = db.wenshu
# print(collection)


if __name__ == '__main__':
    # judgementId = '0d5ce792-69cb-494a-8eca-2725b5eea1de'
    # find_MONGO_one(judgementId)
    # db.get_count()
    db.get_one()