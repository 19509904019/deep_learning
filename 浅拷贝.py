"""
利用浅拷贝复制原列表，原列表清空后不会造成拷贝的列表清空
"""
import os
import copy

path = r'C:\Users\12414\Desktop\matrix\2'

filename = os.listdir(path)

container1 = []
container2 = []
container3 = []
for file in filename:
    fullpath = os.path.join(path, file)
    with open(fullpath, 'r') as f:
        lines = f.readlines()
    for line in lines:
        a = line.split()
        b = a[0]
        container1.append(b)
    container2 = copy.copy(container1)
    container3.append(container2)
    container1.clear()
print(container3[0])
