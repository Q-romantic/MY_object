# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/7  007 下午 18:26
@Author  : Jan
@File    : 机票信息查询.py
"""
import time

""" {} """

import requests

# headers = {
#     "origin":"https://www.airasia.cn",
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
# }
# url = 'https://ssor.airasia.com/config/v2/clients/by-origin'
# response = requests.get(url, headers=headers)
# data = response.json()
# # print(data)
# # print(response)
# apikey = data['apiKey']
# print(apikey)


# url = 'https://astg.widerplanet.com/delivery/storage'
# response = requests.get(url, headers=headers)
# # print(response)
# print(response.cookies)


# url = 'https://track.airasia.com/com.snowplowanalytics.snowplow/tp2'
# response = requests.get(url, headers=headers)
# # print(response)
# print(response.cookies)


import base64
import json
from datetime import datetime, timedelta

payload = {
    'iss': '45z6lwBVohUEGSZyF7ZDJH8WYA6vnRVr',
    'aud': 'pwa-search',
    'exp': str(time.mktime((datetime.now() + timedelta(minutes=30)).timetuple())),  # 令牌过期时间
    'sub': '8bf131fb-382a-4a88-9c1e-9494cd787ebf'
}
encoded_jwt = 'ew0KCSJhbGciIDogIk5vbmUiLA0KCSJ0eXAiIDogImp3dCINCn0.' + base64.b64encode(json.dumps(payload).encode()).decode().replace('=', '')


# encoded_jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDM5MzA0NzMsInVzZXJuYW1lIjoiQmlnRmlzaCJ9.5eM02YL0xg1DiMZjx-muuYXahTm2etGOEeixFYYd7iI"
# x = jwt.decode(encoded_jwt,key='',verify=True,  algorithms=['HS256'])
# print(x)


def get_data(encoded_jwt):
    headers = {"authorization": f"Bearer {encoded_jwt}"}
    url = 'https://k.airasia.cn/shopprice-n/api/v4/pricesearch/0/1/HKT/BKK/2024-02-04/1/0/0'
    response = requests.get(url, headers=headers)
    data = response.text
    print(data)


get_data(encoded_jwt)

# start_time = time.time()
#
# from seleniumwire import webdriver
# from seleniumwire.webdriver import ChromeOptions
#
# url = 'https://www.airasia.cn/select/en/gb/HKT/BKK/2024-02-04/N/1/0/0/O/N/CNY/ST'
#
# chrome_options = ChromeOptions()
# chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 消除警告提示"Chrome 正在受自动化测试软件控制的控制。"
# chrome_options.add_argument('--start-maximized')  # 界面窗口最大化
# chrome_options.add_argument('--headless')  # 设置chrome浏览器无界面模式(设置无头浏览器)
#
# browser = webdriver.Chrome(options=chrome_options)
# browser.maximize_window()  # 界面窗口最大化
#
#
#
# browser.get(url)
# time.sleep(10)
#
# print('----------------------------------')
#
#
# # content = browser.page_source
# # print(content)
# for res in browser.requests:
#     authorization = res.headers.get('authorization')
#     if isinstance(authorization, str):
#         authorization = authorization.replace('Bearer ', '')
#         try:
#             get_data(authorization)
#         except:
#             print('error')
#
# end_time = time.time() - start_time
# print(end_time)


# l='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVuZElkIjoiMTIzNDU2IiwiaWF0IjoxNjY5NzE1MTY5NzMwLCJleHAiOjE2Njk3MjIzNjk3MzB9.HOxtQuxMgEplqJT2zcowttMlutS4Wd-Q73HWUygzrts'
# x = jwt.decode(l,key='code2022',algorithms=['HS256'])
# print(x)
# print('ok')


