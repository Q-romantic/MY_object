import hashlib
import json
import pprint
import random
import time

import execjs
import requests


def get_c(a):
    index = open('aaaa.js', 'r', encoding='utf-8')
    js = execjs.compile(index.read())
    a = js.call('get_c', a)
    return a


def get_x_request_token(s):
    a = []
    for i in s:
        a.append(ord(i))
    b = [71, 81, 87, 75, 85, 69, 50, 67, 86, 71, 79, 79, 66, 75, 88, 85]  # 固定值左移+后添加新增值，传递给js处理后取返回值第一个
    # b = [85, 84, 183, 129, 243, 96, 217, 5, 238, 190, 166, 237, 135, 160, 60, 5, 202, 164, 127, 137, 41, 200, 169, 128]  # 来自js->c中第一个数
    c = []
    for i in range(24):
        y = get_c(b)
        x = a[i] ^ y[0]
        c.append(x)
        b.append(x)
        b = b[1:]
    cc = []
    ss = '0123456789abcdef'
    for o in c:
        x = (o & 240) >> 4
        y = o & 15
        data = ss[x] + ss[y]
        cc.append(data)
    token = ''.join(cc)
    print(token)

    return token


if __name__ == '__main__':
    # s = "1656483259216:0:34758807"
    # s = "1656484253841:0:60967073"
    # s = "1656519848743:0:56769413"
    s = "1656519848743:0:56769413"
    get_x_request_token(s)
