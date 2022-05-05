import sys

path = r'C:\Users\Dell\Desktop\1111111.txt'  # 数据路径
f = open(path, encoding='utf-8')
line = f.readline()
list = []
while line:
    a = line.split(" ")  # 将数据以空格的方式分隔开
    b = a[1:]
    list.append(b)
    # list.append('\n')
    line = f.readline()
f.close()

with open(r'C:\Users\Dell\Desktop\11.txt', 'a') as month_file:  # 提取后的数据文件
    for line in list:
        s = ' '.join(line)  # 以指定的字符连接生成一个新的字符串
        month_file.write(s)
