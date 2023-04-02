# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/7  007 上午 11:42
@Author  : Jan
@File    : 拼多多课堂.py
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

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
proxies = {}

# url = 'https://www.mv-voice.com/news/2023/03/05/man-arrested-in-mountain-view-in-connection-with-2020-sexual-assault-of-child'
# url = 'https://www.mv-voice.com/news/2021/05/04/mountain-view-whisman-students-sent-home-after-children-test-positive-for-covid-19'
# response = requests.get(url, headers=headers, params={}, data={}, proxies=proxies)
# data = response.text
# print(data)
# print(response)
# sel = parsel.Selector(response.text)
# a = sel.xpath('//div[@id="u1"]/a/text()').getall()
# print(a)
# xml = etree.HTML(response.text)
# b = xml.xpath('//div[@id="s-top-left"]/a/@target')
# print(b





import cloudscraper
from lxml.html import fromstring
scraper = cloudscraper.create_scraper()
url = 'https://www.mv-voice.com/news/2021/05/04/mountain-view-whisman-students-sent-home-after-children-test-positive-for-covid-19'
# url = 'https://wallhere.com/' # 有人机检查验证

response = scraper.get(url, headers=headers, params={}, data={}, proxies=proxies)
# print(response.text)
sel = fromstring(response.text)
a = sel.xpath('//div[@class="text-block"]//p/text()')
print(a)












































