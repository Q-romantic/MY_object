# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/2  002 下午 19:02
@Author  : Jan
@File    : DOC88.COM_v3.py
"""

""" {} """

import requests
from lxml import etree
import pprint
import parsel
import random
from working.all_tools.tools import get_ua
from working.all_tools.tools import get_ip

# from working.all_tools.tools import curl_to_python

""" {} """

# headers = {"User-Agent": get_ua()}
# proxies = (lambda ips: {'http': r'http://' + ips, 'https': r'http://' + ips})(get_ip())

# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
# proxies = {}












# url = ''
# response = requests.get(url, headers=headers, params={}, data={}, proxies=proxies)
# data = response.text
# print(data)
# print(response)
# sel = parsel.Selector(response.text)
# a = sel.xpath('//div[@id="u1"]/a/text()').getall()
# print(a)
# xml = etree.HTML(response.text)
# b = xml.xpath('//div[@id="s-top-left"]/a/@target')
# print(b)










import hashlib
import time

import httpx


def get_md5(str):
    m = hashlib.md5()
    if not isinstance(str, bytes):
        str = str.encode()
    m.update(str)
    return m.hexdigest()


def get_token_list(page, timestamp):
    params = f'api/v2/market/search?album_id=&keywords=&market_type=0&order=id&page={page}&timestamp={timestamp}&key=6rnrdpjjv6wz2sspxqeibesov1itxddc'
    return get_md5(params)


def get_list(page=1):
    timestamp = int(time.time())
    headers = {
        'Host': 'api.onemeta.com.cn',

        'x-token': get_token_list(page, timestamp),
        'token': '2d48569d-830f-42c4-88db-6acbc93aaf9f',
        'version': '4.0.12,2',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Mobile Safari/537.36 Edg/103.0.1264.37',
    }
    params = {
        'keywords': '',
        'product_id': '',
        'album_id': '',
        'page': page,
        'market_type': '0',
        'order': 'id',
        'timestamp': timestamp,
    }

    with httpx.Client(http2=True) as client:
        response = client.get(url='https://api.onemeta.com.cn/api/v2/market/search', params=params, headers=headers)
    results = response.json()
    if not results.get('code'):
        return get_list(page)
    print(results)


if __name__ == '__main__':
    get_list()



























































