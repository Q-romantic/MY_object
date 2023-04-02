# -*- coding: utf-8 -*-
"""
@Time    : 2022/6/23  023 下午 16:06
@Author  : Jan
@File    : 鲜花店.py
"""
import json
import re
import parsel
import pprint
import requests

""" {} """


def get_list():
    url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/1'
    for page in range(1, 6):
        headers = {
            # "Accept": "*/*",
            # "Accept-Encoding": "gzip, deflate, br",
            # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5",
            # "Cache-Control": "no-cache",
            # "Connection": "keep-alive",
            "Cookie": "uuid=300f1676c1a641409e64.1655864783.1.0.0; _lxsdk_cuid=181893b7455c8-0b237ed6c0e96f-623e5653-1fa400-181893b7455c8; ci=1; mtcdn=K; userTicket=HNPNLsLemxEVOnZIknZgTvwVnzumHHRnHLmdmLHf; _lxsdk=181893b7455c8-0b237ed6c0e96f-623e5653-1fa400-181893b7455c8; _hc.v=7399ea34-7a0c-a1a2-3e5b-cb55eddd14ee.1655864906; lat=40.061107; lng=116.584477; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; lt=_FrAa41JSZG1lC8MveTSi679ra0AAAAAexIAACp5n-SGG5r2U9aC0Bcoa1ENMAGQjVrBVOu1LkU9m0UAecE8eXsesn_crjNF6hX4_w; u=913901191; n=gAC776427767; token2=_FrAa41JSZG1lC8MveTSi679ra0AAAAAexIAACp5n-SGG5r2U9aC0Bcoa1ENMAGQjVrBVOu1LkU9m0UAecE8eXsesn_crjNF6hX4_w; unc=gAC776427767; firstTime=1655971235039; _lxsdk_s=1818fb4aa31-516-5b4-f72%7C%7C221",
            "Host": "apimobile.meituan.com",
            # "Origin": "https://bj.meituan.com",
            # "Pragma": "no-cache",
            "Referer": "https://bj.meituan.com/",
            # "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Microsoft Edge\";v=\"102\"",
            # "sec-ch-ua-mobile": "?0",
            # "sec-ch-ua-platform": "\"Windows\"",
            # "Sec-Fetch-Dest": "empty",
            # "Sec-Fetch-Mode": "cors",
            # "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36"
        }

        params = {
            "uuid": "300f1676c1a641409e64.1655864783.1.0.0",
            "userid": "913901191",
            "limit": "32",
            "offset": (page - 1) * 32,
            "cateId": "-1",
            "q": "鲜花",
            "token": '_FrAa41JSZG1lC8MveTSi679ra0AAAAAexIAACp5n-SGG5r2U9aC0Bcoa1ENMAGQjVrBVOu1LkU9m0UAecE8eXsesn_crjNF6hX4_w'
        }
        response = requests.get(url, headers=headers, params=params, data={})
        # pprint.pprint(response.json())
        data = response.json()['data']['searchResult']
        for searchResult in data:
            shop_id = searchResult['id']
            shop_url = f'https://www.meituan.com/shenghuo/{shop_id}/'
            print(shop_url)
        print('---' * 30)
        # break


def get_detail_info(url):
    headers = {
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5",
        # "Cache-Control": "no-cache",
        # "Connection": "keep-alive",
        "Cookie": "__mta=147692040.1655971229713.1655971229713.1655971229713.1; uuid=300f1676c1a641409e64.1655864783.1.0.0; _lxsdk_cuid=181893b7455c8-0b237ed6c0e96f-623e5653-1fa400-181893b7455c8; ci=1; mtcdn=K; userTicket=HNPNLsLemxEVOnZIknZgTvwVnzumHHRnHLmdmLHf; _lxsdk=181893b7455c8-0b237ed6c0e96f-623e5653-1fa400-181893b7455c8; _hc.v=7399ea34-7a0c-a1a2-3e5b-cb55eddd14ee.1655864906; lat=40.061107; lng=116.584477; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; lt=_FrAa41JSZG1lC8MveTSi679ra0AAAAAexIAACp5n-SGG5r2U9aC0Bcoa1ENMAGQjVrBVOu1LkU9m0UAecE8eXsesn_crjNF6hX4_w; u=913901191; n=gAC776427767; token2=_FrAa41JSZG1lC8MveTSi679ra0AAAAAexIAACp5n-SGG5r2U9aC0Bcoa1ENMAGQjVrBVOu1LkU9m0UAecE8eXsesn_crjNF6hX4_w; unc=gAC776427767; firstTime=1655971229047; _lxsdk_s=1818f8b7aaf-da1-cd3-0d9%7C%7C76",
        "Host": "www.meituan.com",
        # "Pragma": "no-cache",
        "Referer": "https://bj.meituan.com/",
        # "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Microsoft Edge\";v=\"102\"",
        # "sec-ch-ua-mobile": "?0",
        # "sec-ch-ua-platform": "\"Windows\"",
        # "Sec-Fetch-Dest": "document",
        # "Sec-Fetch-Mode": "navigate",
        # "Sec-Fetch-Site": "same-site",
        # "Sec-Fetch-User": "?1",
        # "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers, params={}, data={})
    # print(response.text)
    selector = parsel.Selector(response.text)
    class_type = selector.xpath('//div[@class="crumb"]/a/text()').getall()
    class_type = '/'.join(class_type)
    # print(class_type)
    data = re.search('<script>window.AppData = (?P<data>.*?);</script>', response.text, re.S).group('data')
    data = json.loads(data)
    for group in data['groupDealList']['group']:
        # pprint.pprint(group)
        headIcon = group['headIcon']
        if 'https:' not in headIcon:
            headIcon = 'http:' + headIcon
        title = group['title']
        price = group['price']
        value = group['value']
        print(class_type, title, price, value, headIcon)
        # break
    # pprint.pprint(data)


if __name__ == '__main__':
    # get_list()

    url = 'https://www.meituan.com/shenghuo/1637534751/'
    get_detail_info(url)
