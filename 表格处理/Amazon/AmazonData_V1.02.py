#打开数据总表
from calendar import month
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

monNum = 'testData'

def dfXLS(xls):
    oldXlsPath = 'D:/data/Amazon/原始数据/'+ xls +'月表单.xlsx'
    newXlsPath = 'D:/data/Amazon/测试数据/'+ xls + '.xlsx'
    if xls == 'testData':
        df_xls = pd.read_excel(newXlsPath,skiprows=1).fillna('///')
        return df_xls
    elif xls == '10':
        df_xls = pd.read_excel(newXlsPath,skiprows=1).fillna('///')
        return df_xls
    elif xls == '11':
        df_xls = pd.read_excel(newXlsPath,skiprows=1).fillna('///')
        return df_xls
    elif xls == '12':
        df_xls = pd.read_excel(newXlsPath,skiprows=1).fillna('///')
        return df_xls

memoryData = dfXLS(monNum)
memoryData10 = dfXLS('10')
memoryData11 = dfXLS('11')
memoryData12 = dfXLS('12')
x_shape = memoryData.shape#表格行与列
t2 = time.time()

# keyName = memoryData.keys()[abcTrans('B')]
searchWord = memoryData.iloc[1,abcTrans('B')]
# searchWord = memoryData12.iloc[15,abcTrans('B')]
def getColValues(xls, abc):
    if xls == 'testData':
        colValues = list(memoryData[memoryData.keys()[abcTrans(abc)]].values)
        return colValues
    elif xls == '10':
        colValues = list(memoryData[memoryData10.keys()[abcTrans(abc)]].values)
        return colValues
    elif xls == '11':
        colValues = list(memoryData[memoryData11.keys()[abcTrans(abc)]].values)
        return colValues
    elif xls == '12':
        colValues = list(memoryData[memoryData12.keys()[abcTrans(abc)]].values)
        return colValues

'''
逐行读取数据
'''
'''B
读取12月表单G、K、O栏之和小于40%的，按搜索排名升序填入
数据已处理，读取即可
'''
BtoB_Value = memoryData12.iloc[1,abcTrans('B')]
print('B:',BtoB_Value,'-SearchWord')

'''C
判断B栏搜索词字数，调用变量时，设置行数
若该行搜索词（本表单B栏内容）为Christmas tree字数为2，此处填入2；Christmas light tree字数为3，此处填入3
'''
# for i in range(1, x_shape[0]):
#     searchWord = memoryData.iloc[i,abcTrans('B')]
#     wordCount = searchWord.count(' ')
#     print('have',wordCount+1,'words')
wordCount = searchWord.count(' ') + 1
print('C:',wordCount,'-words')

'''D
该搜索词在本表单中出现的次数
大小写、空格、顺序：spc = ['hello world','Hello World','helloworld','world hello']
只计大小写，其余不计数
'''
searchWordList = getColValues('testData','B')
# print(searchWordList)
testLsit = ['hello world','Hello World','helloworld','world hello', 'Hello world']
tempList = []
#将列表字符串全部转换小写，再进行对比计数
for i in searchWordList:
    tempList.append(i.lower())
totalNum = tempList.count(i.lower())
print('D:',totalNum,'-times')

'''F
12月表单C栏内容
'''
# CtoF_List = getColValues('testData','C')
CtoF_Value = memoryData12.iloc[1,abcTrans('C')]
print('F:',CtoF_Value,'-12 ranking No')

'''G
相同搜索词11月表单C栏内容，若无填0/ 通过行号，去11月表单C栏取值
'''
CtoG_Value = memoryData11.iloc[1,abcTrans('C')]
if CtoG_Value == ' ' or CtoG_Value == 'nan' or CtoG_Value == '///':
  CtoG_Value = 0
print('G:',CtoG_Value,'-11 ranking No')

'''H
相同搜索词10月表单C栏内容，若无填0 /通过行号，去10月表单C栏取值
'''
CtoH_Value = memoryData10.iloc[1,abcTrans('C')]
if CtoH_Value == ' ' or CtoH_Value == 'nan' or CtoH_Value == '///':
    CtoH_Value = 0
print('H:',CtoH_Value,'-10 ranking No')

'''E
(F+G+H)/3
'''
E_average  = (CtoF_Value + CtoG_Value + CtoH_Value)/3
print('E:',E_average,'-ranking average (F+G+H)/3')


'''J
F-H
'''
J_ = CtoF_Value - CtoH_Value
print('J:',J_,'-(F-H)')

'''I
1.若G、H单项或两项为0，该处填入New 
2.若J=0，该处填入Steady
3.若J为负数，该处填入Up
4.若J为正数，该处填入Down
'''
I_Value = ''
if CtoG_Value == 0 and CtoH_Value == 0:
    I_Value = 'New'
elif J_ == 0:
    I_Value = 'Steady'
