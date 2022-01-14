# import re


# file = open("kris.txt", mode="w")
# file.write("Hello Kris")
# file.close()

# line = "Cats are sma23rter than dogs"

# res = re.compile(r'^e\S(.*\S)t')

# matchObj = re.search(res, line, re.M|re.I)
# print(matchObj)
# #print(len(line))
# #print(matchObj.span())
# #print(matchObj.group())
#
#==============================================================
# import os

# file = 'D:/369/www/lego/img/official'
# # 遍历文件夹
# # def walkFile(file):
# for root, dirs, files in os.walk(file):
#         # root 表示当前正在访问的文件夹路径
#         # dirs 表示该文件夹下的子目录名list
#         # files 表示该文件夹下的文件list
#         # 遍历文件
#         # for f in files:
#         #     print(os.path.join(root, f))

#         # 遍历所有的文件夹
#         for d in dirs:
#             print(os.path.join(root, d))    
# with open('d:/Python/haha.html', mode='w', encoding='utf-8') as file:
#     file.write('<html><head><meta charset="utf-8"></head><body>')
#     file.write('<p>hello world</p>')
#     file.write('<p>'+ root +'</p>')
#     file.write('</body></html>')                
# for root, dirs, files in os.walk(file):
#     print(files)
#=============================================================================

# dict = {'朱佳茜':'jessie', '柳汐子':'kris', '柳丰':'leo'}
# ilike = list(dict.values()).index('kris')
# print(ilike)
# print(list(dict.keys())[ilike])

# list = ['jessie', 'kris', 'leo']
# print(list.index('kris'))

#===============================================================================
tt = ['274637437', '274637437/answer/1729082895']
if 'answer' in tt[1]:
    print('yes')
else:
    pass

x = -10.00
for x in range(-10,10):
    if (x*50)/(0.8*100) == 1.49:
        print(x)
    else:
        x = x + 1
        print(x)