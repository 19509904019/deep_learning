import csv
import torch
from network_convnet import *
import torch.nn as nn
from torch.optim import *
import time

s11 = []
parameters = []
# 电磁响应
with open(r"C:\Users\12414\Desktop\dataset\dataset2\train_set\s11.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
    for row in reader:  # each row is a list
        s11.append(row)
    s11 = torch.tensor(s11, dtype=torch.float)

# 几何参数
with open(r"C:\Users\12414\Desktop\dataset\dataset2\train_set\parameters.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
    for row in reader:  # each row is a list
        parameters.append(row)
    parameters = torch.tensor(parameters, dtype=torch.float)

# print(s11)
# print(type(s11))
# print(parameters)
# print(type(parameters))

# GPU加速
device = torch.device('cuda:0')

# 生成网络
mymodel = MyModel().to(device)

# 损失函数
loss_F = nn.L1Loss().to(device)

# 优化器
lr = 1e-3
optimizer = Adam(mymodel.parameters(), lr=lr)

# 训练的轮数
epoch = 0
flag = True

while flag:
    # 计数,每一次训练总数据量
    train_loss = 0
    # 训练的轮数
    epoch += 1
    print(f'--------------第{epoch}轮--------------')
    # 训练开始
    mymodel.train()
    for number in range(len(s11)):
        train_loss += 1
        data = torch.reshape(s11[number], (1, 1, -1)).to(device)
        outputs = mymodel(data).to(device)
        # print(outputs)
        # 结构参数
        parameter = torch.reshape(parameters[number], (1, -1)).to(device)
        # print(parameter)
        # 计算损失函数
        loss = loss_F(outputs, parameter).to(device)
        # print(loss)

        # 优化模型
        optimizer.zero_grad()  # 梯度清零
        loss.backward()
        optimizer.step()

        if train_loss % 100 == 0:
            print(f'训练数据数量:{train_loss},loss:{loss.item()}')

        if loss.item() < 0.01:
            flag = False
            print(f"训练已结束,当前loss:{loss.item()}")
            break

# 保存模型
torch.save(mymodel, 'mymodel2.pth')
print("保存成功!")
