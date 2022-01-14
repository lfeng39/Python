import re
import requests
from bs4 import BeautifulSoup
from headers import Headers

def Topics_DICT():

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

    #构建父话题字典
    topicsDict = dict(zip(topics_id, topics_name))

    return topicsDict

# print(Topics_DICT())

def Topics_Child_DICT(Topic_ID, index):
    
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

    topics_name_child_eval = []
    for i in range(len(topics_name_child)):
        xxx = eval("u"+"'"+topics_name_child[i]+"'")
        topics_name_child_eval.append(xxx)
    # return xxx

    #构建子话题字典
    topicDict_child = dict(zip(topics_id_child, topics_name_child_eval))
    
    return topicDict_child

# print(Topics_Child_DICT())

def I_want(word, topicName):
#选择想要的话题并返回该话题在字典中的Key值
    #关键词
    # i_want = ['时尚', '生活方式', '咖啡', '凯恩斯主义', '', '']

    # #构建字典values列表
    # topics_name_ = list(Topics_DICT().values())
    # #目标关键词列表对比爬到的话题名称列表，取交集
    # resulte_ = list(set(I_want).intersection(set(topics_name_)))
    
    # #选择的父话题在字典中的Key值列表
    # cho_topics_id = []
    # for values_ in resulte_:
    #     key_no = list(Topics_DICT().values()).index(values_)
    #     cho_topic_id = list(Topics_DICT().keys())[key_no]
    #     cho_topics_id.append(cho_topic_id)

    #指定父话题'生活方式'
    # try:
    #     cho_topic_name = list(Topics_DICT().values()).index(topicName)
    #     cho_topic_key = list(Topics_DICT().keys())[cho_topic_name]
    # except:
    #     print('未检索到关键词') #return '未检索到关键词' 

    cho_topic_name = list(Topics_DICT().values()).index(topicName)
    cho_topic_key = list(Topics_DICT().keys())[cho_topic_name]


    #根据父话题Key创建子话题字典
    topics_child_dict = {}
    for i in range(10):
        index = i*20
        # topic_id = 
        jessie = Topics_Child_DICT(cho_topic_key, index)
        topics_child_dict.update(jessie)

    #关键词与话题比对取交集
    resulte_ = list(set(word).intersection(set(list(topics_child_dict.values()))))

    cho_topics_id_child = []
    for values_ in resulte_:
        key_no = list(topics_child_dict.values()).index(values_)
        cho_topic_id = list(topics_child_dict.keys())[key_no]
        cho_topics_id_child.append(cho_topic_id)

    #返回选中的子话题ID列表（key值）
    return cho_topics_id_child

# print(I_want())

