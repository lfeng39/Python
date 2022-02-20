'''
V2.01
完成创建新表格的数据，按行创建
完成DF创建，并写入表格

'''
from operator import index
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


#计时器开始
t1 = time.time()
print('读取原始表格中...')
'''
第一步：读取10、11、12三张表，并分别存储到内存变量、-3k-01-测试数据-原始数据
'''
pd_10 = pd.read_excel('D:/data/Amazon/原始数据/11.xlsx',skiprows=1).fillna('///')
tx = time.time()
print('完成memoryData10读取，耗时：',round(tx-t1,2))

pd_11 = pd.read_excel('D:/data/Amazon/原始数据/12月表单.xlsx',skiprows=1).fillna('///')
ty = time.time()
print('完成memoryData11读取，耗时：',round(ty-tx,2))

pd_12 = pd.read_excel('D:/data/Amazon/原始数据/202201.xlsx',skiprows=1).fillna('///')
tz = time.time()
print('完成memoryData12读取，耗时：',round(tz-ty,2),'\n')
print('读表总耗时：',round(tz-t1,2))

'''
比较模块
对比对象：12月搜索词元素
被对比对象：11、10月搜索词元素
取值：1）被对比对象存在对比对象，取需求列元素
取值：2）被对比对象不存在对比对象，取值0
'''
# 提取B列对比对象与被对比对象列表
colValues_12 = list(pd_12[pd_12.keys()[abcToCol['B']]].values)
colValues_11 = list(pd_11[pd_11.keys()[abcToCol['B']]].values)
colValues_10 = list(pd_10[pd_10.keys()[abcToCol['B']]].values)
t2 = time.time()
print('完成B的读取，耗时：',round(t2-tz,2),'\n')

# 先将三个B栏列表的每个元素转换成可对比的小写
# print('abc?',colValues_12[0],colValues_12[3])
for i in range(len(colValues_12)):
    colValues_12[i] = colValues_12[i].lower()
for i in range(len(colValues_11)):
    colValues_11[i] = colValues_11[i].lower()
for i in range(len(colValues_10)):
    colValues_10[i] = colValues_10[i].lower()
# print('abc:',colValues_12[0],colValues_12[3])
t3 = time.time()
print('完成lower转化，耗时：',round(t3-t2,2),'\n')

# 基于12月表格的长度，获取其他表的行号
# 耗时最长
# 初始化用于接收行号的列表，列表最终为不规则的行号序列
indexNumList_11 = []
indexNumList_10 = []
# 当获取的行号
# 获取11月表中，存在的搜索词的行号
for i in range(len(pd_12)):
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
print('完成11月行号提取，耗时：',round(t4-t3,2))

# 获取10月表中，存在的搜索词的行号
for i in range(len(pd_12)):
    # 判断真假，取行号，或赋值
    if colValues_12[i] in colValues_10:
        indexNum10 = colValues_10.index(colValues_12[i])
        indexNumList_10.append(indexNum10)
    else:
        setNum = '///'
        indexNumList_10.append(setNum)
t5 = time.time()
print('完成10月行号提取，耗时：',round(t5-t4,2),'\n')

print('提取11月行号的长度:',len(indexNumList_11))
print('提取10月行号的长度:',len(indexNumList_10))
print('12月表格长度:',len(pd_12),'\n')

# 初始化用于接收获取行值的列表
# 行值数据类型为列表
rowsValuesList_11 = []
rowsValuesList_10 = []
# 获取11月行值，行值以列表向rowsValuesList_11添加
for i in range(len(indexNumList_11)):
    if indexNumList_11[i] == '///':
        rowsValuesList_11.append([k*0 for k in range(pd_11.shape[1])])
        # pass
    else:
        rowsValuesList_11.append(list(pd_11.loc[indexNumList_11[i]]))
        # print(list(memoryData1101.loc[indexNumList_11[i]]))
t6 = time.time()
print('完成11行值的提取，耗时：',round(t6-t5,2))

# 获取10月行值，行值以列表向rowsValuesList_10添加
for i in range(len(indexNumList_10)):
    if indexNumList_10[i] == '///':
        rowsValuesList_10.append([k*0 for k in range(pd_10.shape[1])])
        # pass
    else:
        rowsValuesList_10.append(list(pd_10.loc[indexNumList_10[i]]))
t7 = time.time()
print('完成10行值的提取，耗时：',round(t7-t6,2),'\n')

print('提取11月行值的长度:',len(rowsValuesList_11))
print('提取10月行值的长度:',len(rowsValuesList_10),'\n')

