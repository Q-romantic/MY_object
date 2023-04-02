# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/31  031 下午 22:15
@Author  : Jan
@File    : 2.py
"""
import time
import urllib.parse

""" {} """

import requests
from lxml import etree
from lxml.html import fromstring
import pprint
import parsel
import random
from working.all_tools.tools import get_ua
from working.all_tools.tools import get_ip

# from working.all_tools.tools import curl_to_python

""" {} """

# headers = {"User-Agent": get_ua()}
# proxies = (lambda ips: {'http': r'http://' + ips, 'https': r'http://' + ips})(get_ip())


# headers = {
#     # "cookie":"cf_clearance=5IHUmuRCy.rNW2unJGXx7GGF4NLehUwK96nl.D15ARE; ",
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.37 (KHTML, like Gecko) Chrome/108.0.5359.95 Safari/537.37"
#     # "user-agent":get_ua()
# }
# print(headers)


# import cloudscraper
# from lxml.html import fromstring
# scraper = cloudscraper.create_scraper()
# url = 'https://wallhere.com/' # 有人机检查验证
key = "我的"
searchkey = urllib.parse.quote(key, encoding="GBK")
print(searchkey)
# https://m.800xsw.net/modules/article/search.php?searchtype=articlename&searchkey=%CE%D2%B5%C4&t_btnsearch=
url = f'https://m.800xsw.net/modules/article/search.php?searchtype=articlename&searchkey={searchkey}&t_btnsearch='
# url = 'https://m.800xsw.net'
# print(urllib.parse.unquote("%E8%AF%B7%E7%A8%8D%E5%80%99%E2%80%A6", encoding="utf-8"))
# print(urllib.parse.quote("请稍候…", encoding="utf-8"))
# print(urllib.parse.unquote("%CE%D2%B5%C4", encoding="GBK"))
# print(urllib.parse.quote("我的", encoding="GBK"))

headers = {
    # "cookie":"cf_clearance=1FyZj1_iO9wGf.FdGWW3.osewTxl8xTHiKKuj_3icpY-1680274886-0-160; ",
    # "cookie":"cf_clearance=cTs2jSjnRCX908VrwgAdgAg91OAIMqBTca6djQGm8HY-1680277142-0-160; ",
    # "cookie": "cf_clearance=jSjhGfFRuya9ZssshJ9fZnL7l.hjKTllVPtHqis.v4g-1680279380-0-160; ",
    # "cookie": "cf_clearance=jmBIYUcEdykpld1O8grKYo.EGWfeGMoeNCdNg69_BOY-1680284492-0-160; ",
    # "cookie": "cf_clearance=LufLlPSbps4xtCNgI4cvy.Qj1GTmMz_mlXr_E5Ui1Hg-1680327670-0-160; ",
    # "cookie": "cf_clearance=uyCRNpEUypNGHUUv6Xle_1kpmK9G2Kvimhh0MGp700U-1680334995-0-250",
    # "cookie": "cf_clearance=bfMr572ao79oatZplMUGNtmn8Y5pu3dcd6ct8FMbYLw-1680337887-0-250",
    # "cookie": "cf_clearance=bEYD6LoBsJHw6kuUc4x6zo.FEZ0IdXU8IJGUceaXy44-1680405892-0-250",
    "cookie": "cf_clearance=jZ_uXmw48HixxuastfZGKI6XMlPX5jdmWvYrK8Ty4tM-1680410874-0-250",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

# import cfscrape
#
# # get请求
# # 实例化一个create_scraper对象
# scraper = cfscrape.create_scraper(delay=20)
# # 获取网页源代码
# resp = scraper.get(url, headers=headers)
# print(resp.text)

# # post请求
# # 实例化一个create_scraper对象
# scraper = cfscrape.create_scraper()
# # 获取真实网页源代码
# resp = scraper.post("http://example.com")
# print(resp.text)


s = time.time()
print(s)
for i in range(1, 2):
    response = requests.get(url, headers=headers)
    print(response.text)
    print(i, response.status_code, f'{time.time() - s}秒 <--------')
    sel = fromstring(response.text)
    a = sel.xpath('//table//div/a[1]/text()')[i]
    b = sel.xpath('//table//div/a[1]/@href')[i]
    print(i, a, b)



# _cf_chl_opt = {
#     cvId: '2',
#     cZone: 'm.800xsw.net',
#     cType: 'managed',
#     cNounce: '73097',
#     cRay: '7b09f0b01cf9fa3a',
#     cHash: '959617888c676ee',
#     cUPMDTk: "\/modules\/article\/search.php?searchtype=articlename&searchkey=%CE%D2%B5%C4&t_btnsearch=&__cf_chl_tk=4C05Zdn0RjUhTiy49RvCQeiJLH6k3a.E1LRpzDkU8Qs-1680279841-0-gaNycGzNCvs",
#     cFPWv: 'b',
#     cTTimeMs: '1000',
#     cMTimeMs: '0',
#     cTplV: 5,
#     cTplB: 'cf',
#     cK: "",
#     cRq: {
#         ru: 'aHR0cHM6Ly9tLjgwMHhzdy5uZXQvbW9kdWxlcy9hcnRpY2xlL3NlYXJjaC5waHA/c2VhcmNodHlwZT1hcnRpY2xlbmFtZSZzZWFyY2hrZXk9JUNFJUQyJUI1JUM0JnRfYnRuc2VhcmNoPQ==',
#         ra: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54',
#         rm: 'GET',
#         d: 'jYhJaNBbq8v8Jla21VJwSF6drhsgZUUmqjY6CIU+OwM7HHxA/6bI2yRXJA3bXoBtT5Da9lKtYGGNf/XuzZP3Sh8+D0xD9wpHhwx9Tp3HnGYLoPvZdtJK8PtD+WqjcR5bmX6ia6ZugO8VUP9Kj8ZnL0JNfBwtmqT2n6fw79e1G3dszXM3Vk8D+YjT96VJvw1TCk+l1pmA4R5JPh9tvfvUIL8ZaTwtspyBnVAb4UVv63RviZBA+/zyTa/vjsw9wk+N6GbaecqihkUMio/LkOR2KeYYJ/g+hefB5myfhKSccxFUJazvAriw1mXJLGme6dtit2oBaLoyfLGW8MCUiNWx5HaABQrImjuL950ewZqgpDgo3BWTAXHPb+lRWwGfnhPOHiEC4DOhuDszjI0XqPUpoL9uP8/krl9GRiqnP065urEQoGwNBUPzeRxlWKHGFZ3uv+6aAcpt6Ca3f1+ooVbG6MF9UuTaydlubHHudmqSEJwf+XqHHe6g6e4uXYTdRGPLlwTWS7I7Gbm99GSflxBy0hDO3Wwm+KIM1/ne1oFIcDsjZmMG9so51T05+slSwaDHTw4bjkaHrBKqUmv3xIknng==',
#         t: '1680279841.299000',
#         m: 'rkHy0xDgG+60wPMtZtt/nGdMxMA/CUZ8oGCGqpyqXLM=',
#         i1: 'pLC5u2Lpcq0h7IqkXQzSdQ==',
#         i2: 'p6ebrIonfCEL5FnQBgA8MQ==',
#         zh: 'T/JxUjpuWeWK+fj6ayplweTZyX9WBvH3xvGe0/06nzI=',
#         uh: 'y0+1o8Xr6aVFFJfWxoQDNUQiYfBduZoa/bebz7EkyRM=',
#         hh: 'sQyZuCxosvvirVF0qmh06UMryKlK/Zt34zL7NfLMCE0=',
#     }
# }


# -*- coding=utf-8 -*-
import os
import sqlite3

import keyring
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

# for windows
# my_pass = keyring.get_password('Chrome Safe Storage', 'Chrome')
# my_pass = my_pass.encode('utf8')
# iterations = 1003
cookie_file = os.path.expanduser(r'C:\Users\11390\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies')


# for mac
# my_pass = keyring.get_password('Chrome Safe Storage', 'Chrome')
# my_pass = my_pass.encode('utf8')
# iterations = 1003
# cookie_file = os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/Cookies')

# for linux
# my_pass = 'peanuts'.encode('utf8')
# iterations = 1
# cookie_file = cookie_file or os.path.expanduser('~/.config/chromium/Default/Cookies')

salt = b'saltysalt'
length = 16
iv = b' ' * length


def expand_str(token):
    token_len = len(token)
    expand_len = (token_len // length + 1) * length - token_len
    return token.encode('ascii') + b'\x0c' * expand_len


def aes_encrypt(token):
    key = PBKDF2(my_pass, salt, length, iterations)
    cipher = AES.new(key, AES.MODE_CBC, IV=iv)
    enc_token = cipher.encrypt(token)
    return b'v10' + enc_token


def aes_decrypt(token):
    key = PBKDF2(my_pass, salt, length, iterations)
    cipher = AES.new(key, AES.MODE_CBC, IV=iv)
    dec_token = cipher.decrypt(token)
    return dec_token


def query_cookies():
    with sqlite3.connect(cookie_file) as conn:
        # result = conn.execute("select host_key, name, encrypted_value from cookies where host_key = '.800xsw.net'").fetchall()
        result = conn.execute("select host_key, name, encrypted_value from cookies where name='cf_clearance';").fetchone()
    return result


def write_cookies(enc_token):
    with sqlite3.connect(cookie_file) as conn:
        b = sqlite3.Binary(enc_token)
    sql = """update cookies set encrypted_value = ? where name = 'remember_token'"""
    conn.execute(sql, (b,))


def change_user(token):
    # write_cookies(ase_encrypt(expand_str(token)))
    pass

print(query_cookies())
