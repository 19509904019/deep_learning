import os
import cst.interface
import numpy as np
from function import func
from picture_processing.get_01_array import get_0_1_array

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
l = 1
h = 1
# 在CST中添加模型基本参数
modeler.add_to_history(f'StoreParameter', 'MakeSureParameterExists("theta","0")')
modeler.add_to_history(f'StoreParameter', 'MakeSureParameterExists("phi","0")')
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("p","{p}")')
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("l","{l}")')
modeler.add_to_history(f'StoreParameter', f'MakeSureParameterExists("h","{h}")')

line_break = '\n'
# 全局单位初始化
sCommand = ['With Units',
            '.Geometry "mm"',
            '.Frequency "GHz"',
            '.Voltage "V"',
            '.Resistance "Ohm"',
            '.Inductance "H"',
            '.TemperatureUnit  "Kelvin"',
            '.Time "ns"',
            '.Current "A"',
            '.Conductance "Siemens"',
            '.Capacitance "F"',
            'End With']
sCommand = line_break.join(sCommand)
modeler.add_to_history('define units', sCommand)
# 全局单位初始化结束


# 设置工作频率
frq1 = 2
frq2 = 18
sCommand = 'Solver.FrequencyRange "%f", "%f"' % (frq1, frq2)
modeler.add_to_history('define frequency range', sCommand)
# 工作频率设置结束


# 设置背景材料
sCommand = ['With Background',
            '.Type "Normal"',
            '.Epsilon "1.0"',
            '.Mu "1.0"',
            '.Rho "1.204"',
            '.ThermalType "Normal"',
            '.ThermalConductivity "0.026"',
            '.HeatCapacity "1.005"',
            '.XminSpace "0.0"',
            '.XmaxSpace "0.0"',
            '.YminSpace "0.0"',
            '.YmaxSpace "0.0"',
            '.ZminSpace "0.0"',
            '.ZmaxSpace "0.0"',
            'End With']
sCommand = line_break.join(sCommand)
modeler.add_to_history("define background", sCommand)
# 背景材料设置结束


# 设置边界条件
sCmmand = ['With Boundary',
           '.Xmin "unit cell"',
           '.Xmax "unit cell"',
           '.Ymin "unit cell"',
           '.Ymax "unit cell"',
           '.Zmin "electric"',
           '.Zmax "expanded open"',
           '.Xsymmetry "none"',
           '.Ysymmetry "none"',
           '.Zsymmetry "none"',
           '.ApplyInAllDirections "False"',
           '.XPeriodicShift "0.0"',
           '.YPeriodicShift "0.0"',
           '.ZPeriodicShift "0.0"',
           '.PeriodicUseConstantAngles "False"',
           '.SetPeriodicBoundaryAngles "theta", "phi"',
           '.SetPeriodicBoundaryAnglesDirection "inward"',
           '.UnitCellFitToBoundingBox "True"',
           '.UnitCellDs1 "0.0"',
           '.UnitCellDs2 "0.0"',
           '.UnitCellAngle "90.0"',
           'End With']
sCmmand = line_break.join(sCmmand)
modeler.add_to_history('define boundary', sCommand)
# 设置边界条件结束


# 设置求解器
sCommand = 'ChangeSolverType("HF Frequency Domain")'
modeler.add_to_history('set slover type', sCommand)
# 求解器设置结束


# 设置端口
sCommand = ['With FloquetPort',
            '.Reset',
            '.SetDialogTheta "0"',
            '.SetDialogPhi "0"',
            '.SetSortCode "+beta/pw"',
            '.SetCustomizedListFlag "False"',
            '.Port "Zmin"',
            '.SetNumberOfModesConsidered "2"',
            '.Port "Zmax"',
            '.SetNumberOfModesConsidered "2"',
            'End With']
sCommand = line_break.join(sCommand)
modeler.add_to_history('define FloquetPort', sCommand)
# 端口设置结束


