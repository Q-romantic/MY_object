# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/12  012 下午 17:38
@Author  : Jan
@File    : 拼多多课堂.py
"""
import json
import time
import execjs
from jsonpath import jsonpath
from io import BytesIO
from PIL import Image
import requests

""" {} """


# 搜索 messagePack
def get_anti_contnt(a):
    index = open('拼多多课堂_v1.js', 'r', encoding='utf-8')
    js = execjs.compile(index.read())
    a = js.call('get_anti_contnt', a)
    return a


t = str(int(time.time() * 1000))
anti_contnt = get_anti_contnt(t)
# print(anti_contnt)

headers = {
    "anti-content": anti_contnt,
    "content-type": "application/json",
    # "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"
}

params = {
    "courseId": "4617",
    "lastId": "0",
    "pageSize": "50"
}

url = 'https://mms.pinduoduo.com/cambridge/api/duoduoCollege/queryCourseCommentsV2'
response = requests.post(url, headers=headers, data=json.dumps(params))
res = response.json()
# print(res)
img_urls = jsonpath(res, '$..mallLogo')
# created_times = jsonpath(res, '$..createdAt')
img_urls = [i.split('?')[0] for i in img_urls]
# img_urls = [(t, i.split('?')[0]) for t, i in zip(created_times, img_urls)]
# print(img_urls)

li = []
for url in img_urls:
    res = requests.get(url).content
    img = Image.open(BytesIO(res))
    li.append(img)


def get_merge_img(ims, row=2):
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
    result.show()

    return result


out = get_merge_img(li, 5)
# 保存合成图
# out.save('test.PNG')
