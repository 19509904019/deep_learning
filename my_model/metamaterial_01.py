"""
建立三层超材料仿真吸波器
"""
import os
import cst.interface

# 当前文件所在路径
path = r'C:\Users\Dell\Desktop\仿真文件'
filename = input("请输入仿真文件名称：")
# 仿真文件路径
fullname = os.path.join(path, filename + '.cst')
# print(fullname)

# 建立工作环境
cst = cst.interface.DesignEnvironment()
# 打开微波工作室
mws = cst.new_mws()
mws.save(fullname)
# 建模
modeler = mws.modeler




