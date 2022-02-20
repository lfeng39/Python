import pandas as pd
import time
from openpyxl import Workbook
import numpy

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
#计时器开始
t1 = time.time()
print('读取原始表格中...')
'''
第一步：读取10、11、12三张表，并分别存储到内存变量
'''
# memoryData = pd.read_excel('D:/data/Amazon/测试数据/testData.xlsx',skiprows=1).fillna('///')
memoryData10 = pd.read_excel('D:/data/Amazon/测试数据/10-3k-01.xlsx',skiprows=1).fillna('///')
tx = time.time()
print('完成memoryData10读取，耗时：',round(tx-t1,2))

memoryData11 = pd.read_excel('D:/data/Amazon/测试数据/11-3k-01.xlsx',skiprows=1).fillna('///')
ty = time.time()
print('完成memoryData11读取，耗时：',round(ty-tx,2))

memoryData12 = pd.read_excel('D:/data/Amazon/测试数据/12-3k-01.xlsx',skiprows=1).fillna('///')
tz = time.time()
print('完成memoryData12读取，耗时：',round(tz-ty,2))

def dfXLS(xls):
    if xls == '10':
        return memoryData10
    elif xls == '11':
        return memoryData11
    elif xls == '12':
        return memoryData12
    # elif xls == 'testData':
    #     return memoryData
# print(type(dfXLS('11')))
t2 = time.time()
print('总耗时：',round(t2-t1,2),'\n')
print('开始计算...')

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
print(lenRows11)
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

            if type(getUnitCell) == ' ' or getUnitCell == 'nan' or getUnitCell == '///' or getUnitCell == '-':
                getUnitCell = 0

            freqRankList.append(getUnitCell)

        else:
            freqRankList.insert(i,0)

    return freqRankList
t3 = time.time()
print('搜索词比较完成，耗时：',round(t3-t2,2),'\n')
print('开始初始化新表的字段列表...')

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

'''
初始化数据
'''
B_List_12 = getColValues('12','B')
'''C
判断B栏搜索词字数，调用变量时，设置行数
若该行搜索词（本表单B栏内容）为Christmas tree字数为2，此处填入2；Christmas light tree字数为3，此处填入3
'''
#初始化搜索词字数列表
searchWordCountList = []
for i in range(lenRows12):
    wordCount = B_List_12[i].count(' ')
    searchWordCountList.append(wordCount + 1)
    # print('CCC--',i,searchWordCountList)
tc = time.time()
print('C完成，耗时：',round(tc-t3,2),'\n')
print('D...')
'''D
该搜索词在本表单中出现的次数
大小写、空格、顺序：spc = ['hello world','Hello World','helloworld','world hello']
只计大小写，其余不计数
'''
#转化小写，并用于比较计数的临时列表
tempList12 = []
for i in range(lenRows12):
    searchWordABC = B_List_12[i].lower()
    tempList12.append(searchWordABC)
    # print('DDD--',i,tempList12)
# print(tempList)
appearTimes = []
for i in range(lenRows12):
    totalNum = tempList12.count(B_List_12[i].lower())
    appearTimes.append(totalNum)
    # print('DDD--',i,totalNum,'-times')
# print(appearTimes)
t4 = time.time()
print('D完成，耗时：',round(t4-tc,2),'\n')
print('F...')

'''F
12月表单C栏内容
'''
CtoF_List = getColValues('12','C')
# CtoF_Value = memoryData12.iloc[1,abcTrans('C')]
# print('F:',CtoF_List,'-12 ranking No')
t5 = time.time()
print('F完成，耗时：',round(t5-t4,2),'\n')
print('G/H计算，调用getUnitCell函数运算，耗时很长...')

'''G
相同搜索词11月表单C栏内容，若无填0
表中有非int、float数据类型，例如：str、int64等
处理数据类型，重新构建列表
'''
CtoG_List = getUnitCell('11','C')
print(CtoG_List[1],'haha')
# 清理数据类型
CtoGNewList = []
for i in range(lenRows11):
    # print(CtoG_List[i],type(CtoG_List[i]))
    if type(CtoG_List[i]) != int and type(CtoG_List[i]) == str:
        CtoG_List[i] = 0
    elif type(CtoG_List[i]) != int and type(CtoG_List[i]) != str:
        CtoG_List[i] = int(CtoG_List[i])
    CtoGNewList.append(CtoG_List[i])
    # print('new',CtoG_List[i],type(CtoGNewList[i]))
