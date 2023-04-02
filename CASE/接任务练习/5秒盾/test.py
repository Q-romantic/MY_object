# -*- coding: utf-8 -*-
"""
@Time    : 2023/4/2  002 下午 13:46
@Author  : Jan
@File    : test.py
"""

""" {} """

from pycookiecheat import chrome_cookies
import requests

url = 'https://m.800xsw.net/modules/article/search.php?searchtype=articlename&searchkey=%CE%D2%B5%C4&t_btnsearch='

# Uses Chrome's default cookies filepath by default
cookies = chrome_cookies(url)
# r = requests.get(url, cookies=cookies)
print(cookies)





































































