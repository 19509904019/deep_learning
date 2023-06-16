import shutil, os

files = []

path = r'C:\Users\Dell\Desktop\data1\new_data_2\matrix'
movepath = r'C:\Users\Dell\Desktop\81'
for i in range(40001, 50001):
    a = '%d.txt' % i
    files.append(a)

for file in files:
    fullpath = os.path.join(path, file)
    shutil.copy(fullpath, movepath)
