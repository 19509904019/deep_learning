from PIL import Image
import os

path = r'图片存储的路径'
newpath = r'转换后存储图片的路径'


def RGBtoGray(path):
    files = os.listdir(path)
    for file in files:
        imgpath = path + '/' + file
        # print(imgpath)
        #
        im = Image.open(imgpath).convert('L')
        # resize将图像像素转换成自己需要的像素大小
        img = im.resize((512, 512))
        dirpath = newpath
        file_name, file_extend = os.path.splitext(f)
        dst = os.path.join(os.path.abspath(dirpath), file_name + '.jpg')
        img.save(dst)


if __name__ == "__main__":
    RGBtoGray(path)
