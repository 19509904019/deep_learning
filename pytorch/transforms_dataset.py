import torchvision
from torch.utils.tensorboard import SummaryWriter
from torchvision.transforms import *

"""
基本操作
"""
# train_set = torchvision.datasets.CIFAR10(root='CIFAR10', train=True, download=True)
test_set = torchvision.datasets.CIFAR10(root='CIFAR10', train=False, download=True)


print(test_set.classes)  # 测试集种类 十种共10000张图片
# print(train_set.classes)  # 训练集种类  始终共50000张图片
# print(test_set[0]) # 测试集第一张图片
#
# img, target = test_set[1]  # 图片 标签索引  每个数据由这两个元素组成
# print(img)  # 图像
# print(target)  # 标签索引
#
# print(test_set.classes[target]) # 标签
print(test_set.classes[1]) # 标签
# # img.show() # 显示图片


"""
对数据集用transforms做预处理
"""

# transformer = Compose([
#
#     ToTensor()
# ])

# train_set = torchvision.datasets.CIFAR10(root='./CIFAR10', transform=transformer, train=True, download=True)
# test_set = torchvision.datasets.CIFAR10(root='./CIFAR10', transform=transformer, train=False, download=True)

# print(train_set[0])
# print(train_set[0][0].shape)

# writer = SummaryWriter('../logs')
# for i in range(10):
#     img, target = train_set[i]
#     writer.add_image('train_set', img, i)
# writer.close()
