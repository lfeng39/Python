import re
import requests
import headers
import pandas as pd

'''
Sponesored
Natural
'''


def amz():
    #构建链接
    keyWord = 'montessori toys for 3 years old'
    keyWord = keyWord.replace(' ', '+')
    url_Product = 'https://www.amazon.com/s?k=' + keyWord + '&ref=nb_sb_noss'

    amz_ladybug = requests.get(url_Product, headers = headers.Headers('amazon'))
    print(amz_ladybug) 

    html_Con = amz_ladybug.text

    '''    
    led headlight bulbs
    montessori toys for 3 years old
    
    '''
    # 正则表达式
    re_AdHolder = r'<div\sdata-asin="(B.{9})"\sdata-index="(\d+)"\sdata-uuid=".*?".*?class=".*?(.{3})sg-col\s.+inner">\s+<.*?>\s+<.*?>\s+<.*?>\s+<div\sclass="s-card.*?><.+\ssrc="(.....).*?"\s.*?/>(..........)'
    # re_AdHolder = r'<div\sdata-asin="(B.{9})"\sdata-index="(\d+)"\sdata-uuid=".*?".*?class=".*?(.{3})sg-col\s.+inner">\s+<.*?>\s+<.*?>\s+<.*?>\s+<div\sclass="s-card.*?><.+\ssrc="(.....).*?"\s.*?/></div></a></span></div><div.*?><div class="a-section.*?><div.*?><span.*?><a.*?><span.*?><span.*?>Sponsored</span></span><span.*?><span.*?>Sponsored</span></span>\s+<span.*?></span></a></span><div.*?><span>.*?</span><div.*?><span.*?><a.*?><span>.*?</span>\s+</a>\s+</span></div></div></div><h2.*?><a.*?><span.*?>(.{9}).*?</span>\s+</a>\s+</h2></div><div.*?><div.*?><.*?><span.*?><.*?><i.*?><.*?>(.*?)<.*?><.*?><.*?>.*?<.*?><.*?>.*?<.*?>.*?<.*?>.*?<.*?><.*?><.*?>(.*?)<.*?>.*?<.*?>.*?<.*?>.*?<.*?><.*?><.*?><.*?><.*?><.*?><.*?>(.*?)<.*?>[\s\S]<.*?><.*?>.*?</span.*?><span.*?>\d+<span.*?>\.</span></span><span.*?>(\d+)</span></span></span>\s<.*?>.*?<.*?>.*?<'
    
    # re_Highly_Rated = r'<div\sdata-asin="(B.{9})"\sclass="sg-col.*?\s.*?\s.*?\s.*?\s.*?"><div.*?>\s+<div.*?>\s+<div.*?>\s+<div.*?><div.*?><span.*?><a.*?><div.*?><(img).*?(src)="(.....).*?"\s.*?/></div></a></span></div><div.*?><div class="a-section.*?><h2.*?><a.*?><span.*?>(.{9}).*?</span>\s+</a>\s+</h2></div><div.*?><div.*?><span.*?><span.*?><a.*?><i.*?><span.*?>(.{3}).*?</span></i><i.*?></i></a></span>\s+</span><span.*?><a.*?><span.*?>(.*?)</span>\s+</a>\s+</span></div></div><div.*?><div.*?><a.*?><span.*?><span.*?>(.{6}).*?</span><span.*?><span.*?>\$</span><span.*?>\d\d<span.*?>\.</span></span><span.*?>\d\d</span></span></span>\s+<.*?><.*?>(.*?)<.*?><.*?>(.*?)<.*?>(.*?)<.*?>.*?<.*?>.*?<.*?><.*?>(.*?)<.*?><.*?>'
    
    # re_Natural = r'<div\sdata-asin="(B.{9})"\sdata-index="(\d+)"\sdata-uuid=".*?".*?class=".*?(.{3})sg-col\s.+inner">\s+<div.*?>\s+<div\sclass="s-card.*?><.+\ssrc="(.....).*?"\s.*?/></div></a></span></div><div.*?><div class="a-section.*?><h2.*?><a.*?><span.*?>(.{9}).*?</span>\s+</a>\s+</h2></div><div.*?><div.*?><span.*?><span.*?><a.*?><i.*?><span.*?>(.{3}).*?</span></i><i.*?></i></a></span>\s+</span><span.*?><a.*?><span.*?>(.*?)</span>\s+</a>\s+</span></div></div><div.*?><div.*?><.*?><span.*?><span.*?>(.{6}).*?</span><span.*?><span.*?><span.*?>(.).*?<span.*?>.*?<span.*?>(.*?)</span></span><.*?><.*?>.*?<.*?><.*?>.*?<.*?>(.*?)<.*?>.*?<.*?>.*?<.*?><.*?>.*?<.*?>.*?<.*?>.*?<.*?>.*?<.*?>.*?<.*?>.*?<.*?>.*?<.*?>(.*?)<.*?>.*?<.*?>.*?<.*?>'
    
    '''    
    step for car door
    baby monitor
    tire inflator
    '''
    # 正则表达式
    # re_AdHolder = r'<div\sdata-asin="(B.*?)"\sdata-index="(\d+)"\sdata-uuid=".*?".*?class=".*?(.{3})sg-col\s.+inner">\s+<.*?>\s+<.*?>\s+<.*?>\s+<div\sclass="s-card.*?><.+\ssrc="(.....).*?"\s.*?/></div></a></span></div><div.*?><div class="a-section.*?><div.*?><span.*?><a.*?><span.*?><span.*?>Sponsored</span></span><span.*?><span.*?>Sponsored</span></span>(.{30})'
    
    # re_Highly_Rated = r'<div\sdata-asin="(B.{9})"\sclass="sg-col.*?\s.*?\s.*?\s.*?\s.*?"><div.*?>\s+<div.*?>\s+<div.*?>\s+<div.*?><div.*?><span.*?><a.*?><div.*?><img.*?src="(.....).*?"\s.*?/></div></a></span></div><div.*?><div class="a-section.*?><h2.*?><a.*?><span.*?>(.{9}).*?</span>\s+</a>\s+</h2></div><div.*?><div.*?><span.*?><span.*?><a.*?><i.*?>(.{30})'

    # re_Natural = r'<div\sdata-asin="(B.*?)"\sdata-index="(\d+)"\sdata-uuid=".*?".*?class=".*?(.{3})sg-col\s.+inner">\s+<div.*?>\s+<div\sclass="s-card.*?><.+\ssrc="(.....).*?"\s.*?/></div></a></span></div><div.*?><div class="a-section.*?><h2.*?><a.*?><span.*?>(.{9}).*?</span>\s+</a>\s+</h2></div><div.*?><div.*?><span.*?><span.*?><a.*?><i.*?><span.*?>(.{5}).*?</span></i>(.{30})'
    
    # 匹配结果
    AdHolder = re.findall(re_AdHolder, html_Con)
    print('re_ad')
    # Highly_Rated = re.findall(re_Highly_Rated, html_Con)
    print('re_bs')
    # Natural = re.findall(re_Natural, html_Con)
    print('re_na')
    # with open("html.txt", mode="w", encoding="utf-8") as file:
    #     file.write(html_Con)

    ad_ = [AdHolder, len(AdHolder)]
    # hr_ = [Highly_Rated, len(Highly_Rated)]
    # na_ = [Natural, len(Natural)]
    print('lis')
    return ad_, #hr_, na_

# print(amz()[2])
sum_ = amz()

lis_ad = sum_[0][0]
len_ad = sum_[0][1]

# lis_hr = sum_[1][0]
# len_hr = sum_[1][1]

# lis_na = sum_[2][0]
# len_na = sum_[2][1]

# print('createXLS')
# createXls = pd.DataFrame(lis_na)
# createXls.to_excel('D:/data/Amazon/aboutKeyWords.xlsx', index = False)
# print('have done')

for i in range(len_ad):
    print(lis_ad[i])

print('Sponesored:', len_ad)

# for i in range(len_hr):
#     print(lis_hr[i])

# print('HighlyRated:', len_hr)

# for i in range(len_na):
#     print(lis_na[i])

# print('Natural:', len_na)

