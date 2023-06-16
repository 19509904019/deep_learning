import numpy as np
import random


# 生成不重复的0-1序列
def generateSequence(n):
    x = [[0 for number in range(n)]]
    xTran = []
    m = 0
    while len(x) != 2 ** n:
        for i in range(len(x)):
            for j in range(n):
                xTran.append(x[i][j])
            xTran[n - m - 1] = 1
            x.append(xTran)
            xTran = []
        m += 1
    return x


if __name__ == '__main__':
    # 生成所有的0-1组合
    array = generateSequence(21)
    # print(len(array))
    re_array = []  # 存储对称矩阵
    ran_array = []  # 存储随机抽取的对称矩阵
    number = 0

    # 遍历生成的矩阵
    for i in array:
        # 生成全是1的矩阵
        swap_array = np.ones(36).reshape(6, 6)
        index = 0  # 列表下标
        # 替换swap_array矩阵
        for m in range(6):
            for n in range(m + 1):
                swap_array[m][n] = i[index]
                swap_array[n][m] = swap_array[m][n]
                index += 1
        re_array.append(swap_array)
    # print(re_array[200])
    # print(len(re_array))

    # 从矩阵集中选出不同的矩阵
    ran = random.sample(range(len(re_array)), 100000)
    for i in ran:
        ran_array.append(re_array[i])

    for i in ran_array:
        number += 1
        # 存储矩阵
        f = open(r'C:\Users\Dell\Desktop\matrix_ran\%d.txt' % number, 'a')
        for j in i:
            for k in j:
                f.write(str(k) + '\n')
        f.close()
