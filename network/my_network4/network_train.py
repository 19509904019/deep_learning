# 创建数据集对象
import torch
from torch.utils.data import Dataset, DataLoader
from create_network import *
import torch.nn as nn
from torch.optim import *
import csv


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
        return len(self.matrix)

    def __getitem__(self, idx):
        """
        使用参数idx,指定索引访问元素的方法，并指定返回元素
        :param idx:
        :return:
        """
        label = self.matrix[idx]
        data = self.phase[idx]
        return data, label


# 存储矩阵
matrixs = []
# 存储相位
phases = []
# 读取数据源
with open(r'D:\deep_learning\my_dataset\train\matrix.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        a = list(map(int, i))
        matrixs.append(a)
    matrixs = torch.tensor(matrixs, dtype=torch.float)
with open(r'D:\deep_learning\my_dataset\train\phase.csv', 'r') as f:
    reader = csv.reader(f)
    for j in reader:
        b = list(map(float, j))
        phases.append(b)
    phases = torch.tensor(phases, dtype=torch.float)
# 实例化新的数据集
my_dataset = MyDataset(phases, matrixs)

# 传入DataLoader
train_loader = DataLoader(dataset=my_dataset, batch_size=64)

# 生成网络
mymodel = MyModel()

# 损失函数
loss_F = nn.MSELoss()

# 优化器
lr = 1e-4
optimizer = Adam(mymodel.parameters(), lr=lr)

# 训练的轮数
epoch = 20000
count = 0
for i in range(epoch):
    # 记录训练次数
    total_train_step = 0

    # 记录训练轮数
    count += 1

    # 每300轮学习率减半
    if count % 2000 == 0:
        lr = lr / 2

    print(f'---------第{i + 1}轮---------')
    # 训练步骤开始
    mymodel.train()
    # 整个训练集的loss
    total_train_loss = 0
    for data in train_loader:
        # 记录次数
        total_train_step += 1
        # 获取数据
        phases, matrixs = data
        outputs = mymodel(matrixs)
        loss = loss_F(outputs, phases)

        # 优化器优化模型
        optimizer.zero_grad()  # 必须先对参数梯度进行清零
        loss.backward()  # 反向传播求梯度,更新参数
        optimizer.step()

        # 整体训练集的loss
        total_train_loss += loss.item()
        if total_train_step % 10 == 0:
            print(f'训练次数:{total_train_step},loss:{loss.item()}')
    print(f"整体训练集的Loss:{total_train_loss}")


# 保存模型
torch.save(mymodel, 'mymodel.pth')
print("模型保存成功！")
