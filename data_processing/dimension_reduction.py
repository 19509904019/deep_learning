import os

# 文件路径
filepath = r'C:\Users\Dell\Desktop\new_data\phase'
# 打开文件夹
filename = os.listdir(filepath)
filename.sort(key=lambda x: int(x[:-4]))

# 读取文件
count = 0
container = []
for file in filename:
    count += 1
    # 文件完整路径
    fullpath = os.path.join(filepath, file)
    with open(fullpath, 'r') as f:
        lines = f.readlines()
        new_lines = lines[::5]  # 均匀取点

        # 存储新文件
        savepath = r'C:\Users\Dell\Desktop\data-processing\phase\%d-phase.txt' % int(count)
        with open(savepath, 'a') as f:
            for line in new_lines:
                f.write(str(line))
