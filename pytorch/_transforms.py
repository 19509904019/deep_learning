from torchvision import transforms
from PIL import Image

'''
通过transform.ToTensor看两个问题
1.transform如何使用
2.为什么我们需要Tensor数据类型
'''
img_path = r'D:\deep_learning\pytorch\dataset\train\ants_image\0013035.jpg'
img = Image.open(img_path)
