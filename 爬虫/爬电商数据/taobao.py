import requests
import re

def getHtmlText(url):
    try:
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
        r = requests.get(url, headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
 
        return r.text
    except:
        print("爬取失败")
        return ""
    
    
def parsePage(ilist,html):
    try:
        plt = re.findall(r'\"view_price\":\"\d+\.\d*\"',html)
        tlt = re.findall(r'\"raw_title\":\".*?\"',html)
        print(tlt[0])
        #"raw_title":"乐高 21309 LEGO 积木玩具 想象系列 阿波罗土星5号运载火箭 绝版"
        print(len(plt))
        for i in range(len(plt)):
            price = eval(plt[i].split('\"')[3])
            title = tlt[i].split('\"')[3]
            ilist.append([title,price])
        #print(ilist)
    except:
        print("解析出错")
    
def printGoodsList(ilist,num):
    print("=====================================================================================================")
    tplt = "{0:<3}\t{1:<30}\t{2:>6}"
    print(tplt.format("序号","商品名称","价格"))
    count = 0
    for g in ilist:
        count += 1
        if count <= num:   
            print(tplt.format(count,g[0],g[1]))
    print("=====================================================================================================")
    
def main():
    goods = "lego21309"
    depth = 1
    start_url = "https://s.taobao.com/search?q="+goods
    infoList = []
    num = 20
    for i in range(depth):
        try:
            url = start_url + '$S=' + str(44*i)
            html = getHtmlText(url)
            parsePage(infoList,html)
        except:
            continue
    
    printGoodsList(infoList,num)
    
main() 
