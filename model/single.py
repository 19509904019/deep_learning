import cst.interface
import cst.results
import numpy as np
import pandas as pd

# 建模矩阵
path = r'C:\Users\Dell\Desktop\ran.csv'
arr = pd.read_csv(path, header=None)
arr = arr.values.tolist()
# 建模矩阵加载完成


# 建立仿真环境与模型
cst = cst.interface.DesignEnvironment()
mws = cst.new_mws()
modeler = mws.modeler
# 建立环境与模型完成


# 模型基本参数
p = 9.6  # 周期
h = 3.26  # 介质层厚度
t = 0.8  # 金属片长度
# 在CST中添加模型基本参数
modeler.add_to_history('StoreParameter', 'MakeSureParameterExists("theta","0")')
modeler.add_to_history('StoreParameter', 'MakeSureParameterExists("phi","0")')
modeler.add_to_history('StoreParameter', f'MakeSureParameterExists("p","{p}")')
modeler.add_to_history('StoreParameter', f'MakeSureParameterExists("h","{h}")')
modeler.add_to_history('StoreParameter', f'MakeSureParameterExists("t","{t}")')
# 基本参数设置完成


# 全局初始化
line_break = '\n'
# set the units
sCommand = ['With Units',
            '.Geometry "mm"',
            '.Frequency "GHz"',
            '.Voltage "V"',
            '.Resistance "Ohm"',
            '.Inductance "H"',
            '.TemperatureUnit  "Kelvin"',
            '.Time "s"',
            '.Current "A"',
            '.Conductance "Siemens"',
            '.Capacitance "F"',
            'End With']
sCommand = line_break.join(sCommand)
modeler.add_to_history('set units', sCommand)

sCommand = 'Plot.DrawBox False'
modeler.add_to_history('set DrawBox', sCommand)

# set the Background
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

# define Floquet port boundaries
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
modeler.add_to_history("set Floquet", sCommand)

# define boundaries
sCommand = ['With Boundary',
            '.Xmin "unit cell"',
            '.Xmax "unit cell"',
            '.Ymin "unit cell"',
            '.Ymax "unit cell"',
            '.Zmin "expanded open"',
            '.Zmax "expanded open"',
            '.Xsymmetry "none"',
            '.Ysymmetry "none"',
            '.Zsymmetry "none"',
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
sCommand = line_break.join(sCommand)
modeler.add_to_history("set boundaries", sCommand)

# set tet mesh as default
sCommand = ['With Mesh',
            '.MeshType "Tetrahedral"',
            'End With']
sCommand = line_break.join(sCommand)
modeler.add_to_history("set tet mesh", sCommand)

# FD solver excitation with incoming plane wave at Zmax
sCommand = ['With FDSolver',
            '.Reset',
            '.Stimulation "List", "List"',
            '.ResetExcitationList',
            '.AddToExcitationList "Zmax", "TE(0,0);TM(0,0)"',
            '.LowFrequencyStabilization "False"',
            'End With']
sCommand = line_break.join(sCommand)
modeler.add_to_history("set solver", sCommand)

sCommand = ['With MeshSettings',
            '.SetMeshType "Hex"',
            '.Set "Version", 1%',
            'End With']
sCommand = line_break.join(sCommand)
modeler.add_to_history("MeshSettings", sCommand)

sCommand = ['With Mesh',
            '.MeshType "PBA"',
            'End With']
sCommand = line_break.join(sCommand)
modeler.add_to_history("Mesh", sCommand)

# set the solver type
sCommand = 'ChangeSolverType("HF Time Domain")'
modeler.add_to_history('set solver type', sCommand)
# 全局数据初始化结束


# 定义材料
# define Copper(annealed)
sCommand = ['With Material',
            '.Reset',
            '.Name "Copper (annealed)"',
            '.Folder ""',
            '.FrqType "static"',
            '.Type "Normal"',
            '.SetMaterialUnit "Hz", "mm"',
            '.Epsilon "1"',
            '.Mu "1.0"',
            '.Kappa "5.8e+007"',
            '.TanD "0.0"',
            '.TanDFreq "0.0"',
            '.TanDGiven "False"',
            '.TanDModel "ConstTanD"',
            '.KappaM "0"',
            '.TanDM "0.0"',
            '.TanDMFreq "0.0"',
            '.TanDMGiven "False"',
            '.TanDMModel "ConstTanD"',
            '.DispModelEps "None"',
            '.DispModelMu "None"',
            '.DispersiveFittingSchemeEps "Nth Order"',
            '.DispersiveFittingSchemeMu "Nth Order"',
            '.UseGeneralDispersionEps "False"',
            '.UseGeneralDispersionMu "False"',
            '.FrqType "all"',
            '.Type "Lossy metal"',
            '.SetMaterialUnit "GHz", "mm"',
            '.Mu "1.0"',
            '.Kappa "5.8e+007"',
            '.Rho "8930.0"',
            '.ThermalType "Normal"',
            '.ThermalConductivity "401.0"',
            '.SpecificHeat "390", "J/K/kg"',
            '.MetabolicRate "0"',
            '.BloodFlow "0"',
            '.VoxelConvection "0"',
            '.MechanicsType "Isotropic"',
            '.YoungsModulus "120"',
            '.PoissonsRatio "0.33"',
            '.ThermalExpansionRate "17"',
            '.Colour "1", "1", "0"',
            '.Wireframe "False"',
            '.Reflection "False"',
            '.Allowoutline "True"',
            '.Transparentoutline "False"',
            '.Transparency "0"',
            '.Create',
            'End With']
sCommand = line_break.join(sCommand)
modeler.add_to_history("define Copper(annealed)", sCommand)

# define medium
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
            '.Colour "0", "0.7", "1"',
            '.Wireframe "False"',
            '.Reflection "False"',
            '.Allowoutline "True"',
            '.Transparentoutline "False"',
            '.Transparency "0"',
            '.Create',
            'End With']
