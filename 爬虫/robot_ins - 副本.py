from cgi import print_form
import requests
import os


headers = {
    #这边请输入你自己的浏览器的对应参数，不要照抄，否则不work
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'cookie': 'mid=YbymrwALAAEzEsPPRlnStgdMPN2E; ig_did=0AA66AEE-F134-483A-B8F0-15C7039B1E7E; ig_nrcb=1; ig_lang=zh-hk; ds_user_id=207843075; sessionid=207843075%3AcelhbwceJgHL0q%3A18; csrftoken=guEVNaiBM3YkJ2dQcoIDJBcEv0Ij1cft; shbid="6728\054207843075\0541673712042:01f7a14522b2d7d03401e06629a0a5587f95e66c535f993aedf154a3290ce30abcbb8197"; shbts="1642176042\054207843075\0541673712042:01f7d9ae6c7d3ab5c109d657b1c3e16ac2de87f746745d13d5d5d6dd6c902c7737990838"; rur="PRN\054207843075\0541673714027:01f7297bb60e60433bc6c60034c3e0e57f27cf87ce1bb86e2ba7edd91154295376d40c74"'
}

url = 'https://www.instagram.com/graphql/query/?query_hash=8c2a529969ee035a5063f2fc8602a0fd&variables=%7B%22id%22%3A%2240661333%22%2C%22first%22%3A12%2C%22after%22%3A%22QVFDcGNiWm93MWxaMEdIbUVZZVk3b015b2NIN1M5SHAyM1U0anRtcG5IQUdCWEgxMVM4VVdSaDFUZXdoRUlUa2ZVNVV0YUY2S1pVRDk4cWloTEtPb1piUQ%3D%3D%22%7D'
html = requests.get(url,headers=headers)
data = html.json()

#获取图片list
def getImageURL(data):
    img_data_info = data['data']['user']['edge_owner_to_timeline_media']['edges']
    #print(img_data_info)

    img_url_list = []
    for i in img_data_info:
        img_url = i['node']['display_url']
        img_url_list.append(img_url)
    #print(img_url_list)
    # print("共"+str(len(img_url_list))+"张")
    return img_url_list


for i in range(len(getImageURL(data))):
    print(getImageURL(data)[i])



