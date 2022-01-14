import re
import requests
from bs4 import BeautifulSoup

#存在的问题：执行代码后，下载一个问题ID下的回答图片，会被另一个问题ID下的回答图片覆盖


headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'
        }

#1）进入话题广场，提取5个话题
#构建话题访问链接
topic_base_url = 'https://www.zhihu.com/topic'
topics_url = topic_base_url + 's'

#爬取话题列表
get_topicstitle_data = requests.get(topics_url, headers = headers)

topicstitle_data_text = get_topicstitle_data.text
re_topicstitle_id = r'<a.*?target="_blank".*?href="/topic/(.*?)"'
topicstitle_id_list = re.findall(re_topicstitle_id, topicstitle_data_text)

topic_id = [topicstitle_id_list[0], topicstitle_id_list[1]]#提取2个话题ID

# def topic_ID():
#     for i in 


#遍历每个话题ID并提取单个话题中的前5个问题
for i in range(len(topic_id)):
    topic_url = topic_base_url + '/' + topic_id[i]
    #2）进入某话题，提取前5个问题标题
    get_questiontitle_data = requests.get(topic_url, headers = headers)
    questiontitle_data_text = get_questiontitle_data.text
    re_questiontitle_id = r'content="https://www.zhihu.com/question/(.*?)"'
    questiontitle_id_list = re.findall(re_questiontitle_id, questiontitle_data_text)
    
    question_id = [questiontitle_id_list[0], questiontitle_id_list[1]]
    
    for i in range(len(question_id)):
        # print(hh)

        # print(type(hh), hh)
        #3）进入某问题，提取回答中的图片
        #构建回答链接及爬取数据限制
        api_url = 'https://www.zhihu.com/api/v4/questions/'
        req_url = '/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit='
        limit = 5
        # question_id = 34243513

        url_ = api_url + question_id[i] + req_url + str(limit)

        #请求数据
        get_pic_data = requests.get(url_, headers = headers)
        pic_data_text = get_pic_data.text

        #正则匹配图片地址
        re_pic_src = r'src=."(https:.*?)"'

        #查找图片
        pic_src_list = re.findall(re_pic_src, pic_data_text)
        # print(len(pic_src_list))
        for i in range(len(pic_src_list)):
            print('【', i+1, '】', pic_src_list[i], '\n')

            #保存图片，默认位置C:\Users\lfeng
            # img_src = pic_src_list[i]
            # r = requests.get(img_src,stream=True)
            # with open(str(i+1)+'.jpg', 'wb') as fd:
            #     for chunk in r.iter_content():
            #         fd.write(chunk)