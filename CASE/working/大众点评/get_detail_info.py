# -*- coding: utf-8 -*-
"""
@Time    : 2022/6/22  022 下午 17:10
@Author  : Jan
@File    : get_detail_info.py
"""
import base64
import re
import time
import zlib
import requests
import pprint

""" {} """

info = str(
    {"rId": "", "ts": int(time.time() * 1000), "cts": int(time.time() * 1000) + 100, "brVD": [], "brR": [], "bI": [], "mT": [], "kT": [], "aT": [], "tT": [],
     "sign": 'eJwDAAAAAAE='}).encode()
token = base64.b64encode(zlib.compress(info)).decode()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36"}

with open('test.txt', mode='r', encoding='utf-8') as f:
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
                    print('no key!')
            except:
                try:
                    k = i.split('_')
                    i = big_dic['address'][k[-1]]
                except:
                    try:
                        k = i.split('_')
                        i = big_dic['num'][k[-1]]
                    except:
                        try:
                            k = i.split('_')
                            i = big_dic['review'][k[-1]]
                        except:
                            try:
                                k = i.split('_')
                                i = big_dic['shopdesc'][k[-1]]
                            except:
                                try:
                                    k = i.split('_')
                                    i = big_dic['hours'][k[-1]]

                                except:
                                    try:
                                        k = i.split('_')
                                        i = big_dic['dishname'][k[-1]]

                                    except:
                                        pass

                                    else:
                                        pass

                                else:
                                    pass

                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass

            else:
                pass
        li.append(i)
    s = ''.join(li)
    return s


def get_info(url):
    url_i = 'http://www.dianping.com/ajax/json/shopDynamic/basicHideInfo'
    params = {
        "shopId": url[-16:],
        "_token": token,
        "tcv": "xrxf0306d0",
        "uuid": "d0bc69ea-087f-04f7-ca47-ca53213761fb.1637378507",
        "platform": "1",
        "partner": "150",
        "optimusCode": "10",
        "originUrl": "http://www.dianping.com/shop/" + url[-16:]
    }
    response = requests.get(url_i, headers=headers, params=params)
    # print(response.text)
    shopInfo = response.json()['msg']['shopInfo']
    shopName = shopInfo['shopName']
    branchName = shopInfo['branchName']
    address = shopInfo['address']
    crossRoad = shopInfo['crossRoad']
    phoneNo = shopInfo['phoneNo']
    # print(address)
    print('店名：' + shopName, branchName)
    address = str_to_dic_data(address)
    print('地址：' + address)
    crossRoad = str_to_dic_data(crossRoad)
    print('交叉路：' + crossRoad)
    phoneNo = str_to_dic_data(phoneNo)
    print('电话：' + phoneNo)

    url_s = 'http://www.dianping.com/ajax/json/shopDynamic/reviewAndStar'
    params = {
        "shopId": url[-16:],
        "cityId": "2",
        "mainCategoryId": "114",
        "_token": token,
        "uuid": "d0bc69ea-087f-04f7-ca47-ca53213761fb.1637378507",
        "platform": "1",
        "partner": "150",
        "optimusCode": "10",
        "originUrl": "http://www.dianping.com/shop/" + url[-16:]
    }
    resp2 = requests.get(url_s, headers=headers, params=params)
    # print(resp2.text)
    avgPrice = resp2.json()['avgPrice']
    avgPrice = str_to_dic_data(avgPrice)
    print('人均：' + avgPrice + '元')
    defaultReviewCount = resp2.json()['defaultReviewCount']
    defaultReviewCount = str_to_dic_data(defaultReviewCount)
    print('评论量：' + defaultReviewCount)
    shopRefinedScoreValueList = resp2.json()['shopRefinedScoreValueList']
    shopRefinedScoreValueList[0] = str_to_dic_data(shopRefinedScoreValueList[0])
    shopRefinedScoreValueList[1] = str_to_dic_data(shopRefinedScoreValueList[1])
    shopRefinedScoreValueList[2] = str_to_dic_data(shopRefinedScoreValueList[2])
    print('口味：' + shopRefinedScoreValueList[0])
    print('环境：' + shopRefinedScoreValueList[1])
    print('服务：' + shopRefinedScoreValueList[2])


if __name__ == '__main__':
    # url = 'http://www.dianping.com/shop/ivbjaqnpAdOCsiY4'
    # url = 'http://www.dianping.com/shop/H3SyNUSShP5BYm87'
    url = 'http://www.dianping.com/shop/H1yiLJXcxZbY0xAn'

    get_info(url)

# strinfo = re.compile(r'[/:*?"<>|\\]')
# name = strinfo.sub('-', title)
