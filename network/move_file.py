import shutil, os

files = []

path = r'C:\Users\Dell\Desktop\data'
movepath = r'C:\Users\Dell\Desktop\8'
for i in range(70001, 80001):
    a = '%d.txt' % i
    files.append(a)

for file in files:
    fullpath = os.path.join(path, file)
    shutil.copy(fullpath, movepath)
