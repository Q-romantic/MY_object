# -*- coding: utf-8 -*-
"""
@Time    : 2023/4/1  001 下午 13:10
@Author  : Jan
@File    : 3.py
"""
import time

""" {} """
import urllib.parse
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

key = "我的"
searchkey = urllib.parse.quote(key, encoding="GBK")
print(searchkey)
url = f'https://m.800xsw.net/modules/article/search.php?searchtype=articlename&searchkey={key}&t_btnsearch='

# from selenium import webdriver
# from selenium.webdriver import ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# chrome_options = ChromeOptions()
# chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 消除警告提示"Chrome 正在受自动化测试软件控制的控制。"
# chrome_options.add_argument('--start-maximized')  # 界面窗口最大化
# # chrome_options.add_argument('--headless')  # 设置chrome浏览器无界面模式(设置无头浏览器)
# ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
# chrome_options.add_argument(f'user-agent={ua}')   # 指定UA
#
# browser = webdriver.Chrome(options=chrome_options)
# browser.maximize_window()  # 界面窗口最大化
#
# browser.execute_cdp_cmd(
#     "Network.setUserAgentOverride",
#     {
#         "userAgent": browser.execute_script(
#             "return navigator.userAgent"
#         ).replace("Headless", "")
#     },
# )
# browser.execute_cdp_cmd(
#     "Page.addScriptToEvaluateOnNewDocument",
#     {
#         "source": """
#             Object.defineProperty(window, 'chrome', {
#                     get: () => {}
#             })"""
#     },
# )
# browser.execute_cdp_cmd(
#     "Page.addScriptToEvaluateOnNewDocument",
#     {
#         "source": """
#             Object.defineProperty(navigator, 'webdriver', {
#                     get: () => undefined
#             })"""
#     },
# )
# browser.execute_cdp_cmd(
#     "Page.addScriptToEvaluateOnNewDocument",
#     {
#         "source": """
#             Object.defineProperty(navigator, 'webdriver', {
#                     get: () => [1, 2, 3]
#             })"""
#     },
# )
# browser.execute_cdp_cmd(
#     "Page.addScriptToEvaluateOnNewDocument",
#     {
#         "source": """
#             Object.defineProperty(navigator, 'languages', {
#                     get: () => ['en-US', 'en']
#             })"""
#     },
# )
# browser.execute_cdp_cmd(
#     "Page.addScriptToEvaluateOnNewDocument",
#     {
#         "source": """
#         Object.defineProperty(Notification, 'permission', { get: () => "default"});
#         """
#     },
# )
#
# # browser.implicitly_wait(30)
# browser.get(url)
# # browser.get('https://baike.baidu.com/item/%E9%9B%85%E4%B8%87%E9%AB%98%E9%80%9F%E9%93%81%E8%B7%AF?fromtitle=%E9%9B%85%E4%B8%87%E9%AB%98%E9%93%81&fromid=18385773&fromModule=lemma_search-box')
#
# try:
#     # browser.find_element(By.XPATH, '//input[@type="checkbox"]').click()
#     # WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//label[@class="ctp-checkbox-label"]/span')))
#     element = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//input[@type="checkbox"]'))).click()
#     # element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@class="btn-list"]/a[@target="_blank"]')))
#     # element
# except:
#     pass
# time.sleep(20)
# print('----------------------------------')
# content = browser.page_source
# print(content)
#
# '//td[@id="cf-stage"]//label[@class="ctp-checkbox-label"]/input'
# # WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//td[@id="cf-stage"]//label[@class="ctp-checkbox-label"]/input'))).click()
#
#
# # //input[@type="checkbox"]





























































