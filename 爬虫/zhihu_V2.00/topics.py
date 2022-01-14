import re
import requests
from bs4 import BeautifulSoup
from headers import Headers

#取父话题
def Topics_Data(type, key):

    #构建话题请求链接
    topic_base_url = 'https://www.zhihu.com/topic'
    topics_url = topic_base_url + 's'

    #构建话题请求
    topics_data = requests.get(topics_url, headers = Headers('zhihu'))

    #提取父话题文本
    topics_text = topics_data.text

    #正则提取父话题Name&ID
    re_topic_id = r'data-id="(.*?)"'
    re_topic_name = r'<li.*?">.*?">(.*?)<'
    topics_id = re.findall(re_topic_id, topics_text)
    topics_name = re.findall(re_topic_name, topics_text)

    #根据需要，返回父话题名称、ID、字典组合
    if type == 'name':
        return topics_name
    elif type == 'id':
        return topics_id
    elif type == dict:
        topicsDict = dict(zip(topics_id, topics_name))
        return topicsDict

    #查询名称、ID
    

# print(Topics_Data(list))

#取子话题
def Topics_Child_Data(Topic_ID, index, type):
    
    post_url = 'https://www.zhihu.com/node/TopicsPlazzaListV2'

    data = {
        "method":"next",
        "params": '{"topic_id": ' + str(Topic_ID) + ', "offset": ' + str(index) + ', "hash_id": "40b294bd32442bd6a654497741c02b17"}'
        }

    #构建子话题请求
    topics_data_child = requests.post(url = post_url, headers = Headers('zhihu'), data = data)
    
    #提取子话题文本
    topics_text_child = topics_data_child.text

    #正则提取子话题Name&ID
    re_topic_id_child = r'href=.*?".*?topic\\\/(.*?)\\"'
    re_topic_name_child = r'<strong>(.*?)<.*?/strong>'
    topics_id_child = re.findall(re_topic_id_child, topics_text_child)
    topics_name_child = re.findall(re_topic_name_child, topics_text_child)

    #转译Unicode编码
    topics_name_child_eval = []
    for i in range(len(topics_name_child)):
        xxx = eval("u"+"'"+topics_name_child[i]+"'")
        topics_name_child_eval.append(xxx)

    if type == 'name':
        return topics_name_child_eval
    elif type == 'id':
        return topics_id_child
    elif type == dict:
        #构建子话题字典
        topicDict_child = dict(zip(topics_id_child, topics_name_child_eval))
        
        return topicDict_child

# print(Topics_Child_Data(1761, 20, dict))

#关键词对比子话题
def I_want(word, topicName):

    #选择父话题，取ID
    cho_topic_name = Topics_Data('name').index(topicName)
    cho_topic_key = Topics_Data('id')[cho_topic_name]

    #根据父话题ID取子话题数据
    #构建子话题字典
    #加载子话题，将取到的子话题字典合并到构建的字典中
    topics_child_dict = {}
    for i in range(10):
        index = i*20
        jessie = Topics_Child_Data(cho_topic_key, index, dict)
        topics_child_dict.update(jessie)

    #关键词与子话题比对取交集
    resulte_ = list(set(word).intersection(set(list(topics_child_dict.values()))))

    #关键词匹配子话题，并构建子话题ID列表
    cho_topics_id_child = []
    for values_ in resulte_:
        key_no = list(topics_child_dict.values()).index(values_)
        cho_topic_id = list(topics_child_dict.keys())[key_no]
        cho_topics_id_child.append(cho_topic_id)

    #返回选中的子话题ID列表（key值）
    return cho_topics_id_child

# word = ['时尚', '', '', '', '', '']
# topicName = '生活方式'
# print(I_want(word, topicName))