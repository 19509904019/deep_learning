from torch.utils.data import Dataset
from PIL import Image
import os


class Mydata(Dataset):
    def __init__(self, root_dir, label_dir):
        """
        获得数据集路径
        :param root_dir: 根目录
        :param label_dir: 标签目录（图片）
        """
        self.root_dir = root_dir
        self.label_dir = label_dir  # 文件夹名为标签
        self.path = os.path.join(self.root_dir, self.label_dir)  # 存放图片路径
        self.all_img = os.listdir(self.path)  # 全部图片

    def __getitem__(self, idx):
        """
        获取每张图片的路径
        :param idx: 图片索引
        :return: None
        """
        img_name = self.all_img[idx]
        img_item_path = os.path.join(self.path, img_name)
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.all_img)
