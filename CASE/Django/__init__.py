# -*- coding: utf-8 -*-
"""
@Time    : 2022/11/2  002 下午 14:24
@Author  : Jan
@File    : __init__.py.py
"""

import requests
from working.all_tools.tools import getip
from working.all_tools.tools import getua

""" {} """

headers = {
    "User-Agent": getua(),
    
}
proxies = {
    'http': 'http://' + getip(),
    'https': 'http://' + getip(),
}

url = ''



response = requests.get(url, headers=headers, params={}, data={}, proxies=proxies)
data = response.text
print(data)
print(response)
























































