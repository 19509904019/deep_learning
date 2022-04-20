import os
import sys
import numpy as np
import pickle

sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from PIL import Image  # 图像的显示使用的是PIL模块


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def softmax(x):
    c = np.max(x)
    exp_a = np.exp(x - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y


# 获取数据
def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=True, one_hot_label=False)
    return x_test, t_test


# 读入学习到的权重参数
def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)

        return network


# 输入信号转化为输出信号
def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


x, t = get_data()
network = init_network()

accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])  # 用predict函数进行分类
    p = np.argmax(y)  # 获取概率最高的元素的索引
    if p == t[i]:  # 比较神经网络所预测的答案和正确解标签
        accuracy_cnt += 1  # 加入到预测的正确行列

print("Accuracy:", int(accuracy_cnt) / len(x))

"""
在该例子当中做了一种预处理， normalize=True，将各个像素值除以255，进行了简单的正规化
实际上，很多预处理都会考虑到数据的整体分布。比如，利用数据整体的均值或标准差，移动数据，使数据以0为中心分布

"""

"""
# 输出神经网络的各层的权重的形状
x, t = get_data()  # 输入一张图像数据时的处理流程
network = init_network()
W1, W2, W3 = network['W1'], network['W2'], network['W3']
print(x.shape)
print(x[0].shape)
print(W1.shape)
print(W2.shape)
print(W3.shape)
"""

# 进行批处理
x, t = get_data()  # 获取数据
network = init_network()  # 生成网络

batch_size = 100  # 批处理
accuracy_cnt = 0

for i in range(0, len(x), batch_size):  # 一次处理100张图片数据
    x_batch = x[i:i + batch_size]  # x[0:100],x[100:200]....
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p == t[i:i + batch_size])

print("Accuracy:", int(accuracy_cnt) / len(x))
