import torch
import torch.nn as nn
import torch.nn.functional as F


# 残差链接
class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.ConvTranspose2d(in_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.ConvTranspose2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channels)

    def forward(self, x):
        residual = x
        out = self.conv1(x)
        out = self.bn1(out)
        out = F.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)
        out += residual
        out = F.relu(out)

        return out


# 生成器
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()

        self.generator = nn.Sequential(
            # 1*1*51
            nn.ConvTranspose2d(100, 512, kernel_size=4, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(512),
            nn.ReLU(),

            # 4*4*512
            ResidualBlock(512, 512),
            nn.ConvTranspose2d(512, 256, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(256),
            nn.ReLU(),

            # 8*8*256
            ResidualBlock(256, 256),
            nn.ConvTranspose2d(256, 128, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(),

            # 16*16*128
            ResidualBlock(128, 128),
            nn.ConvTranspose2d(128, 64, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),

            # 32*32*64 ---> 64*64*1
            nn.ConvTranspose2d(64, 1, kernel_size=4, stride=2, padding=1, bias=False),
            nn.Tanh()
        )

        self.weight_init()

    # 权重初始化
    def weight_init(self):
        for m in self.generator.modules():
            if isinstance(m, nn.ConvTranspose2d):
                nn.init.normal_(m.weight.data, 0, 0.02)

            elif isinstance(m, nn.BatchNorm2d):
                nn.init.normal_(m.weight.data, 0, 0.02)
                nn.init.constant_(m.bias.data, 0)

    def forward(self, x):
        # 增加高斯噪声
        noise = torch.randn_like(x)[:, :49]
        x = torch.cat((x, noise), dim=1)
        # 进行网络训练
        x = x.view(x.size(0), -1, 1, 1)
        x = self.generator(x)
        return x
