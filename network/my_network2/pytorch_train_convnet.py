import csv
import torch
from pytorch_deep_convnet import *
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

# 几何参数
with open(r"C:\Users\Dell\Desktop\parameters.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
    for row in reader:  # each row is a list
        parameters.append(row)
    parameters = torch.tensor(parameters, dtype=torch.float32)

# print(s11)
# print(type(s11))
# print(parameters)
# print(type(parameters))

# 生成网络
mymodel = MyModel()

# 损失函数
loss_F = nn.L1Loss()

# 优化器
lr = 1e-3
optimizer = Adam(mymodel.parameters(), lr=lr)

# 计数
train_loss = 0
epoch = 100

for i in range(epoch):
    print(f"-------------第{i + 1}轮--------------")
    # 训练开始
    mymodel.train()
    for number in range(len(s11)):
        train_loss += 1
        data = torch.reshape(s11[number], (1, 1, -1))
        outputs = mymodel(data)
        # print(outputs)
        # 结构参数
        parameter = torch.reshape(parameters[number], (1, -1))
        # print(parameter)
        # 计算损失函数
        loss = loss_F(outputs, parameter)
        # print(loss)

        # 优化模型
        optimizer.zero_grad()  # 梯度清零
        loss.backward()
        optimizer.step()

        if train_loss % 100 == 0:
            print(f'训练次数:{train_loss},loss:{loss.item()}')

# 保存模型
torch.save(mymodel, 'mymodel1.pth')
print("保存成功!")
