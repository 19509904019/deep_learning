import pandas as pd
import os

# 文件路径
path = r'C:\Users\Dell\Desktop\3'
# 打开文件夹
filename = os.listdir(path)
# 按顺序排列
filename.sort(key=lambda x: int(x[:-11]))

df1 = []
for i in filename:
    # 重构文件路径
    filepath = os.path.join(path, i)
    # 将txt转换成DataFrame
    a = pd.read_csv(filepath)

    # 保存到新列表中
    df1.append(a)

# 多个DataFrame合并为一个
df = pd.concat(df1, axis=1)
# print(df)
# 保存为csv文件
new_path = r'C:\Users\Dell\Desktop\3.csv'
df.to_csv(new_path, index=False, encoding='UTF-8')
