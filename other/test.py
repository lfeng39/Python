# import re


# file = open("kris.txt", mode="w")
# file.write("Hello Kris")
# file.close()

# line = "Cats are sma23rter than dogs"

# res = re.compile(r'^e\S(.*\S)t')

# matchObj = re.search(res, line, re.M|re.I)
# print(matchObj)
# #print(len(line))
# #print(matchObj.span())
# #print(matchObj.group())
#
#==============================================================
# import os

# file = 'D:/369/www/lego/img/official'
# # 遍历文件夹
# # def walkFile(file):
# for root, dirs, files in os.walk(file):
#         # root 表示当前正在访问的文件夹路径
#         # dirs 表示该文件夹下的子目录名list
#         # files 表示该文件夹下的文件list
#         # 遍历文件
#         # for f in files:
#         #     print(os.path.join(root, f))

#         # 遍历所有的文件夹
#         for d in dirs:
#             print(os.path.join(root, d))    
# with open('d:/Python/haha.html', mode='w', encoding='utf-8') as file:
#     file.write('<html><head><meta charset="utf-8"></head><body>')
#     file.write('<p>hello world</p>')
#     file.write('<p>'+ root +'</p>')
#     file.write('</body></html>')                
# for root, dirs, files in os.walk(file):
#     print(files)
#=============================================================================

# dict = {'朱佳茜':'jessie', '柳汐子':'kris', '柳丰':'leo'}
# ilike = list(dict.values()).index('kris')
# print(ilike)
# print(list(dict.keys())[ilike])

# list = ['jessie', 'kris', 'leo']
# print(list.index('kris'))

#===============================================================================
# tt = ['274637437', '274637437/answer/1729082895']
# if 'answer' in tt[1]:
#     print('yes')
# else:
#     pass

# x = -10.00
# for x in range(-10,10):
#     if (x*50)/(0.8*100) == 1.49:
#         print(x)
#     else:
#         x = x + 1
#         print(x)

#===============================================================================
import re
import requests
import os
#获取图片list
def getImageURL():
    headers = {
    #这边请输入你自己的浏览器的对应参数，不要照抄，否则不work
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'cookie': 'mid=YbymrwALAAEzEsPPRlnStgdMPN2E; ig_did=0AA66AEE-F134-483A-B8F0-15C7039B1E7E; ig_nrcb=1; ig_lang=zh-hk; ds_user_id=207843075; sessionid=207843075%3AcelhbwceJgHL0q%3A18; csrftoken=guEVNaiBM3YkJ2dQcoIDJBcEv0Ij1cft; shbid="6728\054207843075\0541673712042:01f7a14522b2d7d03401e06629a0a5587f95e66c535f993aedf154a3290ce30abcbb8197"; shbts="1642176042\054207843075\0541673712042:01f7d9ae6c7d3ab5c109d657b1c3e16ac2de87f746745d13d5d5d6dd6c902c7737990838"; rur="PRN\054207843075\0541673714027:01f7297bb60e60433bc6c60034c3e0e57f27cf87ce1bb86e2ba7edd91154295376d40c74"',

    'Cross-Origin-Resource-Policy': 'cross-origin'
    }

    url = 'https://www.instagram.com/graphql/query/?query_hash=8c2a529969ee035a5063f2fc8602a0fd&variables=%7B%22id%22%3A%222172028796%22%2C%22first%22%3A12%2C%22after%22%3A%22QVFBa1RFRG5yX1FvdUt1a1M5cm1vWXRmZWZKbVExT25WOUp0SHpaTkhKSE82NlV3WHhPdVh0U2d2dGRZVTNsYnI1RS1oQ3J3ZEdoVC1pbkRKRWUtU01XLQ%3D%3D%22%7D'
    html = requests.get(url,headers=headers)
    data = html.json()
    img_data_info = data['data']['user']['edge_owner_to_timeline_media']['edges']
    #print(img_data_info)

    img_url_list = []
    for i in img_data_info:
        img_url = i['node']['display_url']
        img_url_list.append(img_url)
    #print(img_url_list)
    # print("共"+str(len(img_url_list))+"张")
    return img_url_list

def scapyImage(img_url_list,id):
    for img_url in img_url_list:
        img_data = requests.get(img_url).content
        img_name = img_url.split('?')[0].split('/')[-1].split('_')[0] + ".jpg"
        file_name = "D:\MySite\static\image\ins\\" + "id=" + id

        #判断文件夹是否存在，不存在便新建一个
        if not os.path.exists(file_name):
            os.mkdir(file_name)
        with open(file_name+"\\" + img_name,"wb") as f:
            print('正在下载：' + img_name)
            f.write(img_data)

# for i in range(len(getImageURL())):
#     print(getImageURL()[i])
# scapyImage(getImageURL(),'222172028796')

uuu = 'https://www.instagram.com/graphql/query/?query_hash=8c2a529969ee035a5063f2fc8602a0fd&variables=%7B%22id%22%3A%222172028796%22%2C%22first%22%3A12%2C%22after%22%3A%22QVFBa1RFRG5yX1FvdUt1a1M5cm1vWXRmZWZKbVExT25WOUp0SHpaTkhKSE82NlV3WHhPdVh0U2d2dGRZVTNsYnI1RS1oQ3J3ZEdoVC1pbkRKRWUtU01XLQ%3D%3D%22%7D'
img_data = requests.get(uuu).content
print(img_data)