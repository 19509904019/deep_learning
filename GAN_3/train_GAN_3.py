import torch
import os
from PIL import Image
import torch.nn as nn
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
import pandas as pd
import torch.optim as optim
from Discriminator_3 import Discriminator
from Generator_3 import Generator
import numpy as np
import matplotlib.pyplot as plt


# 保存图片
def generate_and_save_images(model, epoch, test_input):
    predictions = np.squeeze(model(test_input).cpu().numpy())
    plt.figure(figsize=(4, 4))
    for i in range(predictions.shape[0]):
        plt.subplot(4, 4, i + 1)
        plt.imshow((predictions[i] + 1) / 2, cmap='gray')
        plt.axis('off')
    plt.savefig(r'C:\Users\Dell\Desktop\image\image_at_epoch_{:04d}.bmp'.format(epoch))
    plt.show()


# 自定义数据集
class EMResponseDataset(Dataset):
    def __init__(self, csv_file, root_dir):
        self.csv_data = pd.read_csv(csv_file, header=None)
        self.root_dir = root_dir

    def __len__(self):
        return len(self.csv_data)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        # 读取电磁响应参数
        em_response = self.csv_data.iloc[idx, :].values.tolist()
        em_response = torch.tensor(em_response)

        # 读取对应的01矩阵
        img_name = os.path.join(self.root_dir, str(idx + 1) + "-matrix.bmp")
        image = Image.open(img_name)

        # 在GAN中,将数据归一化到（-1，1）之间
        transform = transforms.Compose([
            transforms.ToTensor(),  # 归一化,浮点化,通道重排
            transforms.Normalize(0.5, 0.5)  # 从(0,1)到(-1,1)
        ])
        image = transform(image)

        return em_response, image


"""
实例化数据集
"""
# 数据集路径
test_phase = r'D:\deep_learning\GAN_3\dataset\test\phase.csv'
test_matrix = r'D:\deep_learning\GAN_3\dataset\test\test_pic'
train_phase = r'D:\deep_learning\GAN_3\dataset\train\phase.csv'
train_matrix = r'D:\deep_learning\GAN_3\dataset\train\train'
# 获得数据集
train_set = EMResponseDataset(train_phase, train_matrix)
test_set = EMResponseDataset(test_phase, test_matrix)

"""
加载数据集
"""
batch_size = 256
train_dataloader = DataLoader(dataset=train_set, batch_size=batch_size, shuffle=True)
test_dataloader = DataLoader(dataset=test_set, batch_size=batch_size, shuffle=False)

# 定义损失函数
criterion = nn.BCELoss()

# 实例化生成器和判别器模型
generator = Generator()
discriminator = Discriminator()

# 设置GPU设备
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
generator.to(device)
discriminator.to(device)

# 定义优化器
beta1, beta2 = 0.5, 0.999
optimizer_G = optim.Adam(generator.parameters(), lr=0.001, betas=(beta1, beta2))
optimizer_D = optim.Adam(discriminator.parameters(), lr=0.00001, betas=(beta1, beta2))

# 模型训练
D_loss = []
G_loss = []
T_loss = []
# 循环训练
num_epochs = 100
for epoch in range(num_epochs):
    print(f'---------第{epoch + 1}轮---------')
    D_epoch_loss = 0
    G_epoch_loss = 0
    # 训练生成器和判别器
    generator.train()
    discriminator.train()
    for i, (response, real_matrix) in enumerate(train_dataloader):
        response = response.to(device)
        real_matrix = real_matrix.to(device)
        # 训练判别器
        optimizer_D.zero_grad()
        # 判别真实矩阵
        pred_real = discriminator(real_matrix)
        loss_D_real = criterion(pred_real, torch.ones_like(pred_real, device=device))  # 真实01矩阵损失值
        loss_D_real.backward()
        # 判别虚假矩阵
        fake_matrix = generator(response).to(device)
        pred_fake = discriminator(fake_matrix.detach()).to(device)
        loss_D_fake = criterion(pred_fake, torch.zeros_like(pred_fake, device=device))  # 虚假01矩阵损失值
        loss_D_fake.backward()
        # 判别器总体损失值
        loss_D = loss_D_real + loss_D_fake
        optimizer_D.step()

        # 训练生成器
        optimizer_G.zero_grad()
        pred_fake = discriminator(fake_matrix)
        # 使用真实标签判断生成矩阵
        loss_G = criterion(pred_fake, torch.ones_like(pred_fake, device=device))
        loss_G.backward()
        optimizer_G.step()

        with torch.no_grad():
            D_epoch_loss += loss_D.item()
            G_epoch_loss += loss_G.item()

    with torch.no_grad():
        D_epoch_loss /= len(train_dataloader.dataset)
        G_epoch_loss /= len(train_dataloader.dataset)
        D_loss.append(D_epoch_loss)
        G_loss.append(G_epoch_loss)
        # generate_and_save_images(generator, epoch, response)
    print(f"train:Generator Loss: {G_epoch_loss:.8f} | Discriminator Loss: {D_epoch_loss:.8f}")

    # 在测试集上评估生成器
    generator.eval()
    test_loss = 0
    with torch.no_grad():
        for response, real_matrix in test_dataloader:
            response = response.to(device)
            real_matrix = real_matrix.to(device)

            fake_matrix = generator(response).to(device)  # 生成器生成假的矩阵
            # print(real_matrix, fake_matrix)
            pred_fake = discriminator(fake_matrix).to(device)  # 判别器判断矩阵真假
            loss = criterion(pred_fake, torch.ones_like(pred_fake))
            with torch.no_grad():
                test_loss += loss.item()
    with torch.no_grad():
        test_loss /= len(test_dataloader.dataset)
        T_loss.append(test_loss)
    print(f"test: Generator Loss: {test_loss:.8f}")

plt.plot(D_loss, label='D_loss')
plt.plot(G_loss, label='G_loss')
plt.plot(T_loss, label='T_loss')

# 保存模型参数
torch.save({'mymodel': generator.state_dict()}, 'Generator_3.pth')
print("模型保存成功！")

