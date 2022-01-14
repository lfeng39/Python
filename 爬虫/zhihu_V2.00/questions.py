import re
import requests
from bs4 import BeautifulSoup
from topics import I_want
from headers import Headers

def Questions_ID(word, topicName):

    topic_base_url = 'https://www.zhihu.com/topic'

    topic_url = []
    question_id = []
    for i in range(1):
        #I_want函数提供子话题ID
        topic_url.append(topic_base_url + '/' + I_want(word, topicName)[i])
        get_questiontitle_data = requests.get(topic_url[i], headers = Headers('zhihu'))
        questiontitle_data_text = get_questiontitle_data.text
        re_question_id = r'content="https://www.zhihu.com/question/(.*?)"'
        # re_question_name = r'content="(.*?)"'
        question_id_list = re.findall(re_question_id, questiontitle_data_text)
        # question_name_list = re.findall(re_question_name, questiontitle_data_text)
        # print(question_name_list)
        
        #去重
        for i in range(len(question_id_list)):
            if 'answer' in question_id_list[i]:
                pass
            else:
                question_id.append(question_id_list[i])

    return question_id

# word = ['时尚', '', '', '', '', '']
# topicName = '生活方式'
# print(Questions_ID(word, topicName))