# 设置激励
sCommand = ['With FDSolver',
            '.Reset',
            '.Stimulation "List", "List"',
            '.ResetExcitationList',
            '.AddToExcitationList "Zmax", "TE(0,0);TM(0,0)"',
            '.LowFrequencyStabilization "False"',
            'End With']
sCommand = line_break.join(sCommand)
modeler.add_to_history('set excitation', sCommand)
# 设置完成

# 建模开始

# 介质层
sCommand = ['With Brick',
            '.Reset',
            '.Name "%s"' % 'solid1',
            '.Component "%s"' % 'component1',
            '.Material "%s"' % 'Vacuum',
            f'.Xrange "-p/2", "p/2"',
            f'.Yrange "-p/2", "p/2"',
            f'.Zrange "0", "h"',
            '.Create',
            'End With']
sCommand = line_break.join(sCommand)
modeler.add_to_history('define brick', sCommand)

# 金属层
arr = get_0_1_array(np.eye(int(p / 2)), rate=0.4)

for x in range(arr.shape[0]):
    for y in range(arr.shape[1]):
        if arr[x][y] == 1:
            # 创建金属单元
            sCommand = ['With Brick',
                        '.Reset',
                        '.Name "metal_%.0f_%.0f"' % (x + 1, y + 1),
                        '.Component "component1"',
                        '.Material "Copper (annealed)"',
                        '.Xrange "%d","%d"' % (x, x + 1),
                        '.Yrange "%d","%d"' % (y, y + 1),
                        '.Zrange "h","h + 0.1"',
                        '.Create',
                        'End With']
            sCommand = line_break.join(sCommand)
            modeler.add_to_history('define brick', sCommand)

            # 镜像操作 以x平面为轴
            sCommand = ['With Transform',
                        '.Reset',
                        '.Name "component1:metal_%.0f_%.0f"' % (x + 1, y + 1),
                        '.Origin "Free"',
                        '.Center "0", "0", "0"',
                        '.PlaneNormal "1", "0", "0"',
                        '.MultipleObjects "True"',
                        '.GroupObjects "False"',
                        '.Repetitions "1"',
                        '.MultipleSelection "False"',
                        '.Destination ""',
                        '.Material ""',
                        '.Transform "Shape", "Mirror"',
                        'End With']
            sCommand = line_break.join(sCommand)
            modeler.add_to_history('transform:mirror', sCommand)

            # 镜像操作 以y平面为轴
            sCommand = ['With Transform',
                        '.Reset',
                        '.Name "component1:metal_%.0f_%.0f"' % (x + 1, y + 1),
                        '.Origin "Free"',
                        '.Center "0", "0", "0"',
                        '.PlaneNormal "0", "1", "0"',
                        '.MultipleObjects "True"',
                        '.GroupObjects "False"',
                        '.Repetitions "1"',
                        '.MultipleSelection "False"',
                        '.Destination ""',
                        '.Material ""',
                        '.Transform "Shape", "Mirror"',
                        'End With']
            sCommand = line_break.join(sCommand)
            modeler.add_to_history('transform:mirror', sCommand)

            # 镜像操作 以x,y平面为轴
            sCommand = ['With Transform',
                        '.Reset',
                        '.Name "component1:metal_%.0f_%.0f"' % (x + 1, y + 1),
                        '.Origin "Free"',
                        '.Center "0", "0", "0"',
                        '.Angle "0", "0", "180"',
                        '.MultipleObjects "True"',
                        '.GroupObjects "False"',
                        '.Repetitions "1"',
                        '.MultipleSelection "False"',
                        '.Destination ""',
                        '.Material ""',
                        '.Transform "Shape", "Rotate"',
                        'End With']
            sCommand = line_break.join(sCommand)
            modeler.add_to_history('transform:rotate', sCommand)

# # 仿真开始
# modeler.run_solver()
# # 仿真结束

# 保存
mws.save(fullname)
