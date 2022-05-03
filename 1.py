# path1 = r'C:\Users\Dell\Desktop\s11_linear.txt'
# path2 = r'C:\Users\Dell\Desktop\s11_linear1.txt'
#
# with open(path1,'rb') as r1:
#     for eachline in

path = r'C:\Users\Dell\Desktop\1.txt'  # 数据路径
with open(path,'r') as f:
    container = f.readline()
    container = container.split(' ')
    print(container)