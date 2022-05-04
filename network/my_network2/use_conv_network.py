from pytorch_deep_convnet import *
import csv
import torch

# 测试数据
test = []
with open(r"C:\Users\Dell\Desktop\test.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
    for row in reader:  # each row is a list
        test.append(row)
test = torch.tensor(test, dtype=torch.float32)
test = torch.reshape(test, (1, 1, -1))  # C=1 输入1000个数据

# 加载已经训练好的模型
mymodel = torch.load('mymodel.pth')

# 进行测试
mymodel.eval()
with torch.no_grad():  # 无需梯度
    output = mymodel(test)

print(output)
