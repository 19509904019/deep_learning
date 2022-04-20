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
img = x_train[1]  # 学习数据存放在一维数组里
label = t_train[1]  # 记录学习的数字
print(label)

print(img.shape)  # 此时为一维数组，784个元素构成一维数组
img = img.reshape(28, 28)  # 变为原来的28像素*28像素的形状，reshape()方法
print(img.shape)

img_show(img)
