# -*- coding: utf-8 -*-
"""
@Time    : 2022/6/26  026 下午 16:53
@Author  : Jan
@File    : main.py
"""
import base64
import json
import re
import urllib.parse
from jsmin import jsmin
import execjs
import requests
import pprint
from lxml import etree


""" {参考：https://github.com/Crack-DanShiFu/apiStudy} """

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36"}
# proxy = {"https": f"http://115.226.155.112:41699"}
with open(f'C:\Y\Case\subcase\疫情大数据\ip.txt', mode='r') as f:
    proxy = {"https": f"http://{f.read()}"}


def get_citys():
    city_url = 'https://www.aqistudy.cn/historydata/'
    html_info = requests.get(city_url, headers=headers, proxies=proxy, timeout=3)
    html = etree.HTML(html_info.text)  # 初始化生成一个XPath解析对象
    items = html.xpath('//div[@class="all"]//a/text()')
    print(items)
    return items


def get_city_data():
    city_url = 'https://www.aqistudy.cn/historydata/'
    html_info = requests.get(city_url, headers=headers, proxies=proxy, timeout=3)
    result = []
    html = etree.HTML(html_info.text)  # 初始化生成一个XPath解析对象
    items = html.xpath('//div[@class="all"]//ul[@class="unstyled"]')
    for i in items:
        cityName = i.xpath('div/li/a/text()')
        first_letter = i.xpath('div/b/text()')
        for c in cityName:
            result.append([c, first_letter[0][:-1]])
    for k, v in enumerate(result):
        result[k].append(k)
    print(result)
    return result


def get_month_info_by_city(url):
    info = re.findall('city=(.*?)&month=(.*)', url)[0]
    city = urllib.parse.unquote(info[0])
    response = requests.get(url, headers=headers, proxies=proxy, timeout=3)
    data = response.text
    # print(data)
    head_url = 'https://www.aqistudy.cn/historydata/'
    main_js_urls = re.findall('<script type="text/javascript" src="(.*?)"></script>', data)  # xpath:'/html/body/script[2]'
    # print(main_js_urls)
    main_js_url = head_url + main_js_urls[1]
    response = requests.get(main_js_url, headers=headers)
    data = response.text
    data = data.replace('eval', '')
    data = execjs.eval(data)
    # print(data)
    if 'dweklxde(' in data:
        str_count = data.count('dweklxde')
        # print(str_count)
        data = re.findall("\'(.*?)\'", data)[0]
        # print(data)
        while str_count:
            data = base64.b64decode(data)
            str_count -= 1
        data = jsmin(data.decode())
    params_name = re.search('data:\{(.*?):(.*?)\},', data)
    params_key = params_name.group(1)
    params_value = params_name.group(2)
    encode_fn_name = re.findall('if\(!.*?\)\{var .*?=(.*?)\(', data)[0]

    method = "GETDAYDATA"
    str_object = {"city": city, "month": month}
    with open('1.js', mode='r') as f1:
        data1 = f1.read()
    data = data1 + data
    params = {
        params_key: execjs.compile(data).call(encode_fn_name, method, str_object)
    }
    print(params)
    # print(params_key, params_value, encode_fn_name)

    name = re.findall('success:function\((.*?)\)\{', data)[0]
    decode_fn_name = re.findall(f'success:function\({name}\).*{name}=(.*?)\({name}\);', data)[0]
    # print(name)
    # print(decode_fn_name)

    data_url = 'https://www.aqistudy.cn/historydata/api/historyapi.php'
    response = requests.post(data_url, headers=headers, data=params, proxies=proxy, timeout=3)
    last_data = response.text
    print(last_data)
    data = execjs.compile(data).call(decode_fn_name, last_data)
    data = json.loads(data)
    # pprint.pprint(data)
    for i in data['result']['data']['items']:
        i['city'] = city
        print(i)
        # break


if __name__ == '__main__':
    city = '神农架林区'
    month = '202112'
    url = f'https://www.aqistudy.cn/historydata/daydata.php?city={city}&month={month}'
    get_month_info_by_city(url)  # 'https://www.aqistudy.cn/historydata/daydata.php?city=神农架林区&month=202112'
