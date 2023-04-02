# -*- coding: utf-8 -*-
import requests
from login import login_headers

""" 
绝大部分网页是 http1.1，少量http2.0获取如下
python中用http2.0的话需要安装 pip3 install httpx
还要根据提示安装 pip install httpx[http2]
"""

url = 'https://match.yuanrenxue.com/api/match/17'

total = 0

# 方法二：貌似有点小问题，单独执行无问题，放一起有顺序？？？
from hyper.contrib import HTTP20Adapter

session = requests.session()
session.mount('https://match.yuanrenxue.com', HTTP20Adapter())
for page in range(1, 6):
    params = {'page': page}
    response = session.get(url, headers=login_headers, params=params)
    print(response.status_code, response.text)

# 方法一：
import httpx

for i in range(1, 6):
    params = {'page': i}
    with httpx.Client(headers=login_headers, http2=True) as client:
        response = client.get(url, headers=login_headers, params=params)
        print(response.text)
        data = response.json()["data"]
        for d in data:
            total += d["value"]

answer = total
print(answer)
url = 'https://match.yuanrenxue.com/api/answers'
params = {'answer': answer, 'id': 17}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)

# 方法三：缺点较多，不支持代理，不支持传参
from hyper import HTTP20Connection

with HTTP20Connection(host='match.yuanrenxue.com', secure=True) as conn:
    for page in range(1, 6):
        req = conn.request('GET', f'/api/match/17?page={page}', headers=login_headers)
        response = conn.get_response(req)
        print(response.status, response.read().decode())