t6 = time.time()
print('lenRows11长度：',lenRows11)
print('CtoG_List长度：',len(CtoG_List),CtoG_List[0])
print('CtoGNewList长度：',len(CtoGNewList),CtoGNewList[0])
print('G完成，耗时：',round(t6-t5,2),'\n')
print('H开始...')

'''H
相同搜索词10月表单C栏内容，若无填0
'''
CtoH_List = getUnitCell('10','C')
# 清理数据类型
CtoHNewList = []
for i in range(lenRows10):
    # print(CtoH_List[i],type(CtoH_List[i]))
    if type(CtoH_List[i]) != int and type(CtoH_List[i]) == str:
        CtoH_List[i] = 0
    elif type(CtoH_List[i]) != int and type(CtoH_List[i]) != str:
        CtoH_List[i] = int(CtoH_List[i])
    CtoHNewList.append(CtoH_List[i])
    # print('new',CtoH_List[i],type(CtoHNewList[i]))

t7 = time.time()
print('H完成，耗时：',round(t7-t6,2),'\n')
print('完成C/D/F/G/H的构建，耗时：',round(t7-t3,2),'\n')
print('开始计算E/J/I...')
'''
E/J/I/K计算类循环
'''
# 初始化E/J/I/K列表
E_averageList = []
J_List = []
I_valueList = []
K_valueList = []
for rowIndex in range(len(getUnitCell('12','B'))):
    '''E
    (F+G+H)/3
    '''
    E_average  = round((CtoF_List[rowIndex] + CtoGNewList[rowIndex] + CtoHNewList[rowIndex])/3,2)
    # print('E:',E_average,'-ranking average (F+G+H)/3')
    E_averageList.append(E_average)

    '''J
    F-H
    '''
    J_ = CtoF_List[rowIndex] - CtoHNewList[rowIndex]
    # print('J:',J_,'-(F-H)')
    J_List.append(J_)

    '''I
    1.若G、H单项或两项为0，该处填入New 
    2.若J=0，该处填入Steady
    3.若J为负数，该处填入Up
    4.若J为正数，该处填入Down
    '''
    I_value = ''
    if CtoGNewList[rowIndex] == 0 and CtoHNewList[rowIndex] == 0:
        I_Value = 'New'
    elif J_ == 0:
        I_Value = 'Steady'
    elif J_ < 0:
        I_Value = 'Up'
    elif J_ > 0:
        I_Value = 'Down'
    # print(rowIndex,'I:',I_Value,'- Trend')
    I_valueList.append(I_Value)

    '''K
    F/G/H非0的数量
    经过数据类型的处理后，FGHList中的元素均为int或float类型，0作为计数元素，也需要是int或float类型
    '''
    K_value = ''
    FGHList = [CtoF_List[rowIndex],CtoGNewList[rowIndex],CtoHNewList[rowIndex]]
    for i in range(len(FGHList)):
        if FGHList.count(0) == i:
            K_value = -i + 3
    # print(FGHList)
    # print('K:',K_value,type(K_value))
    K_valueList.append(K_value)
# print(K_valueList)
t8 = time.time()
print('完成E/J/I/K的循环计算，耗时：',round(t8-t7,2),'\n')
print('开始计算L/M/N及剩余构建...')

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



outXlsDict[keys[abcToCol['B']]] = getColValues('12','B')
outXlsDict[keys[abcToCol['C']]] = searchWordCountList
outXlsDict[keys[abcToCol['D']]] = appearTimes
outXlsDict[keys[abcToCol['E']]] = E_averageList

outXlsDict[keys[abcToCol['F']]] = CtoF_List
outXlsDict[keys[abcToCol['G']]] = CtoGNewList
outXlsDict[keys[abcToCol['H']]] = CtoHNewList

outXlsDict[keys[abcToCol['I']]] = I_valueList
outXlsDict[keys[abcToCol['J']]] = J_List
outXlsDict[keys[abcToCol['K']]] = K_valueList

outXlsDict[keys[abcToCol['L']]] = L_List
outXlsDict[keys[abcToCol['M']]] = M_List
outXlsDict[keys[abcToCol['N']]] = N_List

t9 = time.time()
print('计算类列表构建完成,耗时：',round(t9 - t3,2),'\n')
print('开始读取类列表构建O-AX列...')

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

#计时器结束
t10 = time.time()
print('完成读取类列表构建O-AX列,耗时：',round(t10 - t9,2),'\n')
print('总耗时：',round(t10 - t1,2))

'''
从OPQ开始，循环处理
'''
# print(len(outXlsDict))
createXls = pd.DataFrame(outXlsDict)
# create_xls_home.set_index('序号')
createXls.to_excel('D:/data/Amazon/12_big.xlsx')