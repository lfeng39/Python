#打开数据总表
import pandas as pd
from openpyxl.styles import colors, PatternFill
import time

start = time.time()
######################################打开表格，读取数据############################################
path_xls_win = 'J:/Python/2021年订单执行及详细记录 - 副本.xlsx'#★★★★★★这里是你要读取的总表表格，路径及文件名可根据自己的需要自定义★★★★★★
r_xls = pd.read_excel(path_xls_win, sheet_name='订单执行', engine='openpyxl').fillna('///')#, dtype={'要求到货时间': str}
# r_xls = pd.read_excel(path_xls_win, sheet_name='订单执行')#, dtype={'要求到货时间': str}

#表格行数、列数
rows = r_xls.shape[0]#表格行数
cols = r_xls.shape[1]#表格列数
# print(cols)
totals = list(r_xls['结算金额'].values)
total = list(r_xls['已投资金额'].values)
act = list(r_xls['执行情况'].values)
mon = list(r_xls['实际利润'].values)
act_ = len(act)
# print(len(totals))
sum_01 = 0
for i in range(rows):
    sum_01 = sum_01 + totals[i]

sum_02 = 0
for i in range(rows):
    if act[i] == '是':
        sum_02 = sum_02 + total[i]
    else:
        pass
        
sum_03 = 0
for i in range(rows):
    sum_03 = sum_03 + mon[i]

sum_04 = 0
for i in range(rows):
    if act[i] == '是':
        sum_04 = sum_04 + totals[i]
    else:
        pass

sum_05 = 0
for i in range(rows):
    if act[i] == '否':
        sum_05 = sum_05 + totals[i]
    else:
        pass

sum_06 = 0
for i in range(rows):
    if act[i] == '是':
        sum_06 = sum_06 + mon[i]
    else:
        pass

print('已接订单金额:',round(sum_01,2))
print('已执行金额:',round(sum_04,2))
print('未执行金额:',round(sum_05,2))
print('已投资金额:',round(sum_02,2))
print('可预见的净利润:',round(sum_03,2))
print('以产生的净利润:',round(sum_06,2))
# print('已投资金额:',round(sum_02,2))
end = time.time()
print(end-start)







