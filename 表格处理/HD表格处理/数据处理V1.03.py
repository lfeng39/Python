#打开数据总表
import pandas as pd
import re
import datetime
######################################打开表格，读取数据############################################
#path_xls_mac = '/Users/liufeng/Documents/Python/data/【恒大】采购物资情况台账.xlsx'
path_xls_win = 'D:/Python/HD表格处理/data/采购物资情况台账(4).xlsx'#★★★★★★这里是你要读取的总表表格，路径及文件名可根据自己的需要自定义★★★★★★
r_xls = pd.read_excel(path_xls_win, sheet_name='采购台账')#, dtype={'要求到货时间': str}
print('1)成功读取数据库...')

#表格属性参数、行数、列数、类型
x_shape = r_xls.shape#表格行与列
nrows = r_xls.shape[0]#表格行数
ncols = r_xls.columns.size#表格列数
x_type = type(r_xls)

######################################按指定条件，获取到读取的数据行############################################
sel_rows = []#储存需要数据的所在行
input_time = '2020-07'#★★★★★★这里是你要选择的月份，格式不要改，直接改单引号中的数字即可★★★★★★
avl_time = r_xls['定标日期'].values#★★★★★★这里是你要选择的列名，直接修改单引号中间的文字即可★★★★★★
#print(type(avl_time))
for i in range(0, nrows):
    if type(avl_time[i]) == float:
        pass
    elif type(avl_time[i]) == str:
        pass
    elif input_time in str(avl_time[i]):
        sel_rows.append(i)#将需要数据所在行添加进list
    else:
        pass
print('2)成功抓取指定数据行...')
#########创建新表需要的数据列表，逐行数据添加，并对每行数据列表（rows_values_list）元素进行排序############################################

new_df = []#创建新表格总表内容数据，并以列表形式储存

sel_cols = [0, 19, 4, 10, 11, 12, 13, 14, 7, 6]#排序索引列表

######遍历指定的每一行######
for k in range(len(sel_rows)):
    row_values_list = []#{}#创建用于储存指定行的指定列的值的列表
    new_df.append(row_values_list)#讲获取到的指定行的数据添加到新表中
    
    ######遍历列值，并排序添加至列表######
    for i in sel_cols:
        ncols_values = str(r_xls.iloc[sel_rows[k], i])
        if i in [2, 3, 14, 15, 17, 20]:#将时间列缩减
            ncols_values = ncols_values[:10]
        elif ncols_values == 'nan':
            ncols_values = '///'
        row_values_list.append(ncols_values)
    
    ######插入缺损字段到新列表中，满足14个元素######
    row_values_list.insert(0, str(k+1))
    row_values_list.insert(2, '湖北公司')
    row_values_list.insert(6, '单价包干')
    row_values_list.insert(9, '/')
    row_values_list.insert(12, '/')
    row_values_list.insert(14, '/')
print('3)成功排列数据顺序，并创建新表数据...')
# print(type(row_values_list[10]))
# print(row_values_list[10])
# print(new_df)
###############################################################创建和排序结束#####################################################

######处理类别名称######
for k in range(len(new_df)):
    if new_df[k][1] == '工程':#★★★★★★这里及以下是类别名称的对应模块，可自行修改单引号中的内容★★★★★★
        new_df[k][1] = '采购-工程类'
    elif new_df[k][1] == '营销':
        new_df[k][1] = '采购-营销'
    elif new_df[k][1] == '资产':
        new_df[k][1] = '采购-行政类'
    elif new_df[k][1] == '物业':
        new_df[k][1] = '采购-物业类'
    else:
        pass

