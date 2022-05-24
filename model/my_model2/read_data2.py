import cst.results
# import model.my_model2.model2 as model2
project = cst.results.ProjectFile(r'C:\Users\Dell\Desktop\simulation\1.cst', allow_interactive=True)  # 允许窗口打开读取
s11 = project.get_3d().get_result_item(r'1D Results\S-Parameters\SZmax(1),Zmax(1)')
data1 = s11.get_ydata()
print(data1)
# print(len(data1))
print(s11.ylabel)
# data2 = s11.
# for i in data:
#     with open(r'C:\Users\Dell\Desktop\123.txt', 'a') as wstream:
#         wstream.write(str(i) + '\n')
