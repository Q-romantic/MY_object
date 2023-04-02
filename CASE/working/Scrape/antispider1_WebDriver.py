# -*- coding: utf-8 -*-
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

""" 对接 WebDriver 反爬，检测到使用 WebDriver 就不显示页面，适合用作 WebDriver 反爬练习。 """
""" 提示：没搞懂题意？？？ """

for i in range(1, 11):
    url = f'https://antispider1.scrape.center/api/movie/?limit=10&offset={(i - 1) * 10}'
    # driver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])  # 消除警告提示"Chrome 正在受自动化测试软件控制的控制。"
    # chrome_options.add_argument('--start-maximized')    # 界面窗口最大化
    chrome_options.add_argument('--headless') # 设置chrome浏览器无界面模式(设置无头浏览器)
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument(f'user-agent={ua}')   # 指定UA
    # chrome_options.add_argument(f'--proxy-server=http://{ip}:port"')  # 代理
    browser = webdriver.Chrome(options=chrome_options)
    # browser.maximize_window()   # 界面窗口最大化
    # 开始请求
    browser.get(url)
    # 打印页面源代码
    print(browser.page_source)
    # 关闭浏览器
    # browser.close()
    # 关闭chreomedriver进程
    # browser.quit()
    break

print('---' * 30)

# from selenium import webdriver
# from selenium.webdriver import ChromeOptions
#
# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 消除警告提示"Chrome 正在受自动化测试软件控制的控制。"
# # option.add_experimental_option('useAutomationExtension', False)
# # option.add_argument('--headless')
# browser = webdriver.Chrome(options=option)
# # browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
# #     'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
# # })
# for i in range(1, 11):
#     url = f'https://antispider1.scrape.center/api/movie/?limit=10&offset={(i - 1) * 10}'
#     browser.get(url)
#     data = browser.page_source
#     print(data)
#     break
