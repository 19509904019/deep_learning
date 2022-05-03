import torch
from PIL import Image
from torchvision.transforms import *
from cifar10_network import *

img_path = r'../../picture/original_picture/air.png'
img = Image.open(img_path)
img = img.convert('RGB')  # png格式是四个通道,所以对图片应该转换成三通道,如果本来就是三通道则经过此操作不变
# print(img.size)  # (165, 161) 需要转换成输入大小：Resize

transformer = Compose([
    Resize((32, 32)),  # 训练的网络是32*32，所以测试图片需要转换成32*32
    ToTensor()
])
img = transformer(img)  # 读数据进行预处理
# print(img.shape)  # torch.Size([3, 32, 32])

mymodel = torch.load('mymodel.pth')
# print(mymodel)

img = torch.reshape(img, (1, 3, 32, 32))

# 进行测试
mymodel.eval()
with torch.no_grad():  # 无需梯度，节约内存提高性能
    output = mymodel(img)
print(output.argmax(1))
print(output)


