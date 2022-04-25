import os
import sys
import numpy as np

from dataset.mnist import load_mnist
from PIL import Image

sys.path.append(os.pardir)


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))  # 把数组数据转化为图像
    pil_img.show()


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
img = x_train[0]  # 第一张图片数据信息
label = t_train[0]  # 第一张图片数据标签
print(label)

print(img.shape)  # 第一张图片一维数组信息
img = img.reshape(28, 28)  # 变为原来的28像素*28像素的形状表示原始信息，reshape()方法
print(img.shape)

img_show(img)  # 将数组转为图片
