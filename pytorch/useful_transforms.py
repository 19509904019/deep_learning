from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
from torchvision.transforms import *
import numpy as np
import cv2 as cv

img_path = r'D:\deep_learning\pytorch\dataset\train\ants_image\9715481_b3cb4114ff.jpg'
PIL_img = Image.open(img_path)
print(PIL_img)
cv_img = cv.imread(img_path)
#


# Compose transforms操作放在一起
'''
Example:
        >>> transforms.Compose([
        >>>     transforms.CenterCrop(10),
        >>>     transforms.PILToTensor(),
        >>>     transforms.ConvertImageDtype(torch.float),
        >>> ])
'''
#


# ToTensor使用方法  tensorboard --logdir=logs
# write = SummaryWriter('../logs')
# tensor_img = ToTensor()(PIL_img)
# write.add_image('img', tensor_img)
# write.close()


# PILToTensor
"""
Convert a ``PIL Image`` to a tensor of the same type. This transform does not support torchscript.

    Converts a PIL Image (H x W x C) to a Tensor of shape (C x H x W).
"""
# print('-' * 50)
# # 初始类型
# np_img = np.array(PIL_img)
# print('初始形状：', np_img.shape)
#
# # 转换类型
# result = PILToTensor()(img)
# print('转换后形状:', result.shape)
# #


# ToPILImage
"""
Convert a tensor or an ndarray to PIL Image. This transform does not support torchscript.

    Converts a torch.*Tensor of shape C x H x W or a numpy ndarray of shape
    H x W x C to a PIL Image while preserving the value range.
"""
# print('-' * 50)
#
# # numpy数组  使用opencv读取
# result = ToPILImage()(cv_img)
# print(type(result))
# print(result)
#
# # Tensor  使用PIL读取
# result1 = PILToTensor()(PIL_img)
# result2 = ToPILImage()(result1)
# print(type(result1))
# print(result1.shape)
#
# print(type(result2))
#


# Normalize 归一化
"""
Normalize(mean(n),std(n)) 通道几个写几个
Normalize a tensor image with mean and standard deviation.

This transform does not support PIL Image.(ToTensor)

output[channel] = (input[channel] - mean[channel]) / std[channel]
"""
# print('-' * 50)
# tensor_img = ToTensor()(cv_img)
# print(type(tensor_img))

# for i in range(5):
#     print(tensor_img[0][0][0])  # 没有进行归一化
#     norm = Normalize(np.random.randint(3), np.random.randint(3))  # 归一化操作
#     norm_img = norm(tensor_img)  # 归一化后的图片
#     writer = SummaryWriter('../logs')
#     writer.add_image('tensor_img1', img_tensor=norm_img, global_step=i)
#     writer.close()
#     print(norm_img[0][0][0])  # 进行归一化
#


# Resize 重新改变图片的大小尺寸
# print('-' * 50)
# # 旧版只支持PIL类型
# resize = Resize((512, 512))  # 填入修改后的尺寸大小
# # resize_img = resize(cv_img)  # img should be PIL Image
# resize_img = resize(PIL_img)
# print(resize_img)
# print(type(resize_img))
#
# resize_img = ToTensor()(resize_img)
# print(type(resize_img))

# # 新版支持tensor类型
# tensor_img = ToTensor()(PIL_img)
# resize = Resize((512, 512))  # 填入修改后的尺寸大小
# resize_img = resize(tensor_img)  # 也可以直接输入tensor类型
# # print(resize_img)
# print(type(resize_img))
# print(resize_img.shape)
#


# Compose
'''
compose()中的参数需要一个列表,存放一系列transforms操作
即compose([transforms参数1,transforms参数1,transforms参数2,transforms参数3...])
'''
# compose = Compose([ToTensor(), Resize((512, 512))])  # 前一个参数的输出是后一个参数的输入
# resize_img = compose(PIL_img)
# # print(resize_img)
# print(resize_img.shape)


# # RandomCrop(size,scale,ratio) 随机裁剪，连续调用两次得到的裁剪结果可能不一致
# # randomcrop = RandomCrop((64,64))
# compose = Compose([ToTensor(), RandomCrop((64, 64))])
# # rand_img = compose(PIL_img)
# for i in range(10):
#     rand_img = compose(PIL_img)
#     SummaryWriter('../logs').add_image('rand_img', rand_img, i)
# SummaryWriter('../logs').close()


'''
1.关注输入和输出

2.多看官方文档

3.方法需要什么参数
'''

# # example
# # 将不同的transforms组合，但是这样的变换是有顺序的
# transformer = transforms.Compose([
#     transforms.Resize((224, 224)),
#     # 随机旋转
#     transforms.RandomRotation(15, expand=False),
#     transforms.RandomHorizontalFlip(p=0.1),
#     transforms.RandomVerticalFlip(p=0.1),
#     # 中心裁剪
#     transforms.CenterCrop(224),
#     transforms.ToTensor(),
#     transforms.Normalize(mean=[0.85223039, 0.8524969, 0.8526602],
#                          std=[0.27402772, 0.2744828, 0.2744293])
# ])
# print(transformer(PIL_img).shape)
# writer = SummaryWriter('../logs')
#
# writer.add_image('image', img_tensor=transformer(PIL_img), global_step=1)
# writer.close()


'''
transforms.RandomChoice：从给定的一系列transforms中选一个进行操作

transforms.RandomApply：给一个transforms加上概率，以一定的概率执行该操作

transforms.RandomOrder：将transforms中的操作顺序随机打乱

'''
# transformer = transforms.Compose([
#     transforms.RandomChoice([transforms.RandomVerticalFlip(p=1), transforms.RandomHorizontalFlip(p=1)]),
#
#     transforms.RandomApply([transforms.RandomAffine(degrees=0, shear=45, fillcolor=(255, 0, 0)),
#                             transforms.Grayscale(num_output_channels=3)], p=0.5),
#
#     transforms.RandomOrder([transforms.RandomRotation(15),
#                             transforms.Pad(padding=32),
#                             transforms.RandomAffine(degrees=0, translate=(0.01, 0.1), scale=(0.9, 1.1))]),
#
#     transforms.ToTensor(),
#     transforms.Normalize(mean=[0.85223039, 0.8524969, 0.8526602],
#                          std=[0.27402772, 0.2744828, 0.2744293])
#
# ])
