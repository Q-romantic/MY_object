# -*- coding: utf-8 -*-
import requests
from login import login_headers
import time
import math
import random
import pywasm

""" 引入了wasm """

url = 'https://match.yuanrenxue.com/api/match/15'

total = 0
for i in range(1, 6):
    t = int(time.time())
    t1 = int(t / 2)
    t2 = int(t / 2 - math.floor(random.random() * 50 + 1))
    wasm = pywasm.load("main_to_15.wasm")
    sign = wasm.exec("encode", [t1, t2])
    m = f"{sign}|{t1}|{t2}"
    params = {
        'page': i,
        'm': m
    }
    response = requests.get(url, headers=login_headers, params=params)
    print(response.text)
    data = response.json()["data"]
    for d in data:
        total += d["value"]

answer = total
print(answer)
url = 'https://match.yuanrenxue.com/api/answers'
params = {'answer': answer, 'id': 15}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)
