import os
import matplotlib.pyplot as plt
import numpy as np

filepath = r'C:\Users\Dell\Desktop\new_data'
filename = os.listdir(filepath)
# 按顺序排列
filename.sort(key=lambda x: int(x[:-4]))
# 读取文件夹内容
y = []
for file in filename:
    fullpath = os.path.join(filepath, file)
    # 对文件内容进行读取
    with open(fullpath, 'r') as f:
        # 按行读取全部内容
        lines = f.readlines()
        for line in lines:
            a = line.split()  # 数组
            a = float(a[0])  # 转化为浮点数
            y.append(a)

    # 画图
    x = np.arange(5, 15, 0.01)
    plt.plot(x, y)
    plt.xlabel("Frequency(GHz)")
    plt.ylabel("Phase(degree)")
    # plt.legend()
    # 清空数组
    y.clear()

# 放大图片
# plt.rcParams['figure.figsize'] = (50, 7.2)
plt.show()
