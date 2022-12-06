import os

# 文件夹路径
filepath = r'C:\Users\Dell\Desktop\data_all_51'
# 打开文件夹
filename = os.listdir(filepath)
filename.sort(key=lambda x: int(x[:-9]))
# 读取文件
count = 0
for file in filename:
    count += 1
    # 文件完整路径
    fullpath = os.path.join(filepath, file)
    # 对文件进行截取操作
    with open(fullpath, 'r') as f:
        # 按行读取全部内容
        lines = f.readlines()
        new_lines = lines[::20]

        container1 = []  # 相位
        for line in new_lines:
            a = line.split()
            b = float(a[-1])  # 相位
            container1.append(b)  # 相位

        # 用文件保存
        # 相位
        with open(r'C:\Users\Dell\Desktop\data\%d.txt' % int(count), 'a') as f:  # 提取后的数据文件
            for line in container1:
                f.write(str(line) + '\n')

        # 清空列表
        container1.clear()
