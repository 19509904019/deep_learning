import os
# 换行符，用于VB代码拼接用
line_break = '\n'


# 初始化
def set_units():
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
    return sCommand


# 设置工作频率
def set_frequency(frq1, frq2):
    sCommand = 'Solver.FrequencyRange "%f", "%f"' % (frq1, frq2)
    return sCommand


# 使用Bounding Box显示
def use_BoundingBox():
    sCommand = 'Plot.DrawBox "True"'
    return sCommand


# 设置背景材料
def set_background():
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
    return sCommand


# 设置端口参数
def set_floquetport():
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
    return sCommand


# 设置边界条件
def set_boundary():
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
    return sCmmand


# 设置频域求解器
def set_frequencydomain():
    sCommand = 'ChangeSolverType("HF Frequency Domain")'
    return sCommand


# 设置时域求解器
def set_timedomain():
    sCommand = 'ChangeSolverType("HF Time Domain")'
    return sCommand


# 设置激励
def solver_excitation():
    sCommand = ['With FDSolver',
                '.Reset',
                '.Stimulation "List", "List"',
                '.ResetExcitationList',
                '.AddToExcitationList "Zmax", "TE(0,0);TM(0,0)"',
                '.LowFrequencyStabilization "False"',
                'End With']
    sCommand = line_break.join(sCommand)
    return sCommand


# 设置网格划分
def mesh_type():
    # 四面体网格
    sCommand = ['With Mesh',
                '.MeshType "Tetrahedral"',
                'End With']
    sCommand = line_break.join(sCommand)
    return sCommand


# 创建新材料
def create_material(name, epsilon):
    sCommand = ['With Material',
                '.Reset ',
                '.Name "%s"' % name,
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
                '.MaterialUnit "Time", "ns"',
                '.MaterialUnit "Temperature", "Kelvin"',
                '.Epsilon "%f"' % epsilon,
                '.Mu "1"',
                '.Sigma "0"',
                '.TanD "0.0"',
                '.TanDFreq "0.0"',
                '.TanDGiven "False"',
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
                '.DispModelEps  "None"',
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
                '.Colour "0", "1", "1" ',
                '.Wireframe "False" ',
                '.Reflection "False" ',
                '.Allowoutline "True"',
                '.Transparentoutline "False"',
                '.Transparency "0"',
                '.Create',
                'End With']
    sCommand = line_break.join(sCommand)
    return sCommand


# 创建brick对象
def create_brick(str_name, str_component, str_material, x1, x2, y1, y2, z1, z2):
    sCommand = ['With Brick',
                '.Reset',
                '.Name "%s"' % str_name,
                '.Component "%s"' % str_component,
                '.Material "%s"' % str_material,
                f'.Xrange "{x1}", "{x2}"',
                f'.Yrange "{y1}", "{y2}"',
                f'.Zrange "{z1}", "{z2}"',
                '.Create',
                'End With']
    sCommand = line_break.join(sCommand)
    return sCommand


def create_Lossymetal(name, ohm):
    sCommand = ['With Material',
                '.Reset',
                '.Name "%s"' % name,
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
                '.Type "Lossy metal"',
                '.MaterialUnit "Frequency", "GHz"',
                '.MaterialUnit "Geometry", "mm"',
                '.MaterialUnit "Time", "ns"',
                '.MaterialUnit "Temperature", "Kelvin"',
                '.OhmicSheetImpedance "%f", "0"' % ohm,
                '.OhmicSheetFreq "0"',
                '.ReferenceCoordSystem "Global"',
                '.CoordSystemType "Cartesian"',
                '.NLAnisotropy "False"',
                '.NLAStackingFactor "1"',
                '.NLADirectionX "1"',
                '.NLADirectionY "0"',
                '.NLADirectionZ "0"',
                '.Colour "1", "1", "0"',
                '.Wireframe "False"',
                '.Reflection "False"',
                '.Allowoutline "True"',
                '.Transparentoutline "False"',
                '.Transparency "0"',
                '.Create',
                'End With']
    sCommand = line_break.join(sCommand)
    return sCommand


