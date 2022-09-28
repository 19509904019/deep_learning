import shutil, os

files = []

path = r'C:\Users\Dell\Desktop\data\matrix'
movepath = r'C:\Users\Dell\Desktop\4'
for i in range(15001, 30001):
    a = '%d-matrix.txt' % i
    files.append(a)

for file in files:
    fullpath = os.path.join(path, file)
    shutil.copy(fullpath, movepath)
