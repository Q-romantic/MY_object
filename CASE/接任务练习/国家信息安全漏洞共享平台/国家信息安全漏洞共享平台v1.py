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

""" { 最终判定为 UA 限制，检测拦截多次访问 } """

N = 0  # 累计访问次数
m = 100  # 重置 N ，即单个代理 ip 使用次数
timeout = 10
threadLock = Lock()
socket.setdefaulttimeout(timeout)  # 设置socket层的超时时间为10秒


def get_proxies():
    api_url = "http://v2.api.juliangip.com/dynamic/getips?city_code=1&city_name=1&filter=1&ip_remain=1&num=1&pt=1&result_type=json&trade_no=1727174320704510&sign=611c92295f7a001bbecaedf800064d33"
    ips = requests.get(api_url).json()["data"]["proxy_list"][0].split(",")[0]
    proxies = {'http': 'http://' + ips, 'https': 'http://' + ips}
    while True:
        try:
            url = 'https://www.baidu.com'
            res = requests.get(url, proxies=proxies)
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


def get_cookies(url, headers, proxies):
    response = requests.get(url, headers=headers, proxies=proxies, timeout=timeout, verify=False)
    # print(headers, proxies)
    response.close()
    res = response.text
    cookies = response.cookies
    # print(cookies)
    __jsl_clearance_s = execjs.eval(res[24:-57]).split(';')[0].split('=')[1]
    cookies.update({"__jsl_clearance_s": __jsl_clearance_s})
    # print(cookies)
    response = requests.get(url, headers=headers, proxies=proxies, cookies=cookies, timeout=timeout, verify=False)
    # print(headers, proxies)
    response.close()
    res = response.text
    # print(res)
    # print(res[8:-9])

    # 主要验证如下正则表达式是否通用 '}};var (.*?)=.*(\)\]\);if)'
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


def get_titles_and_hrefs(url, page, cookies, headers, proxies):
    # x 翻页，是从 0 开始
    params = {
        "number": "请输入精确编号",
        "startDate": "",
        "endDate": "",
        "field": "",
        "order": "",
        "numPerPage": 100,  # 数值貌似不重要
        "offset": page * 100 - 100,
        "max": 100  # 最大可填写值 100
    }
    response = requests.post(url, headers=headers, params=params, proxies=proxies, cookies=cookies, timeout=timeout, verify=False)  # 请求完后服务器会清除 cookie
    # print(headers, proxies)
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

    # # 去除以获取数据页，写入当前还未获取到数据的页，由于写入数据量小，可以快写，不需要加同步锁
    # # threadLock.acquire()
    # global target
    # target.remove(page)
    # with open('111.txt', mode='w', encoding='utf-8') as f:
    #     f.write(str(target))
    # # threadLock.release()

    # return hrefs


def get_detail(detail_url, cookies, headers, proxies):
    response = requests.get(detail_url, headers=headers, proxies=proxies, cookies=cookies, timeout=timeout, verify=False)
    # print(headers, proxies)
    response.close()
    html_table = re.search('(<table class="gg_detail">.*?</table>)', response.text, re.S).group()
    return html_table


def save_to_execl(html_table):
    tables = pd.read_html(html_table)
    table = pd.DataFrame(tables[0])
    table.to_csv('123.csv', mode='a', header=False, index=False)
    # table.to_excel('123.xlsx', mode='a', header=False, index=False)


def main(page, headers, proxies):
    try:
        homepage = 'https://www.cnvd.org.cn'
        cookies = get_cookies(homepage, headers, proxies)
        url = 'https://www.cnvd.org.cn/flaw/list?flag=true'
        get_titles_and_hrefs(url, page, cookies, headers, proxies)
    except:
        headers = {"User-Agent": get_ua(), "Host": "www.cnvd.org.cn"}
        main(page, headers, proxies)


# # 如下可以解释在函数内部，一般用var声明的为局部变量，没用var声明的一般为全局变量
# sss = "function add(a,b){c=3;var d=4;return a+b+c+d;};x=add(1,2);console.log(x);return x,c;"
# out = execjs.exec_(sss)
# print(out)

# # 此方法没有返回值，不能赋值操作，且不能后面加 return
# cmd = 'node -e "function add(a,b){c=3;var d=4;return a+b+c+d;};x=add(1,2);console.log(x);"'
# out = os.system(cmd)
# print(out)

if __name__ == '__main__':
    pages = 2
    # 用于记录未成功获取数据页
    target = [i + 1 for i in range(pages)]
    for page in range(1, pages + 1):
        # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.35"}
        headers = {"User-Agent": get_ua(), "Host": "www.cnvd.org.cn"}
        proxies = _proxies()
        try:
            Thread(target=main, args=(page, headers, proxies)).start()
            # time.sleep(random.random())
        except:
            print('--------------------error--------------------->', page)
