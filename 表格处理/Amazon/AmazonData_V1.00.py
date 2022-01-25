#打开数据总表
import pandas as pd
import re
import datetime
import time


def abcTrans(str):
    abcNumber = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
        'N': 13,'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }
    return abcNumber[str]
#计时器开始
start = time.time()
def dfXLS():
    path_xls_win = 'D:/data/Amazon/12月表单 - 3000.xlsx'#★★★★★★这里是你要读取的总表表格，路径及文件名可根据自己的需要自定义★★★★★★
    df_xls = pd.read_excel(path_xls_win)#, dtype={'要求到货时间': str}
    # print('1)成功读取数据库...')
    return df_xls
#表格属性参数、行数、列数、类型
memoryData = dfXLS()
x_shape = memoryData.shape#表格行与列
nrows = memoryData.shape[0]#表格行数
ncols = memoryData.shape[1]#表格列数
print(x_shape)

rowsList = []
for i in range(1,10):
    get_G_Data = memoryData.iloc[i,abcTrans('G')]
    get_K_Data = memoryData.iloc[i,abcTrans('K')]
    get_O_Data = memoryData.iloc[i,abcTrans('O')]
    he = round((get_G_Data + get_K_Data + get_O_Data)*100, 2)

    if he < 40:
        rowsList.append(memoryData.loc[i,:])
        # memoryData.drop([i])
    else:
        # rowsList.append(i)
        pass

rowsList.insert(0, memoryData.loc[0,:])
create_xls_home = pd.DataFrame(rowsList)
create_xls_home.to_excel('D:/data/Amazon/12_new.xlsx', index = 0)#★★★★★★这里是创建的表格路径及名称，可自己修改单引号中的内容★★★★★★

#计时器结束
end = time.time()
total_time = end - start
print(total_time)
