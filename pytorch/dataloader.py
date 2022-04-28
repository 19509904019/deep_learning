from torch.utils.data import DataLoader
from torchvision.datasets import CIFAR10
from torchvision.transforms import *
from torch.utils.tensorboard import SummaryWriter

# 对数据进行transforms操作
transformer = Compose([

    ToTensor()
])

# 获取测试数据集
test_data = CIFAR10(
    './CIFAR10',
    train=False,
    transform=transformer,
    download=True)

# 加载测试数据集
test_loader = DataLoader(
    dataset=test_data,  # 加载的数据集
    batch_size=64,  # 一次处理数据的批量
    shuffle=True,  # 是否打乱
    drop_last=True  # 是否删除最后剩余的数据
)

# # 显示数据集（一次）
# writer = SummaryWriter('../logs')
# count = 0
# for data in test_loader:  # data由元组组成，包含图片和标签
#     count += 1
#     imgs, target = data
#     writer.add_images('data_loader', imgs, count)
# writer.close()

# # 多次
# writer = SummaryWriter('../logs')
# for epoch in range(2):
#     step = 0
#     for data in test_loader:  # data由元组组成，包含图片和标签
#         step += 1
#         imgs, target = data
#         writer.add_images(f'data_loader_epoch:{epoch}', imgs, step)
# writer.close()
