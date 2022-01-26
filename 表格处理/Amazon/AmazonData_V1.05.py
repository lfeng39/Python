#打开数据总表
from tkinter import ROUND
import pandas as pd
import re
import datetime
import time

'''
初始化输出表格的内容，已字典方式储存，Dict
生产每列内容列表时，向字典添加该列的键值对
'''
outXlsDict = {}

'''
初始化输出表格字典的keys
'''


'''
第一步：读取10、11、12三张表，并分别存储到内存变量
'''
memoryData = pd.read_excel('D:/data/Amazon/测试数据/testData.xlsx',skiprows=1).fillna('///')
memoryData10 = pd.read_excel('D:/data/Amazon/测试数据/'+'10'+'.xlsx',skiprows=1).fillna('///')
memoryData11 = pd.read_excel('D:/data/Amazon/测试数据/11.xlsx',skiprows=1).fillna('///')
memoryData12 = pd.read_excel('D:/data/Amazon/测试数据/12.xlsx',skiprows=1).fillna('///')

def dfXLS(xls):
    if xls == '10':
        return memoryData10
    elif xls == '11':
        return memoryData11
    elif xls == '12':
        return memoryData12
    elif xls == 'testData':
        return memoryData
# print(type(dfXLS('11')))
'''
第二步：初始化全局变量
'''
# def abcToCol(str):
abcToCol = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
    'N': 13,'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

#获取列值，返回list列表
def getColValues(xls, abc):
    if xls == 'testData':
        colValues = list(dfXLS(xls)[dfXLS(xls).keys()[abcToCol[abc]]].values)
        return colValues
    elif xls == '10':
        colValues = list(dfXLS(xls)[dfXLS(xls).keys()[abcToCol[abc]]].values)
        return colValues
    elif xls == '11':
        colValues = list(dfXLS(xls)[dfXLS(xls).keys()[abcToCol[abc]]].values)
        return colValues
    elif xls == '12':
        colValues = list(dfXLS(xls)[dfXLS(xls).keys()[abcToCol[abc]]].values)
        return colValues
# print(getColValues('12','B'))
#表格长度
lenRows12 = memoryData12.shape[0]#0为行，1为列
lenRows11 = memoryData11.shape[0]
lenRows10 = memoryData10.shape[0]
#表格宽度
widCol12 = memoryData12.shape[1]#0为行，1为列
widCol11 = memoryData11.shape[1]
widCol10 = memoryData10.shape[1]
# 搜索词列表长度
lenSWL12 = len(getColValues('12','B'))
lenSWL11 = len(getColValues('11','B'))
lenSWL10 = len(getColValues('10','B'))

# 比较搜索词，确定指定列值，并返回该值，缺损值用0代替
# 需优化：对数据类型处理，防止异常；业务逻辑分离
def getUnitCell(xls,abc):
    #创建对比列表
    tempList = str('tempList' + xls)
    tempList = []
    for i in range(len(getColValues(xls,'B'))):
        tempList.append(getColValues(xls, 'B')[i].lower())

    #创建对比对象，并生产列表元素，缺损值用0代替，元素数据类型为int
    freqRankList = []
    for i in range(len(getColValues('12','B'))):
        if getColValues('12','B')[i].lower() in tempList:
            getIndex = tempList.index(getColValues('12','B')[i].lower())
            getUnitCell = dfXLS(xls).iloc[getIndex,abcToCol['C']]
            # print(type(getUnitCell))

            if getUnitCell == ' ' or getUnitCell == 'nan' or getUnitCell == '///':
                getUnitCell = 0

            freqRankList.append(getUnitCell)

        else:
            freqRankList.insert(i,0)

    return freqRankList


'''
第三步: 创建字段列表
'''
'''A
序列号
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
CtoF_List = getColValues('12','C')
# CtoF_Value = memoryData12.iloc[1,abcTrans('C')]
# print('F:',CtoF_List,'-12 ranking No')

'''G
相同搜索词11月表单C栏内容，若无填0
'''
CtoG_List = getUnitCell('11','C')
# print()

'''H
相同搜索词10月表单C栏内容，若无填0
'''
CtoH_List = getUnitCell('10','C')
# print(getUnitCell('10','C'))

for rowIndex in range(len(getUnitCell('12','B'))):
    '''E
    (F+G+H)/3
    '''

    E_average  = round((CtoF_List[rowIndex] + CtoG_List[rowIndex] + CtoH_List[rowIndex])/3,2)
    # print('E:',E_average,'-ranking average (F+G+H)/3')

    '''J
    F-H
    '''

    J_ = CtoF_List[rowIndex] - CtoH_List[rowIndex]
    # print('J:',J_,'-(F-H)')

    '''I
    1.若G、H单项或两项为0，该处填入New 
    2.若J=0，该处填入Steady
    3.若J为负数，该处填入Up
    4.若J为正数，该处填入Down
    '''

    I_Value = ''
    if CtoG_List[rowIndex] == 0 and CtoH_List[rowIndex] == 0:
        I_Value = 'New'
    elif J_ == 0:
        I_Value = 'Steady'
    elif J_ < 0:
        I_Value = 'Up'
    elif J_ > 0:
        I_Value = 'Down'
    # print(rowIndex,'I:',I_Value,'- Trend')

    '''K
    F/G/H非0的数量
    '''
    K_Value = ''
    FGHList = [CtoF_List[rowIndex],CtoG_List[rowIndex],CtoH_List[rowIndex]]
    for i in range(len(FGHList)):
        if FGHList.count('0') == i:
            K_Value = -i + 3
    # print('K:',K_Value,'- !=0 Num')

'''L
G_K_O_1
'''
L_List = getUnitCell('12','L').append('///')

'''M
G_K_O_2
'''
M_List = getUnitCell('12','M').append('///')

'''N
G_K_O_3
'''
N_List = getUnitCell('12','N').append('///')

'''O
12月表单D栏内容
'''
DtoO_List = getColValues('12','D')

'''P
相同搜索词11月表单D栏内容，若无填/
'''
DtoP_List = getUnitCell('11','D')

'''q
相同搜索词11月表单D栏内容，若无填/
'''
DtoQ_List = getUnitCell('10','D')

'''
从OPQ开始，循环处理
'''