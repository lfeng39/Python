from bs4 import BeautifulSoup
import requests
import re

wikipedia_url = requests.get("https://zh.wikipedia.org/wiki/尼古拉·特斯拉").content
soup = BeautifulSoup(wikipedia_url, 'html.parser')

links = soup.p
'''print(links.contents)'''
print('\n' + links.text)

p = soup.find_all("p")
print(len(p))
for i in p:
    pp = i.text
    print(pp)

mulu = soup.find_all("div", attrs = {"class":"toc", "id":"toc"})
print(len(mulu))

for i in mulu:
    i = i.contents
    print(i)

'''his = "dakjfdajl"
h1 = soup.find("h1").text
url = '--url: ' + his
print(h1 + '   ' + url)'''

wiki_href_list = soup.find_all("a", attrs = {"href":re.compile("^/wiki/%"), "class":False})
for wiki_base_info in wiki_href_list:
    title = wiki_base_info.text
    href = wiki_base_info["href"]
    print(title + '   ' + "href:" + ' ' + href)
print(len(wiki_href_list))
