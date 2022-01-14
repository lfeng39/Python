#打开数据总表
import pandas as pd
import re
import datetime
######################################按指定条件，获取到读取的数据行############################################
#path_xls_mac = '/Users/liufeng/Documents/Python/data/【恒大】采购物资情况台账.xlsx'
path_xls_win = 'D:/Python/data/采购物资情况台账(4).xlsx'
r_xls = pd.read_excel(path_xls_win, sheet_name='采购台账')#, dtype={'要求到货时间': str}
print('yeah')

#表格属性参数、行数、列数、类型
x_shape = r_xls.shape#表格行与列
nrows = r_xls.shape[0]#表格行数
ncols = r_xls.columns.size#表格列数
x_type = type(r_xls)

sel_rows = []#储存需要数据的所在行
input_time = '2020-07'
avl_time = r_xls['定标日期'].values
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

#########创建新表需要的数据列表，逐行数据添加，并对每行数据列表（rows_values_list）元素进行排序############################################

new_df = []#创建新表格总表内容数据，并以列表形式储存
new_df_xn = []#创建咸宁表格内容数据，并以列表形式储存
new_df_other = []#创建其他表格内容数据，并以列表形式储存
sel_cols = [0, 19, 4, 10, 11, 12, 13, 14, 7, 6]#排序索引列表

######遍历指定的每一行######
for k in range(len(sel_rows)):
    rows_values_list = []#{}#创建用于储存指定行的指定列的值的列表
    new_df.append(rows_values_list)#讲获取到的指定行的数据添加到新表中
    
    ######遍历列值，并排序添加至列表######
    for i in sel_cols:
        ncols_values = str(r_xls.iloc[sel_rows[k], i])
        ncols_values = ncols_values.replace('资产', '采购-行政类').replace('营销', '采购-营销').replace('工程', '采购-工程类').replace('物业', '采购-物业类')
        # ncols_values = ncols_values.replace('nan', '///')
        if '红安' in ncols_values:#将指定列值为空的，替换成/
            ncols_values = '红安恒大文化旅游康养城'
        elif '咸宁' in ncols_values:
            ncols_values = '咸宁梓山湖恒大养生谷'
        elif '湖北合瑞旅游开发有限公司' in ncols_values:
            ncols_values = '武汉恒大文化旅游城'
        elif '鄂州朗恒旅游开发有限公司' in ncols_values:
            ncols_values = '武汉恒大文化旅游城'
        elif '湖北嘉祥旅游开发有限公司' in ncols_values:
            ncols_values = '武汉恒大文化旅游城'
        elif '武汉巴登城投资有限公司' in ncols_values:
            ncols_values = '武汉恒大科技旅游城'
        elif '武汉楚水云山农业开发有限公司' in ncols_values:
            ncols_values = '武汉恒大时代新城'
        elif i in [2, 3, 14, 15, 17, 20]:#将时间列缩减
            ncols_values = ncols_values[:10]
        elif ncols_values == 'nan':
            ncols_values = '///'
        else:
            pass
        rows_values_list.append(ncols_values)
    
    ######插入缺损字段到新列表中，满足14个元素######
    rows_values_list.insert(0, str(k+1))
    rows_values_list.insert(5, '单价包干')
    rows_values_list.insert(8, '/')
    rows_values_list.insert(11, '/')
    rows_values_list.insert(13, '/')
    ###############################################################创建和排序结束#####################################################

    ######处理字段数据######
    print(rows_values_list)

    ######分表######
    if '咸宁' in rows_values_list[2]:
        # print(rows_values_list)
        xn_rows_values_list = rows_values_list
        new_df_xn.append(xn_rows_values_list)
    else:
        other_rows_values_list = rows_values_list
        new_df_other.append(other_rows_values_list)
    
    ###将责任人为指定责任人的，字段为“使用位置”，切不为空的内容，替换至新表中的“工程项目名称”，且加上“到货”二字
    # print(rows_values_list[14])
    if rows_values_list[12] == '朱佳茜' and rows_values_list[14] != '/':
        rows_values_list[3] = rows_values_list[14]# + '到货'
    # del rows_values_list[14]#替换完成后，删除最后一个元素
    rows_values_list.pop()#替换完成后，删除最后一个元素

#########创建xls表列名new_col_name##########################################################################
new_col_name = ['序号', '专业类别', '楼盘名称', '工程项目名称', '中标单位', '计价方式', '招标方式', '投标家数', '规模', '定标总价', '定标日期', '合同签订日期', '经办人', '移交监察分室日期']
create_xls_home = pd.DataFrame(new_df, columns= new_col_name)# index= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34],
create_xls_home.to_excel('D:/Python/data/总表.xlsx')

create_xls_xn = pd.DataFrame(new_df_xn, columns= new_col_name)# index= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34],
create_xls_xn.to_excel('D:/Python/data/咸宁.xlsx')

###“咸宁”表中，字段为“工程项目名称”的列中，有“关于。。。的请示 或者 是。。。的请示”这种句型的，将句型中上述文字删掉，并在后面加上“确定单位”四个文字
# xxx = create_xls_xn['工程项目名称'].values
# for i in range(len(xxx)):
#     # te = re.sub('关于的请示','ha',xxx[i])
#     # print(te)
#     yes = xxx[i].replace('关于', '').replace('的请示', '确定单位').replace('的说明', '确定单位').replace('的沟通', '确定单位')
#     # print(yes)
###“咸宁”表中，字段为“工程项目名称”的列中，有“关于。。。的请示 或者 是。。。的请示”这种句型的，将句型中上述文字删掉，并在后面加上“确定单位”四个文字

create_xls_other = pd.DataFrame(new_df_other, columns= new_col_name)# index= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34],
create_xls_other.to_excel('D:/Python/data/其他.xlsx')


