# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/27  027 下午 19:00
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
proxies = {}





headers = {
    "cookie":"_zap=4a73667f-19da-4a94-8f71-45e5cbfb8723; _xsrf=e79b9b1b-5d15-4322-beac-c939f8a65d3c; d_c0=AFCWj1CzZBaPTlHmJKsFaiS1fveeFJ_8P8U=|1677495014; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1677495014; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1677495014; KLBRSID=ed2ad9934af8a1f80db52dcb08d13344|1677495015|1677495013; arialoadData=false",
    "pragma":"no-cache",
    "referer":"https://www.zhihu.com/search?type=content&q=%E6%BB%B4%E6%BB%B4",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "x-ab-pb":"ClIbAD8ARwC0AGkBagF0ATsCzALXAtgCtwPWBBEFUQWLBYwFngUxBusGJwd0CHkIYAn0CUkKawq+CkMLcQuHC40L1wvgC+UL5gtxDI8MrAzDDPgMEikAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAA==",
    "x-api-version":"3.0.91",
    "x-app-za":"OS=Web",
    "x-requested-with":"fetch",
    "x-zse-93":"101_3_3.0",
    "x-zse-96":"2.0_4dJ8Kt=QWPqLWQRPuyZtSHe0vpcSLRkDlpQxqkrXjIVwfzp8Ll3V92BR/ImDTs4S"
}

params = {
    "gk_version":"gz-gaokao",
    "t":"general",
    "q":"滴滴",
    "correction":"1",
    "offset":"0",
    "limit":"20",
    "filter_fields":"lc_idx: 0",
    "show_all_topics":"0",
    "search_source":"Normal"
}




url = 'https://www.zhihu.com/api/v4/search_v3?gk_version=gz-gaokao&t=general&q=%E6%BB%B4%E6%BB%B4&correction=1&offset=0&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal'
response = requests.get(url, headers=headers, params={}, data={}, proxies=proxies)
data = response.text
print(data)
print(response)
# sel = parsel.Selector(response.text)
# a = sel.xpath('//div[@id="u1"]/a/text()').getall()
# print(a)
# xml = etree.HTML(response.text)
# b = xml.xpath('//div[@id="s-top-left"]/a/@target')
# print(b)





































































