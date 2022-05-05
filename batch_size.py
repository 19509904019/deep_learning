import csv
import numpy as np
import torch
from network.my_network2.pytorch_deep_convnet import *
import torch.nn as nn
from torch.optim import *

s11 = []
parameters = []
# 电磁响应
with open(r"C:\Users\Dell\Desktop\s11.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
    for row in reader:  # each row is a list
        s11.append(row)
    s11 = torch.tensor(s11, dtype=torch.float32)
    s11 = torch.reshape(s11, (1, 1, -1, 1000))

# 几何参数
with open(r"C:\Users\Dell\Desktop\parameters.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
    for row in reader:  # each row is a list
        parameters.append(row)
    parameters = torch.tensor(parameters, dtype=torch.float32)
    parameters = torch.reshape(parameters, (1, -1, 10))
    # print(parameters.shape)
    print(parameters[0])

# 生成网络
mymodel = MyModel()
#
# 损失函数
loss_F = nn.L1Loss()
#
# 优化器
lr = 1e-3
optimizer = Adam(mymodel.parameters(), lr=lr)
#
# 计数
train_loss = 0
epoch = 10
batch_size = 10

for i in range(epoch):
    print(f"-------------第{i + 1}轮--------------")
    # 训练开始
    mymodel.train()
    for number in range(len(s11) // batch_size):
        train_loss += 1
        # 随机取一组数据
        batch_mask = np.random.choice(s11.shape[0], batch_size)
        # 输入数据
        data = s11[batch_mask]
        outputs = mymodel(data)
        # 标签
        targets = parameters[batch_mask]
        # 计算损失函数
        loss = loss_F(outputs, targets)
        # print(loss)

        # 优化模型
        optimizer.zero_grad()  # 梯度清零
        loss.backward()
        optimizer.step()

        if train_loss % 5 == 0:
            print(f'训练次数:{train_loss},loss:{loss.item()}')
