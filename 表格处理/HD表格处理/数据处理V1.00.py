#打开数据总表
import pandas as pd
import datetime

# import time
# from datetime import datetime
# from datetime import timedelta
print('=================================', '\n')
#path_xls_mac = '/Users/liufeng/Documents/Python/data/【恒大】采购物资情况台账.xlsx'
path_xls_win = 'D:/Python/data/【恒大】采购物资情况台账.xlsx'
pr = pd.read_excel(path_xls_win, sheet_name='采购台账')#, dtype={'要求到货时间': str}
print('yeah')

#表格属性参数、行数、列数、类型
x_shape = pr.shape
nrows = pr.shape[0]
ncols = pr.columns.size
x_type = type(pr)

print('表格行数：', nrows)
print('表格列数：', ncols)
print('表格规模：', x_shape, x_type)
#print(pr.head())#打印表格头5行
print('=================================', '\n')
# for iCol in range(ncols):#历遍列名+编号
#     print(str(iCol+1)+':'+pr.columns[iCol])
print('=================================', '\n')
print('打印df整表第38行第3列的值和数据类型：')
rc = pr.iloc[38,3]
print(rc, type(rc))
print('=================================', '\n')
# print(pr['要求到货时间'].head())
# print(pr['要求到货时间'].dtype)
print('打印要求到货时间values值：')
print(pr['要求到货时间'][:10].values)
# print(pr['要求到货时间'].date())
# print(pr['要求到货时间'].time())
print('=================================', '\n')
print('打印2020年6月的数据，不包含没有时间记录的数据：【方法一】')
sel_time = []#储存需要数据的所在行
input_time = '2020-06'#2020.6
jessie = pr['要求到货时间'].values
print(type(jessie))
for ss in range(0, nrows):
    #print(type(jessie[ss]))
    if type(jessie[ss]) == float:
        # print(ss+2, '--', jessie[ss], type(jessie[ss]), '浮点')
        pass
    elif type(jessie[ss]) == str:
        # print(ss+2, '--', jessie[ss], type(jessie[ss]), '字符串')
        pass
    # elif jessie[ss] == 'nan':
    #     print(ss+2, '--', jessie[ss], '无内容')
    #     pass
    # elif jessie[ss] == '已收货':
    #     print(ss+2, '--', jessie[ss], type(jessie[ss]), '已收货')
    # elif avl_time[itime].find(str('2019')):
    # elif input_time in jessie[ss]:
    #     print(ss+2, '--', jessie[ss][:10], type(jessie[ss][:10]))
    #     sel_time.append(ss+2)#将需要数据所在行添加进list
        
    elif input_time in str(jessie[ss]):
        
        jessie[ss] = jessie[ss].strftime("%Y-%m-%d")
        print(ss+2, '--', jessie[ss], type(jessie[ss]))
        sel_time.append(ss+2)#将需要数据所在行添加进list
    else:
        pass
print('【总共】:'+ str(len(sel_time)))

print('=================================', '\n')
##################################################################根据某列查找指定内容
#定位'要求到货时间'列
# avl_time = pr['要求到货时间'].values
# print('打印avl_time第38个元素的值和数类型：')
# print(avl_time[38], type(avl_time))
# print('=================================', '\n')
# sel_time = []#储存需要数据的所在行
# input_time = '2020-06'#2020.6

# print('打印2020年6月的数据，不包含没有时间记录的数据：【方法二，需要加'dtype={'要求到货时间': str}'】')
# for itime in range(0, nrows):
#     #print(itime, type(itime))
#     #print(itime, avl_time[itime], type(avl_time))
#     if type(avl_time[itime]) == float:
#         pass
#     elif avl_time[itime] == 'nan':
#         pass
#     elif avl_time[itime] == '已收货':
#         pass
#     # elif avl_time[itime].find(str('2019')):
#     elif input_time in avl_time[itime]:
#         print(itime+2, '--', avl_time[itime][:10], type(avl_time[itime][:10]))
#         sel_time.append(itime+2)#将需要数据所在行添加进list
#     else:        
#         pass
# print('【总共】:'+ str(len(sel_time)))  

#print(pr.loc[1033])

print('=================================', '\n')

# 定位'中标单位'列
xxx = pr['中标单位'].values
test = '六边'
print(type(xxx))
print(pr['中标单位'].dtype)
# data1 = data.set_index('要求到货时间')
# print(data1.loc['2020-06'].head())

sel_company = []
#历遍指定列中指定内容，并确定所在行
for iRow in range(0, nrows):#循环查找关键字，并打印完整值及所在行
    nlb = str(iRow+2)#转化成字符串
    LB = str(xxx[iRow])#转化成字符串
    #print(type(data))
    if LB.find(str(test)) == 2:#不匹配返回 -1 ，匹配返回 2
        print('【' + nlb + '】' + LB)#字符串，行+指定字段值
        #print(pr.iloc[iRow,4])#对应行的指定列的值
        sel_company.append(nlb)
    else:
        pass
print('【总共】:'+ str(len(sel_company)))

#格式化数据

#创建目标数据表并填充