######处理项目名称######
for k in range(len(new_df)):#★★★★★★这里是公司名称与项目名称的对应模块，可自行修改单引号中的内容★★★★★★
    if new_df[k][2] == '武汉巴登城投资有限公司':
        new_df[k][2] = '武汉恒大科技旅游城'
    elif new_df[k][2] == '武汉楚水云山农业开发有限公司':
        new_df[k][2] = '武汉恒大时代新城'
    elif new_df[k][2] == '湖北合瑞旅游开发有限公司':
        new_df[k][2] = '武汉恒大文化旅游城'
    elif new_df[k][2] == '鄂州朗恒旅游开发有限公司':
        new_df[k][2] = '武汉恒大文化旅游城'
    elif new_df[k][2] == '湖北嘉祥旅游开发有限公司':
        new_df[k][2] = '武汉恒大文化旅游城'
    elif new_df[k][2] == '武汉出水云山农业开发有限公司':
        new_df[k][2] = '武汉恒大时代新城'
    elif '红安' in new_df[k][2]:
        new_df[k][2] = '红安恒大文化旅游康养城'
    elif '咸宁' in new_df[k][2]:
        new_df[k][2] = '咸宁梓山湖恒大养生谷'
    elif '江西' in new_df[k][2]:
        new_df[k][2] = '江西恒大养生谷'
    else:
        pass

######处理符合条件的项目名称(填充"使用位置数据")######
for k in range(len(new_df)):
    if new_df[k][13] == '朱佳茜' and new_df[k][15] != '///':
        new_df[k][4] = new_df[k][15]# + '到货'
    new_df[k].pop()#替换完成后，删除最后一个元素
print('4)成功处理新表数据...')

# print(len(new_df[0]),new_df[0][7],new_df[0][8],new_df[0][9])

######处理投标家数字段数据类型######
for k in range(len(sel_rows)):
    if new_df[k][8] == '///':
        pass
    else:
        new_df[k][8] = int(float(new_df[k][8]))
    
    # new_df[k][9] = '%.2f' % int(float(new_df[k][9]))
    if new_df[k][10] == '///':
        pass
    else:
        new_df[k][10] = '{:.2f}'.format(float(new_df[k][10]))#修改金额小数点
        aa = new_df[k][10]
        print(type(int(str(aa))))
    # print(type(new_df[k][9]), new_df[k][9])

# for i in new_df:
#     print(i)
# print(new_df[1][12])
######分表######
new_df_xn = []#创建咸宁表格内容数据，并以列表形式储存
new_df_other = []#创建其他表格内容数据，并以列表形式储存
for k in range(len(new_df)):
    if '咸宁' in new_df[k][2]:
        new_df_xn.append(new_df[k])
    else:
        new_df_other.append(new_df[k])

for x in range(len(new_df_xn)):
    new_df_xn[x][0] = x + 1
    # print(x, new_df_xn[x][0])

for x in range(len(new_df_other)):
    new_df_other[x][0] = x + 1
    # print(x, new_df_xn[x][0])

# for i in new_df_xn:
#     print(i)
# print('##############################################/n')
# for i in new_df_other:
#     print(i)
print('5)成功分表...')


new_col_name = ['序号', '专业类别', '地区公司', '楼盘名称', '工程项目名称', '中标单位', '计价方式', '招标方式', '投标家数', '规模', '定标总价', '定标日期', '合同签订日期', '经办人', '移交监察分室日期']
create_xls_home = pd.DataFrame(new_df, columns= new_col_name)#
create_xls_home = create_xls_home.set_index('序号')
create_xls_home.to_excel('D:/Python/HD表格处理/data/总表.xlsx')#★★★★★★这里是创建的表格路径及名称，可自己修改单引号中的内容★★★★★★
# print(create_xls_home)

create_xls_xn = pd.DataFrame(new_df_xn, columns= new_col_name)# index= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34],
create_xls_xn = create_xls_xn.set_index('序号')
create_xls_xn.to_excel('D:/Python/HD表格处理/data/咸宁.xlsx')#★★★★★★这里是创建的表格路径及名称，可自己修改单引号中的内容★★★★★★

create_xls_other = pd.DataFrame(new_df_other, columns= new_col_name)# index= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34],
create_xls_other = create_xls_other.set_index('序号')
create_xls_other.to_excel('D:/Python/HD表格处理/data/其他.xlsx')#★★★★★★这里是创建的表格路径及名称，可自己修改单引号中的内容★★★★★★

print('6)成功生成xls文件...')
print('7)OK,接下来你可以去查看生成的表格了！！！')
print('注意：运行本文件的时候，请关闭生成的表格，否则文件执行无效。执行完毕后，再打开查看。')
# # x = -3
# for x in range(10):
#     if x <= 10:
#         x += 1
#         print(x)

s = '2198.00'
b = int(float(s))
print(b)