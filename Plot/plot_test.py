import os

filepath = r'C:\Users\Dell\Desktop\test'
filename = os.listdir(filepath)

container = []
for file in filename:
    fullpath = os.path.join(filepath, file)
    with open(fullpath, 'r') as f:
        lines = f.readlines()
    for line in lines:
        a = line.split()
        b = float(a[-1])
        container.append(b)
    # print(container)
    flag = 0
    for i in range(1, len(container)):
        if container[i] - container[i - 1] > 180:
            flag += 1
    # 跳变几次则循环几次
    for number in range(flag):
        n = 0
        while True:
            if (container[n + 1] - container[n]) > 300:
                for i in range(n + 1, len(container)):
                    container[i] = container[i] - 360
                break
            else:
                n += 1

    print(container)