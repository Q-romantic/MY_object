# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/4  004 上午 11:43
@Author  : Jan
@File    : api_tgnet_com.py
"""
import base64
import re
from PIL import Image
from io import BytesIO
from 证码缺口位置坐标 import SlideCrack

""" {} """

import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70"}
url = 'http://api.tgnet.com/SlidingVerificationCode/GetVerificationCode'
response = requests.get(url, headers=headers, params={}, data={})
data = response.json()['data']
# print(data)
# print(response)
array = data['array']
imgx = data['imgx']
imgy = data['imgy']
normal = data['normal']
small = data['small']
position_y = data['position_y']


def img_base64_to_byte(src: str) -> bytes:
    result = re.search("data:image/(?P<ext>.*?);base64,(?P<data>.*)", src, re.DOTALL)
    # ext = result.groupdict().get("ext")
    data = result.groupdict().get("data")
    # 2、base64解码(如下2种方法)
    # img = base64.urlsafe_b64decode(data)
    img = base64.b64decode(data)
    return img


normal = img_base64_to_byte(normal)
small = img_base64_to_byte(small)
# SlideCrack.show(normal)


def recover(img: bytes, serilize: [list, tuple]):
    img = Image.open(BytesIO(img))
    # img.show()
    target = Image.new('RGB', (300, 200))
    for i in range(20):
        c = 100 if 9 < serilize[i] else 0
        u = 100 if i > 9 else 0
        box = (i % 10 * 30, u, i % 10 * 30 + 30, u + 100)
        region = img.crop(box)
        target.paste(region, (serilize[i] % 10 * 30, c))
    # target.show()
    return SlideCrack.pil_to_byte(target)
normal = recover(normal, eval(array))
out = SlideCrack(normal, small)
print(out)

url = 'http://api.tgnet.com/VerificationCode/CheckCode'
params = {
    "code":"[{\"_X\":155,\"_Y\":170},{\"_X\":113,\"_Y\":94}]",
    "key":""
}
data = {}


