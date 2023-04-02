# -*- coding: utf-8 -*-
"""
@Time    : 2022/7/18  018 下午 14:31
@Author  : Jan
@File    : 口碑.py
"""
import re
from fontTools.ttLib import TTFont
from PIL import ImageFont, Image, ImageDraw
from io import BytesIO
import ddddocr
import parsel
import requests
from working.all_tools.tools import getip
from working.all_tools.tools import getua

""" {} """

headers = {
    "User-Agent": getua(),

}
proxies = {
    'http': 'http://' + getip(),
    'https': 'http://' + getip(),
}

url = 'https://k.autohome.com.cn/detail/view_01dmht7gbq68vkadhm6cr00000.html'

response = requests.get(url, headers=headers, params={}, data={}, proxies=proxies)
data = response.text
font_url = re.findall("url\('(.*?)'\) format\('woff'\);", data)[0]
print(font_url)
cont = requests.get(font_url).content


# with open('1.woff', 'wb') as f:
#     f.write(cont)
# font = TTFont('1.woff')
# font.saveXML('1.xml')
# uni_list = font.getGlyphOrder()[1:]
# print(uni_list)

def identify_word(bin: bytes):
    """识别ttf字体结果"""

    # 由于TTFont接收一个文件类型
    # BytesIO(bin_data) 把二进制数据当作文件来操作
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

    dic = {}
    font = TTFont(BytesIO(bin))
    ocr = ddddocr.DdddOcr()
    for cmap_code, glyph_name in font.getBestCmap().items():
        bytes_io = BytesIO()
        pil = font_to_img(cmap_code, BytesIO(bin))
        pil.save(bytes_io, format="PNG")
        word = ocr.classification(bytes_io.getvalue())  # 识别字体
        # print(cmap_code, glyph_name, word)
        dic[glyph_name] = word
    # print(dic)
    return dic


# tmp = identify_word('1.woff')
tmp = identify_word(cont)

obj = re.findall("&#x(.*?);", data)
for key in obj:
    data = data.replace(f"&#x{key};", tmp["uni" + key.upper()])
# print(tmp)
selector = parsel.Selector(data)
divs = selector.xpath('//div[@class="kb-con"]/div')
for div in divs:
    info = div.xpath('./p//text()').getall()
    info = "".join(info)
    print(info)
    # li = []
    # for i in info:
    #     if "uni" in i:
    #         i = i.upper().replace("UNI", "uni").replace(";", "")
    #         i = tmp[i]
    #     li.append(i)
    # s = "".join(li)
    # print(s)
    # break
# print(data)
# print(response)
# print(divs)
