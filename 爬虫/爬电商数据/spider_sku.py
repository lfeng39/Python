import re
import requests
from headers import Headers

#模拟淘宝头部访问信息
# headers = {
#             'authority': 's.taobao.com',
#             'cache-control': 'max-age=0',
#             'upgrade-insecure-requests': '1',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
#             'sec-fetch-user': '?1',
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#             'sec-fetch-site': 'same-origin',
#             'sec-fetch-mode': 'navigate',
#             'referer': 'https://www.taobao.com/?spm=a230r.1.0.0.18434f0fZ0XBOG',
#             'accept-encoding': 'gzip, deflate, br',
#             'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
#             'cookie': 'thw=cn; v=0; cna=ba/BFhNadHgCARsSEUxw1LSm; cookie2=1e442ba61c5425457fbebe075e26de5f; t=add1e52914eb6b2016ee6d22120993af; _tb_token_=71ee7533e5de4; _samesite_flag_=true; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&id2=UoLfdCpv5t6I&nk2=0%2BFaWwjTPm8%3D&vt3=F8dBxdsXGDvOYjaB7kg%3D; csg=6c8ad4c6; lgc=%5Cu554A%5Cu54E9%5Cu8DEF%5Cu8FC7; dnk=%5Cu554A%5Cu54E9%5Cu8DEF%5Cu8FC7; skt=c149b9211e8c32ee; existShop=MTU4MDkxMjY2MA%3D%3D; uc4=id4=0%40UOrptUgWFjW%2BSDCzGvbpHBpU%2BNI%3D&nk4=0%400VoIkNFbMLOWIlARu3ield73yQ%3D%3D; tracknick=%5Cu554A%5Cu54E9%5Cu8DEF%5Cu8FC7; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; enc=WmrrgcHnzMECUXK5Bd0pEoDu5afsV9a894wVWiyPk4vBa6PjkJJ2om7H9JCVtpwO5%2B0QWiuQzvoXN3IKdiHeaA%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _m_h5_tk=3368371eacfccc8f82862a86dd7b8dfd_1582826745984; _m_h5_tk_enc=ce0978d905508de861ab72e478d76a9a; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=UtASsssmfaCONGki4KTH3w%3D%3D&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie14=UoTUOLr0PocV7g%3D%3D&cart_m=0&tag=10&lng=zh_CN; mt=ci=-1_0; isg=BD09yBmkPwUVjZtnjAo1pyidTJk32nEskr7nYP-CeRTDNl1oxyqB_Atk5GpwrYnk; l=dBg7ckIgQhWWcsvkBOCanurza77OSIRYYuPzaNbMi_5BA6T6xJ7OoRsl8F96VjWfT2LB4Tn8Nrv9-etuZ7DmndK-g3fPaxDc.; JSESSIONID=37DFFF827495F13075CA01C510DE2A11'
#         }

# amazon_headers = {
#             'authority': 'www.amazon.com',
#             'method': 'GET',
#             'path': '/s?k=led+outdoor&ref=nb_sb_noss_2',
#             'scheme': 'https',
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#             'accept-encoding': 'gzip, deflate, br',
#             'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
#             'cache-control': 'max-age=0',
#             'cookie': 'session-id=142-0742346-9197407; ubid-main=133-7610726-3999729; x-main="4kcZZToPabr9kasOAP@fUF?gnBEFaM5G"; at-main=Atza|IwEBIHakK7hcNKZ8SnOHIESyAbGkJm881U1DzVVSDUsQtW4m9IBGj3eRSHyCTielSYV5LFEZgM52WDU-iPqlVlfoyFH50lsV1lcHWTw-Lx0TKAQtyZ6lNtbPPeR61oLvW9lrKdJhmGKMyb_q4CM05NPDtIWwNwNlfDHJlWJiyMvDVj_ei_0q8rIGvCsv0iSo5UecLdunGbhQcvp1cCOQl9JecTQY; sess-at-main="QG3NzTZK9Oq/AnB9D2p9/kHvrdx2o/40aMhb9ncESI0="; sst-main=Sst1|PQFB0bUIS1fXsMsV2S59DyOUCW5nwqhMy78gX87n0biokDXU_fAKXLMZr9qeysTcdSa7CZu1fReugmLsmJSOEcuOW6rifXNp3uuO-9JwzfegBoGOwKCMPvM2DVFb9vKeL8qsOvwdE1CF1nsDPO7C67FLmrV3ReHONyDcqc58rITDQebzhrYOXYIRj-Lx4memd-sVbkKPZGLrw7pE7Flqpoodv66BW8DlE1lWRyZv5DvGAIivV_7JHGD3hJCJM_WYWjmiQJfLy4fx_c_iVECH2s1IHTppiitYq8kwq54gZUOfmO4; lc-main=en_US; session-id-time=2082787201l; csd-key=eyJ3YXNtVGVzdGVkIjp0cnVlLCJ3YXNtQ29tcGF0aWJsZSI6dHJ1ZSwid2ViQ3J5cHRvVGVzdGVkIjpmYWxzZSwidiI6MSwia2lkIjoiYjVjNzZlIiwia2V5IjoiVDk4S251VHI2aWMvdE44OGVYcEhsVXBOdjM1dEdsdjR2UEJZOVpNL052SjVmRzNsMEV4RjlzdStQcU9LZ1dTQ1owSTF4bWQ3amJXY1RUSE55OWJleDNaMGRYSG93eW5kRk1aaDF2c2Zpc0ZZTmdFeXllZ2lybktCNUd4Y0REdUF3eEhiUit5RytoU1QvSnZvTDh5SnRiT1JJVDBqanJtK2N3blFGbGpXTHZRYnhjSkZiNWJ6MTdJL0ZZUmRockZ3ejI3Z20wVGVwRFVmNHRGc1A1K3RZbFVSTHp4ckNQWHBCMm8xQ0RqTVIrK0l0dVNhelR6Q2FyVEl0UmJUdE0yZ2xVUGtqYU44UDRoUEl2NzFQT25QVWVBQWpMSWRkMURrSXlJb0FXZlBKalByaE9pOXV4Q0RVSjVYVUdrVzJtY0J6cFJHMEtydTg0R1QyZEs4R2JuQzNBPT0ifQ==; session-token="iYYndurGfOfXDEnCsH9uwyeX7b0S+ZABM97JVwXRTvNCEaqpBjoPjB5SmgoBsH8RZRpnTyH3FR3j0vVnX2Jlm96lE8f/iksXfejUBpTe5aVQQ6iCjhz/i/rSjgLeZ2aG8khFYc6fXz/7BaqN2qGUsVjZ+NDN0VmQXQHey4LkWKp58hQbDH6JW9jFkhDwgPC7hfZhQDMsUMH4ZaycRAq2qYLsqy5iTaJW5pUsXmBnZgaCx2DW3EkX9TEmOtVijRRhEt6ML6qD0/+9mVgz1Y26ig=="; csm-hit=adb:adblk_no&t:1608966225254&tb:FCA9V8C9Y22B2CENQZCH+s-QNQR62MA46RMT9NTY65E|1608966225254',
#         }
# amazon_headers

