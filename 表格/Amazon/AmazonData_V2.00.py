'''
V2.00
完成11、10月的行值提取
'''
import pandas as pd
import time

'''
初始化输出表格字典的keys
'''
abcToCol = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
    'N': 13,'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
    'AA': 26, 'AB': 27, 'AC': 28, 'AD': 29, 'AE': 30, 'AF': 31, 'AG': 32, 'AH': 33, 'AI': 34, 'AJ': 35, 'AK': 36, 'AL': 37, 'AM': 38,
    'AN': 39,'AO': 40, 'AP': 41, 'AQ': 42, 'AR': 43, 'AS': 44, 'AT': 45, 'AU': 46, 'AV': 47, 'AW': 48, 'AX': 49,
}
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
初始化字典，创建空字典，用来接收和储存最终表格内容
'''
dfDict = {
    keys[abcToCol['A']]: [],keys[abcToCol['B']]: [],keys[abcToCol['C']]: [],keys[abcToCol['D']]: [],keys[abcToCol['E']]: [],
    keys[abcToCol['F']]: [],keys[abcToCol['G']]: [],keys[abcToCol['H']]: [],keys[abcToCol['I']]: [],keys[abcToCol['J']]: [],
    keys[abcToCol['K']]: [],keys[abcToCol['L']]: [],keys[abcToCol['M']]: [],keys[abcToCol['N']]: [],keys[abcToCol['O']]: [],
    keys[abcToCol['P']]: [],keys[abcToCol['Q']]: [],keys[abcToCol['R']]: [],keys[abcToCol['S']]: [],keys[abcToCol['T']]: [],
    keys[abcToCol['U']]: [],keys[abcToCol['V']]: [],keys[abcToCol['W']]: [],keys[abcToCol['X']]: [],keys[abcToCol['Y']]: [],
    keys[abcToCol['Z']]: [],keys[abcToCol['AA']]: [],keys[abcToCol['AB']]: [],keys[abcToCol['AC']]: [],keys[abcToCol['AD']]: [],
    keys[abcToCol['AE']]: [],keys[abcToCol['AF']]: [],keys[abcToCol['AG']]: [],keys[abcToCol['AH']]: [],keys[abcToCol['AI']]: [],
    keys[abcToCol['AJ']]: [],keys[abcToCol['AK']]: [],keys[abcToCol['AL']]: [],keys[abcToCol['AM']]: [],keys[abcToCol['AN']]: [],
    keys[abcToCol['AO']]: [],keys[abcToCol['AP']]: [],keys[abcToCol['AQ']]: [],keys[abcToCol['AR']]: [],keys[abcToCol['AS']]: [],
    keys[abcToCol['AT']]: [],keys[abcToCol['AU']]: [],keys[abcToCol['AV']]: [],keys[abcToCol['AW']]: [],keys[abcToCol['AX']]: [],
}


# memoryData1001 = pd.read_excel('D:/data/Amazon/测试数据/10-3k-01.xlsx',skiprows=1).fillna('///')
# memoryData1002 = pd.read_excel('D:/data/Amazon/测试数据/10-3k-02.xlsx',skiprows=1).fillna('///')
# memoryData1003 = pd.read_excel('D:/data/Amazon/测试数据/10-3k-03.xlsx',skiprows=1).fillna('///')

# memoryData1101 = pd.read_excel('D:/data/Amazon/测试数据/11-3k-01.xlsx',skiprows=1).fillna('///')
# memoryData1102 = pd.read_excel('D:/data/Amazon/测试数据/11-3k-02.xlsx',skiprows=1).fillna('///')
# memoryData1103 = pd.read_excel('D:/data/Amazon/测试数据/11-3k-03.xlsx',skiprows=1).fillna('///')

# memoryData1201 = pd.read_excel('D:/data/Amazon/测试数据/12-3k-01.xlsx',skiprows=1).fillna('///')
# memoryData1202 = pd.read_excel('D:/data/Amazon/测试数据/12-3k-02.xlsx',skiprows=1).fillna('///')
# memoryData1203 = pd.read_excel('D:/data/Amazon/测试数据/12-3k-03.xlsx',skiprows=1).fillna('///')

# print(list(memoryData1201.iloc[5]))
# print(memoryData1201.iloc[:10])

#计时器开始
t1 = time.time()
print('读取原始表格中...')
'''
第一步：读取10、11、12三张表，并分别存储到内存变量-3k-01测试数据
'''
memoryData10 = pd.read_excel('D:/data/Amazon/测试数据/10-3k-01.xlsx',skiprows=1).fillna('///')
tx = time.time()
# print(memoryData10.info())
print('完成memoryData10读取，耗时：',round(tx-t1,2))

memoryData11 = pd.read_excel('D:/data/Amazon/测试数据/11-3k-01.xlsx',skiprows=1).fillna('///')
ty = time.time()
# print(memoryData11.info())
print('完成memoryData11读取，耗时：',round(ty-tx,2))

memoryData12 = pd.read_excel('D:/data/Amazon/测试数据/12-3k-01.xlsx',skiprows=1).fillna('///')
tz = time.time()
print('完成memoryData12读取，耗时：',round(tz-ty,2),'\n')

'''
比较模块
对比对象：12月搜索词元素
被对比对象：11、10月搜索词元素
取值：1）被对比对象存在对比对象，取需求列元素
取值：2）被对比对象不存在对比对象，取值0
'''
# 提取B列对比对象与被对比对象列表
colValues_12 = list(memoryData12[memoryData12.keys()[abcToCol['B']]].values)
colValues_11 = list(memoryData11[memoryData11.keys()[abcToCol['B']]].values)
colValues_10 = list(memoryData10[memoryData10.keys()[abcToCol['B']]].values)
t2 = time.time()
# print(memoryData12.info())
print('完成B的读取，耗时：',round(t2-tz,2),'\n')

# 先将三个列表的每个元素转换成可对比的小写
for i in range(len(colValues_12)):
    colValues_12[i] = colValues_12[i].lower()
for i in range(len(colValues_11)):
    colValues_11[i] = colValues_11[i].lower()
for i in range(len(colValues_10)):
    colValues_10[i] = colValues_10[i].lower()

t3 = time.time()
# print(memoryData12.info())
print('完成lower转化，耗时：',round(t3-t2,2),'\n')


# 基于12月表格的长度，获取其他表的行号
# 耗时最长
indexNumList_11 = []
indexNumList_10 = []
for i in range(len(memoryData12)):
    # 判断真假，取行号，或赋值
    if colValues_12[i] in colValues_11:
        indexNum11 = colValues_11.index(colValues_12[i])
        indexNumList_11.append(indexNum11)
        # print(indexNum)
    else:
        setNum = '///'
        indexNumList_11.append(setNum)
        # print(setNum)

t4 = time.time()
# print(memoryData12.info())
print('完成11月行号提取，耗时：',round(t4-t3,2))

for i in range(len(memoryData12)):
    # 判断真假，取行号，或赋值
    if colValues_12[i] in colValues_10:
        indexNum10 = colValues_10.index(colValues_12[i])
        indexNumList_10.append(indexNum10)
        # print(indexNum10)
    else:
        setNum = '///'
        indexNumList_10.append(setNum)

t5 = time.time()
# print(memoryData12.info())
print('完成10月行号提取，耗时：',round(t5-t4,2),'\n')

# print(indexNumList_11,len(indexNumList_11))
# print(len(indexNumList_10),indexNumList_10)
print('提取11月行号的长度:',len(indexNumList_11))
print('提取10月行号的长度:',len(indexNumList_10))
print('12月表格长度:',len(memoryData12),'\n')

# 初始化用于接收获取行值的列表
rowsValuesList_11 = []
rowsValuesList_10 = []
# 根据行号获取该行值
for i in range(len(indexNumList_11)):
    if indexNumList_11[i] == '///':
        c = [k for k in range(memoryData10.shape[1])]
        rowsValuesList_11.append(c)
        # pass
    else:
        rowsValuesList_11.append(list(memoryData11.loc[indexNumList_11[i]]))
        # print(list(memoryData1101.loc[indexNumList_11[i]]))

t6 = time.time()
print('完成11行值的提取，耗时：',round(t6-t5,2))

for i in range(len(indexNumList_10)):
    if indexNumList_10[i] == '///':
        c = [k for k in range(memoryData10.shape[1])]
        rowsValuesList_10.append(c)
        # pass
    else:
        rowsValuesList_10.append(list(memoryData10.loc[indexNumList_10[i]]))

t7 = time.time()
print('完成10行值的提取，耗时：',round(t7-t6,2),'\n')

print('提取11月行值的长度:',len(rowsValuesList_11))
print('提取10月行值的长度:',len(rowsValuesList_10),'\n')
# print(rowsValuesList_11[0],'\n',rowsValuesList_10[0])
print('总耗时：',round(t7-t1,2))

for i in range(10):
    print(rowsValuesList_11[i][1],'/',rowsValuesList_10[i][1],'/',colValues_12[i])

# print(rowsValuesList_11[0][abcToCol['B']])

# rowsValuesList_11.extend(rowsValuesList_10)
# # 根据行号获取该行值
# createXls = pd.DataFrame(rowsValuesList_11)
# # create_xls_home.set_index('序号')
# createXls.to_excel('D:/data/Amazon/te.xlsx')
