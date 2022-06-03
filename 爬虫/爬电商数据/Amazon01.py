import re
from numpy import product
import requests
import headers

def amz():
    #适合获取亚马逊BestSellers页面产品信息
    url_Product = 'https://www.amazon.com/s?k=baby+monitor&ref=nb_sb_noss'
    url_BSR = 'https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers'
    spray_gun = 'https://www.amazon.com/s?k=spray+gun+for+cars&crid=1QR7UF10WA38Y&sprefix=spray+gun+for+cars%2Caps%2C382&ref=nb_sb_noss_1'
    inflator_ = 'https://www.amazon.com/s?k=inflator&crid=1YDC4HFPGOO3K&sprefix=inflator%2Caps%2C593&ref=nb_sb_noss'

    keyWord = 'baby monitor'
    keyWord = keyWord.replace(' ', '+')
    url_Product = 'https://www.amazon.com/s?k=' + keyWord + '&ref=nb_sb_noss'

    amz_ladybug = requests.get(url_Product, headers = headers.Headers('amazon'))
    # soup = BeautifulSoup(url_spray_gun,parser = 'html.parser')
    print(amz_ladybug) #r.status_code   200

    html_Con = amz_ladybug.text
    # print(amz_ladybug.content)
    
    content = bytes(amz_ladybug.text, amz_ladybug.encoding).decode('utf-8')
    # print(content)

    get_BSR_Img_Asin_Title = r'<img\salt=".*?"\ssrc="(.*?)".*?<a class="a-link-normal" href=".*?_rd_i=(.*?)&.*?link"><span><div class="p13n.*?">(.*?)</div>'
    get_Search_Img_Asin_Title = r'<div\sdata-asin="(B.*?)"\sdata-index="(\d+)"\sdata-uuid=".*?".*?class=".*?(.{10})sg-col\s.+inner">\s+<.*?>\s+<.*?>\s+<.+<img.+src="(.*?)"'
    #r'<div\sdata-asin="(B.*?)"\sdata-index="(\d+)"\sdata-uuid=".*?".*?class=".*?(.{10})sg-col\s.+inner">\s+<.+>\s+<.+<img.+src="(.*?)".+<span\s.+normal">(.*?)</span>.+base"><span class="a-offscreen">(.*?)</span>.+secondary"><span class="a-offscreen">(.*?)</span>'

    BSR_Img_Asin_Title = re.findall(get_BSR_Img_Asin_Title, html_Con)
    Search_Img_Asin_Title = re.findall(get_Search_Img_Asin_Title, html_Con)

    # bs4 = soup.find_all('img')

    # with open("html.txt", mode="w", encoding="utf-8") as file:
    #     file.write(html_Con)

    sum = [Search_Img_Asin_Title,len(Search_Img_Asin_Title)]
    return BSR_Img_Asin_Title,Search_Img_Asin_Title,sum
print(amz()[2])