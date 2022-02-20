#打开数据总表
import pandas as pd
import datetime, time

###初始化#############################################
#字典#################################################
_serial_dict = {
                '序号': '序号', 
                '专业类别': '项目类别', 
                '楼盘名称': '项目公司', 
                '工程项目名称': '项目名称', 
                '中标单位': '中标单位', 
                '计价方式': '单价包干', #不取原表
                '招标方式': '招标方式', 
                '投标家数': '投标家数', 
                '规模': '/', #新增
                '定标总价': '订单金额',
                '定标日期': '定标日期', 
                '合同签订日期': '合同签订日期', 
                '经办人': '责任人',
                '移交监察日期': '暂未移交',#新增
                '经济指标': '/',
                '是否含重点项目三层预交楼':'/'
                }

#keys值列表
keys_ = list(_serial_dict.keys())
#values值列表
values_ = list(_serial_dict.values())



######################################打开表格，读取数据############################################
#path_xls_mac = '/Users/liufeng/Documents/Python/data/【恒大】采购物资情况台账.xlsx'
path_xls_win = 'D:/data/HD/湖北公司采购物资情况台账(4).xlsx'#★★★★★★这里是你要读取的总表表格，路径及文件名可根据自己的需要自定义★★★★★★
r_xls = pd.read_excel(path_xls_win, sheet_name='采购台账', engine='openpyxl').fillna('///')#, dtype={'要求到货时间': str}
print('1)成功读取数据库...')

#表格行数、列数
rows = r_xls.shape[0]#表格行数
cols = r_xls.shape[1]#表格列数

#列表-数据源列名
xls_cols_name = list(r_xls.columns.values)

cho_date = '2021-01'#★★★★★★这里是你要选择的月份，格式不要改，直接改单引号中的数字即可★★★★★★
cho_col = list(r_xls['定标日期'].values)#★★★★★★这里是你要选择的列名，直接修改单引号中间的文字即可★★★★★★
#print(type(avl_time))
# print(cho_col)

#新表列名在总表中的位置###############################
cho_cols_index = []
# cho_cols = [0, 19, 4, 10, 11, 12, 13, 14, 20, 7]
for i in range(1, len(values_)):
    if values_[i] in xls_cols_name:
        # print(xls_cols_name.index(values_[i]))
        cho_cols_index.append(xls_cols_name.index(values_[i]))
    else:
        pass
# print(cho_cols_index)
######################################按指定条件，获取到读取的数据行############################################
cho_rows = []#储存需要数据的所在行
#cho_rows = [1938, 1939, 1941, 1942, 1943, 1947, 1948, 1950, 1952, 1953, 1954, 1955, 1956, 1957, 1959, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1973, 1987, 1988, 1989, 1990, 1991, 3678, 3680, 3697]
for i in range(rows):
    if cho_date in str(cho_col[i]):
        cho_rows.append(i)#将需要数据所在行添加进list
print(cho_rows)
print('2)成功抓取指定数据行...')

new_df = []
for k in range(len(cho_rows)):

    new_row = []#{}#创建用于储存指定行的指定列的值的列表
    for i in cho_cols_index:
        new_col = r_xls.iloc[cho_rows[k], i]#按照index序列，和选择的行，读取单元格数据

        if i == 14:#将时间列缩减
            new_col = str(new_col)[:10]
        
        new_row.append(new_col)
    #补齐缺损字段
    new_row.insert(0, str(k+1))
    new_row.insert(5, values_[5])
    new_row.insert(8, values_[8])
    new_row.insert(13, values_[13])
    new_row.insert(14, values_[14])
    new_row.insert(15, values_[15])
    
    new_df.append(new_row)

######处理类别名称######
for k in range(len(new_df)):
    if new_df[k][1] == '工程':#★★★★★★这里及以下是类别名称的对应模块，可自行修改单引号中的内容★★★★★★
        new_df[k][1] = '采购-工程类'
    elif new_df[k][1] == '营销':
        new_df[k][1] = '采购-营销类'
    elif new_df[k][1] == '资产':
        new_df[k][1] = '采购-行政类'
    elif new_df[k][1] == '物业':
        new_df[k][1] = '采购-行政类'
    elif new_df[k][1] == '运营':
        new_df[k][1] = '采购-行政类'
    else:
        pass

######处理项目名称######
for k in range(len(new_df)):#★★★★★★这里是公司名称与项目名称的对应模块，可自行修改单引号中的内容★★★★★★
    if new_df[k][2] == '武汉巴登城投资有限公司':
        new_df[k][2] = '武汉恒大科技旅游城'
    elif new_df[k][2] == '武汉楚水云山农业开发有限公司':
        new_df[k][2] = '武汉恒大时代新城'
    elif new_df[k][2] == ['湖北合瑞旅游开发有限公司', '湖北恒祥旅游开发有限公司', '鄂州朗恒旅游开发有限公司', '湖北嘉翔旅游开发有限公司', '湖北恒大童世界旅游开发有限公司']:
        new_df[k][2] = '武汉恒大文化旅游城'
    elif '红安' in new_df[k][2]:
        new_df[k][2] = '红安恒大文化旅游康养城'
    elif '咸宁' in new_df[k][2]:
        new_df[k][2] = '咸宁梓山湖恒大养生谷'
    elif '江西' in new_df[k][2]:
        new_df[k][2] = '江西恒大养生谷'
    else:
        pass

# print(len(new_df))
print(new_df[0])
# for i in range(len(new_df)):
#     print(new_df[i])

# print(type(cho_col), '\n', len(cho_col))
# datetime.datetime

# print(len(keys_), ':', keys_, '\n', len(new_row), ':', new_row)

create_xls_home = pd.DataFrame(new_df, columns= keys_)
create_xls_home = create_xls_home.set_index('序号')
create_xls_home.to_excel('D:/data/HD/test.xlsx')#★★★★★★这里是创建的表格路径及名称，可自己修改单引号中的内容★★★★★★

print('yes')

