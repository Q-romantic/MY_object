# -*- coding: utf-8 -*-
"""
@Time    : 2022/7/9  009 上午 10:12
@Author  : Jan
@File    : www_maoyan_com.py
"""
import hashlib
import os
import random
import re
import time
from PIL import ImageFont, Image, ImageDraw
from io import BytesIO
import ddddocr
from fontTools.ttLib import TTFont
import requests

""" {} """
url = 'https://www.maoyan.com/films/416'
# ua = getua()
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
headers = {
    "User-Agent":ua,
    "Referer": url,
}
proxies = {
    # # 'http': 'http://' + getip(),
    # 'https': 'http://' + getip(),
}

ts = str(int(time.time()*1000))
index = str(int(random.random()*10))
s = f"method=GET&timeStamp={ts}&User-Agent={ua}&index={index}&channelId=40011&sVersion=1&key=A013F70DB97834C0A5492378BD76C53A"
# s = f"method=GET&timeStamp=1657433384745&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44&index=9&channelId=40011&sVersion=1&key=A013F70DB97834C0A5492378BD76C53A"
signKey = hashlib.md5(s.encode()).hexdigest()
params = {
    "timeStamp":ts,
    "index":index,
    "signKey":signKey,
    "channelId":"40011",
    "sVersion":"1",
    "webdriver":"false"
}
print(params)
# response = requests.get(url, headers=headers)
# time.sleep(1)
response = requests.post(url, headers=headers, json=params, proxies=proxies)
response.encoding = response.apparent_encoding
data = response.text
print(data)
print(response.url)
woff_url = "http:" + re.findall(',url\(\"(.*?)"\);', data)[0]
response = requests.get(woff_url)
data = response.content
with open(woff_url[-13:], mode='wb') as f:
    f.write(data)
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

def get_big_dic():
    files = [
        woff_url[-13:],
    ]
    dic = {}
    li = []
    for path in files:
        name = path[:-5]
        # print(name)
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
    # print(li)
    with open('test.txt', mode='a', encoding='utf-8') as f:
        data = str(dic)
        f.write(data)
        f.write("\n")
    get_single('test.txt')  # 对文件内容去重

get_big_dic()

















# with open(file='index.js', mode='r', encoding='utf-8') as f:
#     js = f.read()
# ctx = execjs.compile(js)  # 执行js代码
# n = ctx.call('getMD5Sign')
# print(n)

















































