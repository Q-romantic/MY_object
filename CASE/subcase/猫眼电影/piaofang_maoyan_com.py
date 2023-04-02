# -*- coding: utf-8 -*-
"""
@Time    : 2022/7/9  009 下午 23:24
@Author  : Jan
@File    : piaofang_maoyan_com.py
"""
import base64
import hashlib
import random
import time

import requests
import pprint
from working.all_tools.tools import getua

""" {} """

headers = {
    "User-Agent": getua(),

}
proxies = {
    # 'http': 'http://' + getip(),
    # # 'https': 'https://' + getip(),
}

url = 'https://piaofang.maoyan.com/dashboard-ajax'
ts = str(int(time.time() * 1000))
index = str(int(random.random() * 10))
ua = base64.b64encode(getua().encode()).decode()
s = f"method=GET&timeStamp={ts}&User-Agent={ua}&index={index}&channelId=40009&sVersion=2&key=A013F70DB97834C0A5492378BD76C53A"
signKey = hashlib.md5(s.encode()).hexdigest()
params = {
    "orderType": "0",
    "uuid": "181e1834073c8-0f346a0fb9e5a2-4a617f5c-1fa400-181e1834073c8",
    "timeStamp": ts,
    "User-Agent": ua,
    "index": index,
    "channelId": "40009",
    "sVersion": "2",
    "signKey": signKey
}
print(params)
response = requests.get(url, headers=headers, params=params, data={}, proxies=proxies)
data = response.json()
pprint.pprint(data)
print(response)
