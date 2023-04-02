# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/6  006 下午 17:49
@Author  : Jan
@File    : 图片处理.py
"""

""" { 切割图片随机组合再还原 & 滑块验证缺口坐标识别 & 图片无损放大 } """

import cv2
import requests
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
    def other(im, row, col, serilize: list = None):
        ims_1 = get_split_img(im, row=row, col=col)
        ims_1, serilize1 = random_combined(ims_1, serilize=serilize)

        ims_2 = get_split_img(img, row=2, col=2)  # 4 x 4 中间的 2 x 2
        ims_1[5] = ims_2[0].resize(ims_1[5].size)  # 中心四个位置替换
        ims_1[6] = ims_2[1].resize(ims_1[6].size)
        ims_1[9] = ims_2[2].resize(ims_1[9].size)
        ims_1[10] = ims_2[3].resize(ims_1[10].size)

        out = get_random_img(ims_1, img=img, row=row)
        return out

    # # ims[serilize.index(4)] = 拼多多(ims[serilize.index(4)], row=3, col=3, serilize=None)  # 原图的中间 serilize.index(4)
    # ims[4] = 拼多多(ims[4], row=3, col=3, serilize=None)  # 打乱后的中间 4
    # 2、放个缩小图
    # ims[(row * col) // 2] = img.resize(ims[0].size)  # 这样无告警提示
    # ims[serilize.index((row * col) // 2)] = img.resize(ims[0].size)  # 这样无告警提示

    serilize_1 = [i for i in range(16)]
    serilize_1[1], serilize_1[2] = serilize_1[2], serilize_1[1]  # 第一行和第四行中间左右交换
    serilize_1[4], serilize_1[8] = serilize_1[8], serilize_1[4]  # 第一列和第四列中间上下交换
    serilize_1[7], serilize_1[11] = serilize_1[11], serilize_1[7]
    serilize_1[13], serilize_1[14] = serilize_1[14], serilize_1[13]

    im_1 = other(img, row=4, col=4, serilize=serilize_1)  # 内部 4 x 4

    ims[(row * col) // 2] = im_1.resize(ims[0].size)

    # 拼接打乱后的图片
    out = get_random_img(ims, img, row=row)
    # out.save('C:/Users/11390/Desktop/33.PNG')

    # 还原
    result = get_recover_img(out, serilize=serilize, row=row)
    # result.save('C:/Users/11390/Desktop/44.PNG')


if __name__ == '__main__':
    pass
    # 切割图片并随机排列再还原
    url = 'https://uploadfiles.nowcoder.com/images/20230206/993219759_1675676787618/156005C5BAF40FF51A327F1C34F2975B'
    data = requests.get(url).content
    # SlideCrack.show(data)
    img = SlideCrack.bytes_to_pil(data)

    img = img.convert('RGBA')  # (此处有个小坑) 需要图像数据的预处理，从'P','RGBA','RGB'等多种 mode 的图像转换

    # 切割行列可以是任意整数，按宽高比例整倍数最佳
    row = 3
    col = 3
    main(img, row=row, col=col, serilize=[0, 7, 2, 5, 4, 3, 6, 1, 8])

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
