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
    # 挑选合适比例的数列
    new_array = []
    re_array = []
    number = 0
    for i in array:
        count = 0
        for j in i:
            if j == 1:
                count += 1
        # 1 的个数
        if count == 12:
            # 生成全是1的矩阵
            swap_array = np.ones(36).reshape(6, 6)
            index = 0  # 列表下标
            # 替换swap_array矩阵
            for m in range(6):
                for n in range(m + 1):
                    swap_array[m][n] = i[index]
                    swap_array[n][m] = swap_array[m][n]
                    index += 1
            new_array.append(swap_array)

    # 从矩阵集中选出不同的矩阵
    ran = random.sample(range(len(new_array)), 50000)
    for i in ran:
        re_array.append(new_array[i])

    for i in re_array:
        number += 1
    # 存储矩阵
        f = open(r'C:\Users\user2\Desktop\64\%d.txt' % number, 'a')
        for n in range(i.shape[0]):
            for m in range(i.shape[1]):
                f.write(str(i[n][m]) + '\n')
        f.close()


