# -*- coding: utf-8 -*-
"""
@Time    : 2022/6/22  022 下午 14:29
@Author  : Jan
@File    : update_big_dic_from_woffs.py
"""
import os
import re
import requests
from PIL import ImageFont, Image, ImageDraw
from io import BytesIO
import ddddocr
from fontTools.ttLib import TTFont
import pprint

""" {可能是字典库调用会不定期变动，故首次使用时必须先执行此程序，更新字典 big_dic 内容} """

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36"}


def font_to_img(_code, filename):
    """将字体画成图片"""
    img_size = 1024
    img = Image.new('1', (img_size, img_size), 255)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(filename, int(img_size * 0.7))
    txt = chr(_code)
    x, y = draw.textsize(txt, font=font)
    draw.text(((img_size - x) // 2, (img_size - y) // 2), txt, font=font, fill=0)
    return img


def identify_word(_ttf_path):
    """识别ttf字体结果"""
    dic = {}
    font = TTFont(_ttf_path)
    ocr = ddddocr.DdddOcr()
    for cmap_code, glyph_name in font.getBestCmap().items():
        bytes_io = BytesIO()
        pil = font_to_img(cmap_code, _ttf_path)
        pil.save(bytes_io, format="PNG")
        word = ocr.classification(bytes_io.getvalue())  # 识别字体
        # print(cmap_code, glyph_name, word)
        # dic.update({glyph_name: word})
        dic[glyph_name] = word
    # print(dic)
    return dic


def get_single(file_name):
    list01 = []
    for i in open(file_name):
        if i in list01:
            continue
        list01.append(i)
    with open('tmp.txt', 'w') as handle:
        handle.writelines(list01)
    os.remove(file_name)
    os.rename('tmp.txt', file_name)


def get_woff_files(url, flags: [bool, int] = 0):
    response = requests.get(url, headers=headers, params={}, data={})
    data = response.text
    # print(data)
    woff_info = re.findall('font-family: "PingFangSC-Regular-(?P<name>.*?)";.*?,url\("(?P<url>.*?)"\);', data)
    for name, woff_url in woff_info:
        name = 'tmp_' + name + woff_url[-5:]
        woff_url = f'http:{woff_url}'
        print([name, woff_url])

        def save_woffs_to_files():
            response = requests.get(woff_url)
            data = response.content
            with open(name, mode='wb') as f:
                f.write(data)

        def save_woffs_url_to_file():
            data = str([name, woff_url])
            with open('woffs_url.txt', mode='a') as f:
                f.write(data)
                f.write('\n')

        if flags:
            save_woffs_to_files()  # 保存 woffs
        save_woffs_url_to_file()  # 保存 woffs_url
    get_single('woffs_url.txt')  # 对文件内容去重


def get_big_dic():
    files = [
        'tmp_address.woff',
        'tmp_dishname.woff',
        'tmp_hours.woff',
        'tmp_num.woff',
        'tmp_review.woff',
        'tmp_shopdesc.woff'
    ]
    dic = {}
    li = []
    for path in files:
        name = path[4:-5]
        print(name)
        tmp = identify_word(path)
        for j in tmp:
            if tmp[j] == 'o':
                tmp[j] = '0'
                li.append(('dic["' + name + '"]["' + j + '"]'))  # 统计列出字母 o 所在位置并替换为 0
            elif tmp[j] == '':
                tmp[j] = 'x'
                li.append(('dic["' + name + '"]["' + j + '"]'))  # 统计列出值为空 所在位置并替换为 x

        dic[name] = tmp
        os.remove(path)
        # break
    print(dic)
    print(li)
    with open('test.txt', mode='w', encoding='utf-8') as f:
        data = str(dic)
        f.write(data)


if __name__ == '__main__':
    url = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/1fc8d061d6c9692ecd4edd85d955e08c.css'
    with open('woffs_url.txt', mode='r') as f:
        data = f.read()
        print(data)
    get_woff_files(url)  # 默认不保存 woffs

    # get_woff_files(url, flags=1)
    # get_big_dic()     # 首次执行是打开即可，耗时大约1分钟，上下联合使用
