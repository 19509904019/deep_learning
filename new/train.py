import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


# 计算均方根误差
def rmse(predictions, targets):
    return torch.sqrt(torch.mean((predictions - targets) ** 2))


# 初始化模型、优化器和损失函数
model = Net()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
criterion = torch.nn.MSELoss()


# 定义卷积神经网络训练函数
def train(model, optimizer, criterion, X_train, y_train, num_epochs, batch_size=64):
    train_loss = []
    for epoch in range(num_epochs):
        # 随机划分数据集并前向传播
        index = torch.randperm(X_train.size()[0])
        for i in range(0, len(index), batch_size):
            indices = index[i:i + batch_size]
            outputs = model(X_train[indices])

            # 计算损失函数
            loss = criterion(outputs.squeeze(), y_train[indices])

            # 反向传播与优化
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # 打印当前损失值，并将其记录下来
        if (epoch + 1) % 10 == 0:
            print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch + 1, num_epochs, loss.item()))
        train_loss.append(loss.item())

    return model, train_loss


# 开始训练模型，并观察损失函数的变化过程
num_epochs = 250
batch_size = 20
model, train_loss = train(model, optimizer, criterion, X_train, y_train, num_epochs, batch_size)
plt.plot(train_loss)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss Curve')
plt.show()

# 评估模型效果
with torch.no_grad():
    y_pred = model(X_test)
    test_loss = rmse(y_pred, y_test)
print('RMSE on test set: {:.4f}'.format(test_loss))

# 将模型权重和参数保存至指定路径
torch.save(model.state_dict(), 'D:/pytorch/fuxian/data/model_weights2.pth')

# 可视化真实值与预测值的折线图
# 展示预测和实际结果对比
sample_indices = np.random.choice(y_test.shape[0], 5, replace=False)
freq_data = pd.read_csv('C:/Users/dell/Desktop/fre1.csv', header=None).values.flatten()

for i, index in enumerate(sample_indices):
    plt.figure()
    plt.plot(freq_data[:333], y_test[index][:333], color='red', label='Expected ')
    plt.plot(freq_data[:333], y_pred[index][:333], color='blue', label='Predicted')
    plt.legend()
    plt.ylabel('phase')
    plt.xlabel('frequency')
    plt.show()
