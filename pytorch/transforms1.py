from torchvision import transforms
from PIL import Image
import cv2 as cv
from torch.utils.tensorboard import SummaryWriter

'''
通过transform.ToTensor看两个问题
1.transform如何使用
2.为什么我们需要Tensor数据类型
'''
img_path = r'D:\deep_learning\pytorch\dataset\train\ants_image\0013035.jpg'
img = Image.open(img_path)  # 读取图片

# 1.transform的使用
# tensor_trans = transforms.ToTensor()
# tensor_img = tensor_trans(img)  # tensor数组
tensor_img = transforms.ToTensor()(img)

print(type(tensor_img))
print(tensor_img.shape)
# print(tensor_img)

print('--' * 50)

write = SummaryWriter('../logs')

cv_img = cv.imread(img_path)
print(type(cv_img))  # 直接转化为numpy数组
print(cv_img.shape)
# print(cv_img)
write.add_image('cv_img', img_tensor=cv_img, global_step=1, dataformats='HWC')
write.close()
