# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:06:54 2020

@author: tWX5331009
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from os.path import dirname, abspath
import cst.results
import cst
import cst.interface


CstFileName = input("请输入cst文件名(勿带cst后缀)：")
ProjectName = CstFileName + '.cst'
# getcwd()方法获取当前工作目录+文件名=文件目录
# Initialize secondary variables
ProjectPath = os.path.join(os.getcwd(), ProjectName)

# 判断项目是否打开状态

# 首先，用一个开放的DE生成所有PIDs的列表 (cst.interface).
AllPIDs = cst.interface.running_design_environments()
IsOpen = False

# Go through list of PIDs and query projects
for CurrentPID in AllPIDs:
    MyCurrentDE = cst.interface.DesignEnvironment.connect(CurrentPID)
    for ProjectPath in MyCurrentDE.list_open_projects():
        if ProjectPath == ProjectPath:
            MyPID = CurrentPID
            MyCurrentProject = MyCurrentDE.get_open_project(ProjectPath)
            IsOpen = True
            break

# In version 2021 I could e.g. now query if a solver is running or not...

if IsOpen:
    print('Project is already open...')
else:
    print('Project is not open at the moment...')

# If the project is not open already, open it now (cst.interface).

# if not IsOpen:
#    MyCurrentDE      = cst.interface.DesignEnvironment()
#    MyCurrentProject = MyCurrentDE.open_project(ProjectPath)


# Now the project is open and can be worked on...

# PLEASE NOTE: For workflows involving accessing 1D Results it is generally recommended to work with a closed project - although it is also possible to work in interactive mode.
# However, the assumption is that we want to trigger the solver, so we need an open project.

# PLEASE NOTE: With the python interface it is possible at the moment to execute vba commands, but we cannot get information back from the project through this method (at least currently)
# If we wanted to e.g. check on the existance of a 1D Result this could easily be done using the cst.results module.
# But to directly query the existance of e.g. a farfield result we (currently still) need to use the COM interface (which could in principle be done in conjunction with the python interface).
# But, at the moment we are assuming that the farfield has not been calculated yet.
# 运行当前选定的解算器，直到它完成，并返回解算器运行是否成功。
# Run the solver:
# MyCurrentProject.modeler.run_solver()


a = input("请输入需要导出到的频率(以空格间隔)：")
b = int(input("请输入需要连续导出的端口数,如果指定端口导出，请输入-1："))
b_list = []
if b == -1:
    b_assigned = input("请输入需要指定端口(以空格间隔)：")
    b_list = str(b_assigned).split(' ')

else:
    b_list_bef = []
    for z in range(b):
        b_list_bef.append(z)
    b_array = np.array(b_list_bef) + 1
    b_list = b_array.tolist()
