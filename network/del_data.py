# """
# csv转化为txt文档
#
# """
# import csv
#
# count = 10016
# # 读取数据源
# with open(r'C:\Users\Dell\Desktop\all.csv', 'r') as f:
#     reader = csv.reader(f)
#     for i in reader:
#         count += 1
#         for j in i:
#             with open(r'C:\Users\Dell\Desktop\data_all_51\%d-data.txt' % count, 'a') as f:
#                 f.write(j + '\n')


# """
# 删除超过-450的数据
# """
# import os
#
# # 文件夹路径
# filepath = r'C:\Users\Dell\Desktop\data3'
# # 打开文件夹
# filename = os.listdir(filepath)
# filename.sort(key=lambda x: int(x[:-9]))
# # 读取文件
# container = []
# container1 = []
# for file in filename:
#     # 文件完整路径
#     fullpath = os.path.join(filepath, file)
#     # 对文件进行截取操作
#     with open(fullpath, 'r') as f:
#         # 按行读取全部内容
#         lines = f.readlines()
#         new_lines = lines[:1001]
#         for line in new_lines:
#             a = line.split()
#             b = float(a[-1])
#             container.append(b)
#
#         for data in container:
#             if data < -450:
#                 print(file)
#                 container1.append(fullpath)
#                 break
#
#         # 清空列表
#         container.clear()
#
# print(len(container1))
# #
# for path in container1:
#     os.remove(path)

# """
# 删除具有小跳变的数据
# """
# import os
#
# # 文件夹路径
# filepath = r'C:\Users\Dell\Desktop\data3'
# # 打开文件夹
# filename = os.listdir(filepath)
# filename.sort(key=lambda x: int(x[:-9]))
# # 读取文件
# container = []
# container1 = []
# for file in filename:
#     # 文件完整路径
#     fullpath = os.path.join(filepath, file)
#     # 对文件进行截取操作
#     with open(fullpath, 'r') as f:
#         # 按行读取全部内容
#         lines = f.readlines()
#         new_lines = lines[:1001]
#         for line in new_lines:
#             a = line.split()
#             b = float(a[-1])
#             container.append(b)
#
#         for number in range(len(container) - 1):
#             if container[number + 1] - container[number] > 0:
#                 print(file)
#                 container1.append(fullpath)
#                 break
#
#         # 清空列表
#         container.clear()
#
# print(len(container1))
#
# for path in container1:
#     os.remove(path)


"""
清空文件夹
"""
import os

# 文件夹路径
filepath = r'C:\Users\Dell\Desktop\data_all_51'
# 打开文件夹
filename = os.listdir(filepath)
filename.sort(key=lambda x: int(x[:-9]))
# 读取文件
container = []
container1 = []
for file in filename:
    # 文件完整路径
    fullpath = os.path.join(filepath, file)
    container1.append(fullpath)
for path in container1:
    os.remove(path)