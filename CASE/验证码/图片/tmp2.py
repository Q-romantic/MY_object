# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/2  002 下午 16:15
@Author  : Jan
@File    : tmp2.py
"""
import cv2

""" {} """

from PIL import Image


def crop_image(img: Image, x, y, width, height):
    """裁剪图片"""
    return img.crop((x, int(y), int(x + width), int(y + height)))


def paste_image(new_img: Image, img: Image, x, y, width, height):
    """粘贴图片到new_img中"""
    new_img.paste(img, (x, int(y), int(x + width), int(y + height)))


def restore_image(img: Image):
    """还原打乱的验证码图片"""
    img_list = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43,
                42, 12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
    r = 312  # width
    n = 160  # height
    s = n / 2
    u = 10
    new_img = Image.new("RGBA", (r, n))
    for c in range(52):
        f = img_list[c] % 26 * 12 + 1
        _ = s if img_list[c] > 25 else 0
        crop_img = crop_image(img, f, _, u, s)
        paste_image(new_img, crop_img, c % 26 * 10, s if c > 25 else 0, u, s)
    return new_img


def identify_gap(bg, tp, out):
    '''
    bg: 背景图片path
    tp: 缺口图片path
    out:输出图片path
    '''
    # 读取背景图片和缺口图片
    bg_img = cv2.imread(bg)  # 背景图片
    tp_img = cv2.imread(tp)  # 缺口图片

    # # 转换颜色通道,这里为什么要BGR转为RGB，因为np.array转换pillow的图像的结果就是BGR格式的，可选项
    # bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2RGB)
    # tp_img = cv2.cvtColor(tp_img, cv2.COLOR_BGR2RGB)

    # 识别图片边缘
    bg_edge = cv2.Canny(bg_img, 100, 200)
    tp_edge = cv2.Canny(tp_img, 100, 200)

    # 转换图片格式
    bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
    tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

    cv2.waitKey(0)
    # 缺口匹配
    res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
    print(min_val, max_val, min_loc, max_loc)

    # 绘制方框
    th, tw = tp_pic.shape[:2]
    tl = max_loc  # 左上角点的坐标
    br = (tl[0] + tw, tl[1] + th)  # 右下角点的坐标

    # 方式一
    # cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2)  # 绘制矩形
    # # cv2.imwrite(out, bg_img)  # 保存在本地
    # cv2.imshow('1',bg_img)
    # cv2.waitKey(0)

    from PIL import Image, ImageDraw
    # 方式二 使用PIL
    img = Image.open(bg)
    a = ImageDraw.ImageDraw(img)
    # rectangle 坐标的参数格式为左上角（x1, y1），右下角（x2, y2）。
    a.rectangle((tl, br), fill=None, outline='red', width=2)
    # img.save(f'{tl}_{bg}')
    # img.show()

    # 返回缺口的X坐标
    return tl[0]


# li = [1, 11, 111, 1111, 11111]
# for i in li:
#     out = identify_gap(f'{i}.png', f'{i * 3}.png', 'out.png')
#     print(out)
#     break

# def recover(img,serilize):
#     img = Image.open(img)
#     target = Image.new('RGB', (300,200))
#     for i in range(20):
#         c=100 if 9<serilize[i] else 0
#         u=100 if i > 9 else 0
#         box = (i%10*30, u,i%10*30+30,u+100)
#         region = img.crop(box)
#         target.paste(region, (serilize[i]%10*30,c))
#     target.show()
#
#
# img_list = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43,
#                 42, 12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
# recover('滑块_1_big_9794e9f03.webp', img_list)