Frequency_list = str(a).split(' ')
print(Frequency_list)
# 频段和端口双层循环.
for i in range(len(Frequency_list)):
    for j in range(len(b_list)):
        Frequency = Frequency_list[i]
        Port = str(b_list[j])
        FarfieldPath = 'Farfields\\farfield (f=' + Frequency + ') [' + Port + ']\\Abs'
        print(FarfieldPath)
        ExportedFileName = 'f=' + Frequency + Port + 'Export.txt'

        # 设置导出的文件的路径（cst file的父目录+ExportedFileName）
        # Set path for file which is to be exported (parent directory of cst file + ExportedFileName)
        MyFilePath = os.path.abspath(os.path.join(ProjectPath[0:-4], os.pardir))
        MyFilePath = os.path.join(MyFilePath, ExportedFileName)

        # 调用vba命令字符串来导出方向图数据
        # Set up string which contains the VBA commands (to trigger the ASCII export)
        MyVBACommand = '\'#Language "WWB-COM"\n\n'
        MyVBACommand += 'Option Explicit\n\n'
        MyVBACommand += 'Sub Main\n'
        MyVBACommand += '\tSelectTreeItem("' + FarfieldPath + '")\n'
        MyVBACommand += '\tWith FarfieldPlot\n'
        MyVBACommand += '\t\t.Plottype "3D"\n'
        MyVBACommand += '\t\t.Vary "angle1"\n'
        MyVBACommand += '\t\t.Theta "90"\n'
        MyVBACommand += '\t\t.Phi "90"\n'
        MyVBACommand += '\t\t.Step "1"\n'
        MyVBACommand += '\t\t.Step2 "1"\n'
        MyVBACommand += '\t\t.SetLockSteps "True"\n'
        MyVBACommand += '\t\t.SetPlotRangeOnly "False"\n'
        MyVBACommand += '\t\t.SetThetaStart "0"\n'
        MyVBACommand += '\t\t.SetThetaEnd "180"\n'
        MyVBACommand += '\t\t.SetPhiStart "0"\n'
        MyVBACommand += '\t\t.SetPhiEnd "360"\n'
        MyVBACommand += '\t\t.SetTheta360 "False"\n'
        MyVBACommand += '\t\t.SymmetricRange "False"\n'
        MyVBACommand += '\t\t.SetTimeDomainFF "False"\n'
        MyVBACommand += '\t\t.SetFrequency "0.825"\n'
        MyVBACommand += '\t\t.SetTime "0"\n'
        MyVBACommand += '\t\t.SetColorByValue "True"\n'
        MyVBACommand += '\t\t.DrawStepLines "False"\n'
        MyVBACommand += '\t\t.DrawIsoLongitudeLatitudeLines "False"\n'
        MyVBACommand += '\t\t.ShowStructure "False"\n'
        MyVBACommand += '\t\t.ShowStructureProfile "False"\n'
        MyVBACommand += '\t\t.SetStructureTransparent "False"\n'
        MyVBACommand += '\t\t.SetFarfieldTransparent "False"\n'
        MyVBACommand += '\t\t.AspectRatio "Free"\n'
        MyVBACommand += '\t\t.ShowGridlines "True"\n'
        MyVBACommand += '\t\t.SetSpecials "enablepolarextralines"\n'
        MyVBACommand += '\t\t.SetPlotMode "Realized Gain"\n'
        MyVBACommand += '\t\t.Distance "1"\n'
        MyVBACommand += '\t\t.UseFarfieldApproximation "True"\n'
        MyVBACommand += '\t\t.SetScaleLinear "False"\n'
        MyVBACommand += '\t\t.SetLogRange "40"\n'
        MyVBACommand += '\t\t.SetLogNorm "0"\n'
        MyVBACommand += '\t\t.DBUnit "0"\n'
        MyVBACommand += '\t\t.SetMaxReferenceMode "abs"\n'
        MyVBACommand += '\t\t.EnableFixPlotMaximum "False"\n'
        MyVBACommand += '\t\t.SetFixPlotMaximumValue "1"\n'
        MyVBACommand += '\t\t.SetInverseAxialRatio "False"\n'
        MyVBACommand += '\t\t.SetAxesType "currentwcs"\n'
        MyVBACommand += '\t\t.SetAntennaType "unknown"\n'
        MyVBACommand += '\t\t.Phistart "1.000000e+00", "0.000000e+00", "0.000000e+00"\n'
        MyVBACommand += '\t\t.Thetastart "0.000000e+00", "0.000000e+00", "1.000000e+00"\n'
        MyVBACommand += '\t\t.PolarizationVector "0.000000e+00", "1.000000e+00", "0.000000e+00"\n'
        MyVBACommand += '\t\t.SetCoordinateSystemType "spherical"\n'
        MyVBACommand += '\t\t.SetAutomaticCoordinateSystem "True"\n'
        MyVBACommand += '\t\t.SetPolarizationType "Linear"\n'
        MyVBACommand += '\t\t.SlantAngle 4.500000e+01\n'
        MyVBACommand += '\t\t.Origin "bbox"\n'
        MyVBACommand += '\t\t.Userorigin "0.000000e+00", "0.000000e+00", "0.000000e+00"\n'
        MyVBACommand += '\t\t.SetUserDecouplingPlane "False"\n'
        MyVBACommand += '\t\t.UseDecouplingPlane "False"\n'
        MyVBACommand += '\t\t.DecouplingPlaneAxis "X"\n'
        MyVBACommand += '\t\t.DecouplingPlanePosition "0.000000e+00"\n'
        MyVBACommand += '\t\t.LossyGround "False"\n'
        MyVBACommand += '\t\t.GroundEpsilon "1"\n'
        MyVBACommand += '\t\t.GroundKappa "0"\n'
        MyVBACommand += '\t\t.EnablePhaseCenterCalculation "False"\n'
        MyVBACommand += '\t\t.SetPhaseCenterAngularLimit "3.000000e+01"\n'
        MyVBACommand += '\t\t.SetPhaseCenterComponent "boresight"\n'
        MyVBACommand += '\t\t.SetPhaseCenterPlane "both"\n'
        MyVBACommand += '\t\t.ShowPhaseCenter "True"\n'
        MyVBACommand += '\t\t.ClearCuts\n'
        MyVBACommand += '\t\t.AddCut "lateral", "0", "1"\n'
        MyVBACommand += '\t\t.AddCut "lateral", "90", "1"\n'
        MyVBACommand += '\t\t.AddCut "polar", "90", "1"\n\n'
        MyVBACommand += '\t\t.StoreSettings\n'
        MyVBACommand += '\tEnd With\n'
        MyVBACommand += '\tWith ASCIIExport\n'
        MyVBACommand += '\t\t.Reset\n'
        MyVBACommand += '\t\t.FileName ("' + MyFilePath + '")\n'
        MyVBACommand += '\t\t.Execute\n'
        MyVBACommand += '\tEnd With\n'
        MyVBACommand += 'End Sub\n'

        # 导出结果
        # Trigger ASCIIExport of results
        MyCurrentProject.schematic.execute_vba_code(MyVBACommand)


        def original_data(filename):
            data = np.loadtxt(filename, skiprows=2)
            return data


        # 打开文件的目录
        ori_data = 'f=' + Frequency + Port + 'Export.txt'
        data_1 = original_data(ori_data)
        data1 = data_1[:, [0, 1, 3, 4, 5, 6]]
        data_gain = data_1[:, 2]
        # 按phi进行排序，并进行第0列和第1列的互换
        data2 = np.zeros((65160, 6), dtype=np.float64)
        for m in range(181):
            for n in range(360):
                data2[360 * m + n] = data1[181 * n + m]
        data2_real = np.zeros((65160, 6), dtype=np.float64)
        data2_real = data2[:, [1, 0, 2, 3, 4, 5]]


        # 按列分块函数
        def data_split(i, j):

            data3 = data2_real[:, i:j]
            return data3  # 不返还值，为None类型，无法操作


        # 进行切片操作
        part_1 = data_split(0, 2)
        # l3需要进行操作
        part_2 = data_split(2, 3)
        part_3 = data_split(3, 4)

        # l5需要进行操作
        part_4 = data_split(4, 5)
        part_5 = data_split(5, 6)

        # 求A的值
        A = np.max(np.sqrt(pow(10, data2_real[:, 2] / 10) + pow(10, data2_real[:, 4] / 10)))
        print(A)
        # 利用广播进行运算 Theta，Phase
        part_2_1 = 20 * np.log10(pow(10, part_2 / 20) / A)
        part_4_1 = 20 * np.log10(pow(10, part_4 / 20) / A)
        seq_1 = np.hstack((part_1, part_2_1))
        seq_2 = np.hstack((seq_1, part_3))
        seq_3 = np.hstack((seq_2, part_4_1))
        data_final = np.hstack((seq_3, part_5))

        # 取出第三行，计算GAIN
        gain = data_gain


        # 把数组转化为列表并计算其最大值
        # 数组转化为列表函数
        def ndarray_list(s):
            s_list = s.tolist()
            return s_list


        gain_list = ndarray_list(gain)
        Gain = float(max(gain_list))
        first_line = "GAIN %.2f dBi\n" % Gain
        second_line = "PATTERN  Phi[deg.]  Theta[deg.]  Abs(Theta)[dBi]  Phase(Theta)[deg.]  Abs(Phi)[dBi]  Phase(Phi)[deg.] "
        header1 = (first_line + second_line).rstrip()

        # 写入文件的目录
        freq = int(float(Frequency) * 1000)
        if Port.isdigit() == 1:
            if int(Port) % 2 == 1:
                new_file = "HW_AirView_Fre%dM_P45_ET00_Port%s.txt" % (freq, Port)
            elif int(Port) % 2 == 0:
                new_file = "HW_AirView_Fre%dM_M45_ET00_Port%s.txt" % (freq, Port)
        else:

            new_file = "HW_AirView_Fre%dM_X45_ET00_Port%s.txt" % (freq, Port)

        # 获取父目录并保存到变量
        parent_dir = os.getcwd()


        # 判断是否存在路径，不存在则创建
        def create_dir_not_exist(path):
            if not os.path.exists(path):
                os.mkdir(path)


        create_dir_not_exist(CstFileName + "_3DPatternData")
        os.chdir(CstFileName + "_3DPatternData")
        np.savetxt(new_file, data_final, fmt='%.2f', delimiter=' ', newline='\n', header=header1, comments='')
        # 切换到父目录，删除父目录里的原数据。
        os.chdir(parent_dir)
        os.remove(ori_data)
    # 保存cst文件
print('导出完成')
MyCurrentProject.save()