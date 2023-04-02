# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/24  024 上午 9:04
@Author  : Jan
@File    : 有道_v2.py
"""
import json

""" {} """
# execjs 执行js脚本时编码错误问题
# 方法一：
# import subprocess
# from functools import partial
# subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
# 方法二：打开subprocess.py文件，找到初始化函数__init__()，修改参数的默认值为encoding=‘utf-8’，程序运行不再报错
import execjs
import time
import requests
import pprint
from hashlib import md5

headers_2 = {
    "Cookie": "OUTFOX_SEARCH_USER_ID=1100010620@10.169.0.84;",
    "Referer": "https://fanyi.youdao.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50"
}
now = lambda: str(int(time.time() * 1000))


def get_sign(t, e):
    s = f'client=fanyideskweb&mysticTime={t}&product=webfanyi&key={e}'
    m = md5(s.encode('utf-8'))
    return m.hexdigest()


params_1 = lambda t, e: {
    "keyid": "webfanyi-key-getter",
    "sign": get_sign(t, e),
    "client": "fanyideskweb",
    "product": "webfanyi",
    "appVersion": "1.0.0",
    "vendor": "web",
    "pointParam": "client,mysticTime,product",
    "mysticTime": t,
    "keyfrom": "fanyi.web"
}
url = 'https://dict.youdao.com/webtranslate/key'
e = "asdjnjfenknafdfsdfsd"
response = requests.get(url, params=params_1(now(), e))
data = response.json()
# print(data)
# print(response)

params_2 = lambda t, e: {
    "i": "who",
    "from": "auto",
    "to": "",
    "domain": 0,
    "dictResult": "true",
    "keyid": "webfanyi",
    "sign": get_sign(t, e),
    "client": "fanyideskweb",
    "product": "webfanyi",
    "appVersion": "1.0.0",
    "vendor": "web",
    "pointParam": "client,mysticTime,product",
    "mysticTime": t,
    "keyfrom": "fanyi.web"
}
url = 'https://dict.youdao.com/webtranslate'
e = data['data'].get('secretKey')  # 貌似是固定值 e = "fsdsogkndfokasodnaso"
response = requests.post(url, headers=headers_2, data=params_2(now(), e))
data = response.text
# print(data)
# print(response)


# def get_decode(a):
#     index = open('有道_v2.js', 'r', encoding='utf-8')
#     js = execjs.compile(index.read())
#     a = js.call('O', a)
#     return a
#
#
# res = get_decode(data)
# print(res)

# 之前如下方法报错，可通过如上方法修改编码
js_fn = \
    """
    const crypto = require('crypto');


    function m(e) {
        return crypto.createHash("md5").update(e).digest()
    }

    O = (t) => {
        decodeKey = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
        decodeIv = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"

        if (!t)
            return null;
        const a = Buffer.alloc(16, m(decodeKey))
            , r = Buffer.alloc(16, m(decodeIv))
            , i = crypto.createDecipheriv("aes-128-cbc", a, r);
        let s = i.update(t, "base64", "utf-8");
        return s += i.final("utf-8"),
            s
    };
    """
x = execjs.compile(js_fn)
res = x.call('O', data)
pprint.pprint(json.loads(res))
