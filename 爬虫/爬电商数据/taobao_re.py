import re
import requests
import pandas as pd
import time
import datetime

headers = {
            'authority': 's.taobao.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'sec-fetch-user': '?1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'referer': 'https://www.taobao.com/?spm=a230r.1.0.0.18434f0fZ0XBOG',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
            'cookie': 'thw=cn; v=0; cna=ba/BFhNadHgCARsSEUxw1LSm; cookie2=1e442ba61c5425457fbebe075e26de5f; t=add1e52914eb6b2016ee6d22120993af; _tb_token_=71ee7533e5de4; _samesite_flag_=true; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&id2=UoLfdCpv5t6I&nk2=0%2BFaWwjTPm8%3D&vt3=F8dBxdsXGDvOYjaB7kg%3D; csg=6c8ad4c6; lgc=%5Cu554A%5Cu54E9%5Cu8DEF%5Cu8FC7; dnk=%5Cu554A%5Cu54E9%5Cu8DEF%5Cu8FC7; skt=c149b9211e8c32ee; existShop=MTU4MDkxMjY2MA%3D%3D; uc4=id4=0%40UOrptUgWFjW%2BSDCzGvbpHBpU%2BNI%3D&nk4=0%400VoIkNFbMLOWIlARu3ield73yQ%3D%3D; tracknick=%5Cu554A%5Cu54E9%5Cu8DEF%5Cu8FC7; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; enc=WmrrgcHnzMECUXK5Bd0pEoDu5afsV9a894wVWiyPk4vBa6PjkJJ2om7H9JCVtpwO5%2B0QWiuQzvoXN3IKdiHeaA%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _m_h5_tk=3368371eacfccc8f82862a86dd7b8dfd_1582826745984; _m_h5_tk_enc=ce0978d905508de861ab72e478d76a9a; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=UtASsssmfaCONGki4KTH3w%3D%3D&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie14=UoTUOLr0PocV7g%3D%3D&cart_m=0&tag=10&lng=zh_CN; mt=ci=-1_0; isg=BD09yBmkPwUVjZtnjAo1pyidTJk32nEskr7nYP-CeRTDNl1oxyqB_Atk5GpwrYnk; l=dBg7ckIgQhWWcsvkBOCanurza77OSIRYYuPzaNbMi_5BA6T6xJ7OoRsl8F96VjWfT2LB4Tn8Nrv9-etuZ7DmndK-g3fPaxDc.; JSESSIONID=37DFFF827495F13075CA01C510DE2A11'
        }


start_url = 'https://s.taobao.com/search?q='
goods = 'lego 21309'
url = start_url + goods + '&s=' + str(0)

get_url = requests.get(url, headers = headers)
html = get_url.text

#print(html)
res_title = re.compile(r'"raw_title":"([^"]+)"')
res_price = re.compile(r'"view_price":"([^"]+)"')

#res_test = re.compile(r'"view_price":".*?\.\d+"')
#res_list = res_title + res_price

title = re.findall(res_title, html)
price = re.findall(res_price, html)

word = []
sale = []

#遍历关键词和价格元素
for i in range(0, len(title)):
    res_list = '【' + price[i] + '】' + title[i]
    print(res_list)
    word.append(title[i])
    sale.append(price[i])
#print(word)

print('=================================')
location = time.localtime(time.time())
now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(now)
nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
pastTime = (datetime.datetime.now()-datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')#过去一小时时间
afterTomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')#后天
tomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')#明天
#print('\n',nowTime,'\n',pastTime,'\n',afterTomorrowTime,'\n',tomorrowTime)
print('=================================')

lego_21309 = pd.DataFrame({'关键词':word, '售价':sale})
lego_21309 = lego_21309.set_index('售价')
print(lego_21309)

url_win = 'D:/Python-Work/data/lego0601.xlsx'
# url_mac = '/Users/liufeng/Documents/Python/data/lego0601.xlsx'
lego_21309.to_excel(url_win)
#lego_21309[0:3]
#print(lego_21309)