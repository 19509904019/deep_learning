import numpy as np


def get_0_1_array(array, rate):
    """按照数组模板生成对应的0-1矩阵，rate采用随机的方式"""
    zeros_num = int(array.size * rate)  # 根据0的比率来得到0的个数
    new_array = np.ones(array.size)  # 生成与原来模板相同的矩阵，全为1
    new_array[:zeros_num] = 0  # 将一部分换为0
    np.random.shuffle(new_array)  # 将0和1的顺序打乱
    re_array = new_array.reshape(array.shape)  # 重新定义矩阵的维度，与模板相同
    for i in range(re_array.shape[0]):
        for j in range(i):
            re_array[j][i] = re_array[i][j]
    return re_array


if __name__ == '__main__':
    count = 15000
    for i in range(5000):
        count += 1
        a = get_0_1_array(np.eye(8), rate=np.random.randint(3, 8) * 0.1)
        # print(a)
        f = open(r'C:\Users\Dell\Desktop\4\%d.txt' % count, 'a')
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                f.write(str(a[i][j]) + '\n')
        f.close()
