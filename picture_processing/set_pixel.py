from skimage import io, transform, color

import numpy as np
import os


def convert_gray(f, **args):  # 图片处理与格式化的函数
    rgb = io.imread(f)  # 读取图片
    gray = color.rgb2gray(rgb)  # 将彩色图片转换为灰度图片
    dst = transform.resize(gray, (64, 64))  # 调整大小，图像分辨率为64*64
    return dst


datapath = r'D:\deep_learning\picture\original_picture'  # 图片所在的路径
str = datapath + '/*.jpg'  # 识别.jpg的图像

coll = io.ImageCollection(str, load_func=convert_gray)  # 批处理

for i in range(len(coll)):
    io.imsave(r'D:\deep_learning\picture\save_picture' + '\\'+ np.str(i) + '.jpg', coll[i])  # 保存图片在d:/daate/date/
