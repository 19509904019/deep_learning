import torch
from torch.utils.data import Dataset, DataLoader
from network.test3.network_3 import MyModel
import torch.nn as nn
from torch.optim import *
import csv
import math


# 自定义数据集
class MyDataset(Dataset):  # 需要继承Dataset类
    def __init__(self, phase, matrix):
        """
        将传入的序列指定为类的属性
        :param phase:
        :param matrix:
        """
        self.phase = phase
        self.matrix = matrix

    def __len__(self):
        """
        设定数据集的长度
        :return:
        """
        return len(self.phase)

    def __getitem__(self, idx):
        """
        使用参数idx,指定索引访问元素的方法，并指定返回元素
        :param idx:
        :return:
        """
        label = self.matrix[idx]
        data = self.phase[idx]
        return data, label


"""
准备数据集
"""
# 训练集
train_matrixs = []  # 存放训练集矩阵
train_phases = []  # 存放训练集相位
# 读取数据源
with open(r'D:/user2/program/my_dataset/data_200/train/matrix.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        a = torch.tensor(list(map(float, i)))
        a = torch.reshape(a, (1, 8, -1))
        train_matrixs.append(a)
with open(r'D:/user2/program/my_dataset/data_200/train/phase.csv', 'r') as f:
    reader = csv.reader(f)
    for j in reader:
        b = torch.tensor(list(map(float, j)))
        train_phases.append(b)
# 实例化新的训练集
train_set = MyDataset(train_phases, train_matrixs)

# 测试集
test_matrixs = []  # 存放测试矩阵
test_phases = []  # 存放测试相位
# 读取数据源
with open(r'D:/user2/program/my_dataset/data_200/test/matrix.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        a = torch.tensor(list(map(float, i)))
        a = torch.reshape(a, (1, 8, -1))
        test_matrixs.append(a)
with open(r'D:/user2/program/my_dataset/data_200/test/phase.csv', 'r') as f:
    reader = csv.reader(f)
    for j in reader:
        b = torch.tensor(list(map(float, j)))
        test_phases.append(b)
# 实例化新的测试
test_set = MyDataset(test_phases, test_matrixs)

"""
加载数据集
"""
train_dataloader = DataLoader(dataset=train_set, batch_size=128, shuffle=True)
test_dataloader = DataLoader(dataset=test_set, batch_size=128, shuffle=False)

"""
构建网络
"""
# GPU加速
device = torch.device('cuda:0')
# 生成网络
mymodel = MyModel().to(device)
# 损失函数
loss_F = nn.MSELoss().to(device)

# 优化器
lr = 1e-3  # 学习率
optimizer = Adam(mymodel.parameters(), lr=lr)

# 调整学习率函数
# y = lambda x: 0.9 ** x
# scheduler = lr_scheduler.LambdaLR(optimizer=optimizer,lr_lambda=y)
scheduler = lr_scheduler.StepLR(optimizer=optimizer, step_size=5000, gamma=0.1)
"""
设置训练网络的一些参数
"""
# 训练的轮数
epoch = 20000
count = 0
total_train = []  # 记录每轮的整体训练误差
total_test = []  # 记录每轮的整体测试误差
"""
开始训练网络
"""
for i in range(epoch):
    count += 1
    print(f'---------第{i + 1}轮---------')
    # 记录训练的次数
    total_train_step = 0
    # 训练步骤开始
    mymodel.train()
    # 整个训练集的loss
    total_train_loss = 0

    for data in train_dataloader:
        total_train_step += 1
        # 获取数据
        phases, matrixs = data
        phases = phases.to(device)
        matrixs = matrixs.to(device)
        # 输出数据
        outputs = mymodel(matrixs).to(device)
        loss = loss_F(outputs, phases).to(device)
        # 优化器优化模型
        optimizer.zero_grad()  # 必须先对参数梯度进行清零
        loss.backward()  # 反向传播求梯度,更新参数
        optimizer.step()

        # 每100条数据输出一次
        total_train_loss += loss.item()  # 整体训练集的loss
        # if total_train_step % 100 == 0:
        #     print(f'训练次数:{total_train_step},loss:{loss.item()}')
    print(f"整体训练集的Loss:{total_train_loss / 24000}")
    total_train.append(total_train_loss / 24000)
    scheduler.step()

    # 整个测试集的loss
    total_test_loss = 0
    # 测试步骤开始
    mymodel.eval()
    with torch.no_grad():
        for data in test_dataloader:
            # 获取数据
            phases, matrixs = data
            phases = phases.to(device)
            matrixs = matrixs.to(device)
            # 输出数据
            outputs = mymodel(matrixs).to(device)
            loss = loss_F(outputs, phases).to(device)
            total_test_loss += loss.item()  # 整体测试集的loss
        print(f"整体测试集的Loss:{total_test_loss / 3000},均方根误差为：{math.sqrt(total_test_loss / 3000)}")
        total_test.append(total_test_loss / 3000)

"""
保存模型
"""
# 保存模型参数
torch.save({'mymodel': mymodel.state_dict()}, 'mymodel.pth')
print("模型保存成功！")

"""
保存数据画图
"""
with open(r'C:\Users\user2\Desktop\loss\total_train.txt', 'a') as f:
    for i in total_train:
        f.write(str(i) + '\n')
with open(r'C:\Users\user2\Desktop\loss\total_test.txt', 'a') as f:
    for j in total_test:
        f.write(str(j) + '\n')
