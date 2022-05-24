import torch
import torch.nn as nn
import torch.nn.functional as F


class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.model1 = nn.Sequential(
            # 第一层卷积
            nn.Conv1d(1, 16, kernel_size=2, stride=2),
            nn.MaxPool1d(2),
            # 第二层卷积
            nn.Conv1d(16, 32, kernel_size=2),
            nn.MaxPool1d(3),
            # 压平
            nn.Flatten(),
            # 全连接层
            nn.Linear(2656, 1000),
            nn.ReLU(),
            nn.Linear(1000, 50),
            # nn.Linear(50, 1000)
        )

        # 隐藏特征
        self.model2 = nn.Sequential(
            # 第一层卷积
            nn.Conv1d(1, 32, kernel_size=2),
            nn.MaxPool1d(2),
            nn.BatchNorm1d(32),
            # 第二层卷积
            nn.Conv1d(32, 64, kernel_size=2),
            nn.MaxPool1d(2),
            nn.BatchNorm1d(64),
            # 第三层卷积
            nn.Conv1d(64, 128, kernel_size=2),
            nn.MaxPool1d(2),
            nn.BatchNorm1d(128),
            # 第四层卷积
            nn.Conv1d(128, 256, kernel_size=2),
            nn.MaxPool1d(2),
            nn.BatchNorm1d(256),
            nn.Flatten(),
            # 全连接层
            nn.Linear(512, 1024),
            nn.ReLU(),
            nn.Linear(1024, 1024),
            nn.Dropout(0.5),
            nn.Linear(1024, 500),
            nn.ReLU(),
            nn.Linear(500, 128),
            nn.ReLU(),
            nn.Linear(128, 50),
            nn.ReLU(),
            nn.Linear(50, 10)
        )

    def forward(self, x):
        x = self.model1(x)
        x = torch.reshape(x, (1, 1, -1))
        x = self.model2(x)
        return x
