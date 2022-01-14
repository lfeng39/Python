import re
import requests

headers = {
    'authority': 's.taobao.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'referer': 'https://www.taobao.com/?spm=a21bo.7925890.1581860521.1',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'cookie': 'thw=cn; v=0; cna=ba/BFhNadHgCARsSEUxw1LSm; cookie2=1e442ba61c5425457fbebe075e26de5f; t=add1e52914eb6b2016ee6d22120993af; _tb_token_=71ee7533e5de4; _samesite_flag_=true; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&id2=UoLfdCpv5t6I&nk2=0%2BFaWwjTPm8%3D&vt3=F8dBxdsXGDvOYjaB7kg%3D; csg=6c8ad4c6; lgc=%5Cu554A%5Cu54E9%5Cu8DEF%5Cu8FC7; dnk=%5Cu554A%5Cu54E9%5Cu8DEF%5Cu8FC7; skt=c149b9211e8c32ee; existShop=MTU4MDkxMjY2MA%3D%3D; uc4=id4=0%40UOrptUgWFjW%2BSDCzGvbpHBpU%2BNI%3D&nk4=0%400VoIkNFbMLOWIlARu3ield73yQ%3D%3D; tracknick=%5Cu554A%5Cu54E9%5Cu8DEF%5Cu8FC7; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; enc=WmrrgcHnzMECUXK5Bd0pEoDu5afsV9a894wVWiyPk4vBa6PjkJJ2om7H9JCVtpwO5%2B0QWiuQzvoXN3IKdiHeaA%3D%3D; alitrackid=www.taobao.com; mt=ci=-1_0; _m_h5_tk=af8cae554856355fa9d34568f2764fc5_1582994833001; _m_h5_tk_enc=80c618f8d93c7411c0f5b8fffef54fe4; JSESSIONID=F07FA837C8B71C2B6C15075BAB2D3957; lastalitrackid=www.taobao.com; uc1=cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&cookie21=UtASsssmfaCONGki4KTH3w%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&pas=0&cookie14=UoTUOa5sVAYiYA%3D%3D&cart_m=0&tag=10&lng=zh_CN; isg=BJGRzLgNq_t-s8fum97MC2wjoJ0r_gVwRsKb5HMmjdh3GrFsu04VQD_4uO78CZ2o; l=dBNrpAb7QuvkG5ySBOCanurza77OSIRYYuPzaNbMi_5Cv6T13O_OoR0ZpF96VjWfT2LB4Tn8Nrv9-etuZ7DmndK-g3fPaxDc.',
}

url = 'https://s.taobao.com/search'
payload = {'q': 'lego 21309','s': '1','ie':'utf8'}  #字典传递url参数    
file = open('taobao_test.txt','w',encoding='utf-8')
 
for k in range(0,10):        #100次，就是100个页的商品数据
 
    payload ['s'] = 44*k+1   #此处改变的url参数为s，s为1时第一页，s为45是第二页，89时第三页以此类推                          
    resp = requests.get(url, params = payload, headers =headers)
    print(resp.url)          #打印访问的网址
    resp.encoding = 'utf-8'  #设置编码
    title = re.findall(r'"raw_title":"([^"]+)"',resp.text,re.I)  #正则保存所有raw_title的内容，这个是书名，下面是价格，地址
    price = re.findall(r'"view_price":"([^"]+)"',resp.text,re.I)    
    loc = re.findall(r'"item_loc":"([^"]+)"',resp.text,re.I)
    x = len(title)           #每一页商品的数量
 
    for i in range(0,x) :    #把列表的数据保存到文件中
        file.write(str(k*44+i+1)+'名称：'+title[i]+'\n'+'价格：'+price[i]+'\n'+'地址：'+loc[i]+'\n\n')
 
 
file.close()