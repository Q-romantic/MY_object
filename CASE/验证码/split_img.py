# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/4  004 下午 14:31
@Author  : Jan
@File    : split_img.py
"""

""" { 图片无损放大 & 切割图片并随机排列再还原} """

import cv2
import requests
import numpy as np
from PIL import Image
from 验证码.证码缺口位置坐标 import SlideCrack


# 图片无损放大
def retinapad_picture(src: [str, bytes], multiple=2):
    def judg(src: [str, bytes]):
        img = None
        # 1、本地文件路径
        if isinstance(src, str):
            img = cv2.imread(src)
        # 2、二进制 ---> numpy数组
        if isinstance(src, bytes):
            img = SlideCrack.bytes_to_np(src)
        return img

    img = judg(src)
    height, width = img.shape[:2]
    image = SlideCrack.np_to_pil(img)

    li = []
    for y in range(height):  # 循环读取图片的每一个像素点的RGBA值 获取图片的Y轴有多少像素 也相当于长度
        tmp = []
        for x in range(width):  # 获取图片的X轴有多少像素 也相当于宽度
            # image.getpixel((a, aa))  用来获取图片某位置的RGBA像素值
            tmp = tmp + [image.getpixel((x, y))] * multiple  # 读取某坐标的像素值并将元组为列表进行存储   Multiple是倍数
        li += tmp * multiple  # Multiple是倍数  如果是2倍 则生成两个同样的颜色文件   在后期进行单行输出多次 确保以像素点进行放大

    # 图像缩放  要将原图进行翻倍放大  然后在原图的基础上进行绘图
    result = cv2.resize(img, (width * multiple, height * multiple))
    IMAGE = SlideCrack.np_to_pil(result)
    # 转化为RGBA
    RGBA_IMG = IMAGE.convert("RGBA")
    RGBA_IMG.putdata(li)  # 写入图片
    RGBA_IMG.show()


# 切割图片，按几行几列分割
def get_split_img(img, row=2, col=2) -> dict:
    width, height = img.size
    x, y = width // col, height // row
    img = img.resize((x * col, y * row))  # 非整数倍切割时对其缩小至整倍数
    width, height = img.size
    ims = {}
    key = 0
    for j in range(0, height, y):
        for i in range(0, width, x):
            # image = SlideCrack.pil_to_np(img)
            # im = image[j:j + y, i:i + x]  # 使用 OpenCV 模块，裁剪坐标为[y0:y1, x0:x1]
            # im = SlideCrack.np_to_pil(im)

            im = img.crop((i, j, i + x, j + y))  # 使用 Pillow 模块，坐标(left, upper, right, lower)
            ims.update({key: im})
            key += 1
    return ims


def get_random_img(ims, img, row=2):
    pass
    x = y = 0
    col = len(ims) // row
    width, height = ims[0].size
    result = Image.new(ims[0].mode, (width * col, height * row))
    for im in ims:
        result.paste(im, box=(x * width, y))
        x += 1
        if x % col == 0:
            y += height
            x -= col
    result = result.resize(img.size)  # 此处缩放回原来大小会有误差导致还原后失真，不过有真实拼凑的间隙感，可选项
    result.show()
    return result

    # 上下拼接
    # width, height = ims[0].size
    # result = Image.new(ims[0].mode, (width, height * len(ims)))
    # for j, im in enumerate(ims):
    #     result.paste(im, box=(0, j * height))
    # result.show()

    # 左右拼接
    # width, height = ims[0].size
    # result = Image.new(ims[0].mode, (width * len(ims), height))
    # for j, im in enumerate(ims):
    #     result.paste(im, box=(j * width, 0))
    # result.show()


def get_recover_img(img, serilize: [list, tuple], row=2):
    col = len(serilize) // row
    ims = get_split_img(img, row=row, col=col)

    index = sorted(range(len(serilize)), key=lambda x: serilize[x])  # 还原初始位置索引
    ims = [ims[i] for i in index]

    result = get_random_img(ims, img, row)
    return result


def random_combined(ims, serilize: list = None):
    # 打乱列表顺序，随机排序
    lr = [i for i in range(len(ims))]
    serilize = np.random.choice(lr, len(lr), replace=False) if not serilize else serilize
    ims = [ims[i] for i in serilize]
    return ims, list(serilize)


def main(img, row=2, col=2, serilize: list = None):
    # 切割图片
    ims = get_split_img(img, row=row, col=col)

    # 打乱后的图片
    ims, serilize = random_combined(ims, serilize)

    # # 1、继续打乱切割后指定的位置
    # def 拼多多(im, row, col, serilize: list = None):
    #     ims4 = get_split_img(im, row=row, col=col)
    #     ims4, serilize1 = random_combined(ims4, serilize=serilize)
    #     out = get_random_img(ims4, img=img, row=row)
    #     return out
    #
    # # ims[serilize.index(4)] = 拼多多(ims[serilize.index(4)], row=1, col=11, serilize=None)  # 原图的中间 serilize.index(4)
    # ims[4] = 拼多多(ims[4], row=1, col=11, serilize=None)    # 打乱后的中间 4
    # 2、放个缩小图
    # ims[4] = SlideCrack.np_to_pil(cv2.resize(SlideCrack.pil_to_np(img), (121, 121)))
    ims[(row * col) // 2] = img.resize(ims[0].size)  # 这样无告警提示

    # 拼接打乱后的图片
    out = get_random_img(ims, img=img, row=row)
    # out.save('C:/Users/11390/Desktop/11.PNG')

    # 还原
    get_recover_img(out, serilize=serilize, row=row)


if __name__ == '__main__':
    pass
    # # 切割图片并随机排列再还原
    # url = 'http://ydgw.yundasys.com:31620/images/xuanchuan.png'
    # data = requests.get(url).content
    # # SlideCrack.show(data)
    #
    # img = SlideCrack.bytes_to_pil(data)
    # img = img.convert('RGBA')  # (此处有个小坑) 需要图像数据的预处理，从'P','RGBA','RGB'等多种 mode 的图像转换
    # print(img.size)
    #
    # # 切割行列可以是任意整数，按宽高比例整倍数最佳
    # row = 7
    # col = 7
    # main(img, row=row, col=col)

    # # 放大图片
    # k = 8
    # url = 'http://ydgw.yundasys.com:31620/upload/image/20220826/aa710e4b01c732cb2050ba5db845af76.png'
    # data = requests.get(url).content
    # SlideCrack.show(data)
    # src = SlideCrack.bytes_to_np(data)
    # y, x = src.shape[:2]
    # res = cv2.resize(src, (x * k, y * k))
    # SlideCrack.show(SlideCrack.np_to_byte(res))
    #
    # # 无损放大
    # retinapad_picture(data, k)

    row = 3
    col = 3
    img = Image.open('C:/Users/11390/Desktop/2.jpg')
    # main(img, row=row, col=col, serilize=[1, 3, 6, 2, 0, 5, 8, 4, 7])
    # main(img, row=row, col=col, serilize=[i for i in range(9)])
    main(img, row=row, col=col, serilize=[0, 7, 2, 5, 4, 3, 6, 1, 8])
    # main(img, row=row, col=col)
