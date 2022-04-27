import os
import cst.interface
import numpy as np
from function import func

# 文件存储路径
path = r'C:\Users\Dell\Desktop\simulation'
filename = input("请输入文件名:")
fullname = os.path.join(path, filename + '.cst')

# 建立仿真环境
cst = cst.interface.DesignEnvironment()
mws = cst.new_mws()
mws.save(fullname)
# 建立模型
modeler = mws.modeler

# 模型基本参数
p = 16
h1 = 5.01
w1 = 2
w2 = 0.5
h2 = 6
w3 = 2.03
w4 = 0.99
h3 = 4.66
w5 = 3
w6 = 0.48

# 在CST中添加模型基本参数
modeler.add_to_history(f'StoreParameter', 'MakeSureParameterExists("theta","0")')
modeler.add_to_history(f'StoreParameter', 'MakeSureParameterExists("phi","0")')
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("h1","{h1}")')
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("w1","{w1}")')
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("w2","{w2}")')
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("h2","{h2}")')
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("w3","{w3}")')
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("w4","{w4}")')
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("h3","{h3}")')
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("w5","{w5}")')
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("w6","{w6}")')
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("p","{p}")')

# 全局单位初始化
units = func.set_units()
modeler.add_to_history('define units', units)
#


# 设置工作频率
modeler.add_to_history('define frequency range', func.set_frequency(0, 18))
#


# 设置背景材料
background = func.set_background()
modeler.add_to_history("define background", background)
#


# 设置边界条件
boundary = func.set_boundary()
modeler.add_to_history('define boundary', boundary)
#

# 设置求解器
modeler.add_to_history('set slover type', func.set_frequencydomain())
#


# 设置端口
modeler.add_to_history('set floquetport', func.set_floquetport())
#

# 设置激励
modeler.add_to_history('set excitation', func.solver_excitation())
#


# 新建介质材料
PMI = func.create_material('PMI', 1.05)
modeler.add_to_history("create new material", PMI)
#
# 新建金属片
Lossymetal = func.create_Lossymetal('Lossymetal', 220)
modeler.add_to_history("create lossymetal", Lossymetal)

# 建模开始

# 底层
bottom = func.create_brick(str_name='bottom_layer', str_component='component1', str_material='PMI',
                           x1=-p / 2, x2=p / 2, y1=-p / 2, y2=p / 2, z1=0, z2=h3)
modeler.add_to_history('define bottom_layer', bottom)

ring3 = func.create_brick(str_name='ring3', str_component='component1', str_material='Lossymetal',
                          x1=-(p / 2 - w6), x2=(p / 2 - w6), y1=-(p / 2 - w6), y2=(p / 2 - w6), z1=h3, z2=h3)
modeler.add_to_history('define ring3', ring3)
#

ring3_1 = func.create_brick(str_name='ring3_1', str_component='component1', str_material='PEC',
                            x1=-(p / 2 - w5), x2=(p / 2 - w5), y1=-(p / 2 - w5), y2=(p / 2 - w5), z1=h3, z2=h3)
modeler.add_to_history('define ring3_1', ring3_1)
#

modeler.add_to_history('Subtract:ring3-ring3_1', 'Solid.Subtract "component1:ring3", "component1:ring3_1"')

# 中间层
middle = func.create_brick(str_name='middle_layer', str_component='component1', str_material='PMI',
                           x1=-p / 2, x2=p / 2, y1=-p / 2, y2=p / 2, z1=h3, z2=h3 + h2)
modeler.add_to_history('define middle_layer', middle)
#
ring2 = func.create_brick(str_name='ring2', str_component='component1', str_material='Lossymetal',
                          x1=-(p / 2 - w4), x2=(p / 2 - w4), y1=-(p / 2 - w4), y2=(p / 2 - w4), z1=h3 + h2, z2=h3 + h2)
modeler.add_to_history('define ring2', ring2)
#

ring2_1 = func.create_brick(str_name='ring2_1', str_component='component1', str_material='PEC',
                            x1=-(p / 2 - w3), x2=(p / 2 - w3), y1=-(p / 2 - w3), y2=(p / 2 - w3), z1=h3 + h2,
                            z2=h3 + h2)
modeler.add_to_history('define ring2_1', ring2_1)
#
modeler.add_to_history('Subtract:ring2-ring2_1', 'Solid.Subtract "component1:ring2", "component1:ring2_1"')

# 最上层
top = func.create_brick(str_name='top_layer', str_component='component1', str_material='PMI',
                        x1=-p / 2, x2=p / 2, y1=-p / 2, y2=p / 2, z1=h3 + h2, z2=h3 + h2 + h1)
modeler.add_to_history('define top_layer', top)

ring1 = func.create_brick(str_name='ring1', str_component='component1', str_material='Lossymetal',
                          x1=-(p / 2 - w2), x2=(p / 2 - w2), y1=-(p / 2 - w2), y2=(p / 2 - w2), z1=h1 + h3 + h2,
                          z2=h1 + h3 + h2)
modeler.add_to_history('define ring1', ring1)
#

ring1_1 = func.create_brick(str_name='ring1_1', str_component='component1', str_material='PEC',
                            x1=-(p / 2 - w1), x2=(p / 2 - w1), y1=-(p / 2 - w1), y2=(p / 2 - w1), z1=h1 + h3 + h2,
                            z2=h1 + h3 + h2)
modeler.add_to_history('define ring1_1', ring1_1)
#

modeler.add_to_history('Subtract:ring1-ring1_1', 'Solid.Subtract "component1:ring1", "component1:ring1_1"')

# 合并
modeler.add_to_history('insert:bottom,ring3', 'Solid.Insert "component1:bottom_layer", "component1:ring3"')
modeler.add_to_history('insert:middle,ring2', 'Solid.Insert "component1:middle_layer", "component1:ring2"')
modeler.add_to_history('insert:top,ring1', 'Solid.Insert "component1:top_layer", "component1:ring1"')

# 仿真开始
modeler.run_solver()

# 保存
mws.save(fullname)

# dataname = 'example.txt'
# sCommmd = ['With ASCIIExport',
#            '.Reset',
#            '.FileName "%s"' % dataname,
#            '.Mode("FixedNumber")',
#            '.StepX (12)',
#            '.StepY (12)',
#            '.StepZ (8)',
#            '.Execute',
#            'End With']
# sCommmd = '\n'.join(sCommmd)
# modeler.add_to_history('save data', sCommmd)
