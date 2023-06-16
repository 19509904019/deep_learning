import torch
import pandas as pd
import numpy as np

# 读取CSV数据并进行预处理
data_df = pd.read_csv('c:/users/dell/desktop/3.csv')
X = data_df.iloc[:, :64].values.astype(np.float32)
y = data_df.iloc[:, 64:].values.astype(np.float32)

# 将数据集划分为训练集和测试集
train_size = int(len(X) * 0.6)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# 转换为Pytorch张量对象
X_train, X_test = torch.tensor(X_train), torch.tensor(X_test)
y_train, y_test = torch.tensor(y_train), torch.tensor(y_test)


# 构建一个更高级的深度学习模型，并添加dropout层以减轻过拟合问题
class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = torch.nn.Linear(in_features=64, out_features=128)
        self.bn1 = torch.nn.BatchNorm1d(128)
        self.dropout1 = torch.nn.Dropout(0.2)
        self.fc2 = torch.nn.Linear(in_features=128, out_features=64)
        self.bn2 = torch.nn.BatchNorm1d(64)
        self.dropout2 = torch.nn.Dropout(0.2)
        self.fc3 = torch.nn.Linear(in_features=64, out_features=32)
        self.bn3 = torch.nn.BatchNorm1d(32)
        self.output = torch.nn.Linear(in_features=32, out_features=333)

    def forward(self, x):
        x = torch.nn.functional.relu(self.bn1(self.fc1(x)))
        x = self.dropout1(x)
        x = torch.nn.functional.relu(self.bn2(self.fc2(x)))
        x = self.dropout2(x)
        x = torch.nn.functional.relu(self.bn3(self.fc3(x)))
        x = self.output(x)
        return x


# 定义逆向预测模型类
class ReverseNet(torch.nn.Module):
    def __init__(self):
        super(ReverseNet, self).__init__()
        self.fc3 = torch.nn.Linear(in_features=333, out_features=32)
        self.bn3 = torch.nn.BatchNorm1d(32)
        self.fc2 = torch.nn.Linear(in_features=32, out_features=64)
        self.bn2 = torch.nn.BatchNorm1d(64)
        self.fc1 = torch.nn.Linear(in_features=64, out_features=128)
        self.bn1 = torch.nn.BatchNorm1d(128)
        self.output = torch.nn.Linear(in_features=128, out_features=64)

    def forward(self, x):
        x = self.bn3(self.fc3(x))
        x = torch.nn.functional.leaky_relu(x)
        x = self.bn2(self.fc2(x))
        x = torch.nn.functional.leaky_relu(x)
        x = self.bn1(self.fc1(x))
        x = torch.nn.functional.leaky_relu(x)
        x = self.output(x)
        x = torch.sigmoid(x)
        return x.squeeze().round().int()  # 返回所有通道的结果，并变形为(batch_size, 64)的形状


# 加载训练好的正向预测模型权重和参数
model_weights_path = 'D:/pytorch/fuxian/data/model_weights2.pth'
model = Net()
model.load_state_dict(torch.load(model_weights_path))
model.eval()  # 切换为评估模式

# 初始化逆向预测模型、设置输入数据并进行预测
reverse_model = ReverseNet()
reverse_model.eval()  # 切换为评估模式
input_data = y_test[0].cpu().numpy()
with torch.no_grad():
    output_data = reverse_model(torch.tensor(input_data).unsqueeze(0)).squeeze().cpu().numpy().round().astype(
        int)  # 将 numpy 数组转化为 Tensor 类型，并进行逆向预测
    # 将所有输出的元素连接成字符串，再按行打印出来
    print('Output binary values:\n' + ''.join(map(str, output_data.tolist())))

# 输出逆向预测模型的预测结果
print('Input phase values:', input_data.tolist())
print('Output binary values:', output_data.tolist())
