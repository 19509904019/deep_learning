import torch
import torch.nn as nn
from torch.utils.tensorboard import SummaryWriter


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


if __name__ == '__main__':
    mymodel = MyModel()  # 构建神经网络
    inputs = torch.ones((64, 3, 32, 32))  # 64个3维32*32的一维数组
    output = mymodel.forward(inputs)
    print(output.shape)

    writer = SummaryWriter('../logs')
    writer.add_graph(mymodel, inputs)
    writer.close()
