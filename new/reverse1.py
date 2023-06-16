import torch
import pandas as pd
import numpy as np

# 读取CSV数据并进行预处理
data_df = pd.read_csv('c:/users/dell/desktop/77phase.csv')
X = data_df.iloc[:, :64].values.astype(np.float32)
y = data_df.iloc[:, 64:].values.astype(np.float32)

# 将数据集划分为训练集和测试集
train_size = int(len(X) * 0.6)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# 转换为Pytorch张量对象
X_train, X_test = torch.tensor(X_train), torch.tensor(X_test)
y_train, y_test = torch.tensor(y_train), torch.tensor(y_test)

# 正向网络模型
class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # 定义卷积层
        self.conv1 = torch.nn.Conv1d(in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=1)
        # 定义池化层
        self.pool = torch.nn.MaxPool1d(kernel_size=2, stride=2)
        # 定义全连接层
        self.fc = torch.nn.Linear(16 * 32, 77)
        # 定义激活函数ReLU
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        # 输入reshape
        x = x.view(-1, 1, 64)
        # 卷积操作
        x = self.conv1(x)
        x = self.relu(x)
        # 池化操作
        x = self.pool(x)
        # 拉平
        x = x.view(-1, 16 * 32)
        # 全连接层，输出维度为77
        x = self.fc(x)

        return x

# 定义逆向预测模型类
class ReverseNet(torch.nn.Module):
    def __init__(self):
        super(ReverseNet, self).__init__()
        # 定义全连接层
        self.fc = torch.nn.Linear(77, 16 * 32)
        # 定义反卷积层
        self.deconv1 = torch.nn.ConvTranspose1d(in_channels=16, out_channels=2, kernel_size=3, stride=1, padding=1)
        # 定义激活函数ReLU
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        # 全连接层
        x = self.fc(x)
        x = self.relu(x)
        x = x.view(-1, 16, 32)
        # 反卷积操作
        x = self.deconv1(x)
        # 经过sigmoid激活函数获得0-1范围内的值
        x = torch.sigmoid(x)

        return x.squeeze().round().int()  # 返回所有通道的结果，并变形为(batch_size, 64)的形状

# 加载训练好的正向预测模型权重和参数
model_weights_path = 'D:/pytorch/fuxian/data/model_weights1.pth'
model = Net()
model.load_state_dict(torch.load(model_weights_path))
model.eval()  # 切换为评估模式

# 初始化逆向预测模型、设置输入数据并进行预测
reverse_model = ReverseNet()
reverse_model.eval()  # 切换为评估模式
input_data = y_test[0].cpu().numpy()
with torch.no_grad():
    output_data = reverse_model(torch.tensor(input_data).unsqueeze(0)).squeeze().cpu().numpy().round().astype(int)  # 将 numpy 数组转化为 Tensor 类型，并进行逆向预测
    # 将所有输出的元素连接成字符串，再按行打印出来
    print('Output binary values:\n' + ''.join(map(str, output_data.tolist())))

# 输出逆向预测模型的预测结果
print('Input phase values:', input_data.tolist())
print('Output binary values:', output_data.tolist())