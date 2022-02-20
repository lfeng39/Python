import pandas as pd
import re
import datetime
import time

#创建用于建表的表头，len(newXlsTitle)：49
newXlsTitle = [
    'Search Term_1 搜索词', 'Search Term Cnt 搜索词字数', 'Occurrence 出现次数',
    'Search Frequency Rank Rate',
    'Search Frequency Rank 1', 'Search Frequency Rank 2', 'Search Frequency Rank 3',
    'Trend', 'ThreeMonthSFRChange', 'Match',
    'G_K_O_1', 'G_K_O_2', 'G_K_O_3',
    'X.1.Clicked Asin 1', 'X.2.Clicked Asin 1', 'X.3.Clicked Asin 1',
    'X.1.Product_1', 'X.2.Product_1', 'X.3.Product_1',
    'X.1.Click Share_1', 'X.2.Click Share_1', 'X.3.Click Share_1',
    'X.1.Conversion Share_1', 'X.2.Conversion Share_1', 'X.3.Conversion Share_1',
    'X.1.Clicked Asin 2', 'X.2.Clicked Asin 2', 'X.3.Clicked Asin 2',
    'X.1.Product_2', 'X.2.Product_2', 'X.3.Product_2',
    'X.1.Click Share_2', 'X.2.Click Share_2', 'X.3.Click Share_2',
    'X.1.Conversion Share_2', 'X.2.Conversion Share_2', 'X.3.Conversion Share_2',
    'X.1.Clicked Asin 3', 'X.2.Clicked Asin 3', 'X.3.Clicked Asin 3',
    'X.1.Product_3', 'X.2.Product_3', 'X.3.Product_3',
    'X.1.Click Share_3', 'X.2.Click Share_3', 'X.3.Click Share_3',
    'X.1.Conversion Share_3', 'X.2.Conversion Share_3', 'X.3.Conversion Share_3'
    ]

#创建用于新建表格的数据列表
newXlsList = []


#创建新表
newXls = pd.DataFrame(newXlsList, columns = newXlsTitle)