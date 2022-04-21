from PIL import Image

# 缩放比例
SCALE = 0.3


def get_char(pixel, blank_char='1', fill_char='0'):
    if pixel == 0:
        return blank_char
    else:
        return fill_char


# 输入图片路径
im = Image.open(r"D:\deep_learning\picture\save_picture\1.jpg")
size = im.size
# 获取图片的像素
# size[0]*size[1] 横宽像素
width, height = int(size[0] * SCALE), int(size[1] * SCALE)
im = im.resize((width, height))  # 修改图片尺寸
im = im.convert('1')  # 获得二值图像

txt = ""
for i in range(height):
    for j in range(width):
        txt += get_char(im.getpixel((j, i)))  # getpixel是获取图像中某一点像素的RGB颜色值
    txt += '\n'

# 保存为文件
with open(r'result.txt', 'w') as f:
    print(txt, file=f)
