from network_convnet import *
import csv
import torch


# 计算相对光谱误差
def RSE(r, g):
    a = torch.sqrt(torch.sum((r - g) ** 2)) / torch.sqrt(torch.sum(r ** 2))
    return a


# 测试数据
test_s11 = []
with open(r"C:\Users\user2\Desktop\dataset\dataset1\test_set\s11.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
    for row in reader:  # each row is a list
        test_s11.append(row)
    test_s11 = torch.tensor(test_s11, dtype=torch.float)

# 几何参数
test_parameters = []
with open(r"C:\Users\user2\Desktop\dataset\dataset1\test_set\parameters.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
    for row in reader:  # each row is a list
        test_parameters.append(row)
    test_parameters = torch.tensor(test_parameters, dtype=torch.float)

# 加载已经训练好的模型
mymodel = torch.load('mymodel2.pth')

# 进行测试
device = torch.device('cuda:0')  # GPU加速
outputs = torch.tensor([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=torch.float)
outputs = torch.reshape(outputs, (1, -1)).to(device)  # 存放预测结果的总和
parameters = torch.tensor([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=torch.float)
parameters = torch.reshape(parameters, (1, -1)).to(device)  # 存放真实结果的总和

# 计数
test_total = 0
# 开始测试
mymodel.eval()
with torch.no_grad():  # 无需梯度
    for number in range(len(test_s11)):
        test_total += 1
        data = torch.reshape(test_s11[number], (1, 1, -1)).to(device)  # 600个测试数据
        output = mymodel(data).to(device)  # 电磁响应所对应预测的结构参数
        outputs += output
        # 测试数据的真实结构参数
        parameter = torch.reshape(test_parameters[number], (1, -1)).to(device)
        parameters += parameter
        # 真实结果与预测结果相对光谱误差
        result_1 = RSE(parameter, output)
        if test_total % 100 ==0:
            print(f"第{test_total}个:预测结果为：{output},真实结果为：{parameter},相对光谱误差为：{result_1}")

    # 整体的相对光谱误差
    result_2 = RSE(parameters, outputs)
    print(f'整体的相对光谱误差为:{result_2}')