elif J_ < 0:
    I_Value = 'Up'
elif J_ > 0:
    I_Value = 'Down'
print('I:',I_Value,'- Trend')

'''K
F/G/H非0的数量
'''
K_Value = ''
FGHList = [CtoF_Value,CtoG_Value,CtoH_Value]
for i in range(len(FGHList)):
    if FGHList.count('0') == i:
        K_Value = -i + 3
print('K:',K_Value,'- !=0 Num')

'''L
G_K_O_1
'''
L_Value = '///'
print('L:',L_Value,'- nan')

'''M
G_K_O_2
'''
M_Value = '///'
print('M:',M_Value,'- nan')

'''N
G_K_O_3
'''
N_Value = '///'
print('N:',N_Value,'- nan')

'''O
12月表单D栏内容
'''
# DtoO_List = getColValues('testData','D')
DtoO_Value = memoryData12.iloc[1,abcTrans('D')]
print('O:',DtoO_Value,'- ASIN')

'''P
相同搜索词11月表单D栏内容，若无填/
'''
# DtoP_List = getColValues('testData','D')
DtoP_Value = memoryData11.iloc[1,abcTrans('D')]
print('P:',DtoP_Value,'- ASIN')

'''Q
相同搜索词10月表单D栏内容，若无填/
'''
# DtoQ_List = getColValues('testData','D')
DtoQ_Value = memoryData10.iloc[1,abcTrans('D')]
print('Q:',DtoQ_Value,'- ASIN')

'''F
12月表单E栏内容
'''
# EtoF_List = getColValues('testData','E')
EtoF_Value = memoryData12.iloc[1,abcTrans('E')]
print('R:',EtoF_Value,'- ProductName')

'''S
相同搜索词11月表单E栏内容，若无填/
'''
# EtoS_List = getColValues('testData','E')
EtoS_Value = memoryData11.iloc[1,abcTrans('E')]
print('S:',EtoS_Value,'- ProductName')

'''T
相同搜索词10月表单E栏内容，若无填/
'''
# EtoT_List = getColValues('testData','E')
EtoT_Value = memoryData10.iloc[1,abcTrans('E')]
print('T:',EtoT_Value,'- ProductName')

'''U
12月表单F栏内容
'''
# FtoU_List = getColValues('testData','F')
FtoU_Value = memoryData12.iloc[1,abcTrans('F')]
print('U:',FtoU_Value,'- ClickShare')

'''V
相同搜索词11月表单F栏内容，若无填/
'''
# FtoV_List = getColValues('testData','F')
FtoV_Value = memoryData11.iloc[1,abcTrans('F')]
print('V:',FtoV_Value,'- ClickShare')

'''W
相同搜索词10月表单F栏内容，若无填/
'''
# FtoW_List = getColValues('testData','F')
FtoW_Value = memoryData10.iloc[1,abcTrans('F')]
print('W:',FtoW_Value,'- ClickShare')

'''X
12月表单G栏内容
'''
# GtoX_List = getColValues('testData','G')
GtoX_Value = memoryData12.iloc[1,abcTrans('G')]
print('X:',GtoX_Value,'- ToShare')

'''Y
相同搜索词11月表单G栏内容，若无填/
'''
# GtoY_List = getColValues('testData','G')
GtoY_Value = memoryData11.iloc[1,abcTrans('G')]
print('Y:',GtoY_Value,'- ToShare')

'''Z
相同搜索词10月表单G栏内容，若无填/
'''
# GtoZ_List = getColValues('testData','G')
GtoZ_Value = memoryData10.iloc[1,abcTrans('G')]
print('Z:',GtoZ_Value,'- ToShare')

'''AA
12月表单H栏内容
'''
# HtoAA_List = getColValues('testData','H')
HtoAA_Value = memoryData12.iloc[1,abcTrans('H')]
print('AA:',HtoAA_Value,'- Clicked ASIN')

'''AB
相同搜索词11月表单H栏内容，若无填/
'''
# HtoAB_List = getColValues('testData','H')
HtoAB_Value = memoryData11.iloc[1,abcTrans('H')]
print('AB:',HtoAB_Value,'- Clicked ASIN')

'''AC
相同搜索词10月表单H栏内容，若无填/
'''
# HtoAC_List = getColValues('testData','H')
HtoAC_Value = memoryData10.iloc[1,abcTrans('H')]
print('AC:',HtoAC_Value,'- Clicked ASIN')

'''AD
12月表单I栏内容
'''
# ItoAD_List = getColValues('testData','I')
ItoAD_Value = memoryData12.iloc[1,abcTrans('I')]
print('AD:',ItoAD_Value,'- ProductName')

'''AE
相同搜索词11月表单I栏内容，若无填/
'''
# ItoAE_List = getColValues('testData','I')
ItoAE_Value = memoryData11.iloc[1,abcTrans('I')]
print('AE:',ItoAE_Value,'- ProductName')

