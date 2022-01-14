import requests
from bs4 import BeautifulSoup
import re
from random import choice

wiki_http = "https://zh.wikipedia.org"
wiki_page_url = ["https://zh.wikipedia.org/wiki/%E5%B0%BC%E5%8F%A4%E6%8B%89%C2%B7%E7%89%B9%E6%96%AF%E6%8B%89"]

for i in range(1,6):
    '''随机抽取链接数组中的一个链接'''
    ran_url = choice(wiki_page_url)
    
    '''访问随机链接页面并解析页面'''
    wiki_page = requests.get(ran_url).content
    soup = BeautifulSoup(wiki_page, 'html.parser')
    
    '''获取页面中所有符合条件的A标签'''
    a_wrap = soup.find_all("a", attrs = {"href":re.compile("^/wiki/%"), "class":False})
    
    '''从A标签中抽取href元素值，并植入url链接中'''
    for a_single in a_wrap:
        wiki_href = a_single["href"]
        wiki_page_url.append(wiki_http + wiki_href)
        
    '''打印随机爬到的页面标题及链接'''
    pa = soup.find("h1").text
    print(i, pa, ran_url)
