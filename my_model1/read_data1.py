import cst.results
from my_model1 import metamaterial_01

project = cst.results.ProjectFile(r'C:\Users\Dell\Desktop\simulation\123.cst', allow_interactive=True)  # 允许窗口打开读取
s11 = project.get_3d().get_result_item(r'1D Results\S-Parameters\SZmax(1),Zmax(1)')

data = s11.get_data()
for i in data:
    with open(r'C:\Users\Dell\Desktop\data\123.txt', 'a') as wstream:
        wstream.write(str(i) + '\n')
