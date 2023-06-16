import pandas as pd
import os
from sklearn.utils import shuffle

data = pd.read_csv(r'C:\Users\Dell\Desktop\4.csv', sep=',')
data = shuffle(data)  # 打乱
data.to_csv(r'C:\Users\Dell\Desktop\44.csv', index=False, header=False)  # index索引不出现，header表头出现
