#打开数据总表
import pandas as pd
import datetime

print('=================================', '\n')
#path_xls_mac = '/Users/liufeng/Documents/Python/data/【恒大】采购物资情况台账.xlsx'
path_xls_win = 'D:/Python/data/【恒大】采购物资情况台账.xlsx'
r_xls = pd.read_excel(path_xls_win, sheet_name='采购台账')#, dtype={'要求到货时间': str}
print('yeah')

#表格属性参数、行数、列数、类型
x_shape = r_xls.shape#表格行与列
nrows = r_xls.shape[0]#表格行数
ncols = r_xls.columns.size#表格列数
x_type = type(r_xls)
# print('表格行数：', nrows)
# print('表格列数：', ncols)
# print('表格规模：', x_shape, x_type)

print('=================================', '\n')
#历遍列名，并保存到变量中
ncols_name = r_xls.columns
ncols_name_list = []#创建用于储存全部列名字段的列表
for i in range(len(ncols_name)):
    ncols_name_list.append(str(i+1)+'/'+ ncols_name[i])
print(ncols_name_list)

print('=================================', '\n')
# print('打印2020年6月的数据，不包含没有时间记录的数据：【方法一】')
sel_rows = []#储存需要数据的所在行
input_time = '2020-06'#2020.6
avl_time = r_xls['定标日期'].values
#print(type(avl_time))
for i in range(0, nrows):
    if type(avl_time[i]) == float:
        #print(avl_time)
        pass
    elif type(avl_time[i]) == str:
        #print(avl_time)
        pass
    elif input_time in str(avl_time[i]):
        #avl_time[i] = str(avl_time[i])[:10]#avl_time[i].strftime("%Y-%m-%d")#
        sel_rows.append(i)#将需要数据所在行添加进list
    else:
        pass
print('【总共】:', len(sel_rows))
# sel_rows = sel_rows[0]
# rc = pr.iloc[sel_rows,0]#指定指定某行某列，不含index和col
# rc01 = pr.loc[[sel_rows],['要求到货时间']]#指定指定某行某列，含index和col
# print(rc01)

######################################对nrows_values_list值的位置进行排序############################################
new_df = []#创建新表格内容数据，并以列表形式储存
new_df_xn = []
new_df_other = []
sel_cols = [0, 19, 4, 10, 11, 12, 13, 14, 7]#创建用于储存选取指定列序号的列表
for k in range(len(sel_rows)):#执行次数为选择的行的数量
    rows_values_list = []#{}#创建用于储存指定行的指定列的值的列表
    new_df.append(rows_values_list)#讲获取到的指定行的数据添加到新表中
    for i in sel_cols:#按指定序号遍历列值，并按序号的位置进行储存
        ncols_values = str(r_xls.iloc[sel_rows[k], i])
        if ncols_values == 'nan':#将指定列值为空的，替换成/
            ncols_values = '/'
        elif i in [2, 3, 14, 15, 17, 20]:#将时间列缩减
            ncols_values = ncols_values[:10]
        else:
            pass
        # rows_values_list[i] = ncols_values#储存为字典模式
        # rows_values_list.append(str(i) + ':' + ncols_values)
        rows_values_list.append(ncols_values)
    rows_values_list.insert(0, str(k+1))
    rows_values_list.insert(5, '单价包干')
    rows_values_list.insert(8, '/')
    rows_values_list.insert(11, '/')
    rows_values_list.insert(13, '/')
    if '咸宁' in rows_values_list[2]:
        # print(rows_values_list)
        xn_rows_values_list = rows_values_list
        new_df_xn.append(xn_rows_values_list)
    else:
        other_rows_values_list = rows_values_list
        new_df_other.append(other_rows_values_list)

# print(rows_values_list)
# for i in new_df_other:
#     print(i)
# print(new_df)



print('=================================', '\n')
# #创建目标数据表并填充
# _serial_dict = {0: '序号', #序号
#                 1: ncols_name_list[0], #专业类别
#                 2: ncols_name_list[19], #楼盘名称
#                 3: ncols_name_list[4], #工程项目名称
#                 4: ncols_name_list[10], #中标单位
#                 5: '单价包干', #计价方式
#                 6: ncols_name_list[11], #招标方式
#                 7: ncols_name_list[12], #投标家数
#                 8: '/', #规模
#                 9: ncols_name_list[13],#定标总价 
#                 10: ncols_name_list[14], #定标日期
#                 11: '/', #合同签订日期
#                 12: ncols_name_list[7],#经办人
#                 13: '/'}#移交监察分室日期
# # _serial_dict[1] = ncols_name_list[19]
# # _serial_dict[33] = 'kris'
# # print(_serial_dict)
# # print(len(_serial_dict))
# new_df_01_list = zip(
#                         ['序号', '专业类别', '楼盘名称', '工程项目名称', '中标单位', '计价方式', '招标方式', '投标家数', '规模', '定标总价', '定标日期', '合同签订日期', '经办人', '移交监察分室日期'], 
#                         ['序号', ncols_name_list[0], ncols_name_list[19], ncols_name_list[4], ncols_name_list[10], '单价包干', ncols_name_list[11], ncols_name_list[12], '/', ncols_name_list[13], ncols_name_list[14], '/', ncols_name_list[7], '/']
#                     )
# new_df_01_dict = {'序号': '序号', '专业类别': '项目类别', '楼盘名称': '项目公司', '工程项目名称': '项目名称', '中标单位': '中标单位', '计价方式': '单价包干', '招标方式': '招标方式', '投标家数': '投标家数', '规模': '/', '定标总价': '订单金额', '定标日期': '定标日期', '合同签订日期': '/', '经办人': '责任人', '移交监察分室日期': '/'}

# # print(dict(new_df_01_list))
# # print(new_df_01_list)
# # print(new_df_01_dict)
###########################################创建xls表列名_colName_01##########################################################################
new_col_name = ['序号', '专业类别', '楼盘名称', '工程项目名称', '中标单位', '计价方式', '招标方式', '投标家数', '规模', '定标总价', '定标日期', '合同签订日期', '经办人', '移交监察分室日期']
create_xls_c = pd.DataFrame(new_df, columns= new_col_name)# index= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34],
create_xls_c.to_excel('D:/Python/data/总表.xlsx')

create_xls_b = pd.DataFrame(new_df_xn, columns= new_col_name)# index= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34],
create_xls_b.to_excel('D:/Python/data/咸宁.xlsx')

create_xls_a = pd.DataFrame(new_df_other, columns= new_col_name)# index= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34],
create_xls_a.to_excel('D:/Python/data/其他.xlsx')
