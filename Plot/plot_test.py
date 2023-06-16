import os
import matplotlib.pyplot as plt
import copy

# 相位数据存储路径
outputPath = r'C:\Users\Dell\Desktop\output'
phasePath = r'C:\Users\Dell\Desktop\phase'
frequencyPath = r'C:\Users\Dell\Desktop\data30000\new_data\frequency\frequency.txt'

# 打开文件夹
phaseName = os.listdir(phasePath)
outputName = os.listdir(outputPath)

# 按文件顺序排列
phaseName.sort(key=lambda x: int(x[:-4]))

# 存放文件内容
phase = []
phase1 = []
phase2 = []
output = []
output1 = []
output2 = []
frequency = []

# 频率
with open(frequencyPath, 'r') as f:
    # 按行读取全部内容
    lines = f.readlines()
    for line in lines:
        a = line.split()  # 数组
        a = float(a[0])  # 转化为浮点数
        frequency.append(a)

# 首先读取相位数据
for file in phaseName:
    fullPhasePath = os.path.join(phasePath, file)
    # 对文件内容进行读取
    with open(fullPhasePath, 'r') as f:
        # 按行读取全部内容
        lines = f.readlines()
        for line in lines:
            a = line.split()  # 数组
            a = float(a[0])  # 转化为浮点数
            phase1.append(a)
        phase2 = copy.copy(phase1)
        phase.append(phase2)
        phase1.clear()

# 首先读取相位数据
for file in outputName:
    fullOutputPath = os.path.join(outputPath, file)
    # 对文件内容进行读取
    with open(fullOutputPath, 'r') as f:
        # 按行读取全部内容
        lines = f.readlines()
        for line in lines:
            a = line.split()  # 数组
            a = float(a[0])  # 转化为浮点数
            output1.append(a)
        output2 = copy.copy(output1)
        output.append(output2)
        output1.clear()

    # # 画图
    # plt.plot(frequency, phase)
    # plt.xlabel("Frequency(GHz)")
    # plt.ylabel("Phase(degree)")
    #
    # # 清空数组
    # phase.clear()

# plt.rcParams['figure.figsize']=(20, 15)
# plt.show()

for i in range(len(phase)):
    plt.plot(frequency, phase[i], label="real")
    plt.plot(frequency, output[i], label="output")
    plt.xlabel("Frequency(GHz)")
    plt.ylabel("Phase(degree)")
    plt.legend()
    plt.show()
# print(len(frequency))