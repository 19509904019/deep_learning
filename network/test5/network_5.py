import torch.nn as nn


class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.model1 = nn.Sequential(
            # 第一层卷积
            nn.Conv2d(1, 32, kernel_size=3, padding=1, stride=1),
            nn.PReLU(),
            nn.MaxPool2d(2),
            # 第二层卷积
            nn.Conv2d(32, 64, kernel_size=3, padding=1, stride=1),
            nn.PReLU(),
            nn.MaxPool2d(2),
            # 第三层卷积
            nn.Conv2d(64, 128, kernel_size=3, padding=1, stride=1),
            nn.PReLU(),
            nn.MaxPool2d(2),

            # 全连接层
            nn.Flatten(),
            nn.Linear(128, 256),
            nn.BatchNorm1d(256),
            nn.PReLU(),
            nn.Linear(256, 512),
            nn.BatchNorm1d(512),
            nn.PReLU(),
            nn.Linear(512, 1024),
            nn.BatchNorm1d(1024),
            nn.PReLU(),
            nn.Linear(1024, 512),
            nn.BatchNorm1d(512),
            nn.PReLU(),
            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.PReLU(),
            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.PReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 50)
        )

    def forward(self, x):
        x = self.model1(x)
        return x
