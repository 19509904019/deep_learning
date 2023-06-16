import pandas as pd
import numpy as np

# 读取csv文件
data = pd.read_csv(r'C:\Users\Dell\Desktop\csv\matrix.csv', header=None)

# 将数据转换为NumPy数组
data_arr = np.array(data)

# 将数据重新组织为(40000, 6, 6)的形状
data_reshaped = data_arr.reshape((len(data_arr), 6, 6))

# 创建一个空的二维数组用于存储所有下三角矩阵
result_arr = np.empty((len(data_arr), 21), dtype=int)

# 循环遍历每个矩阵，将其转换为下三角矩阵，并将结果存储到result_arr中
for i in range(len(data_reshaped)):
    m_tril = np.tril(data_reshaped[i])
    m_symm = m_tril + m_tril.T - np.diag(m_tril.diagonal())
    result_arr[i] = m_symm[np.tril_indices(6)]

# 将处理后的数据保存为新的csv文件
result_df = pd.DataFrame(result_arr)
result_df.to_csv(r'C:\Users\Dell\Desktop\result.csv', index=False, header=None)

