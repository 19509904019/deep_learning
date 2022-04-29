"""
GPU加速：
    网络模型
    数据
    损失函数

"""
import torch
from torch import nn
from torch import optim
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from torchvision.datasets import *
from torchvision.transforms import *
import time
# 准备数据集

train_set = CIFAR10(
    '../CIFAR10',
    train=True,
    transform=Compose([ToTensor()]),
    download=True
)

test_set = CIFAR10(
    root='../CIFAR10',
    train=False,
    transform=Compose([ToTensor()]),
    download=True
)

# 加载数据集
train_dataloader = DataLoader(train_set, batch_size=64)
test_dataloader = DataLoader(test_set, batch_size=64)


# 构建网络
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.model1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=5, stride=1, padding=2),
            nn.MaxPool2d(2),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=5, stride=1, padding=2),
            nn.MaxPool2d(2),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5, stride=1, padding=2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(1024, 64),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        x = self.model1(x)
        return x


# 生成网络
mymodel = MyModel()
# GPU加速
if torch.cuda.is_available():
    mymodel.cuda()

# 损失函数
loss_func = nn.CrossEntropyLoss()
if torch.cuda.is_available():
    loss_func = loss_func.cuda()

# 优化器
lr = 1e-2
optimizer = optim.SGD(mymodel.parameters(), lr=lr)

# 设置训练网络的一些参数
# 记录训练次数
total_train_step = 0
# 记录测试次数
total_test_step = 0
# 训练的轮数
epoch = 10

writer = SummaryWriter('../../logs')
for i in range(epoch):
    print(f'---------第{i + 1}轮---------')

    # 训练步骤开始
    start = time.time()
    # 整个训练集的loss
    total_train_loss = 0
    for data in train_dataloader:
        # 记录次数
        total_train_step += 1
        # 获取数据并加速
        imgs, targets = data
        if torch.cuda.is_available():
            imgs = imgs.cuda()
            targets = targets.cuda()

        outputs = mymodel(imgs)
        loss = loss_func(outputs, targets)

        # 优化器优化模型
        optimizer.zero_grad()  # 必须先对参数梯度进行清零
        loss.backward()  # 反向传播求梯度,更新参数
        optimizer.step()

        total_train_loss += loss.item()
        if total_train_step % 100 == 0:
            end = time.time()
            print(f'time:{end-start}')
            print(f'训练次数:{total_train_step},loss:{loss.item()}')
    print(f"整体训练集的Loss:{total_train_loss}")
    writer.add_scalar('train_loss', loss.item(), total_train_step)

    # 整个测试集的loss
    total_test_loss = 0
    # 整个测试集的准确率
    total_test_accuracy = 0
    # 测试步骤开始
    with torch.no_grad():
        for data in test_dataloader:
            imgs, targets = data
            if torch.cuda.is_available():
                imgs = imgs.cuda()
                targets = targets.cuda()

            outputs = mymodel(imgs)
            loss = loss_func(outputs, targets)
            total_test_loss += loss.item()  # 将所有的loss值相加
            # 每次进行的准确率
            accuracy = (outputs.argmax(1) == targets).sum() / len(test_set)
            # 训练整体的准确率
            total_test_accuracy += accuracy
        print(f"整体测试集的Loss:{total_test_loss},准确率:{total_test_accuracy}")
        writer.add_scalar('test_loss', total_test_loss, total_test_step)

# 保存模型
# torch.save(mymodel, 'mymodel.pth')
# print("模型保存成功！")
writer.close()
