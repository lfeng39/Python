import pandas as pd
import time

'''
V1.01将原始表单初始化，将百万条数据，按照GKO之和小于40的提取，缩减表单数据至30万条左右
'''
abcToCol = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
    'N': 13,'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
    'AA': 26, 'AB': 27, 'AC': 28, 'AD': 29, 'AE': 30, 'AF': 31, 'AG': 32, 'AH': 33, 'AI': 34, 'AJ': 35, 'AK': 36, 'AL': 37, 'AM': 38,
    'AN': 39,'AO': 40, 'AP': 41, 'AQ': 42, 'AR': 43, 'AS': 44, 'AT': 45, 'AU': 46, 'AV': 47, 'AW': 48, 'AX': 49,
}
#计时器开始
t1 = time.time()
print('读取原始表格中...')

# 将XLS中数据，储存到内存变量中，加快后续程序调用及计算速度
memoryData = pd.read_excel('D:/data/Amazon/原始数据/1月.xlsx',skiprows=1).fillna('///')

#表格长度
lenRows = memoryData.shape[0]#0为行，1为列
#表格宽度
widCol = memoryData.shape[1]#0为行，1为列

t2 = time.time()
print('完成读取，耗时：',round(t2-t1,2))
print('开始计算...')

# 判断数据类型并统一格式
# 遍历第一行每个单元格
# for i in range(widCol):
#     getCellType = type(memoryData.iloc[1,list(abcToCol.values())[i]])
#     # print(list(abcToCol.keys())[i],'--',type(getCellType),'/',getCellType)
#     if getCellType != int and getCellType != str and getCellType != float:
#         getColIndex = list(abcToCol.keys())[i]
#         print(getColIndex)

# 条件：GKO之和小于40
# 目的：提取整行数据添加到rowsList列表
rowsList = []
for i in range(1,lenRows):
    keyWordValue = [
        memoryData.iloc[i,abcToCol['G']],
        memoryData.iloc[i,abcToCol['K']],
        memoryData.iloc[i,abcToCol['O']],
        ]
    if type(keyWordValue[0]) == str:
        keyWordValue[0] = 0
    if type(keyWordValue[1]) == str:
        keyWordValue[1] = 0
    if type(keyWordValue[2]) == str:
        keyWordValue[2] = 0

    he = round(sum(keyWordValue)*100,2)

    if he < 40:
        rowsList.append(memoryData.loc[i,:])

# 创建新列表的key，创建新表的保存路径，输出处理后的表
rowsList.insert(0, memoryData.loc[0,:])
create_xls_home = pd.DataFrame(rowsList)
dataMonth = 'D:/data/Amazon/原始数据/' + '202201' +'.xlsx'
create_xls_home.to_excel(dataMonth, index = 0)#★★★★★★这里是创建的表格路径及名称，可自己修改单引号中的内容★★★★★★

#计时器结束
t3 = time.time()
print('完成计算,耗时：',round(t3-t2,2))
print('总耗时：',round(t3-t1,2))
