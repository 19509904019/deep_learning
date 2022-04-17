import cst.results

project = cst.results.ProjectFile(r'D:\CST Studio Suite 2020\project\example_6.cst')
s11 = project.get_3d().get_result_item(r'1D Results\S-Parameters\SZmax(1),Zmax(1)')

# 获取x轴的信息
x_label = s11.xlabel
print(x_label)

# x轴数值 频率
x_data = s11.get_xdata()
y_data = s11.get_ydata()
for data1, data2 in x_data, y_data:
    with open(r'd:\123.txt', 'a') as wstream:
        wstream.write(str(data1) + '\t' + str(data2) + '\n')

# # y轴数值 dB值
# y_data = s11.get_ydata()
# for data in y_data:
#     print(data)

