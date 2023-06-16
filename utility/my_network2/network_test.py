import csv
from torch.utils.data import DataLoader, Dataset
from create_network import *
import math


# 平均绝对误差
def calculate_the_MAE(predicted_data, actual_data):
    '''
    该函数用于计算平均绝对误差
    Parameters
    ----------
    predicted_data : 一维列表
        预测数据.
    actual_data : 一维列表
        真实数据.
    Returns
    -------
    MAE : 浮点型
        平均绝对误差.
    '''
    # 定义一个变量用于存储所有样本的绝对误差之和
    the_sum_of_error = 0
    # 开始逐渐遍历每一个样本
    for i in range(len(actual_data)):
        # 不断累加求和，计算所有样本的绝对误差之和
        the_sum_of_error += abs(predicted_data[i] - actual_data[i])
    # 计算所有样本的平均绝对误差
    MAE = the_sum_of_error / float(len(actual_data))
    return MAE


# 加载测试数据集
class MyDataset(Dataset):  # 需要继承Dataset类
    def __init__(self, phase, matrix):
        """
        将传入的序列指定为类的属性
        :param phase:
        :param matrix:
        """
        self.phase = phase
        self.matrix = matrix

    def __len__(self):
        """
        设定数据集的长度
        :return:
        """
        return len(self.matrix)

    def __getitem__(self, idx):
        """
        使用参数idx,指定索引访问元素的方法，并指定返回元素
        :param idx:
        :return:
        """
        label = self.matrix[idx]
        data = self.phase[idx]
        return data, label


# 存储矩阵
matrixs = []
# 存储相位
phases = []
# 读取数据源
with open(r'D:\deep_learning\my_dataset\dataset1\test\matrix.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        a = [j - 0.1 for j in list(map(int, i))]
        matrixs.append(a)
    matrixs = torch.tensor(matrixs, dtype=torch.float)
with open(r'D:\deep_learning\my_dataset\dataset1\test\phase.csv', 'r') as f:
    reader = csv.reader(f)
    for j in reader:
        b = list(map(float, j))
        phases.append(b)
    phases = torch.tensor(phases, dtype=torch.float)

# 实例化测试集
test_set = MyDataset(phases, matrixs)

# 加载测试集
test_dataloader = DataLoader(dataset=test_set)

# 生成网络
mymodel = MyModel()

# loss
loss_F = nn.MSELoss()

# 测试步骤开始
count = 0
total_test_loss = 0  # 整个测试集的loss
mymodel.eval()
with torch.no_grad():
    for data in test_dataloader:
        count += 1
        phases, matrixs = data
        outputs = mymodel(matrixs)
        loss = loss_F(outputs, phases)
        total_test_loss += loss.item()  # 将所有的loss值相加
        if count % 100 == 0:
            print(f'第{count // 100}次：预测数据为：{outputs},\n真实数据为：{phases},'
                  f'Loss值为：{loss.item()},均方根误差为：{math.sqrt(loss.item())}'
                  )
    print(f"整体测试集的Loss:{total_test_loss}")
