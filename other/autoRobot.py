#导入库
import re
import requests
import sys
sys.path.append('../LeoStudio/Python/函数库/')
import headers

'''
表格读取模块
'''
#打开表格

#读取链接


'''
爬虫模块
'''
#获取headers

#爬取网页内容
requests.get(mall_url, headers = headers)

#解析目标数据

'''
价格权限及计算模块
01:1.32 / 02:1.5 / 03:1.6 / 04:2
'''
input_code = ''
if input_code == '01':
    dianshu = 1.32
elif input_code == '02':
    dianshu = 1.5
elif input_code == '03':
    dianshu = 1.6
elif input_code == '04':
    dianshu = 2
else:
    pass



#填写表格