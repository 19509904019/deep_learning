import shutil, os

files = []

path = r'C:\Users\Dell\Desktop\shuffle_data\data2'
movepath = r'C:\Users\Dell\Desktop\2'
for i in range(20001, 29519):
    a = '%d-data.txt' % i
    files.append(a)

for file in files:
    fullpath = os.path.join(path, file)
    shutil.copy(fullpath, movepath)
