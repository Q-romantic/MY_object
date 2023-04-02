# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/21  021 下午 20:28
@Author  : Jan
@File    : 58同城.py
"""

""" {} """

import re
import base64
import parsel
import requests
from fontTools.ttLib import TTFont
from io import BytesIO

# TTFont 消除提示告警：2 extra bytes in post.stringData array
import logging

logging.basicConfig(level=logging.CRITICAL)

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
url = 'https://cs.58.com/ershouche/53194090469786x.shtml?adtype=5&ClickID=70&infotype=z_2&iuType=z_2&productid=10003&dispcname=cs&entinfo=53194090469786_z&PGTID=0d30001d-0019-e26e-cec4-ab4b4597a2f2&page_id=501&end=end&oCate=29&psid=191893164219805571173015768&TID=fc669f3e-098c-423b-8db7-ca8534b5a5eb&typos=topinfo_l1&dispcid=414&slotid=1000789'

response = requests.get(url, headers=headers, params={}, data={})
data = response.text
# print(data)
font_data = re.findall("font-family:'fangchan-secret';src:url\('data:application/font-ttf;charset=utf-8;base64,(.*?)'\) format", data)[0]
byte_woff = base64.b64decode(font_data)
font = TTFont(BytesIO(byte_woff))
# font.save('1.woff')
# font.saveXML('1.xml')
# 如上分析字体由来后得出结论，每套字体编码对应关系是固定的，使用键对应值时需要 -1
cmap = font['cmap'].getBestCmap()
# print(cmap)
# 此处可通过 ddddocr 识别对应字体，因为规律很明显所以省去
cmap = {hex(key): int(re.search(r'\d+', value).group()) - 1 for key, value in cmap.items()}
# print(cmap)

# print(font_data)
sel = parsel.Selector(data)
name = sel.xpath('/html/body/section[1]/div/div[4]/h1/text()').get()
print(name)
# data = sel.xpath('/html/body/section[1]/div/div[4]/div[2]/div[2]//text()').getall()
# data = ''.join(data).replace('\n', '').replace(' ', '')
# print(data)

data = sel.xpath('/html/body/section[1]/div/div[4]/div[2]/div[2]/em/text()').get()
# print(data.encode('unicode_escape'))  # 可能是我之前windows系统修改默认编码为utf-8导致网页源代码自动转码导致乱码
print(data)
data = data.encode('unicode_escape').decode().replace('\\u', '0x')
for i in cmap:
    data = re.sub(i, str(cmap[i]), data)
data += '万'
print(data)
data = sel.xpath('/html/body/section[1]/div/div[4]/div[2]/div[2]/a/text()').get()
print(data)

from PIL import ImageFont, Image, ImageDraw
from io import BytesIO
import ddddocr
from fontTools.ttLib import TTFont


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
        # print(hex(cmap_code), glyph_name, word)  # 三者对应关系
        # dic.update({glyph_name: word})
        dic[glyph_name] = word
        dic[hex(cmap_code)] = word
    # print(dic)
    return dic


# dic = identify_word('1.woff')
# print(dic)
