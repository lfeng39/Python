import abc
import pandas as pd
import time

'''
初始化输出表格的内容，已字典方式储存，Dict
生产每列内容列表时，向字典添加该列的键值对
'''
outXlsDict = {}

'''
初始化输出表格字典的keys
'''
keys = [
    '序号', 'Search Term_1 搜索词', 'Search Term Cnt 搜索词字数',
    'Occurrence 出现次数', 'Search Frequency Rank Rate',
    'Search Frequency Rank 1', 'Search Frequency Rank 2',
    'Search Frequency Rank 3', 'Trend', 'ThreeMonthSFRChange', 'Match',
    'G_K_O_1', 'G_K_O_2', 'G_K_O_3', 'X.1.Clicked Asin 1',
    'X.2.Clicked Asin 1', 'X.3.Clicked Asin 1', 'X.1.Product_1',
    'X.2.Product_1', 'X.3.Product_1', 'X.1.Click Share_1',
    'X.2.Click Share_1', 'X.3.Click Share_1', 'X.1.Conversion Share_1',
    'X.2.Conversion Share_1', 'X.3.Conversion Share_1',
    'X.1.Clicked Asin 2', 'X.2.Clicked Asin 2', 'X.3.Clicked Asin 2',
    'X.1.Product_2', 'X.2.Product_2', 'X.3.Product_2', 'X.1.Click Share_2',
    'X.2.Click Share_2', 'X.3.Click Share_2', 'X.1.Conversion Share_2',
    'X.2.Conversion Share_2', 'X.3.Conversion Share_2',
    'X.1.Clicked Asin 3', 'X.2.Clicked Asin 3', 'X.3.Clicked Asin 3',
    'X.1.Product_3', 'X.2.Product_3', 'X.3.Product_3', 'X.1.Click Share_3',
    'X.2.Click Share_3', 'X.3.Click Share_3', 'X.1.Conversion Share_3',
    'X.2.Conversion Share_3', 'X.3.Conversion Share_3'
    ]

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
    'N': 13,'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
    'AA': 26, 'AB': 27, 'AC': 28, 'AD': 29, 'AE': 30, 'AF': 31, 'AG': 32, 'AH': 33, 'AI': 34, 'AJ': 35, 'AK': 36, 'AL': 37, 'AM': 38,
    'AN': 39,'AO': 40, 'AP': 41, 'AQ': 42, 'AR': 43, 'AS': 44, 'AT': 45, 'AU': 46, 'AV': 47, 'AW': 48, 'AX': 49,
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
# # 搜索词列表长度
# lenSWL12 = len(getColValues('12','B'))
# lenSWL11 = len(getColValues('11','B'))
# lenSWL10 = len(getColValues('10','B'))

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
# set_index('序号')

'''B
读取12月表单G、K、O栏之和小于40%的，按搜索排名升序填入
数据已处理，读取即可
'''
#添加表格字典
outXlsDict[keys[abcToCol['B']]] = getColValues('12','B')

'''C
判断B栏搜索词字数，调用变量时，设置行数
若该行搜索词（本表单B栏内容）为Christmas tree字数为2，此处填入2；Christmas light tree字数为3，此处填入3
'''
#初始化搜索词字数列表
searchWordCountList = []
for i in range(lenRows12):
    wordCount = getColValues('12','B')[i].count(' ')
    searchWordCountList.append(wordCount + 1)
#添加表格字典
outXlsDict[keys[abcToCol['C']]] = searchWordCountList

'''D
该搜索词在本表单中出现的次数
大小写、空格、顺序：spc = ['hello world','Hello World','helloworld','world hello']
只计大小写，其余不计数
'''
#转化小写，并用于比较计数的临时列表
tempList12 = []
for i in range(lenRows12):
    searchWordABC = getColValues('12','B')[i].lower()
    tempList12.append(searchWordABC)
# print(tempList)
appearTimes = []
for i in range(lenRows12):
    totalNum = tempList12.count(getColValues('12','B')[i].lower())
    appearTimes.append(totalNum)
    # print('D:',totalNum,'-times',searchWordList[i].lower())
# print(appearTimes)
#添加表格字典
outXlsDict[keys[abcToCol['D']]] = appearTimes

'''F
12月表单C栏内容
'''
CtoF_List = getColValues('12','C')
# CtoF_Value = memoryData12.iloc[1,abcTrans('C')]
# print('F:',CtoF_List,'-12 ranking No')
#添加表格字典
outXlsDict[keys[abcToCol['F']]] = CtoF_List

'''G
相同搜索词11月表单C栏内容，若无填0
表中有非int、float数据类型，例如：str、int64等，无法正常处理？？？？？？？？？？？？？？
'''
CtoG_List = getUnitCell('11','C')
#添加表格字典
outXlsDict[keys[abcToCol['G']]] = CtoG_List

'''H
相同搜索词10月表单C栏内容，若无填0
'''
CtoH_List = getUnitCell('10','C')
#添加表格字典
outXlsDict[keys[abcToCol['H']]] = CtoH_List

