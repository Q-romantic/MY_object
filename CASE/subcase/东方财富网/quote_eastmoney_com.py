# -*- coding: utf-8 -*-
"""
@Time    : 2022/6/27  027 下午 20:22
@Author  : Jan
@File    : quote_eastmoney_com.py
"""
import json

import requests
import time
import pprint

""" {} """

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36"}
def get_target_1():
    for page in range(1, 3):
        url = 'http://53.push2.eastmoney.com/api/qt/clist/get'
        params = {
            "cb": "jQuery11240844869824948961_" + str(int(time.time()*1000)),
            "pn": page,
            "pz": "20",
            "po": "1",
            "np": "1",
            "ut": "bd1d9ddb04089700cf9c27f6f7426281",
            "fltt": "2",
            "invt": "2",
            "wbp2u": "|0|0|0|web",
            "fid": "f3",
            "fs": "m:0 t:6,m:0 t:80,m:1 t:2,m:1 t:23,m:0 t:81 s:2048",
            "fields": "f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152",
            "_": str(int(time.time()*1000))
        }

        response = requests.get(url, headers=headers, params=params, data={})
        data = response.text[41:-2]
        for diff in json.loads(data)['data']['diff']:
            print(diff)
        # pprint.pprint(data)
        # print(response)
        print('---' * 30)
        # break



if __name__ == '__main__':
    get_target_1()    # http://quote.eastmoney.com/center/gridlist.html#hs_a_board
