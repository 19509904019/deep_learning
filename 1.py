import os
import numpy as np
import csv

# 建模矩阵
arr = []
with open(r"C:\Users\12414\Desktop\matrix\matrix6.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # 将文本转换为浮点数
    for row in reader:  # 每行存储为一个列表
        arr.append(row)

for i in range(len(arr)):
    count = 0
    # 将列表转为矩阵
    a = np.asarray(arr[i]).reshape(8, -1)
    # print(a)
    # 表面金属建模
    for x in range(a.shape[0]):
        for y in range(a.shape[1]):
            if a[x][y] == 1:
                count += 1

    if 20 < count < 30:
        print(count)