'''AF
相同搜索词10月表单I栏内容，若无填/
'''
# ItoAF_List = getColValues('testData','I')
ItoAF_Value = memoryData10.iloc[1,abcTrans('I')]
print('AF:',ItoAF_Value,'- ProductName')

'''AG
12月表单J栏内容
'''
# JtoAG_List = getColValues('testData','J')
JtoAG_Value = memoryData12.iloc[1,abcTrans('J')]
print('AG:',JtoAG_Value,'- ClickShare')

'''AH
相同搜索词11月表单J栏内容，若无填/
'''
# JtoAH_List = getColValues('testData','J')
JtoAH_Value = memoryData11.iloc[1,abcTrans('J')]
print('AH:',JtoAH_Value,'- ClickShare')

'''AI
相同搜索词10月表单J栏内容，若无填/
'''
# JtoAI_List = getColValues('testData','J')
JtoAI_Value = memoryData10.iloc[1,abcTrans('J')]
print('AI:',JtoAI_Value,'- ClickShare')

'''AJ
12月表单K栏内容
'''
# KtoAJ_List = getColValues('testData','K')
KtoAJ_Value = memoryData12.iloc[1,abcTrans('K')]
print('AJ:',KtoAJ_Value,'- ToShare')

'''AK
相同搜索词11月表单K栏内容，若无填/
'''
# KtoAK_List = getColValues('testData','K')
KtoAK_Value = memoryData11.iloc[1,abcTrans('K')]
print('AK:',KtoAK_Value,'- ToShare')

'''AL
相同搜索词10月表单K栏内容，若无填/
'''
# KtoAL_List = getColValues('testData','K')
KtoAL_Value = memoryData10.iloc[1,abcTrans('K')]
print('AL:',KtoAL_Value,'- ToShare')

'''AM
12月表单L栏内容
'''
# LtoAM_List = getColValues('testData','L')
LtoAM_Value = memoryData12.iloc[1,abcTrans('L')]
print('AM:',LtoAM_Value,'- Clicked')

'''AN
相同搜索词11月表单L栏内容，若无填/
'''
# LtoAN_List = getColValues('testData','L')
LtoAN_Value = memoryData11.iloc[1,abcTrans('L')]
print('AN:',LtoAN_Value,'- Clicked')

'''AO
相同搜索词10月表单L栏内容，若无填/
'''
# LtoAO_List = getColValues('testData','L')
LtoAO_Value = memoryData10.iloc[1,abcTrans('L')]
print('AO:',LtoAO_Value,'- Clicked')

'''AP
12月表单M栏内容
'''
# MtoAP_List = getColValues('testData','M')
MtoAP_Value = memoryData12.iloc[1,abcTrans('M')]
print('AP:',MtoAP_Value,'- ProductName')

'''AQ
相同搜索词11月表单M栏内容，若无填/
'''
# MtoAQ_List = getColValues('testData','M')
MtoAQ_Value = memoryData11.iloc[1,abcTrans('M')]
print('AQ:',MtoAQ_Value,'- ProductName')

'''AR
相同搜索词10月表单M栏内容，若无填/
'''
# MtoAR_List = getColValues('testData','M')
MtoAR_Value = memoryData10.iloc[1,abcTrans('M')]
print('AR:',MtoAR_Value,'- ProductName')

'''AS
12月表单N栏内容
'''
# NtoAS_List = getColValues('testData','N')
NtoAS_Value = memoryData12.iloc[1,abcTrans('N')]
print('AS:',NtoAS_Value,'- ClickShare')

'''AT
相同搜索词11月表单N栏内容，若无填/
'''
# NtoAT_List = getColValues('testData','N')
NtoAT_Value = memoryData11.iloc[1,abcTrans('N')]
print('AT:',NtoAT_Value,'- ClickShare')

'''AU
相同搜索词10月表单N栏内容，若无填/
'''
# NtoAU_List = getColValues('testData','N')
NtoAU_Value = memoryData10.iloc[1,abcTrans('N')]
print('AU:',NtoAU_Value,'- ClickShare')

'''AV
12月表单O栏内容
'''
# OtoAV_List = getColValues('testData','O')
OtoAV_Value = memoryData12.iloc[1,abcTrans('O')]
print('AV:',OtoAV_Value,'- ToShare')

'''AW
相同搜索词11月表单O栏内容，若无填/
'''
# OtoAW_List = getColValues('testData','O')
OtoAW_Value = memoryData11.iloc[1,abcTrans('O')]
print('AW:',OtoAW_Value,'- ToShare')

'''AX
相同搜索词10月表单O栏内容，若无填/
'''
# OtoAX_List = getColValues('testData','O')
OtoAX_Value = memoryData10.iloc[1,abcTrans('O')]
print('AX:',OtoAX_Value,'- ToShare')