import requests
import os

#request 网址，并返回json data
def getHTML(url):
    headers = {
        #这边请输入你自己的浏览器的对应参数，不要照抄，否则不work
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'cookie': 'mid=YbymrwALAAEzEsPPRlnStgdMPN2E; ig_did=0AA66AEE-F134-483A-B8F0-15C7039B1E7E; ig_nrcb=1; ig_lang=zh-hk; ds_user_id=207843075; sessionid=207843075%3AcelhbwceJgHL0q%3A18; csrftoken=guEVNaiBM3YkJ2dQcoIDJBcEv0Ij1cft; shbid="6728\054207843075\0541673712042:01f7a14522b2d7d03401e06629a0a5587f95e66c535f993aedf154a3290ce30abcbb8197"; shbts="1642176042\054207843075\0541673712042:01f7d9ae6c7d3ab5c109d657b1c3e16ac2de87f746745d13d5d5d6dd6c902c7737990838"; rur="PRN\054207843075\0541673714027:01f7297bb60e60433bc6c60034c3e0e57f27cf87ce1bb86e2ba7edd91154295376d40c74"'
    }
    html = requests.get(url,headers=headers)
    data = html.json()
    return data


#获取所有网址list，一个网址里包含12个url图片src
def getURLlist(url,id):
    url_list = [url]
    while url != None or has_next_page_data_info['has_next_page'] == True:
        data = getHTML(url)

        #判断有没有下一个page
        has_next_page_data_info = data['data']['user']['edge_owner_to_timeline_media']['page_info']
        if has_next_page_data_info['has_next_page'] == True:
            #获取下一页所需要的新的after参数
            after_new = has_next_page_data_info['end_cursor'].rstrip('=')
            url = "https://www.instagram.com/graphql/query/?query_hash=8c2a529969ee035a5063f2fc8602a0fd&variables=%7B%22id%22%3A%22"+id+"%22%2C%22first%22%3A12%2C%22after%22%3A%22" + after_new + "%3D%3D%22%7D"
            url_list.append(url)
        else:
            break

    return url_list


#获取图片list
def getImageURL(data):
    img_data_info = data['data']['user']['edge_owner_to_timeline_media']['edges']
    #print(img_data_info)

    img_url_list = []
    for i in img_data_info:
        img_url = i['node']['display_url']
        img_url_list.append(img_url)
    #print(img_url_list)
    print("共"+str(len(img_url_list))+"张")
    return img_url_list


#访问图片url list内的url，然后下载图片
def scapyImage(img_url_list,id):
    for img_url in img_url_list:
        img_data = requests.get(img_url).content
        img_name = img_url.split('?')[0].split('/')[-1].split('_')[0] + ".jpg"
        file_name = "id=" + id

        #判断文件夹是否存在，不存在便新建一个
        if not os.path.exists(file_name):
            os.mkdir(file_name)
        with open(file_name+"\\" + img_name,"wb") as f:
            print('正在下载：' + img_name)
            f.write(img_data)





if __name__ == "__main__":
    id = input('请输入该个人IG的id参数是（在network的字符参数查看）：')
    after = input('请输入after参数：')

    print("正在准备中，请稍后。。。")

    #目标网址，第一个url
    first_url = 'https://www.instagram.com/graphql/query/?query_hash=8c2a529969ee035a5063f2fc8602a0fd&variables=%7B%22id%22%3A%22'+id+ '%22%2C%22first%22%3A12%2C%22after%22%3A%22'+after+'%3D%3D%22%7D'
    url_list = getURLlist(first_url,id)

    for url_li in url_list:
        print('==============正在下载第{}页数据：'.format(str(url_list.index(url_li)+1)))
        data = getHTML(url_li)
        img_url_list = getImageURL(data)
        scapyImage(img_url_list,id)