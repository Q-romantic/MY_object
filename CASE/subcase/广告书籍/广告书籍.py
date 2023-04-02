# -*- coding: utf-8 -*-
"""
@Time    : 2022/6/28  028 下午 15:14
@Author  : Jan
@File    : 广告书籍.py
"""
import json
import random
import re
import time
from jsonpath import jsonpath
import parsel
import requests
import pprint
from aaaa import get_x_request_token

""" {} """

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36"}

url = 'https://www.addog.vip/'

response = requests.get(url, headers=headers, params={}, data={})
data = response.text
# print(data)
# print(response)
sel = parsel.Selector(data)
divs = sel.xpath('//div[@id="adWebList"]/div[22]/div/div/div')
for div in divs[26:27]:
    title = div.xpath('.//h3/text()').get()
    detail_url = div.xpath('.//a/@href').get()
    priceSale = ''
    try:
        response = requests.get(detail_url, headers=headers)
        # print(response.text)
        hrl = re.findall("hrl=\'(.*?)\';", response.text)[0]
        response = requests.get(hrl, headers=headers)
        # print(response.text)
        sel = parsel.Selector(response.text)
        priceSale = ''.join(sel.xpath('//span[@id="priceSale"]//text()').getall()).strip()
        # print(priceSale)
    except:
        try:
            response = requests.get(detail_url, headers=headers)
            # print(response.text)
            num = re.findall('<span class="price J-p-(.*?)"></span>', response.text)[0]
            url = 'https://spu.jd.com/json.html'
            params = {
                "cond": f"1_4_1_0_0_1_{num}_1",
                "callback": "jQuery473967",
                "_": str(int(time.time() * 1000))
            }
            response = requests.get(url, headers=headers, params=params)
            # print(response.text)
            data = json.loads(response.text[13:-1])
            # pprint.pprint(data)
            # priceSale = data['skuStockVenders'][1]['jdPrice']
            priceSale = jsonpath(data, '$..jdPrice')
        except:
            try:
                num = re.findall('\d+', detail_url)[0]
                le = str(int(time.time() * 1000))
                se = str(int(random.random() * 100000000))
                headers = {
                    # "accept": "*/*",
                    # "accept-encoding": "gzip, deflate, br",
                    # "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5",
                    # "cache-control": "no-cache",
                    # "cookie": f"Hm_lvt_046a9150e95f58699927e236d330965a=1656402694; _ga=GA1.2.192228710.1656404789; _gid=GA1.2.753540175.1656404789; _gat=1; Hm_lpvt_046a9150e95f58699927e236d330965a={str(int(time.time()))}",
                    # "pragma": "no-cache",
                    # "referer": f"https://www.duozhuayu.com/books/{num}",
                    # "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Microsoft Edge\";v=\"102\"",
                    # "sec-ch-ua-mobile": "?0",
                    # "sec-ch-ua-platform": "\"Windows\"",
                    # "sec-fetch-dest": "empty",
                    # "sec-fetch-mode": "cors",
                    # "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44",
                    # "x-api-version": "0.0.42",
                    "x-refer-request-id": f"0-{le}-{str(int(random.random() * 100000))}",
                    "x-request-id": f"0-{le}-{str(int(random.random() * 100000))}",
                    # "x-request-misc": "{\"platform\":\"browser\",\"originSource\":null,\"originFrom\":\"normal\",\"webVersion\":\"1.2.137693\"}",
                    "x-request-token": get_x_request_token(f"{le}:0:{se}"),
                    "x-security-key": se,
                    "x-timestamp": le,
                    "x-user-id": "0"
                }
                url = 'https://www.duozhuayu.com/api/books/' + str(num)
                print(url)
                response = requests.get(url, headers=headers)
                print(response.text)
                priceSale = response.json()['localPrice'] / 100
                pass
            except:
                pass
        else:
            pass
    else:
        pass
    print(title, priceSale, detail_url)
    # break
