import os
import cst.interface
import cst.results
import numpy as np
import random
from picture_processing.get_01_array import get_0_1_array

# 建立仿真环境
cst = cst.interface.DesignEnvironment()
mws = cst.new_mws()
# 建立模型
modeler = mws.modeler

# 存储数据量
count = 0
for i in range(200):
    count += 1
    # # 文件存储路径
    # path = r'C:\Users\Dell\Desktop\simulation'
    # fullname = os.path.join(path, f'{count}.cst')
    # mws.save(fullname)

    # 模型基本参数
    p = 8  # 周期
    h = 2  # 介质层厚度
    t = 0.5  # 金属片长度
    # 在CST中添加模型基本参数
    modeler.add_to_history('StoreParameter', 'MakeSureParameterExists("theta","0")')
    modeler.add_to_history('StoreParameter', 'MakeSureParameterExists("phi","0")')
    modeler.add_to_history('StoreParameter', f'MakeSureParameterExists("p","{p}")')
    modeler.add_to_history('StoreParameter', f'MakeSureParameterExists("h","{h}")')
    modeler.add_to_history('StoreParameter', f'MakeSureParameterExists("t","{t}")')
    # 基本参数设置完成

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
    modeler.add_to_history('set units', sCommand)
    # 全局单位初始化结束

    # 设置工作频率
    frq1 = 5
    frq2 = 15
    sCommand = 'Solver.FrequencyRange "%f", "%f"' % (frq1, frq2)
    modeler.add_to_history('set frequency range', sCommand)
    # 工作频率设置结束

    # 设置背景材料:Normal
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
    modeler.add_to_history("set background", sCommand)
    # 背景材料设置结束

    # 设置边界条件
    sCommand = ['With Boundary',
                '.Xmin "electric"',
                '.Xmax "electric"',
                '.Ymin "magnetic"',
                '.Ymax "magnetic"',
                '.Zmin "expanded open"',
                '.Zmax "expanded open"',
                '.Xsymmetry "electric"',
                '.Ysymmetry "magnetic"',
                '.Zsymmetry "none"',
                '.ApplyInAllDirections "False"',
                '.OpenAddSpaceFactor "0.5"',
                'End With']
    sCommand = line_break.join(sCommand)
    modeler.add_to_history('set boundary conditions', sCommand)
    # 设置边界条件结束

    # 设置求解器
    sCommand = 'ChangeSolverType("HF Time Domain")'
    modeler.add_to_history('set slover type', sCommand)
    # 求解器设置结束

    # 设置端口
    sCommand = ['With Port',
                '.Reset',
                '.PortNumber "1"',
                '.Label ""',
                '.Folder ""',
                '.NumberOfModes "1"',
                '.AdjustPolarization "False"',
                '.PolarizationAngle "0.0"',
                '.ReferencePlaneDistance "0"',
                '.TextSize "50"',
                '.TextMaxLimit "1"',
                '.Coordinates "Full"',
                '.Orientation "zmax"',
                '.PortOnBound "True"',
                '.ClipPickedPortToBound "False"',
                '.Xrange "-8", "8"',
                '.Yrange "-8", "8"',
                '.Zrange "10.51281145", "10.51281145"',
                '.XrangeAdd "0.0", "0.0"',
                '.YrangeAdd "0.0", "0.0"',
                '.ZrangeAdd "0.0", "0.0"',
                '.SingleEnded "False"',
                '.WaveguideMonitor "False"',
                '.Create',
                'End With']
    sCommand = line_break.join(sCommand)
    modeler.add_to_history('set Port', sCommand)
    # 端口设置结束

    # 计算方式设置
    sCommand = ['Mesh.SetCreator "High Frequency"',
                'With Solver ',
                '.Method "Hexahedral"',
                '.CalculationType "TD-S"',
                '.StimulationPort "1"',
                '.StimulationMode "1"',
                '.SteadyStateLimit "-40"',
                '.MeshAdaption "False"',
                '.CalculateModesOnly "False"',
                '.SParaSymmetry "False"',
                '.StoreTDResultsInCache  "False"',
                '.FullDeembedding "False"',
                '.SuperimposePLWExcitation "False"',
                '.UseSensitivityAnalysis "False"',
                'End With']
    sCommand = line_break.join(sCommand)
    modeler.add_to_history('set excitation', sCommand)
    # 设置完成

    # 定义中间介质
    sCommand = ['With Material',
                '.Reset',
                '.Name "medium"',
                '.Folder ""',
                '.Rho "0.0"',
                '.ThermalType "Normal"',
                '.ThermalConductivity "0"',
                '.SpecificHeat "0", "J/K/kg"',
                '.DynamicViscosity "0"',
                '.Emissivity "0"',
                '.MetabolicRate "0.0"',
                '.VoxelConvection "0.0"',
                '.BloodFlow "0"',
                '.MechanicsType "Unused"',
                '.FrqType "all"',
                '.Type "Normal"',
                '.MaterialUnit "Frequency", "GHz"',
                '.MaterialUnit "Geometry", "mm"',
                '.MaterialUnit "Time", "s"',
                '.MaterialUnit "Temperature", "Kelvin"',
                '.Epsilon "4.3"',
                '.Mu "1"',
                '.Sigma "0"',
                '.TanD "0.0035"',
                '.TanDFreq "0.0"',
                '.TanDGiven "True"',
                '.TanDModel "ConstTanD"',
                '.EnableUserConstTanDModelOrderEps "False"',
                '.ConstTanDModelOrderEps "1"',
                '.SetElParametricConductivity "False"',
                '.ReferenceCoordSystem "Global"',
                '.CoordSystemType "Cartesian"',
                '.SigmaM "0"',
                '.TanDM "0.0"',
                '.TanDMFreq "0.0"',
                '.TanDMGiven "False"',
                '.TanDMModel "ConstTanD"',
                '.EnableUserConstTanDModelOrderMu "False"',
                '.ConstTanDModelOrderMu "1"',
                '.SetMagParametricConductivity "False"',
                '.DispModelEps "None"',
                '.DispModelMu "None"',
                '.DispersiveFittingSchemeEps "Nth Order"',
                '.MaximalOrderNthModelFitEps "10"',
                '.ErrorLimitNthModelFitEps "0.1"',
                '.UseOnlyDataInSimFreqRangeNthModelEps "False"',
                '.DispersiveFittingSchemeMu "Nth Order"',
                '.MaximalOrderNthModelFitMu "10"',
                '.ErrorLimitNthModelFitMu "0.1"',
                '.UseOnlyDataInSimFreqRangeNthModelMu "False"',
                '.UseGeneralDispersionEps "False"',
                '.UseGeneralDispersionMu "False"',
                '.NLAnisotropy "False"',
                '.NLAStackingFactor "1"',
                '.NLADirectionX "1"',
                '.NLADirectionY "0"',
                '.NLADirectionZ "0"',
                '.Colour "0", "0.501961", "1"',
                '.Wireframe "False"',
                '.Reflection "False"',
                '.Allowoutline "True"',
                '.Transparentoutline "False"',
                '.Transparency "0"',
                '.Create',
                'End With']
    sCommand = line_break.join(sCommand)
    modeler.add_to_history('create material1', sCommand)

    # 建模开始
    # 介质层
    sCommand = ['With Brick',
                '.Reset',
                '.Name "%s"' % 'middle_layer',
                '.Component "%s"' % 'component1',
                '.Material "%s"' % 'medium',
                f'.Xrange "-p/2", "p/2"',
                f'.Yrange "-p/2", "p/2"',
                f'.Zrange "0", "h"',
                '.Create',
                'End With']
    sCommand = line_break.join(sCommand)
    modeler.add_to_history('define brick', sCommand)

    # 金属背板
    sCommand = ['With Brick',
                '.Reset',
                '.Name "%s"' % 'bottom_layer',
                '.Component "%s"' % 'component1',
                '.Material "%s"' % 'Copper (annealed)',
                f'.Xrange "-p/2", "p/2"',
                f'.Yrange "-p/2", "p/2"',
                f'.Zrange "-0.018", "0"',
                '.Create',
                'End With']
    sCommand = line_break.join(sCommand)
    modeler.add_to_history('define brick', sCommand)

    # 金属层
    # 随机生成矩阵并用文档进行存储
    rate = '%.1f' % (random.randint(3, 7) * 0.1)  # 0所占数组的比重
    arr = get_0_1_array(np.eye(8), rate=float(rate))
    # print(arr)
    # f = open(rf'C:\Users\Dell\Desktop\arr_data\{count}-matrix.txt', 'a')
    # for i in range(arr.shape[0]):
    #     for j in range(arr.shape[1]):
    #         f.write(str(arr[i][j]) + '\n')
    # f.close()

    # 利用随机矩阵进行金属片建模
    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            if arr[x][y] == 1:
                # 创建金属单元
                sCommand = ['With Brick',
                            '.Reset',
                            '.Name "metal_%.0f_%.0f"' % (x + 1, y + 1),
                            '.Component "component1"',
                            '.Material "Copper (annealed)"',
                            '.Xrange "%f","%f"' % (y * 0.5 - (p / 2), y * 0.5 - (p / 2) + t),
                            '.Yrange "%f","%f"' % ((p / 2) - (x * 0.5 + t), (p / 2) - x * 0.5),
                            '.Zrange "h","h+0.018"',
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

                # 旋转操作
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

    # 仿真开始
    modeler.run_solver()
    # 仿真结束

    # # 保存
    # mws.save(fullname)

    # 导出phase数据
    sCommmd = ['SelectTreeItem("1D Results\S-Parameters\S1,1")',
               'With Plot1D',
               '.PlotView "phase"',
               'End With',
               'With ASCIIExport',
               '.Reset',
               '.FileName "%s"' % rf'C:\Users\Dell\Desktop\s11_data\phase\{count}-phase.txt',
               '.Execute',
               'End With']
    sCommmd = '\n'.join(sCommmd)
    modeler.add_to_history('save phase', sCommmd)

    # 导出linear数据
    sCommmd = ['SelectTreeItem("1D Results\S-Parameters\S1,1")',
               'With Plot1D',
               '.PlotView "magnitude"',
               'End With',
               'With ASCIIExport',
               '.Reset',
               '.FileName "%s"' % rf'C:\Users\Dell\Desktop\s11_data\linear\{count}-linear.txt',
               '.Execute',
               'End With']
    sCommmd = '\n'.join(sCommmd)
    modeler.add_to_history('save linear', sCommmd)

    # 删除component
    sCommand = 'Component.Delete "component1" '
    modeler.add_to_history('delete component', sCommand)
    # 删除完成
