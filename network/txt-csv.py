import pandas as pd
import os

# 文件路径
path = r'C:\Users\12414\Desktop\data\data2'

df1 = []
for i in os.listdir(path):
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
new_path = r'C:\Users\12414\Desktop\new_csv\new_csv.csv'
df.to_csv(new_path, index=False, encoding='UTF-8')
