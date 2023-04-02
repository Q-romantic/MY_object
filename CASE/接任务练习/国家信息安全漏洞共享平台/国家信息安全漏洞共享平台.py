# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/23  023 上午 2:15
@Author  : Jan
@File    : 国家信息安全漏洞共享平台.py
"""
import random
import re
import socket
import time
import execjs
import parsel
import requests
import pandas as pd
from threading import Thread
from threading import Lock
from multiprocessing import Process
from working.all_tools.tools import get_ua

""" {} """

N = 0  # 累计访问次数
m = 100  # 重置 N ，即单个代理 ip 使用次数
timeout = 10
threadLock = Lock()


# socket.setdefaulttimeout(timeout)  # 设置socket层的超时时间为10秒


def get_proxies():
    api_url = "http://v2.api.juliangip.com/dynamic/getips?city_code=1&city_name=1&filter=1&ip_remain=1&num=1&pt=1&result_type=json&trade_no=1727174320704510&sign=611c92295f7a001bbecaedf800064d33"
    ips = requests.get(api_url).json()["data"]["proxy_list"][0].split(",")[0]
    proxies = {'http': 'http://' + ips, 'https': 'http://' + ips}
    while True:
        try:
            url = 'https://www.baidu.com'
            res = requests.get(url, proxies=proxies, timeout=timeout)
            if res.status_code == 200:
                return proxies
        except:
            pass


proxies = get_proxies()


def _proxies():
    global N, proxies
    N += 1
    # print(N, proxies)
    if N < m: return proxies  # 可能，也许，大概，单个代理 ip 最大可用次数为 m = 10
    N = 0
    proxies = get_proxies()
    return proxies


class ChinaNationalVulnerabilityDatabase:
    # 定义类变量
    # 记录第一个被创建对象的引用，代表着类的私有属性
    _instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __init__(self, headers, proxies):
        # 使用类名调用类变量,不能直接访问。
        if ChinaNationalVulnerabilityDatabase.init_flag:
            return
        # 理论上只需生成一次该 cookies
        self.homepage = 'https://www.cnvd.org.cn'
        self.cookies = self.get_cookies(self.homepage, headers, proxies)
        # print(self.proxies, self.cookies)
        # 修改类属性的标记
        ChinaNationalVulnerabilityDatabase.init_flag = True

    def __new__(cls, *args, **kwargs):
        # 判断该类的属性是否为空；对第一个对象没有被创建，我们应该调用父类的方法，为第一个对象分配空间
        if cls._instance == None:
            # 把类属性中保存的对象引用返回给python的解释器
            cls._instance = object.__new__(cls)
        # 如果cls._instance不为None,直接返回已经实例化了的实例对象
        return cls._instance

    def get_cookies(self, url, headers, proxies):
        response = requests.get(url, headers=headers, proxies=proxies, timeout=timeout)
        response.close()
        res = response.text
        cookies = response.cookies
        # print(cookies)
        __jsl_clearance_s = execjs.eval(res[24:-57]).split(';')[0].split('=')[1]
        cookies.update({"__jsl_clearance_s": __jsl_clearance_s})
        # print(cookies)
        response = requests.get(url, headers=headers, proxies=proxies, cookies=cookies, timeout=timeout)
        response.close()
        res = response.text
        # print(res)
        # print(res[8:-9])

        # # 主要验证如下正则表达式是否通用 '}};var (.*?)=.*(\)\]\);if)'
        # if "__jsl_clearance_s" in res:
        #     threadLock.acquire()
        #     with open('111.js', mode='a', encoding='utf-8') as f:
        #         f.write(res[8:-9])
        #         f.write('\n')
        #     threadLock.release()
        # else:
        #     print('error')

        fn = res[8:-9].replace('"', "'")
        # print(fn)
        value, location = re.findall('}};var (.*?)=.*(\)\]\);if)', fn, re.S)[0]
        # print(value, location)
        fn = re.sub('\)\]\);if', f')]);console.log({value}[0]);window.out={value}[0];if', fn)  # 这里可以是 window/this/global 均指的全局变量
        windows = "window=global;location={};document={cookie:''};navigator={'appCodeName':'','appName':'','userAgent':''};"
        fn = windows + fn + ";return window.out;"

        __jsl_clearance_s = execjs.exec_(fn)
        cookies.update({"__jsl_clearance_s": __jsl_clearance_s})
        # print(__jsl_clearance_s)
        # print(cookies)
        return cookies

    def get_titles_and_hrefs(self, url, page, headers, proxies):
        # x 翻页，是从 0 开始
        params = {
            "number": "请输入精确编号",
            "startDate": "",
            "endDate": "",
            "field": "",
            "order": "",
            "numPerPage": 10,
            "offset": page * 10,
            "max": 10
        }
        response = requests.post(url, headers=headers, params=params, proxies=proxies, cookies=self.cookies, timeout=timeout)  # 请求完后服务器会清除 cookie
        response.close()
        # print(response.text)
        # print(response.status_code, cookies)
        sel = parsel.Selector(response.text)
        hrefs = sel.xpath('//tbody/tr/td[1]/a/@href').getall()
        titles = sel.xpath('//tbody/tr/td[1]/a/@title').getall()
        ranks = sel.xpath('//tbody/tr/td[2]/text()').getall()
        nums = sel.xpath('//tbody/tr/td[3]/text()').getall()
        dates = sel.xpath('//tbody/tr/td[6]/text()').getall()
        for title, href, rank, num, date in zip(titles, hrefs, ranks, nums, dates):
            title = title.strip()
            href = "https://www.cnvd.org.cn" + href
            rank = rank.strip()
            num = num.strip()
            date = date.strip()
            print(page, '--->', title, href, rank, num, date)
        print(page, '--->', response.url)
        # return hrefs

    def get_detail(self, detail_url, headers, proxies):
        response = requests.get(detail_url, headers=headers, proxies=proxies, cookies=self.cookies, timeout=timeout)
        response.close()
        html_table = re.search('(<table class="gg_detail">.*?</table>)', response.text, re.S).group()
        return html_table

    def save_to_execl(self, html_table):
        tables = pd.read_html(html_table)
        table = pd.DataFrame(tables[0])
        table.to_csv('123.csv', mode='a', header=False, index=False)
        # table.to_excel('123.xlsx', mode='a', header=False, index=False)


# 多线程
class MyThread(Thread):
    def __init__(self, page, headers, proxies):
        Thread.__init__(self)
        self.page = page
        self.headers = headers
        self.proxies = proxies

    def sub(self, detail_url, headers, proxies):
        try:
            detail_url = "https://www.cnvd.org.cn" + detail_url
            # print(detail_url)
            html_table = self.cnvd.get_detail(detail_url, headers, proxies)
            # print(html_table)
            # self.cnvd.save_to_execl(html_table)
        except:
            headers = {"User-Agent": get_ua(), "Host": "www.cnvd.org.cn"}
            self.sub(detail_url, headers, proxies)

    def main(self, page, headers, proxies):
        try:
            self.cnvd = ChinaNationalVulnerabilityDatabase(headers, proxies)
            url = 'https://www.cnvd.org.cn/flaw/list?flag=true'
            detail_urls = self.cnvd.get_titles_and_hrefs(url, page, headers, proxies)
            # for detail_url in detail_urls:
            #     Thread(target=self.sub, args=(detail_url,)).start()
        except:
            headers = {"User-Agent": get_ua(), "Host": "www.cnvd.org.cn"}
            self.main(page, headers, proxies)

    def run(self):
        self.main(self.page, self.headers, self.proxies)


if __name__ == '__main__':
    pages = 2
    for i in range(1, pages + 1):
        # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.35"}
        headers = {"User-Agent": get_ua(), "Host": "www.cnvd.org.cn"}
        proxies = _proxies()
        print(headers, proxies)
        MyThread(i, headers, proxies).start()
        # time.sleep(random.random())