allRows = []
for i in range(pd_12.shape[0]):
    J_value = pd_12.iloc[i,abcToCol['C']] - rowsValuesList_10[i][abcToCol['C']]
    I_value = ''
    if rowsValuesList_11[i][abcToCol['C']] == 0 and rowsValuesList_10[i][abcToCol['C']] == 0:
        I_value = 'New'
    elif J_value == 0:
        I_value = 'Steady'
    elif J_value < 0:
        I_value = 'Up'
    elif J_value > 0:
        I_value = 'Down'
    
    FGH = [
        pd_12.iloc[i,abcToCol['C']],
        rowsValuesList_11[i][abcToCol['C']],
        rowsValuesList_10[i][abcToCol['C']]
        ]
    # print(FGH)
    # for k in range(len(FGH)):
    #     if FGH.count(0) == k:
    #         K_value = -k + 3
    K_value = 0
    if FGH.count(0) == 3:
        K_value = 0
    elif FGH.count(0) == 2:
        K_value = 1
    elif FGH.count(0) == 1:
        K_value = 3

    newXlsRowList = []
    newXlsRowList.insert(abcToCol['A'], i+1)
    newXlsRowList.insert(abcToCol['B'], pd_12.iloc[i,abcToCol['B']])
    newXlsRowList.insert(abcToCol['C'], colValues_12[i].count(' ') + 1)
    newXlsRowList.insert(abcToCol['D'], colValues_12.count(colValues_12[i]))
    newXlsRowList.insert(abcToCol['E'], round((pd_12.iloc[i,abcToCol['C']]+rowsValuesList_11[i][abcToCol['C']]+rowsValuesList_10[i][abcToCol['C']])/3,2))
    newXlsRowList.insert(abcToCol['F'], pd_12.iloc[i,abcToCol['C']])
    newXlsRowList.insert(abcToCol['G'], rowsValuesList_11[i][abcToCol['C']])
    newXlsRowList.insert(abcToCol['H'], rowsValuesList_10[i][abcToCol['C']])
    newXlsRowList.insert(abcToCol['I'], I_value)
    newXlsRowList.insert(abcToCol['J'], J_value)
    newXlsRowList.insert(abcToCol['K'], K_value)
    newXlsRowList.insert(abcToCol['L'], 'L')
    newXlsRowList.insert(abcToCol['M'], 'M')
    newXlsRowList.insert(abcToCol['N'], 'N')
    newXlsRowList.insert(abcToCol['O'], pd_12.iloc[i,abcToCol['D']])
    newXlsRowList.insert(abcToCol['P'], rowsValuesList_11[i][abcToCol['D']])
    newXlsRowList.insert(abcToCol['Q'], rowsValuesList_10[i][abcToCol['D']])
    newXlsRowList.insert(abcToCol['R'], pd_12.iloc[i,abcToCol['E']])
    newXlsRowList.insert(abcToCol['S'], rowsValuesList_11[i][abcToCol['E']])
    newXlsRowList.insert(abcToCol['T'], rowsValuesList_10[i][abcToCol['E']])
    newXlsRowList.insert(abcToCol['U'], pd_12.iloc[i,abcToCol['F']])
    newXlsRowList.insert(abcToCol['V'], rowsValuesList_11[i][abcToCol['F']])
    newXlsRowList.insert(abcToCol['W'], rowsValuesList_10[i][abcToCol['F']])
    newXlsRowList.insert(abcToCol['X'], pd_12.iloc[i,abcToCol['G']])
    newXlsRowList.insert(abcToCol['Y'], rowsValuesList_11[i][abcToCol['G']])
    newXlsRowList.insert(abcToCol['Z'], rowsValuesList_10[i][abcToCol['G']])
    newXlsRowList.insert(abcToCol['AA'], pd_12.iloc[i,abcToCol['H']])
    newXlsRowList.insert(abcToCol['AB'], rowsValuesList_11[i][abcToCol['H']])
    newXlsRowList.insert(abcToCol['AC'], rowsValuesList_10[i][abcToCol['H']])
    newXlsRowList.insert(abcToCol['AD'], pd_12.iloc[i,abcToCol['I']])
    newXlsRowList.insert(abcToCol['AE'], rowsValuesList_11[i][abcToCol['I']])
    newXlsRowList.insert(abcToCol['AF'], rowsValuesList_10[i][abcToCol['I']])
    newXlsRowList.insert(abcToCol['AG'], pd_12.iloc[i,abcToCol['J']])
    newXlsRowList.insert(abcToCol['AH'], rowsValuesList_11[i][abcToCol['J']])
    newXlsRowList.insert(abcToCol['AI'], rowsValuesList_10[i][abcToCol['J']])
    newXlsRowList.insert(abcToCol['AJ'], pd_12.iloc[i,abcToCol['K']])
    newXlsRowList.insert(abcToCol['AK'], rowsValuesList_11[i][abcToCol['K']])
    newXlsRowList.insert(abcToCol['AL'], rowsValuesList_10[i][abcToCol['K']])
    newXlsRowList.insert(abcToCol['AM'], pd_12.iloc[i,abcToCol['L']])
    newXlsRowList.insert(abcToCol['AN'], rowsValuesList_11[i][abcToCol['L']])
    newXlsRowList.insert(abcToCol['AO'], rowsValuesList_10[i][abcToCol['L']])
    newXlsRowList.insert(abcToCol['AP'], pd_12.iloc[i,abcToCol['M']])
    newXlsRowList.insert(abcToCol['AQ'], rowsValuesList_11[i][abcToCol['M']])
    newXlsRowList.insert(abcToCol['AR'], rowsValuesList_10[i][abcToCol['M']])
    newXlsRowList.insert(abcToCol['AS'], pd_12.iloc[i,abcToCol['N']])
    newXlsRowList.insert(abcToCol['AT'], rowsValuesList_11[i][abcToCol['N']])
    newXlsRowList.insert(abcToCol['AU'], rowsValuesList_10[i][abcToCol['N']])
    newXlsRowList.insert(abcToCol['AV'], pd_12.iloc[i,abcToCol['O']])
    newXlsRowList.insert(abcToCol['AW'], rowsValuesList_11[i][abcToCol['O']])
    newXlsRowList.insert(abcToCol['AX'], rowsValuesList_10[i][abcToCol['O']])
    allRows.append(newXlsRowList)
print(newXlsRowList,len(allRows),len(newXlsRowList))
t8 = time.time()
print('完成新表格的数据创建，耗时：',round(t8-t7,2),'\n')

createXls = pd.DataFrame(allRows,columns=keys)
t9 = time.time()
print('完成DF创建，耗时：',round(t9-t8,2),'\n')

createXls.to_excel('D:/data/Amazon/brandAnalyze_202202.xlsx', index = False)
t10 = time.time()
print('完成数据写入，耗时：',round(t10-t9,2),'\n')

print('总耗时：',round(t10-t1,2))