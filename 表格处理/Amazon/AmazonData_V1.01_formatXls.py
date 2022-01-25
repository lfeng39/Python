from calendar import month
import pandas as pd
import re
import datetime
import time

'''
V1.01将原始表单初始化，将百万条数据，按照GK0之和小于40的提取，缩减表单数据至30万条左右
'''
def abcTrans(str):
    abcNumber = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
        'N': 13,'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }
    return abcNumber[str]
#计时器开始
t1 = time.time()

monNum = '10'

def dfXLS(dataMonth):
    xlsPath = 'D:/data/Amazon/原始数据'+ dataMonth +'月表单.xlsx'
    if dataMonth == '需求导入的10-12月表单':
        df_xls = pd.read_excel(xlsPath).fillna('///')
        return df_xls
    elif dataMonth == '10':
        df_xls = pd.read_excel(xlsPath).fillna('///')
        return df_xls
    elif dataMonth == '11':
        df_xls = pd.read_excel(xlsPath).fillna('///')
        return df_xls
    elif dataMonth == '12':
        df_xls = pd.read_excel(xlsPath).fillna('///')
        return df_xls

memoryData = dfXLS(monNum)
# x_shape = memoryData.shape#表格行与列
nrows = memoryData.shape[0]#表格行数
# ncols = memoryData.shape[1]#表格列数
# print(nrows,type(nrows))
t2 = time.time()
print(t2-t1)

rowsList = []
for i in range(1,nrows):
    keyWordValue = [
        memoryData.iloc[i,abcTrans('G')],
        memoryData.iloc[i,abcTrans('K')],
        memoryData.iloc[i,abcTrans('O')],
        ]
    if type(keyWordValue[0]) != float:
        keyWordValue[0] = 0
    if type(keyWordValue[1]) != float:
        keyWordValue[1] = 0
    if type(keyWordValue[2]) != float:
        keyWordValue[2] = 0

    he = round(sum(keyWordValue)*100,2)

    if he < 40:
        rowsList.append(memoryData.loc[i,:])

rowsList.insert(0, memoryData.loc[0,:])
create_xls_home = pd.DataFrame(rowsList)
dataMonth = 'D:/data/Amazon/' + monNum +'.xlsx'
create_xls_home.to_excel(dataMonth, index = 0)#★★★★★★这里是创建的表格路径及名称，可自己修改单引号中的内容★★★★★★

#计时器结束
t3 = time.time()
print(t3 - t1)

#关键词对比
# for i in range(1, nrows):
#     searchWord = memoryData.iloc[i,abcTrans('B')]
#     keyWordList = ['Christmas tree', 'Christmas light tree', ' ', 'Christmas movies', 'christmas movies']
#     wordNum = keyWordList.count(' ')
#     print(type(searchWord), searchWord)
#     if searchWord in keyWordList:
#         print(keyWordList.index(searchWord))
#     else:
#         print('no word')