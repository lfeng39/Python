import pandas as pd
import time
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
#搜索词列表长度
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

# print(getUnitCell('11','C'))

'''H
相同搜索词10月表单C栏内容，若无填0
'''
print(getUnitCell('10','C'))