import torch
from network.test3.network_3 import MyModel
import csv
import numpy as np


def calculate_the_mae(predicted_data, actual_data):
    """
    该函数用于计算平均绝对误差
    Parameters
    ----------
    predicted_data : 一维列表
        预测数据.
    actual_data : 一维列表
        真实数据.
    Returns
    -------
    MAE : 浮点型
        平均绝对误差.
    """
    # 定义一个变量用于存储所有样本的绝对误差之和
    the_sum_of_error = 0
    # 开始逐渐遍历每一个样本
    for i in range(len(actual_data)):
        # 不断累加求和，计算所有样本的绝对误差之和
        the_sum_of_error += abs(predicted_data[i] - actual_data[i])
    # 计算所有样本的平均绝对误差
    MAE = the_sum_of_error / float(len(actual_data))
    return MAE


train_matrixs = []
train_phases = []
# 加载模型
mymodel = MyModel()
# 权重数据路径
weight_dic_path = r'mymodel.pth'
# 加载数据
state_dic = torch.load(weight_dic_path, map_location=torch.device('cpu'))
new_state = {}
for k, v in state_dic.items():
    new_state = v
mymodel.load_state_dict(new_state)

# 读取数据
with open(r'D:/deep_learning/dataset/data_200/train/matrix.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        a = torch.tensor(list(map(float, i)))
        a = torch.reshape(a, (1, 1, 8, -1))
        train_matrixs.append(a)

with open(r'D:/deep_learning/dataset/data_200/train/phase.csv', 'r') as f:
    reader = csv.reader(f)
    for j in reader:
        b = torch.tensor(list(map(float, j)))
        train_phases.append(b)

# 随机取整数
# a = np.random.randint(0, 2517)
# matrix = train_matrixs[a]
# phase = train_phases[a]
# 测试
total = 0
for i in range(24000):
    matrix = train_matrixs[i]
    phase = train_phases[i]
    mymodel.eval()
    output = mymodel(matrix).view(-1).tolist()
    # print(phase)
    # print(output)
    mae = calculate_the_mae(output, phase.tolist())
    total += mae
    print('整个验证集的平均绝对误差为:%.4f' % (total / 24000))
