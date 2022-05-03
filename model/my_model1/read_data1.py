# import cst.results
# # import model.my_model1.metamaterial_01
# project = cst.results.ProjectFile(r'C:\Users\12414\Desktop\simulation\123.cst', allow_interactive=True)  # 允许窗口打开读取
# s11 = project.get_3d().get_result_item(r'1D Results\S-Parameters\SZmax(1),Zmax(1)')
#
# data = s11.get_ydata()
# print(data[0])
# for i in data:
#     with open(r'C:\Users\12414\Desktop\data\123.txt', 'a') as wstream:
#         wstream.write(str(i)+'\n')
container1 = []
with open(r'C:\Users\12414\Desktop\data\123.txt', 'r') as f:
        container = f.readlines()
        container = container[::34]
        with open(r'C:\Users\12414\Desktop\1.txt','a') as w:
            w.write(str(container))