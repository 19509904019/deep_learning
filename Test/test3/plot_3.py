import matplotlib.pyplot as plt
import numpy as np

total_test = []
total_train = []
with open(r'total_test.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        a = line.split()
        b = a[0]
        total_test.append(b)

with open(r'total_train.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        a = line.split()
        b = a[0]
        total_train.append(b)

x = np.arange(1, 20000)
plt.plot(x, total_train, label='train')
plt.plot(x, total_test, linestyle='--', label='test')
plt.ylim(0,10)
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.show()