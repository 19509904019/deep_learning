# 将原文件的内容进行划分
container1 = []
with open(r'C:\Users\Dell\Desktop\dB.txt', 'r') as f:
    # 按行读取全部内容
    lines = f.readlines()
    for i in range(0, len(lines), 1007):
        new_lines = lines[i + 2:i + 1002]
        container1.append(new_lines)

# 将每组数据取出(频率  响应数据)
count1 = 0  # 作为文件序列
for data in container1:
    count1 += 1
    with open(r'C:\Users\Dell\Desktop\data\data1\%d.txt' % count1, 'a') as w:
        data = "".join(data)
        w.write(data)

# 取出电磁响应数据
count2 = 0
for i in range(len(container1)):
    count2 += 1
    with open(r'C:\Users\Dell\Desktop\data\data1\%d.txt' % count2, 'r') as f2:
        line = f2.readline()  # 按每行读取,方便切片
        container2 = []  # 存放电磁响应的数据
        while line:
            a = line.split(" ")  # 按照空格划分成列表
            b = a[-1]   # 取最后一列数据，即电磁响应数据
            container2.append(b)
            line = f2.readline()

    # 存放电磁响应数据
    with open(r'C:\Users\Dell\Desktop\data\data2\%d.txt' % count2, 'a') as f3:  # 提取后的数据文件
        for line in container2:
            f3.write(line)

    # 对响应数据进行切片输出50个数据
    with open(r'C:\Users\Dell\Desktop\data\data3\%d.txt' % count2, 'a') as f4:  # 提取后的数据文件
        for line in container2[5::20]:
            f4.write(line)
    # 清空列表
    container2.clear()
