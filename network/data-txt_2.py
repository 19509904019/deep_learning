import os

# 文件夹路径
filepath = r'C:\Users\Dell\Desktop\s11_data\phase'
# 打开文件夹
filename = os.listdir(filepath)
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
        for i in range(0, len(lines)):
            new_lines = lines[2:1002]

        # 分别截取频率和相位
        container1 = []
        container2 = []
        for line in new_lines:
            a = line.split()
            b = a[-1]
            c = a[0]
            container1.append(b)  # 相位
            container2.append(c)  # 频率

        # 用文件保存
        # 相位
        with open(r'C:\Users\Dell\Desktop\new_data\phase\%d.txt' % int(count), 'a') as f:  # 提取后的数据文件
            for line in container1:
                f.write(line+'\n')

        # 频率
        with open(r'C:\Users\Dell\Desktop\new_data\frequency\%d.txt' % int(count), 'a') as f:  # 提取后的数据文件
            for line in container2:
                f.write(line+'\n')
        # 清空列表
        container1.clear()
        container2.clear()
