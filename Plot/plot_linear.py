import os
import matplotlib.pyplot as plt
import numpy as np

# 幅度数据存储路径
linearPath = r'C:\Users\Dell\Desktop\new_data\linear'

# 打开文件夹
linearName = os.listdir(linearPath)

# 按文件顺序排列
linearName.sort(key=lambda x: int(x[:-4]))

# 存放文件内容
linear = []

# 首先读取相位数据
for file in linearName:
    fullLinearPath = os.path.join(linearPath, file)
    # 对文件内容进行读取
    with open(fullLinearPath, 'r') as f:
        # 按行读取全部内容
        lines = f.readlines()
        for line in lines:
            a = line.split()  # 数组
            a = float(a[0])  # 转化为浮点数
            linear.append(a)
        # print(phase)

    # 画图
    x = np.arange(5, 15, 0.01)
    plt.plot(x, linear)
    plt.xlabel("Frequency(GHz)")
    plt.ylabel("magnitude")

    # 清空数组
    linear.clear()

plt.rcParams['figure.figsize']=(20, 15)
plt.show()