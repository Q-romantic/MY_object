# -*- coding: utf-8 -*-
"""
@Time    : 2022/7/5  005 下午 13:06
@Author  : Jan
@File    : 智联招聘.py
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
    # 'https': 'https://' + getip(),
}

url = ''



response = requests.get(url, headers=headers, params={}, data={})
data = response.text
print(data)
print(response)
























































