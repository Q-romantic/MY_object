# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/3  003 上午 11:08
@Author  : Jan
@File    : 证码缺口位置坐标.py
"""

""" { 识别验证码图片缺口位置坐标 & 框选标记 } """

import cv2
import numpy as np
from io import BytesIO
from PIL import Image, ImageDraw

def dec(function):
    return function()

@dec
class SlideCrack(object):
    def __int__(self):
        pass

    def __call__(self, target: [str, bytes], slide: [str, bytes], out: str = 'out'):
        """
        :param target: 背景图片path
        :param slide: 缺口图片path
        :param out: 输出图片path
        """
        self.out = out + '.png'
        # 1、本地文件路径
        if isinstance(target, str):
            self.bg = target
            self.bg_img = cv2.imread(self.bg)
        if isinstance(slide, str):
            self.tp = slide
            self.tp_img = cv2.imread(self.tp)

        # 2、二进制 ---> numpy数组
        if isinstance(target, bytes):
            self.bg_img = self.bytes_to_np(target)
        if isinstance(slide, bytes):
            self.tp_img = self.bytes_to_np(slide)

        return self.discern()

    # 二进制 ---> numpy数组
    @classmethod
    def bytes_to_np(self, byte: bytes):
        data = np.asarray(bytearray(byte), dtype="uint8")
        image = cv2.imdecode(data, cv2.IMREAD_COLOR)
        return image

    # 二进制 ---> PIL
    @classmethod
    def bytes_to_pil(self, byte: bytes):
        img = Image.open(BytesIO(byte))
        return img

    # numpy数组 ---> 二进制
    @classmethod
    def np_to_byte(self, image) -> bytes:
        res = cv2.imencode('.png', image)[1].tobytes()
        return res

    # numpy数组 ---> 二进制 ---> PIL
    @classmethod
    def np_to_pil(self, image):
        data = self.np_to_byte(image)
        img = self.bytes_to_pil(data)
        return img

    # PIL ---> 二进制
    @classmethod
    def pil_to_byte(self, img) -> bytes:
        bytesIO = BytesIO()  # 注意：针对每个图片都要新建，这里并不代表赋值，感觉像是新建一个实例化对象
        img.save(bytesIO, format='PNG')  # format='JPEG'，实际未保存
        res = bytesIO.getvalue()
        return res

    # PIL ---> 二进制 ---> numpy数组
    @classmethod
    def pil_to_np(self, img):
        data = self.pil_to_byte(img)
        image = self.bytes_to_np(data)
        return image

    @classmethod
    def show(self, im: [any, bytes]):
        if isinstance(im, bytes):
            img = self.bytes_to_pil(im)
        else:
            img = self.np_to_pil(im)
        img.show()

        # 不推荐，会暂停占用程序运行时间
        # cv2.imshow('Show', im)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    @staticmethod
    def clear_white(img):
        rows, cols, channel = img.shape
        min_x = min_y = 255
        max_x = max_y = 0
        for x in range(1, rows):
            for y in range(1, cols):
                t = set(img[x, y])
                if len(t) >= 2:
                    if x <= min_x:
                        min_x = x
                    elif x >= max_x:
                        max_x = x
                    if y <= min_y:
                        min_y = y
                    elif y >= max_y:
                        max_y = y
        return img[min_x:max_x, min_y: max_y]

    def template_match(self, target, slide):
        th, tw = slide.shape[:2]
        result = cv2.matchTemplate(target, slide, cv2.TM_CCOEFF_NORMED)
        # 寻找矩阵(一维数组当作向量,用Mat定义) 中最小值和最大值的位置
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        tl = max_loc
        br = (tl[0] + tw, tl[1] + th)
        return tl, br

    # 绘制矩形边框，将匹配区域标注出来
    @classmethod
    def image_draw_save(self, target: [any, bytes], start, end, offset=0):
        if isinstance(target, bytes):
            target = self.bytes_to_np(target)
        # target：目标图像
        # start：矩形定点
        # end：矩形的终点
        # (0,0,255)：矩形边框颜色
        # 1：矩形边框线粗细
        start = (lambda x: (x[0] - offset, x[1] - offset))(start)
        end = (end[0] + offset, end[1] + offset)

        # # 方式一
        # cv2.rectangle(target, start, end, (0, 0, 255), 1)
        # a = 'x, y'  # 类别名称
        # b = start  # 置信度
        # font = cv2.FONT_HERSHEY_SIMPLEX  # 定义字体
        # imgzi = cv2.putText(target, '{} = {}'.format(a, b), (start[0], start[1] - 15), font, 1, (0, 0, 255), 2)
        #                   图像，            文字内容，      坐标(右上角坐标)           字体，大小，  颜色，    字体厚度
        # 显示，保存
        # cv2.imwrite(self.out, target)
        # self.show(imgzi)

        # 方式二，使用PIL
        img = self.np_to_pil(target)
        a = ImageDraw.ImageDraw(img)
        a.rectangle((start, end), fill=None, outline='red', width=1)

        # 显示，保存
        # img.save(self.out)
        img.show()

    def discern(self):
        # 清除图片的空白区域
        self.bg_img = self.clear_white(self.bg_img)
        self.tp_img = self.clear_white(self.tp_img)

        # 转换图片为灰色
        bg_gray = cv2.cvtColor(self.bg_img, cv2.COLOR_RGB2GRAY)
        tp_gray = cv2.cvtColor(self.tp_img, cv2.COLOR_RGB2GRAY)

        # 识别图片边缘
        bg_edge = cv2.Canny(bg_gray, 100, 200)
        tp_edge = cv2.Canny(tp_gray, 100, 200)

        # 转换图片格式
        bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
        tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

        # 获取缺口起止坐标
        start, end = self.template_match(bg_pic, tp_pic)
        self.image_draw_save(self.bg_img, start, end, offset=2)  # 可调整线框偏移量

        print("point:", start)
        return start


if __name__ == '__main__':

    li = [10, 1, 11, 111, 1111, 11111]
    for i in li:
        with open(f'{i}.png', mode='rb') as f1:
            with open(f'{i * 3}.png', mode='rb') as f2:
                # out = SlideCrack(f'{i}.png', f'{i * 3}.png', f'{i * 4}out.png')
                out = SlideCrack(f1.read(), f2.read(), f'{i * 4}out.png')
                print(out)
                break
