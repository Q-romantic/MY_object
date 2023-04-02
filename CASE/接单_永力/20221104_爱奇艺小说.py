# -*- coding: utf-8 -*-
"""
@Time    : 2022/11/4  004 下午 16:37
@Author  : Jan
@File    : 20221104_爱奇艺小说.py
"""

import execjs
import parsel
import requests
from working.all_tools.tools import getip
from working.all_tools.tools import getua

""" {} """


def get_sign(a):
    index = open('1.js', 'r', encoding='utf-8')
    js = execjs.compile(index.read())
    a = js.call('get_sign', a)
    return a


headers = {
    "User-Agent": getua(),
    # "User-Agent": "User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 Edg/107.0.1418.26",

}
proxies = {
    'http': 'http://' + getip(),
    'https': 'http://' + getip(),
}

url0 = 'https://wenxue.iqiyi.com/book/detail-gpwx7lb53d.html'
url = "https://wenxue.iqiyi.com/book/catalog-gpwx7lb53d-1.html"  # 全部章节

response = requests.get(url, headers=headers)
data = response.text
# print(data)
print(response)
sel = parsel.Selector(response.text)
link = sel.xpath('/html/body/div[5]/div/div[1]/div/dl/dd/div/a/@href').getall()
name = sel.xpath('/html/body/div[5]/div/div[1]/div/dl/dd/div/a/text()').getall()
num = 0
for n, l in zip(name, link):
    print(n, l.replace("//wenxue.iqiyi.com", "https://wenxue.m.iqiyi.com"))
    chapterId = l.split("-")[-1].split(".")[0]
    print(chapterId)
    # 方法一：传入参数
    # tt = {"bookId": "gpwx7lb53d", "chapterId": chapterId, "fields": "read", "sourceType": -1}
    # sign = get_sign(chapterId)

    # 方法二：传入字典
    tt = {"bookId": 'gpwx7lb53d', "chapterId": chapterId, "fields": 'read', "sourceType": -1}
    sign = get_sign(tt)
    print(sign)
    url = "https://api-yuedu.iqiyi.com/book/h5/bookRead"
    headers = {
        "User-Agent": "User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 Edg/107.0.1418.26",
    }
    params = {
        "apiKey": "aDVGYWtlZEFwaUtleQ==zzz",
        "sign": sign,
        "srcPlatform": "15",
        "authCookie": "a3X2QMwazskjm2m3m112TcIVEZxnMfE0F6ve3auaJ5nxUjBe5ok6om3dEdr7YZqujOqSlR3c",
        "userId": "1439571610",
        "appType": "2",
        "bookId": "gpwx7lb53d",
        "chapterId": chapterId,
        "fields": "read",
        "sourceType": "-1"
    }
    response = requests.get(url, headers=headers, params=params)
    response.encoding = response.apparent_encoding
    data = response.text
    print(data)
    # time.sleep(2)
    if num < 2:
        num += 1
        continue
    else:
        break
