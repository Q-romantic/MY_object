# -*- coding: utf-8 -*-
"""
@Time    : 2022/11/5  005 下午 14:23
@Author  : Jan
@File    : 20221105_深圳市房屋租赁参.py
"""

import requests
from working.all_tools.tools import getua

""" {} """

headers = {
    "Content-Type": "application/json",
    "Cookie": "JSESSIONID=FXlGcaUlJ5reAI3x5yuMBQhfqmNX5B8Fblddhxf_RmL87x1AHBYN!-783501919; session-cookie=83787257",
    # "Host":"zjj.sz.gov.cn",
    # "Origin":"https://zjj.sz.gov.cn",
    # "Pragma":"no-cache",
    "Referer": "https://zjj.sz.gov.cn/fwzljgcx/vue/list",
    "User-Agent": getua(),
    "X-CSRF-TOKEN": "d861b6fd-293a-4813-822c-fd00e6868720",
    "X-Requested-With": "XMLHttpRequest"
}
url = 'https://zjj.sz.gov.cn/fwzljgcx/pgsj/rentRefer/communityPage'
data = {"area": "", "page": 1, "rows": 20, "searchText": "", "street": ""}

response = requests.post(url, headers=headers, json=data)
data = response.json()
# print(data)
# print(response)
for li in data["data"]["list"]:
    districtname = li["districtname"]
    zoneNo = li["zoneNo"]
    communityName = li["communityName"]
    multiRent = li["multiRent"]
    highRent = li["highRent"]
    lowRent = li["lowRent"]
    print(districtname, zoneNo, communityName, multiRent, highRent, lowRent, )
    # break
