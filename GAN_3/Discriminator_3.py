import torch.nn as nn
import torch.nn.functional as F


# 残差块
class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channels)

    def forward(self, x):
        residual = x
        out = self.conv1(x)
        out = self.bn1(out)
        out = F.leaky_relu(out, 0.2)

        out = self.conv2(out)
        out = self.bn2(out)
        out += residual
        out = F.leaky_relu(out, 0.2)

        return out


# 判别器
class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.discriminator = nn.Sequential(
            # 64*64*1
            nn.Conv2d(1, 64, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.2),
            nn.Dropout2d(),

            # 32*32*64
            ResidualBlock(64, 64),
            nn.Conv2d(64, 128, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2),
            nn.Dropout2d(),

            # 16*16*128
            ResidualBlock(128, 128),
            nn.Conv2d(128, 256, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2),
            nn.Dropout2d(),

            # 8*8*256
            ResidualBlock(256, 256),
            nn.Conv2d(256, 512, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(512),
            nn.LeakyReLU(0.2),
            nn.Dropout2d(),

            # 4*4*512
            nn.Conv2d(512, 1, kernel_size=4, stride=2, padding=0, bias=False),
            nn.Sigmoid(),
        )

        self.weight_init()

    # 权重初始化
    def weight_init(self):
        for m in self.discriminator.modules():
            if isinstance(m, nn.ConvTranspose2d):
                nn.init.normal_(m.weight.data, 0, 0.02)

            elif isinstance(m, nn.BatchNorm2d):
                nn.init.normal_(m.weight.data, 0, 0.02)
                nn.init.constant_(m.bias.data, 0)

    def forward(self, x):
        x = self.discriminator(x)
        x = x.view(x.size(0), -1)
        return x
