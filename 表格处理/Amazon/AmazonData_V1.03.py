#打开数据总表
import pandas as pd
import re
import datetime
import time

'''
第一步：读取10、11、12三张表，并分别存储到内存变量
'''
memoryData = pd.read_excel('D:/data/Amazon/测试数据/testData.xlsx',skiprows=1).fillna('///')
memoryData10 = pd.read_excel('D:/data/Amazon/测试数据/10.xlsx',skiprows=1).fillna('///')
memoryData11 = pd.read_excel('D:/data/Amazon/测试数据/11.xlsx',skiprows=1).fillna('///')
memoryData12 = pd.read_excel('D:/data/Amazon/测试数据/12.xlsx',skiprows=1).fillna('///')

'''
第二步：初始化全局变量
'''
def abcTrans(str):
    abcNumber = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
        'N': 13,'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }
    return abcNumber[str]
#获取字段值列表
def getColValues(xls, abc):
    if xls == 'testData':
        colValues = list(memoryData[memoryData.keys()[abcTrans(abc)]].values)
        return colValues
    elif xls == '10':
        colValues = list(memoryData10[memoryData10.keys()[abcTrans(abc)]].values)
        return colValues
    elif xls == '11':
        colValues = list(memoryData11[memoryData11.keys()[abcTrans(abc)]].values)
        return colValues
    elif xls == '12':
        colValues = list(memoryData12[memoryData12.keys()[abcTrans(abc)]].values)
        return colValues
#表格长度
lenRows12 = memoryData12.shape[0]#0为行，1为列
lenRows11 = memoryData11.shape[0]
lenRows10 = memoryData10.shape[0]
#搜索词列表长度
lenSWL12 = len(getColValues('12','B'))
lenSWL11 = len(getColValues('11','B'))
lenSWL10 = len(getColValues('10','B'))
print(lenSWL11,type(lenSWL11))
yy = '11'
xx = 'lenSWL' + yy
print(xx,type(xx))
#获取单元格值
# def getUnitCell(xls,abc):
#     tempList = str('tempList' + xls)
#     tempList = []
#     for i in range(('lenSWL' + xls)):
#         tempList.append(getColValues(xls, 'B')[i].lower())

#     freqRankList = []
#     for i in range(lenSWL12):
#         if getColValues('12','B')[i].lower() in tempList:
#             getIndex = tempList.index(getColValues('12','B')[i].lower())
#             getUnitCell = str('memoryData' + xls).iloc[getIndex,abcTrans('C')]
#         if getUnitCell == ' ' or getUnitCell == 'nan' or getUnitCell == '///':
#                 getUnitCell = 0
            
#         print('G:',getColValues('12','B')[i],getUnitCell)
#         freqRankList.append(getUnitCell)
#     return freqRankList
'''
第三步: 创建字段列表
'''
'''B
读取12月表单G、K、O栏之和小于40%的，按搜索排名升序填入
数据已处理，读取即可
'''

'''C
判断B栏搜索词字数，调用变量时，设置行数
若该行搜索词（本表单B栏内容）为Christmas tree字数为2，此处填入2；Christmas light tree字数为3，此处填入3
'''
#初始化搜索词字数列表
searchWordCountList = []
for i in range(9):
    wordCount = getColValues('12','B')[i].count(' ')
    searchWordCountList.append(wordCount + 1)
    # print('have',wordCount + 1,'words')
# print(len(searchWordCountList),searchWordCountList)

'''D
该搜索词在本表单中出现的次数
大小写、空格、顺序：spc = ['hello world','Hello World','helloworld','world hello']
只计大小写，其余不计数
'''
#转化小写，并用于比较计数的临时列表
tempList12 = []
for i in range(lenSWL12):
    searchWordABC = getColValues('12','B')[i].lower()
    tempList12.append(searchWordABC)
# print(tempList)
appearTimes = []
for i in range(lenSWL12):
    totalNum = tempList12.count(getColValues('12','B')[i].lower())
    appearTimes.append(totalNum)
#     print('D:',totalNum,'-times',searchWordList[i].lower())
# print(appearTimes)

'''F
12月表单C栏内容
'''
CtoF_List = getColValues('testData','C')
# CtoF_Value = memoryData12.iloc[1,abcTrans('C')]
# print('F:',CtoF_List,'-12 ranking No')

'''G
相同搜索词11月表单C栏内容，若无填0/ 
'''
# def freqRank(xls,abc):
#     tempList11 = []
#     for i in range(lenSWL11):
#         tempList11.append(getColValues('11', 'B')[i].lower())
#     # print(lenSWL10,lenSWL11,lenSWL12)

#     freqRankList = []
#     for i in range(lenSWL12):
#         if getColValues('12','B')[i].lower() in tempList11:
#             getIndex = tempList11.index(getColValues('12','B')[i].lower())
#             getUnitCell = memoryData11.iloc[getIndex,abcTrans('C')]
            
#             if getUnitCell == ' ' or getUnitCell == 'nan' or getUnitCell == '///':
#                 getUnitCell = 0
            
#             print('G:',getColValues('12','B')[i],getUnitCell)
#             freqRankList.append(getUnitCell)
def getUnitCell(xls,abc):
    tempList = str('tempList' + xls)
    tempList = []
    xx = 'lenSWL' + xls
    for i in range(int(xx)):
        tempList.append(getColValues(xls, 'B')[i].lower())

    freqRankList = []
    for i in range(lenSWL12):
        if getColValues('12','B')[i].lower() in tempList:
            getIndex = tempList.index(getColValues('12','B')[i].lower())
            getUnitCell = str('memoryData' + xls).iloc[getIndex,abcTrans('C')]
        if getUnitCell == ' ' or getUnitCell == 'nan' or getUnitCell == '///':
                getUnitCell = 0
            
        print('G:',getColValues('12','B')[i],getUnitCell)
        freqRankList.append(getUnitCell)
    return freqRankList
# getUnitCell('11','C')