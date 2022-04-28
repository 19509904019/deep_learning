import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
from torch.nn import *
from torch.utils.data import DataLoader
from torchvision.datasets import CIFAR10
from torchvision.transforms import *
from torch.utils.tensorboard import SummaryWriter

# class MyModel(nn.Module):
#     """
#     nn.Module为所有模型的基类，自己建立的模型应该继承这个类
#     """
#
#     def __init__(self):
#         super(MyModel, self).__init__()
#         self.conv1 = nn.Conv2d(in_channels=3, out_channels=20, kernel_size=5)  # 卷积层1
#         self.conv2 = nn.Conv2d(in_channels=20, out_channels=20, kernel_size=5)  # 卷积层2
'''
卷积层
Conv2d( in_channels , out_channels , kernel_size , 
stride = 1 , padding = 0 , dilation = 1 , groups = 1 , 
bias = True , padding_mode = 'zeros' , device = None , dtype = None )

in_channels ( int ) – 输入图像中的通道数
out_channels ( int ) – 卷积产生的通道数  
kernel_size ( int or tuple ) – 卷积核的大小  
stride ( int or tuple , optional ) -- 卷积的步幅。默认值：1
padding ( int , tuple或str , optional ) – 添加到输入的所有四个边的填充。默认值：0
padding_mode (字符串,可选) – 'zeros', 'reflect', 'replicate'或'circular'. 默认：'zeros'
dilation ( int or tuple , optional ) -- 内核元素之间的间距。默认值：1
groups ( int , optional ) -- 从输入通道到输出通道的阻塞连接数。默认值：1
bias ( bool , optional ) – If True，向输出添加可学习的偏差。默认：True
'''
#
#     def forward(self, input):
#         x = F.relu(self.conv1(input))  # 激活函数为relu
#         y = F.relu(self.conv2(x))
#         return y
#
"""
卷积运算
F.conv2d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1) → Tensor 

input – 输入的形状 (minibatch,in_channels,iH,iW)
weight – 卷积核形状 (out_channels,in_channels/groups,kH,kW)
bias – 偏置  Default: None
stride – 卷积核的步幅，可以是单个数或者一个元组(sH, sW). Default: 1  (横向和纵向同时控制)
padding – 输入两侧的隐式填充,可以是字符{‘valid’, ‘same’},单个数或者一个元组(padH, padW).Default: 0   (对输入数据进行填充)  
(padding='valid' 等同于没有填充。padding='same' 为输入填充，使输出与输入具有相同的形状。但是，该模式不支持除1以外的任何步幅值)
dilation - 内核元素之间的间距。可以是单个数字或元组(dH, dW)。Default: 1
groups- 将输入分成组，in_channels应该可以被组数整除。Default: 1

主要是输入和卷积核
"""

# mymodel = MyModel()
# path = r'D:\deep_learning\pytorch\dataset\train\ants_image\0013035.jpg'
# img = Image.open(path)
# img_tensor = ToTensor()(img)
# print(img_tensor.shape)
# result = mymodel.forward(img_tensor)
# print(result)
# print(result.shape)

# #--------------------------------------------------------# #

'''
卷积操作
'''
# inputs = torch.tensor([
#     [1, 2, 0, 3, 1],
#     [0, 1, 2, 3, 1],
#     [1, 2, 1, 0, 0],
#     [5, 2, 3, 1, 1],
#     [2, 1, 0, 1, 1]])
#
# kernel = torch.tensor([
#     [1, 2, 1],
#     [0, 1, 0],
#     [2, 1, 0]])
#
# # 转化为（minibatch,channel,h,w）
# inputs = torch.reshape(inputs, (1, 1, 5, 5))
# kernel = torch.reshape(kernel, (1, 1, 3, 3))
# # print(inputs.shape)
# # print(kernel.shape)
# output = F.conv2d(inputs, kernel, stride=1, padding=0)
# print(output)

# #--------------------------------------------------------# #

'''
conv2d
'''

