import os

# 文件夹路径
filepath = r'C:\Users\Dell\Desktop\s11_data'
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

        # 截取相位数据
        container = []
        for line in new_lines:
            a = line.split(" ")
            b = a[-1]
            container.append(b)

        # 用文件保存
        with open(r'C:\Users\Dell\Desktop\new_data\%d.txt' % int(count), 'a') as f:  # 提取后的数据文件
            for line in container:
                f.write(line)

        # 清空列表
        container.clear()
