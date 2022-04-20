"""读入MNIST数据集

    Parameters
    ----------
    normalize : 将图像的像素值正规化为0.0~1.0,若设为False则输入的图像像素会保持原来的 0-255
    one_hot_label :
        one_hot_label为True的情况下，标签作为one-hot数组返回
        one-hot数组是指[0,0,1,0,0,0,0,0,0,0]这样的数组
    flatten : 是否将图像展开为一维数组，即是否展开输入图像，若设为False，则输入图像为1*28*28的三维数组
              若为True，则输入图像会保存为有784个元素构成的一维数组

    Returns
    -------
    (训练图像, 训练标签), (测试图像, 测试标签)  ->  (x_train, t_train), (x_test, t_test)
    """

import os
import sys

sys.path.append(os.pardir)  # 为了导入父目录中的文件而进行的设定
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# 输出各个数据的形状
print(x_train.shape)  # （60000,784）
print(t_train.shape)  # （60000,）
print(x_test.shape)  # （10000,784）
print(t_test.shape)  # （10000,）
