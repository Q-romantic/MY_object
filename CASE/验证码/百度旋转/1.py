# -*- coding: utf-8 -*-
"""
@Time    : 2023/7/1  001 下午 21:43
@Author  : Jan
@File    : 1.py
"""

""" {} """

__author__ = "dengxinyan"

import os
import sys
import time
import base64
import requests
from PIL import Image
from io import BytesIO

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# PIL图片保存为base64编码
def PIL_base64(img, coding='utf-8'):
    img_format = img.format
    if img_format == None:
        img_format = 'JPEG'

    format_str = 'JPEG'
    if 'png' == img_format.lower():
        format_str = 'PNG'
    if 'gif' == img_format.lower():
        format_str = 'gif'

    if img.mode == "P":
        img = img.convert('RGB')
    if img.mode == "RGBA":
        format_str = 'PNG'
        img_format = 'PNG'

    output_buffer = BytesIO()
    # img.save(output_buffer, format=format_str)
    img.save(output_buffer, quality=100, format=format_str)
    byte_data = output_buffer.getvalue()
    base64_str = 'data:image/' + img_format.lower() + ';base64,' + base64.b64encode(byte_data).decode(coding)

    return base64_str


# 根据链接下载旋转图片
def get_img(url):
    header = {
        # "Host": "passport.baidu.com",
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
        # "Accept": "image/avif,image/webp,*/*",
        # "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        # "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://wappass.baidu.com/",
        # "Connection": "keep-alive",
        "Cookie": "BAIDUID=7999A864ECB04BF96DC42141762CF08C:FG=1; BIDUPSID=310DBCE84D6A8388D88171F49E098D2D; PSTM=1634536706; BDRCVFR[gltLrB7qNCt]=mk3SLVN4HKm; delPer=0; PSINO=7; H_PS_PSSID=34837_34439_34067_31254_34741_34525_34584_34504_34706_34806_34578_26350_34725_22158_34691_34671; BDORZ=FFFB88E999055A3F8A630C64834BD6D0",
        # "Sec-Fetch-Dest": "image",
        # "Sec-Fetch-Mode": "no-cors",
        # "Sec-Fetch-Site": "same-site",
        # "Pragma": "no-cache",
        # "Cache-Control": "no-cache",
    }
    response = requests.get(url=url, headers=header)
    print('response.text')

    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))

    # 将图片转换成base64字符串并返回
    return PIL_base64(img)


# 识别
def shibie(base64_img):
    url = "http://www.detayun.cn/tool/verify_code_identify/"
    header = {
        "Host": "www.detayun.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Referer": "http://www.detayun.cn/tool/verifyCodeIdentifyPage/?verify_idf_id=9",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": "134652",
        "Origin": "http://www.detayun.cn",
        "Connection": "keep-alive",
        # "Cookie": 'Hm_lvt_3eecc7feff77952670b7c24e952e8773=1664376578,1664414757,1664465147,1664498440; token="MTY2NDUwMjAzOS42MTc4NTI6ZGYyZDhkMjRmNWYwZTE4OTFiZTY2N2QyNDQ1NDUwNzFiZGQ3ODRhNw=="; sessionid=ciivpb8w0uyoj8xpd4pnp1vqxjehvdxm; Hm_lpvt_3eecc7feff77952670b7c24e952e8773=1664498440',
        "Cookie": 'Hm_lvt_3eecc7feff77952670b7c24e952e8773=1688221232; token="MTY4ODIyNTAyNy4yOTgwMjY6YWY2OTgzYTk0MWVjNzRiMGViNjVjNzk3YTk4NjU2NWIwOWNhMDg3MQ=="; sessionid=gud09guwf2nlrb9oole4i0gvb73cghi5; Hm_lpvt_3eecc7feff77952670b7c24e952e8773=1688221434',
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
    }
    data = {
        'verify_idf_id': '16',
        'img_base64': base64_img,
        'words': '',
    }
    response = requests.post(url=url, headers=header, data=data)
    print(response.json())
    if response.json()['code'] == 401:
        print('请登录识别账号，更新Cookie。登录地址：http://www.detayun.cn/account/loginPage/')
        return

    return int(str(response.json()['data']['res_str']).replace('顺时针旋转', '').replace('度', ''))


if __name__ == '__main__':
    # 加载防检测js
    # with open('.\webdriver\stealth.min.js') as f:
    #     js = f.read()

    s = Service(r'C:\360安全浏览器下载\chromedriver_win32\chromedriver.exe')
    # s.command_line_args()
    # s.start()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])  # 消除警告提示"Chrome 正在受自动化测试软件控制的控制。"

    # driver = webdriver.Chrome(executable_path=r'C:\360安全浏览器下载\chromedriver_win32\chromedriver.exe', options=options)
    driver = webdriver.Chrome(service=s, options=options)

    # driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    #     "source": js
    # })
    # 访问百度首页
    driver.get(
        'https://wappass.baidu.com/static/captcha/tuxing.html?&ak=c27bbc89afca0463650ac9bde68ebe06&backurl=https%3A%2F%2Fwww.baidu.com%2Fs%3Fcl%3D3%26tn%3Dbaidutop10%26fr%3Dtop1000%26wd%3D%25E6%25B6%2588%25E9%2598%25B2%25E6%2588%2598%25E5%25A3%25AB%25E8%25BF%259E%25E5%25A4%259C%25E7%25AD%2591%25E5%259D%259D%25E5%25BA%2594%25E5%25AF%25B9%25E6%25B4%25AA%25E5%25B3%25B0%25E8%25BF%2587%25E5%25A2%2583%26rsv_idx%3D2%26rsv_dl%3Dfyb_n_homepage%26hisfilter%3D1&logid=8309940529500911554&signature=4bce59041938b160b7c24423bde0b518&timestamp=1624535702')
    # time.sleep(10000)
    # 等待滑块出现
    WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '//div[@class="passMod_slide-btn "]'))
    yzm_button = driver.find_element(By.XPATH, '//div[@class="passMod_slide-btn "]')
    time.sleep(1)

    # 等待验证码出现
    WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '//img'))
    img_src = driver.find_element(By.XPATH, '//img').get_attribute('src')
    print(img_src)
    # 下载图片并转化为base64
    img_base64 = get_img(img_src)
    # 识别图片旋转角度
    move_x = shibie(img_base64)
    # 通过旋转角度 * 滑动系数 = 滑动距离
    move_x = move_x * ((290 - 46 - 2 * 3) / 360)
    # 开始滑动
    action = ActionChains(driver)
    action.click_and_hold(yzm_button).perform()  # 鼠标左键按下不放
    action.move_by_offset(move_x, 0).perform()
    action.release().perform()  # 释放鼠标

    time.sleep(2)

    # 第二次滑动
    # 等待滑块出现
    WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '//div[@class="passMod_slide-btn "]'))
    yzm_button = driver.find_element(By.XPATH, '//div[@class="passMod_slide-btn "]')
    time.sleep(1)

    # 等待验证码出现
    WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '//img'))
    img_src = driver.find_element(By.XPATH, '//img').get_attribute('src')
    # 下载图片并转化为base64
    img_base64 = get_img(img_src)
    # 识别图片旋转角度

    move_x = shibie(img_base64)
    # 通过旋转角度 * 滑动系数 = 滑动距离
    move_x = move_x * ((290 - 46 - 2 * 3) / 360)
    # 开始滑动
    action = ActionChains(driver)
    action.click_and_hold(yzm_button).perform()  # 鼠标左键按下不放
    action.move_by_offset(move_x, 0).perform()
    action.release().perform()  # 释放鼠标

    time.sleep(2)
    print(driver.page_source)
