# 创建数据集对象
from torch.utils.data import Dataset, DataLoader
import csv


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


matrixs = []
phases = []
# 读取数据源
with open(r'D:\deep_learning\my_dataset\train\matrix.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        a = list(map(int,i))
        matrixs.append(a)
    # matrixs = torch.tensor(matrixs, dtype=torch.float)
with open(r'D:\deep_learning\my_dataset\train\phase.csv', 'r') as f:
    reader = csv.reader(f)
    for j in reader:
        b = list(map(float, j))
        phases.append(b)

# 实例化新的数据集
my_dataset = MyDataset(phases, matrixs)

# 传入DataLoader
train_loader = DataLoader(dataset=my_dataset, batch_size=2)

print(my_dataset[19999])
