"""
csv转化为txt文档

"""
import csv

count = 0
# 读取数据源
with open(r'C:\Users\Dell\Desktop\phase1\11.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        count += 1
        for j in i:
            with open(r'C:\Users\Dell\Desktop\phase\%d.txt' % count, 'a') as f:
                f.write(j + '\n')
