import numpy as np


def get_0_1_array(array, rate=0.2):
    """按照数组模板生成对应的 0-1 矩阵，默认rate=0.2"""
    zeros_num = int(array.size * rate)  # 根据0的比率来得到 0的个数
    new_array = np.ones(array.size)  # 生成与原来模板相同的矩阵，全为1
    new_array[:zeros_num] = 0  # 将一部分换为0
    np.random.shuffle(new_array)  # 将0和1的顺序打乱
    re_array = new_array.reshape(array.shape)  # 重新定义矩阵的维度，与模板相同
    return re_array


if __name__ == '__main__':
    for i in range(100):
        a = get_0_1_array(np.eye(16))
        with open(rf'C:\Users\12414\Desktop\arr\{i}.txt', 'a') as f:
            f.write(str(a))
