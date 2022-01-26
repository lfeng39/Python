from calendar import month
import pandas as pd
import re
import datetime
import time

'''
V1.01将原始表单初始化，将百万条数据，按照GKO之和小于40的提取，缩减表单数据至30万条左右
'''
def abcTrans(str):
    abcNumber = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
        'N': 13,'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }
    return abcNumber[str]
#计时器开始
t1 = time.time()
print('读取原始表格中...')

memoryData10 = pd.read_excel('D:/data/Amazon/原始数据/'+'10'+'.xlsx',skiprows=1).fillna('///')
memoryData11 = pd.read_excel('D:/data/Amazon/原始数据/11.xlsx',skiprows=1).fillna('///')
memoryData12 = pd.read_excel('D:/data/Amazon/原始数据/12.xlsx',skiprows=1).fillna('///')

def dfXLS(xls):
    if xls == '10':
        return memoryData10
    elif xls == '11':
        return memoryData11
    elif xls == '12':
        return memoryData12

x_shape = memoryData12.shape#表格行与列
nrows = memoryData12.shape[0]#表格行数
ncols = memoryData12.shape[1]#表格列数

t2 = time.time()
print('完成读取，耗时：',t2-t1)
print('开始计算...')

# 条件：GKO之和小于40
# 目的：提取整行数据添加到rowsList列表
rowsList = []
for i in range(1,nrows):
    keyWordValue = [
        memoryData12.iloc[i,abcTrans('G')],
        memoryData12.iloc[i,abcTrans('K')],
        memoryData12.iloc[i,abcTrans('O')],
        ]
    if type(keyWordValue[0]) != float:
        keyWordValue[0] = 0
    if type(keyWordValue[1]) != float:
        keyWordValue[1] = 0
    if type(keyWordValue[2]) != float:
        keyWordValue[2] = 0

    he = round(sum(keyWordValue)*100,2)

    if he < 40:
        rowsList.append(memoryData12.loc[i,:])

# 创建新列表的key，创建新表的保存路径，输出处理后的表
rowsList.insert(0, memoryData12.loc[0,:])
create_xls_home = pd.DataFrame(rowsList)
dataMonth = 'D:/data/Amazon/' + 12 +'.xlsx'
create_xls_home.to_excel(dataMonth, index = 0)#★★★★★★这里是创建的表格路径及名称，可自己修改单引号中的内容★★★★★★

#计时器结束
t3 = time.time()
print('完成计算,耗时：',t3 - t2)
print('总耗时：',t3 - t1)
