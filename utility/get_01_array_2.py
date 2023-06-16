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
    new_array = []  # 存储相应的比例列表
    re_array = []  # 存储列表转换成的矩阵
    ran_array = []  # 存储随机矩阵
    number = 0

    # 挑选合适比例的数列
    for i in array:
        count = 0
        for j in i:
            if j == 1:
                count += 1
        # 1 的个数
        if count == 19:
            new_array.append(i)
    print(len(new_array))

    # 遍历生成的矩阵
    for i in new_array:
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

    # 从矩阵集中选出不同的矩阵
    ran = random.sample(range(len(re_array)), 210)
    for i in ran:
        ran_array.append(re_array[i])

    for i in ran_array:
        number += 1
    # 存储矩阵
        f = open(r'C:\Users\Dell\Desktop\matrix\91\%d.txt' % number, 'a')
        for j in i:
            for k in j:
                f.write(str(k) + '\n')
        f.close()


