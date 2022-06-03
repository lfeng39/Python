import re
import requests
import headers

'''
Sponesored
Natural
'''


def amz():
    #构建链接
    keyWord = 'led headlight bulbs'
    keyWord = keyWord.replace(' ', '+')
    url_Product = 'https://www.amazon.com/s?k=' + keyWord + '&ref=nb_sb_noss'

    amz_ladybug = requests.get(url_Product, headers = headers.Headers('amazon'))
    print(amz_ladybug) 

    html_Con = amz_ladybug.text


    re_Natural = r'<div\sdata-asin="(B.*?)"\sdata-index="(\d+)"\sdata-uuid=".*?".*?class=".*?(.{10})sg-col\s.+inner">\s+<.*?>\s+<.*?>\s+</a>.*?</div></div>(.{30})'

    re_Highly_Rated = r'<div\sdata-asin="(B.{9})"\sclass="sg-col.*?\s.*?\s.*?\s.*?\s.*?"><div.*?>\s+<div.*?>\s+<div.*?>\s+<div.*?><div.*?><span.*?><a.*?><div.*?><img.*?src="(.*?)"\s'

    '''
    baby monitor
    led headlight bulbs
    '''
    re_Results_Sponesored_A = r'<div\sdata-asin="(B.*?)"\sdata-index="(\d+)"\sdata-uuid=".*?".*?class=".*?(.{10})sg-col\s.+inner">\s+<.*?>\s+<.*?>\s+<.*?>\s+<div\sclass="s-card.*?><div.*?><div.*?><div.*?><div.*?><div.*?></div><div.*?><div.*?><span.*?><a.*?><div.*?><img.*?src="(.*?)"\s'

    '''
    montessori toys for 3 years old
    tire inflator
    '''
    re_Results_Sponesored_B = r'<div\sdata-asin="(B.*?)"\sdata-index="(\d+)"\sdata-uuid=".*?".*?class=".*?(.{10})sg-col\s.+inner">\s+<.*?>\s+<.*?>\s+<.*?>\s+<div\sclass="s-card.*?><.+\ssrc="(.*?)"\s'
    # r'<div\sdata-asin="(B.*?)"\sdata-index="(\d+)"\sdata-uuid=".*?".*?class=".*?(.{10})sg-col\s.+inner">\s+<.*?>\s+<.*?>\s+<.*?>\s+<div\sclass="s-card.*?><div.*?><div.*?><.*?><.*?><div.*?><.+\ssrc="(.{30})'

    # BSR_Img_Asin_Title = re.findall(re_Results_Sponesored_A, html_Con)
    BS_Img_Asin_Title = re.findall(re_Highly_Rated, html_Con)
    Sponesored_Img_Asin_Title = re.findall(re_Results_Sponesored_B, html_Con)
    # Img_Asin_Title = re.findall(re_Results, html_Con)

    # bs4 = soup.find_all('img')

    # with open("html.txt", mode="w", encoding="utf-8") as file:
    #     file.write(html_Con)

    ad_ = [Sponesored_Img_Asin_Title, len(Sponesored_Img_Asin_Title)]
    bs_ = [BS_Img_Asin_Title, len(BS_Img_Asin_Title)]

    return ad_, bs_

# print(amz()[2])
sum_ = amz()

len_ad = sum_[0][1]
len_hr = sum_[1][1]

lis_ad = sum_[0][0]
lis_hr = sum_[1][0]



for i in range(len_ad):
    print(lis_ad[i])

print('Sponesored:', len_ad)

for i in range(len_hr):
    print(lis_hr[i])

print('HighlyRated:', len_hr)