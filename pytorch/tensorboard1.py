from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter('..\logs')
image_path = r'D:\deep_learning\pytorch\dataset\train\ants_image\0013035.jpg'
img = Image.open(image_path)  # 打开图片
img_array = np.array(img)  # 将图片转为numpy数组

writer.add_image('test', img_tensor=img_array, global_step=1, dataformats='HWC')
# for i in range(100):
#     writer.add_scalar('y=2x', 2*i, i)  # 画图

writer.close()


"""
从PIL到numpy,需要在add_image()中指定shape中的没有给数字/维表示的含义
"""