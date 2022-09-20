import os

# 文件夹路径
filepath = r'C:\Users\Dell\Desktop\data\s11_data\linear'
# 打开文件
filename = os.listdir(filepath)
filename.sort(key=lambda x: int(x[:-11]))
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
        # 截取数据内容
        for i in range(0, len(lines)):
            new_lines = lines[2:1002]

    # 截取linear数据
    container = []
    for line in new_lines:
        datas = line.split()
        linears = datas[-1]
        # 将截取的linear数据保存到列表
        container.append(linears)

    # 保存截取的linear数据
    savepath = r'C:\Users\Dell\Desktop\new_data\linear\%d.txt' % int(count)
    with open(savepath, 'a') as f:
        for linear in container:
            f.write(str(linear) + '\n')

    # 清空列表保存下一个数据
    container.clear()
