#打开数据总表
import pandas as pd
from openpyxl.styles import colors, PatternFill
import time

start = time.time()

# 初始化数据来源属性
# path_file = 'J:/【【【恒大报价】】】/2021年订单执行及详细记录.xlsx'
path_file = '/Volumes/LeoStudio/【【【恒大报价】】】/2021年订单执行及详细记录.xlsx'
sheet_name = '订单执行'
# 声明全局变量，提高运算效率
# 操作表格
pd_xls = pd.read_excel(path_file, sheet_name=sheet_name)
# 操作列名
col_name_list = list(pd_xls)

rows = pd_xls.shape[0]#表格行数
cols = pd_xls.shape[1]#表格列数

# 取任意值，包括：list、int、string
def get_values(values):
    if values in col_name_list:
        content_list = list(pd_xls[values].values)
        return content_list

sum_01 = 0
sum_02 = 0
sum_03 = 0
sum_04 = 0
sum_05 = 0
for i in range(rows):
    sum_01 = sum_01 + get_values('结算金额')[i]
    sum_04 = sum_04 + get_values('实际利润')[i]
    sum_05 = sum_05 + get_values('计划投资金额')[i]
    if get_values('执行情况')[i] == '是':
        sum_02 = sum_02 + get_values('结算金额')[i]
        sum_03 = sum_03 + get_values('已投资金额')[i]
    else:
        pass

print('已接订单金额:',round(sum_01,2))
print('已执行订单金额:',round(sum_02,2))
print('已投资金额:',round(sum_03,2))
print('预计净利润:',round(sum_04,2))
print('成本利润率:',round((sum_04/sum_05)*100,2),'%')
end = time.time()
print(end-start)




