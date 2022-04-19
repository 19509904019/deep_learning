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
p = 50  # 介质周期长度
h = 0.254  # 介质厚度
w = np.random.randint(20, 25)  # 金属片宽度
l = np.random.randint(30, 35)  # 金属片长度

# 在CST中加如模型基本参数
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("p","{p}")')
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("h","{h}")')
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("w","{w}")')
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("l","{l}")')
modeler.add_to_history(f'StoreParameter', 'MakeSureParameterExists("theta","0")')
modeler.add_to_history(f'StoreParameter', 'MakeSureParameterExists("phi","0")')
#


# 全局单位初始化
units = func.set_units()
modeler.add_to_history('define units', units)
#


# 设置工作频率
modeler.add_to_history('define frequency range', func.set_frequency(2, 6))
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
material1 = func.create_material('material1', 1.05)
modeler.add_to_history("create new material", material1)
#


# 建模开始

# 中间介质
medium = func.create_brick(str_name="medium", str_component="component", str_material="material1",
                           x1=-p / 2, x2=p / 2, y1=-p / 2, y2=p / 2, z1=0, z2=h)
modeler.add_to_history('create brick1', medium)

# ring1
ring_1 = func.create_brick(str_name='ring1', str_component='component', str_material='Copper (annealed)',
                           x1=-l / 2, x2=l / 2, y1=-w / 2, y2=w / 2, z1=h, z2=h)
modeler.add_to_history('create brick2', ring_1)

# ring2
ring_2 = func.create_brick(str_name='ring2', str_component='component', str_material='Copper (annealed)',
                           x1=-w / 2, x2=w / 2, y1=-l / 2, y2=l / 2, z1=h, z2=h)
modeler.add_to_history('create brick2', ring_2)

# 合并
modeler.add_to_history('add ring1 and ring2', 'Solid.Add "component:ring1", "component:ring2"')

# 仿真开始
modeler.run_solver()

# 保存
mws.save(fullname)