# 创建URL组合
start_url = 'https://s.taobao.com/search?q='
goods = 'lego 21309'
url = start_url + goods + '&s=' + str(0)

# 通过URL爬取内容
get_contents = requests.get(url, headers = Headers('taobao'))
get_text = get_contents.text
# print(get_text)

# 正则表达式匹配指定内容
raw_ = r'"title":"([^"]+)"'
title_co = r'"raw_title":"([^"]+)"'
price_co = r'"view_price":"([^"]+)"'
nick_co = r'"nick":"([^"]+)"'
innerText_co = r'"innerText":"([^"]+)"'
view_sales_co = r'"view_sales":"([^"]+)"'
comment_count_co = r'"comment_count":"([^"]+)"'
item_loc_co = r'"item_loc":"([^"]+)"'

tb_sku_title_ = re.findall(title_co, get_text)
tb_sku_prcie_ = re.findall(price_co, get_text)
tb_nick_ = re.findall(nick_co, get_text)
tb_innerText_ = re.findall(innerText_co, get_text)
tb_view_sales_ = re.findall(view_sales_co, get_text)
tb_comment_count_ = re.findall(comment_count_co, get_text)
tb_item_loc_ = re.findall(item_loc_co, get_text)

print(tb_sku_prcie_, '\n', tb_sku_title_, '\n', tb_nick_, '\n', tb_innerText_, '\n', tb_view_sales_, '\n', tb_comment_count_, '\n', tb_item_loc_)
raw_
#名称
tb_sku_title_
#价格
tb_sku_prcie_
#店面
tb_nick_
#售卖渠道
tb_innerText_
#销量
tb_view_sales_
#评价
tb_comment_count_
#发货地
tb_item_loc_


# #适合获取亚马逊BestSellers页面产品信息
# from bs4 import BeautifulSoup

# url_BestSellers = 'https://www.amazon.com/Best-Sellers-Automotive/zgbs/automotive/ref=zg_bs_nav_0'
# try:
#     kv={'user-agent':'Mozilla/5.0'}  #浏览器身份标识的字段
#     amz_BestSellers = requests.get(url_BestSellers, headers=kv)
#     amz_BestSellers.raise_for_status()  #r.status_code   200
#     # print(amz_BestSellers.raise_for_status)
#     amz_BestSellers.encoding=amz__BestSellers.apparent_encoding
#     # print(amz_BestSellers.text)
# except:
#     print("爬取失败")

# # print(r.text[:10000])
# soup = BeautifulSoup(amz_BestSellers.content, 'html.parser')
# amz_sku_title = soup.find_all('div', attrs = {'class':'p13n-sc-truncate-desktop-type2'})
# amz_sku_price = soup.find_all('span', attrs = {'class':'p13n-sc-price'})
# amz_sku_ASIN = soup.find_all('span', attrs = {'class':'helium-data-item'})
# amz_sku_Sellers = soup.find_all('a', attrs = {'class':'helium-sellers-link'})

# amz_BestSellers
# amz_sku_title
# amz_sku_price
# amz_sku_ASIN
# amz_sku_Sellers
