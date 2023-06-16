import os

# 文件夹路径
filepath = r'C:\Users\Dell\Desktop\phase1'
# 打开文件夹
filename = os.listdir(filepath)
filename.sort(key=lambda x: int(x[:-10]))
# 读取文件
count = 49944
for file in filename:
    count += 1
    # 文件完整路径
    fullpath = os.path.join(filepath, file)
    # 对文件进行截取操作
    with open(fullpath, 'r') as f:
        # 按行读取全部内容
        lines = f.readlines()
        new_lines = lines[2:1003]

        # 分别截取频率和相位
        container1 = []  # 相位
        container2 = []  # 频率
        for line in new_lines:
            a = line.split()
            b = float(a[-1])  # 相位
            c = float(a[0])   # 频率
            container1.append(b)  # 相位
            container2.append(c)  # 频率

        # 对相位数据进行unwrap处理
        flag = 0  # 统计相位跳变次数
        for i in range(1, len(container1)):
            if container1[i] - container1[i - 1] > 180:
                flag += 1

        # 跳变几次则循环几次
        for number in range(flag):
            n = 0
            while True:
                if (container1[n + 1] - container1[n]) > 180:
                    for i in range(n + 1, len(container1)):
                        container1[i] = container1[i] - 360
                    break
                else:
                    n += 1

        # 用文件保存
        # 相位
        with open(r'C:\Users\Dell\Desktop\phase\%d.txt' % int(count), 'a') as f:  # 提取后的数据文件
            for line in container1:
                f.write(str(line) + '\n')

        # # 频率
        # with open(r'C:\Users\Dell\Desktop\frequency\%d.txt' % int(count), 'a') as f:  # 提取后的数据文件
        #     for line in container2:
        #         f.write(str(line) + '\n')

        # 清空列表
        container1.clear()
        container2.clear()