'''
E/J/I/K计算类循环
'''
for rowIndex in range(len(getUnitCell('12','B'))):
    '''E
    (F+G+H)/3
    '''
    # E_average  = round((CtoF_List[rowIndex] + CtoG_List[rowIndex] + CtoH_List[rowIndex])/3,2)
    # print('E:',E_average,'-ranking average (F+G+H)/3')

    '''J
    F-H
    '''
    # J_ = CtoF_List[rowIndex] - CtoH_List[rowIndex]
    # print('J:',J_,'-(F-H)')

    '''I
    1.若G、H单项或两项为0，该处填入New 
    2.若J=0，该处填入Steady
    3.若J为负数，该处填入Up
    4.若J为正数，该处填入Down
    '''
    # I_Value = ''
    # if CtoG_List[rowIndex] == 0 and CtoH_List[rowIndex] == 0:
    #     I_Value = 'New'
    # elif J_ == 0:
    #     I_Value = 'Steady'
    # elif J_ < 0:
    #     I_Value = 'Up'
    # elif J_ > 0:
    #     I_Value = 'Down'
    # print(rowIndex,'I:',I_Value,'- Trend')

    '''K
    F/G/H非0的数量
    '''
    # K_Value = ''
    # FGHList = [CtoF_List[rowIndex],CtoG_List[rowIndex],CtoH_List[rowIndex]]
    # for i in range(len(FGHList)):
    #     if FGHList.count('0') == i:
    #         K_Value = -i + 3
    # print('K:',K_Value,'- !=0 Num')

'''
L/M/N
G_K_O_1/G_K_O_2/G_K_O_3
'''
L_List = []
M_List = []
N_List = []
for i in range(lenRows12):
    L_List.append('///')
    M_List.append('///')
    N_List.append('///')
outXlsDict[keys[abcToCol['L']]] = L_List
outXlsDict[keys[abcToCol['M']]] = M_List
outXlsDict[keys[abcToCol['N']]] = N_List


'''
O/P/Q/R/S/T/U/V/W/X/Y/Z/AA/AB/AC/AD/AE/AF/AG/AH/AI/AJ/AK/AL/AM/AN/AO/AP/AQ/AR/AS/AT/AU/AV/AX
O:12月表单D栏内容
P:11月表单D栏内容
Q:10月表单D栏内容
R:12月表单E栏内容
S:11月表单E栏内容
T:10月表单E栏内容
一直到AX，按上述规律类推
'''
DtoO_List = getColValues('12','D')
#添加表格字典
outXlsDict[keys[abcToCol['O']]] = getColValues('12','D')
outXlsDict[keys[abcToCol['P']]] = getColValues('11','D')
outXlsDict[keys[abcToCol['Q']]] = getColValues('10','D')

outXlsDict[keys[abcToCol['R']]] = getColValues('12','E')
outXlsDict[keys[abcToCol['S']]] = getColValues('11','E')
outXlsDict[keys[abcToCol['T']]] = getColValues('10','E')

outXlsDict[keys[abcToCol['U']]] = getColValues('12','F')
outXlsDict[keys[abcToCol['V']]] = getColValues('11','F')
outXlsDict[keys[abcToCol['W']]] = getColValues('10','F')

outXlsDict[keys[abcToCol['X']]] = getColValues('12','G')
outXlsDict[keys[abcToCol['Y']]] = getColValues('11','G')
outXlsDict[keys[abcToCol['Z']]] = getColValues('10','G')

outXlsDict[keys[abcToCol['AA']]] = getColValues('12','H')
outXlsDict[keys[abcToCol['AB']]] = getColValues('11','H')
outXlsDict[keys[abcToCol['AC']]] = getColValues('10','H')

outXlsDict[keys[abcToCol['AD']]] = getColValues('12','I')
outXlsDict[keys[abcToCol['AE']]] = getColValues('11','I')
outXlsDict[keys[abcToCol['AF']]] = getColValues('10','I')

outXlsDict[keys[abcToCol['AG']]] = getColValues('12','J')
outXlsDict[keys[abcToCol['AH']]] = getColValues('11','J')
outXlsDict[keys[abcToCol['AI']]] = getColValues('10','J')

outXlsDict[keys[abcToCol['AJ']]] = getColValues('12','K')
outXlsDict[keys[abcToCol['AK']]] = getColValues('11','K')
outXlsDict[keys[abcToCol['AL']]] = getColValues('10','K')

outXlsDict[keys[abcToCol['AM']]] = getColValues('12','L')
outXlsDict[keys[abcToCol['AN']]] = getColValues('11','L')
outXlsDict[keys[abcToCol['AO']]] = getColValues('10','L')

outXlsDict[keys[abcToCol['AP']]] = getColValues('12','M')
outXlsDict[keys[abcToCol['AQ']]] = getColValues('11','M')
outXlsDict[keys[abcToCol['AR']]] = getColValues('10','M')

outXlsDict[keys[abcToCol['AS']]] = getColValues('12','N')
outXlsDict[keys[abcToCol['AT']]] = getColValues('11','N')
outXlsDict[keys[abcToCol['AU']]] = getColValues('10','N')

outXlsDict[keys[abcToCol['AV']]] = getColValues('12','O')
outXlsDict[keys[abcToCol['AW']]] = getColValues('11','O')
outXlsDict[keys[abcToCol['AX']]] = getColValues('10','O')

'''
从OPQ开始，循环处理
'''
# print(outXlsDict)
createXls = pd.DataFrame(outXlsDict)
# create_xls_home.set_index('序号')
createXls.to_excel('D:/data/Amazon/12_new.xlsx')