# import sys

# sys.path.append('../')

# import headers
import re
import requests
from bs4 import BeautifulSoup
from headers import Headers
from questions import Questions_ID
# from topics import I_want
# from topics import Topics_Data
# from topics import Topics_Child_Data

#构建回答页面链接
api_url = 'https://www.zhihu.com/api/v4/questions/'
req_url = '/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit='
limit = 10
# question_id = 34243513

word = ['时尚', '', '', '', '', '']
topicName = '生活方式'
url_ = api_url + str(Questions_ID(word, topicName)[0]) + req_url + str(limit)

#话题路径
print(topicName, '/', word[0])

#请求数据
get_pic_data = requests.get(url_, headers = Headers('zhihu'))
pic_data_text = get_pic_data.text

#页面标题
# re_name = 

#正则匹配图片地址
re_pic_src = r'src=."(https:.*?)\?'
re_content = r'content":"(.*?)\\u003'

#查找图片
pic_src_list = re.findall(re_pic_src, pic_data_text)
# print(len(pic_src_list))
for i in range(len(pic_src_list)):
    
    print('(', i+1, ')', pic_src_list[i], '\n')

    #保存图片，默认位置C:\Users\lfeng
    # img_src = pic_src_list[i]
    # r = requests.get(img_src,stream=True)
    # with open(str(i+1)+'.jpg', 'wb') as fd:
    #     for chunk in r.iter_content():
    #         fd.write(chunk)