from bs4 import BeautifulSoup
import requests
import re

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'navigate',
    'Referer': 'https://www.baidu.com/link?url=BbvHKit_qS_54fyCEcUBc3ulEWb6cBWqkRKzIPFmjAPiFGWLCNiQJGwnSySGGfB1ISIzAGw7WgvYOt1KGmmgogXgs-qU-2LZtLEF0QJyMacZm2YUopIR94iRvHdlvVUK&wd=&eqid=fecd6d6b00013c33000000065e5a1a70',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
}

baidu_url = "https://baike.baidu.com/item/%E7%89%B9%E6%96%AF%E6%8B%89/2984315?fr=aladdin"

get_content = requests.get(baidu_url, headers = headers).content
soup = BeautifulSoup(get_content, "html.parser")

get_a = soup.find_all("a", attrs={"href":re.compile("^/item/%")})
#print(get_a)

get_para = soup.find_all("div", attrs={"class":"para"})

with open("data.txt", mode="w", encoding="utf-8") as file:
    for i in range(len(get_a)):
        #file.write(get_para[i].text + "\n")
        url = "https://baike.baidu.com" + get_a[i]["href"]
        file.write(str(i+1) + "  " + get_a[i].text + "  " + url + "\n")
