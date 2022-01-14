import requests
from bs4 import BeautifulSoup
import re
from random import choice

'''初始化链接'''
wiki_page_url = ["https://zh.wikipedia.org/wiki/%E5%B0%BC%E5%8F%A4%E6%8B%89%C2%B7%E7%89%B9%E6%96%AF%E6%8B%89"]

'''获取页面以/wiki/%开头的链接元素列表'''
a_wrap = soup.find_all("a", attrs = {"href":re.compile("^/wiki/%"), "class":False})

'''创建url对象'''
wiki_http = "https://zh.wikipedia.org"

'''提取href链接属性值放入url对象包'''
'''print(len(a_wrap))'''
'''for a_single in range(len(a_wrap)):
    print(a_single + 1, a_wrap[a_single]["href"])'''
for a_single in a_wrap:
    wiki_href = a_single["href"]
    '''print(a_wrap.index(a_single)+1, wiki_href)'''
    wiki_page_url.append(wiki_http + wiki_href)

'''循环获取、解析页面，抽取链接、创建url，访问页面、获取页面'''
for i in range(5):
    ran_url = choice(wiki_page_url)
    print(ran_url)
    wiki_page = requests.get(ran_url).content
    soup = BeautifulSoup(wiki_page, 'html.parser')
    pa = soup.find("h1").text
    print(i, pa, ran_url)
