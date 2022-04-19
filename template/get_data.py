import cst.results

project = cst.results.ProjectFile(r'C:\Users\Dell\Desktop\simulation\123.cst', allow_interactive=True)  # 允许窗口打开读取
s11 = project.get_3d().get_result_item(r'1D Results\S-Parameters\SZmax(1),Zmax(1)')

# 获取x轴的信息
x_label = s11.xlabel
y_label = s11.ylabel
print(x_label)
print(y_label)

# # x轴数值 频率
# x_data = s11.get_xdata()
# y_data = s11.get_ydata()
# for data1 in x_data:
#     with open(r'd:\123.txt', 'a') as wstream:
#         wstream.write(str(data1) + '\n')
# x_data = s11.get_xdata()
# count = 0
# for data in x_data:
#     count += 1
#     print(data, end=' ')
#     if count % 5 == 0:
#         print()
#         print()
# y轴数值 dB值
# y_data = s11.get_ydata()
# for data in y_data:
#     print(data)

data = s11.get_data()
for i in data:
    print(i)

# print(s11.treepath)

# print(s11.title)