# -*- coding: utf-8 -*-
"""
@Time    : 2022/6/22  022 下午 13:30
@Author  : Jan
@File    : get_comments.py
"""
import base64
import json
import time
import zlib
import requests
import pprint

""" {} """

with open('big_dic_data.txt', mode='r', encoding='utf-8') as f:
    # with open('test.txt', mode='r', encoding='utf-8') as f:
    data = f.read()
    # print(data)
    # big_dic = json.loads(data)    # 有单引号会报错，舍弃
    big_dic = eval(data)


def str_to_dic_data(s):
    s1 = s.replace('<e class="address">&#x', '|address_uni').replace(';</e>', '|') \
        .replace('<d class="num">&#x', '|num_uni').replace(';</d>', '|') \
        .replace('<svgmtsi class="review">&#x', '|review_uni').replace(';</svgmtsi>', '|') \
        .replace('<svgmtsi class="shopdesc">&#x', '|shopdesc_uni').replace(';</svgmtsi>', '|') \
        .replace('<svgmtsi class="hours">&#x', '|hours_uni').replace(';</svgmtsi>', '|') \
        .replace('<br />', '\n').replace('&nbsp;', '') \
        .split('|')
    li = []
    for i in s1:
        if '_' in i:
            try:
                k = i.split('_')
                i = big_dic[k[0]][k[-1]]
                if i == None:
                    print('There is no key for the value!')
            except:
                pass
            else:
                pass
        li.append(i)
    s = ''.join(li)
    return s


def get_comments(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36"}

    info = str(
        {"rId": "", "ts": int(time.time() * 1000), "cts": int(time.time() * 1000) + 100, "brVD": [], "brR": [], "bI": [],
         "mT": [], "kT": [], "aT": [], "tT": [], "sign": 'eJwDAAAAAAE='}).encode()
    token = base64.b64encode(zlib.compress(info)).decode()
    params = {
        "shopId": url[-16:],
        "cityId": "8",  # 貌似无关参数，可忽略
        "shopType": "10",
        "tcv": "xrxf0306d0",
        "_token": token,
        "uuid": "d0bc69ea-087f-04f7-ca47-ca53213761fb.1637378507",
        "platform": "1",
        "partner": "150",
        "optimusCode": "10",
        "originUrl": "http://www.dianping.com/shop/" + url[-16:]
    }
    url_p = 'http://www.dianping.com/ajax/json/shopDynamic/allReview'
    response = requests.get(url_p, headers=headers, params=params)
    data = response.json()
    # pprint.pprint(data)
    reviewCountAll = data['reviewCountAll']  # 总评论量
    reviewAllDOList = data['reviewAllDOList']
    for i in reviewAllDOList:
        reviewBody = i['reviewDataVO']['reviewBody']
        userNickName = i['user']['userNickName']
        userId = i['user']['userId']
        userId_url = 'http://www.dianping.com/member/' + str(userId)
        print('评论用户网名：' + userNickName + ' ' + userId_url)
        reviewBody = str_to_dic_data(reviewBody)
        print(reviewBody)
        print('----' * 40)
    print(f'单页评论量：{len(reviewAllDOList)}/{reviewCountAll}')


if __name__ == '__main__':
    url = 'http://www.dianping.com/shop/ivbjaqnpAdOCsiY4'
    get_comments(url)
