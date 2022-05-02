import torch.nn as nn


class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.model = nn.Sequential(
            # 第一层卷积
            nn.Conv2d(1, 32, kernel_size=5, padding=2, stride=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            # 第二层卷积
            nn.Conv2d(32, 64, kernel_size=5, padding=2, stride=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            # 第三层卷积
            nn.Conv2d(64, 128, kernel_size=3, padding=1, stride=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Flatten(),
            # 全连接层
            nn.Linear(2 * 2 * 128, 4096),
            nn.ReLU(),
            nn.Linear(4096, 1024),
            nn.ReLU(),
            nn.Linear(1024, 512),
            nn.ReLU(),
            # 输出层
            nn.Linear(512, 49)
        )

    def forward(self, x):
        x = self.model(x)
        return x
