import csv
import torch
from create_network import *


# 计算平均绝对误差
def MAE(r, g):
    a = torch.abs(r - g)
    b = torch.sum(a) / len(a)
    return b


# 矩阵
matrixs = []
# 相位
phases = []

# 测试数据
with open(r'D:\deep_learning\my_dataset\test\matrix.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        a = list(map(int, i))
        matrixs.append(a)
    matrixs = torch.tensor(matrixs, dtype=torch.float)
with open(r'D:\deep_learning\my_dataset\test\phase.csv', 'r') as f:
    reader = csv.reader(f)
    for j in reader:
        b = list(map(float, j))
        phases.append(b)
    phases = torch.tensor(phases, dtype=torch.float)

# 加载已经训练好的模型
mymodel = torch.load('mymodel.pth', map_location=torch.device('cpu'))

# 计数
test_total = 0
# 进行测试
mymodel.eval()
with torch.no_grad():
    for number in matrixs:
        test_total += 1
        output = mymodel(number)
        if test_total % 100 == 0:
            print(f"第{test_total}个:预测结果为：{output}")
