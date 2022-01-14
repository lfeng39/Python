import re
import requests
from bs4 import BeautifulSoup
from topics import I_want
from headers import Headers

def Questions_ID(word, topicName):

    topic_base_url = 'https://www.zhihu.com/topic'

    topic_url = []
    question_id_list = []
    for i in range(1):
        # word = ['时尚', '生活方式', '咖啡', '凯恩斯主义', '', '']
        # topicName = '生活时尚'
        #I_want函数提供子话题ID
        topic_url.append(topic_base_url + '/' + I_want(word, topicName)[i])
        # print(I_want()[i])
        get_questiontitle_data = requests.get(topic_url[i], headers = Headers('zhihu'))
        questiontitle_data_text = get_questiontitle_data.text
        re_questiontitle_id = r'content="https://www.zhihu.com/question/(.*?)"'
        questiontitle_id_list = re.findall(re_questiontitle_id, questiontitle_data_text)

        for i in range(len(questiontitle_id_list)):
            question_id_list.append(questiontitle_id_list[i])
    return question_id_list
    
# print(Questions_ID(list))