sCommand = line_break.join(sCommand)
modeler.add_to_history('define medium', sCommand)
# 自定义材料设置完成


# 设置频率
frq1 = 6
frq2 = 12
sCommand = 'Solver.FrequencyRange "%f", "%f"' % (frq1, frq2)
modeler.add_to_history('set frequency range', sCommand)
# 频率设置完成


# 设置激励
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
            '.Xrange "-6", "6"',
            '.Yrange "-6", "6"',
            '.Zrange "9.8455682777778", "9.8455682777778"',
            '.XrangeAdd "0.0", "0.0"',
            '.YrangeAdd "0.0", "0.0"',
            '.ZrangeAdd "0.0", "0.0"',
            '.SingleEnded "False"',
            '.WaveguideMonitor "False"',
            '.Create',
            'End With']
sCommand = line_break.join(sCommand)
modeler.add_to_history('set excitation', sCommand)
# 激励设置完成


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
modeler.add_to_history('define boundaries', sCommand)
# 设置边界条件结束


# 设置求解器参数
sCommand = ['Mesh.SetCreator "High Frequency"',

            'With Solver',
            '.Method "Hexahedral"',
            '.CalculationType "TD-S"',
            '.StimulationPort "All"',
            '.StimulationMode "All"',
            '.SteadyStateLimit "-40"',
            '.MeshAdaption "False"',
            '.AutoNormImpedance "False"',
            '.NormingImpedance "50"',
            '.CalculateModesOnly "False"',
            '.SParaSymmetry "False"',
            '.StoreTDResultsInCache  "False"',
            '.FullDeembedding "False"',
            '.SuperimposePLWExcitation "False"',
            '.UseSensitivityAnalysis "False"',
            'End With']
sCommand = line_break.join(sCommand)
modeler.add_to_history('define time domain solver parameters', sCommand)
# 求解器参数设置完成


# 设置 PBA 版本
sCommand = 'Discretizer.PBAVersion "2019092520"'
modeler.add_to_history('set PBA version', sCommand)
# PBA版本设置完成


# 数据建模
count = 360  # 文件存储序号
for i in range(len(arr)):
    count += 1

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

    # 将列表转为矩阵建模
    a = np.asarray(arr[i]).reshape(6, -1)
    for x in range(a.shape[0]):
        for y in range(a.shape[1]):
            if a[x][y] == 1:
                # 创建金属单元
                sCommand = ['With Brick',
                            '.Reset',
                            '.Name "1metal_%.0f_%.0f"' % (x + 1, y + 1),
                            '.Component "component1"',
                            '.Material "Copper (annealed)"',
                            '.Xrange "%f","%f"' % (y * 0.8 - (p / 2), y * 0.8 - (p / 2) + t),
                            '.Yrange "%f","%f"' % ((p / 2) - (x * 0.8 + t), (p / 2) - x * 0.8),
                            '.Zrange "h","h+0.018"',
                            '.Create',
                            'End With']
                sCommand = line_break.join(sCommand)
                modeler.add_to_history('define brick', sCommand)

                # 镜像操作 以x平面为轴
                sCommand = ['With Transform',
                            '.Reset',
                            '.Name "component1:1metal_%.0f_%.0f"' % (x + 1, y + 1),
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
                            '.Name "component1:1metal_%.0f_%.0f"' % (x + 1, y + 1),
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
                            '.Name "component1:1metal_%.0f_%.0f"' % (x + 1, y + 1),
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

    # 导出phase数据
    sCommmd = [r'SelectTreeItem("1D Results\S-Parameters\S1,1")',
               'With Plot1D',
               '.PlotView "phase"',
               'End With',
               'With ASCIIExport',
               '.Reset',
               '.FileName "%s"' % rf'C:\Users\Dell\Desktop\phase\{count}-phase.txt',
               '.Execute',
               'End With']
    sCommmd = '\n'.join(sCommmd)
    modeler.add_to_history('save phase', sCommmd)

    # 导出linear数据
    sCommmd = [r'SelectTreeItem("1D Results\S-Parameters\S1,1")',
               'With Plot1D',
               '.PlotView "magnitude"',
               'End With',
               'With ASCIIExport',
               '.Reset',
               '.FileName "%s"' % rf'C:\Users\Dell\Desktop\linear\{count}-linear.txt',
               '.Execute',
               'End With']
    sCommmd = '\n'.join(sCommmd)
    modeler.add_to_history('save linear', sCommmd)

    # 删除component
    sCommand = 'Component.Delete "component1" '
    modeler.add_to_history('delete component', sCommand)
    # 删除完成
