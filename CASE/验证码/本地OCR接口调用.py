# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/10  010 下午 21:43
@Author  : Jan
@File    : 本地OCR接口调用.py
"""
import requests
import base64

""" {} """
"https://gitee.com/alisen39/TrWebOCR"

url = 'http://localhost:8089/api/tr-run/'
img = 'C:/Z/Desktop/拼多多/360截图20170702201921326.jpg'

with open(img, 'rb') as f:
    img_data = f.read()

# 方法一：
img1_file = {
    'file': img_data
}
response = requests.post(url=url, data={'compress': 0}, files=img1_file)
# response.encoding = response.apparent_encoding

# 方法二：
# response = requests.post(url=url, data={'img': base64.b64encode(img_data)})
datas = response.json()['data']['raw_out']
for index, data in enumerate(datas):
    text = data[1]
    print(text, end='')
    # 判断是否属于同一行
    if index < len(datas) - 1 and abs(datas[index][0][1] - datas[index + 1][0][1]) > 5:
        print()