# test_set = CIFAR10(
#     root='.\CIFAR10',
#     train=False,
#     transform=ToTensor(),
#     download=True
# )
#
# dataloder = DataLoader(
#     dataset=test_set,
#     batch_size=64,
#     shuffle=True,
#     drop_last=True
#
# )
#
#
# class MyModel(nn.Module):
#     def __init__(self):
#         super(MyModel, self).__init__()
#         self.conv1 = nn.Conv2d(
#             in_channels=3,
#             out_channels=6,
#             kernel_size=3,
#             stride=1,
#             padding=0
#         )
#
#     def forward(self, inputs):
#         return self.conv1(inputs)
#
#
# if __name__ == '__main__':
#
#     mymodel = MyModel()  # 构建神经网络
#     # print(mymodel)
#
#     writer = SummaryWriter('../logs')
#     step = 0
#     for data in dataloder:
#         step += 1
#         img, target = data
#         # print(img.shape)
#         output = mymodel.forward(img)  # 对神经网络进行输入
#         output = torch.reshape(output, (-1, 3, 30, 30))
#         # print(output.shape)
#         writer.add_images('conv2d_1', img_tensor=img, global_step=step)
#         writer.add_images('conv2d_2', img_tensor=output, global_step=step)
#     writer.close()

# #--------------------------------------------------------# #

'''
池化层
torch.nn.MaxPool2d( kernel_size , stride = None , padding = 0 , 
dilation = 1 , return_indices = False , ceil_mode = False )

kernel_size – 最大的窗口大小

stride – 步幅  Default value: kernel_size

padding – 填充

dilation – 元素之间的间隔

return_indices - 如果True，将返回最大索引以及输出。torch.nn.MaxUnpool2d 以后有用

ceil_mode – 如果为 True，将使用ceil而不是floor来计算输出形状  ceil向上取整(保留剩余)  floor向下取整(不保留剩余)

'''
# test_data = CIFAR10('./CIFAR10', train=False, transform=Compose([ToTensor()]), download=True)
# dataloader = DataLoader(test_data, batch_size=64, shuffle=True, drop_last=True)
#
#
# class MyModel(nn.Module):
#     def __init__(self):
#         super(MyModel, self).__init__()
#         self.maxpool2d = MaxPool2d(kernel_size=3, ceil_mode=True)
#
#     def forward(self, x):
#         return self.maxpool2d(x)
#
#
# if __name__ == '__main__':
#     step = 0
#     writer = SummaryWriter('../logs')
#     mymodel = MyModel()  # 构建网络
#     for data in dataloader:
#         step += 1
#         imgs, targets = data
#         output = mymodel.forward(imgs)
#         writer.add_images('maxpool', output, global_step=step)
#     writer.close()


# #--------------------------------------------------------# #

'''
激活函数
relu
sigmoid
'''
#
# test_data = CIFAR10('./CIFAR10', train=False, transform=Compose([ToTensor()]), download=True)
# dataloader = DataLoader(test_data, batch_size=64, shuffle=True, drop_last=True)
#
#
# class MyModel(nn.Module):
#     def __init__(self):
#         super(MyModel, self).__init__()
#         self.relu1 = ReLU()
#
#     def forward(self, x):
#         return self.relu1(x)
#
#
# if __name__ == '__main__':
#     step = 0
#     writer = SummaryWriter('../logs')
#     mymodel = MyModel()  # 构建网络
#     for data in dataloader:
#         step += 1
#         imgs, targets = data
#         output = mymodel.forward(imgs)
#         writer.add_images('relu', output, global_step=step)
#     writer.close()

# #--------------------------------------------------------# #

'''
Batch Normalization

torch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, 
track_running_stats=True, device=None, dtype=None)

num_features – 来自大小为(N，C，H，W)(N，C，H，W)的预期输入的CC

eps – 为数值稳定性而加到分母上的值。默认值:1e-5

momentum – 用于running_mean和running_var计算的值。对于累积移动平均(即简单平均)，可以设置为无。默认值:0.1

affine – 一个布尔值，当设置为真时，此模块具有可学习的仿射参数。 Default: True

track_running_stats – 一个布尔值，当设置为True时，此模块跟踪运行平均值和方差，
当设置为False时，此模块不跟踪此类统计，并将统计缓冲区running_mean和running_var初始化为None。
当这些缓冲区都不存在时，该模块总是使用批量统计。在训练和评估模式下 Default: True
'''
# test_data = CIFAR10('./CIFAR10', train=False, transform=Compose([ToTensor()]), download=True)
# dataloader = DataLoader(test_data, batch_size=64, shuffle=True, drop_last=True)
#
#
# class MyModel(nn.Module):
#     def __init__(self):
#         super(MyModel, self).__init__()
#         self.affine1 = Linear(196608, 10)
#
#     def forward(self, x):
#         return self.affine1(x)
