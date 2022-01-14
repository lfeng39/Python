import re
import requests
import pandas as pd
import time
import datetime


word = ['土星5号 乐高 Lego','美版土星5号']
sale = ['1234.00','3212.00']

row1 = [1,2]
row2 = [3,5]
row3 = [6,8]
table = [row1, row2, row3]
num_index = ['one','two','three']
num_columns = ['售价','关键词']



print('=================================')
location = time.localtime(time.time())
now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(now)
nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
pastTime = (datetime.datetime.now()-datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')#过去一小时时间
afterTomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')#后天
tomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')#明天
#print('\n',nowTime,'\n',pastTime,'\n',afterTomorrowTime,'\n',tomorrowTime)
print('=================================')

lego_21309 = pd.DataFrame({'关键词':word, '售价':sale})
lego_21309 = lego_21309.set_index('售价')

test = pd.DataFrame(table, index = num_index, columns = num_columns)
print(test)
print(lego_21309)
#lego_21309.to_excel('D:/Python-Work/data/lego.xlsx')
test.to_excel('D:/Python/data/lego_tec.xlsx')
#lego_21309[0:3]
#print(lego_21309)

#===============================================================
print('=================================')
path_xls = 'D:/Python/data/car.xlsx'
pr = pd.read_excel(path_xls, sheet_name='L4')
print(pr)
print('=================================')
