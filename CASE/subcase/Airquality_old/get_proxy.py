# -*- coding: utf-8 -*-
"""
@Time    : 2022/6/26  026 上午 11:39
@Author  : Jan
@File    : get_proxy.py
"""
import parsel
import requests
import pprint

""" {} """

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36"}

import sys
import time
import hashlib

# 个人中心获取orderno与secret 如果不用代理则不用设置
orderno = ""
secret = ""


def get_proxy():
    ip = "dynamic.xiongmaodaili.com"
    port = "8089"
    _version = sys.version_info
    print(_version)
    is_python3 = (_version[0] == 3)
    ip_port = ip + ":" + port
    timestamp = str(int(time.time()))  # 计算时间戳
    txt = ""
    txt = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp
    if is_python3:
        txt = txt.encode()
    md5_string = hashlib.md5(txt).hexdigest()  # 计算sign
    sign = md5_string.upper()  # 转换成大写
    auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp
    proxy = {"http": "http://" + ip_port}
    # headers = {"Proxy-Authorization": auth}
    return auth



# print(get_proxy())
# 动态代理
# headers, proxies = get_proxy()
# proxies = {}
# proxies = get_proxy()[1]
# for i in range(1, 2):
#     url = 'https://spa1.scrape.center/api/movie/'
#     params = {
#         'limit': 10,
#         'offset': (i - 1) * 10,
#     }
#     resp = requests.get(url, params=params, proxies=proxies)
#     print(resp.status_code, resp.url)
#     # print(resp.text)
#     pprint.pprint(resp.json())
#
# defult_data = "{'result':'{'data':'{'items':''}'}'}"
# target_type = ['time_point', 'aqi', 'pm2_5', 'pm10', 'so2', 'no2', 'co', 'o3', 'rank', 'quality']

# years = [str(i + 2013) for i in range(10)]  # 列表推导式得到年份数据
# month = [str(i if i > 9 else '0' + str(i)) for i in range(1, 13)]  # 列表推导式得到月份数据
# print(years)
# print(month)
# years_month = [201312]
# for year in range(2013, 2022):
#     for month in range(0, 12):
#         years_month.append("%d%02d" % (year + 1, month + 1))
# print(years_month)
