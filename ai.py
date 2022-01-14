while True:
    str = input()
    str = str.replace("吗", "")
    str = str.replace("？", "！")
    print(str)