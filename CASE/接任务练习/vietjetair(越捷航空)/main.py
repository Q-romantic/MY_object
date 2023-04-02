# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/23  023 下午 21:57
@Author  : Jan
@File    : 1111111111111.py
"""
import json
import re

import execjs

""" {} """

import requests
from lxml import etree
from lxml.html import fromstring
import pprint
import parsel
import random
from working.all_tools.tools import get_ua
from working.all_tools.tools import get_ip

# from working.all_tools.tools import curl_to_python

""" {} """

js_fn = \
    """
    const crypto = require('crypto');
    
    randomUUID = crypto.randomUUID.bind(crypto)
    sessionStorage = {"ss-data-ga": randomUUID()}
    localStorage = {"temp-data-ga": "".concat(randomUUID() + "-" + (new Date).getTime())}
    P = {
        "b": "c3MtZGF0YS1nYQ==",
        "c": "dGVtcC1kYXRhLWdh",
        "f": "eC1wb3dlci13ZWItcy1k",
        "e": "dXNlci1hZ2VudC1scy1kYXRh",
        "d": "metaSearchKey",
        "a": {
            "Token": "token",
            "ExpireAt": "tokenExpireAt",
            "Provider": "auth_provider"
        }
    }
    var n = sessionStorage[atob(P.b)]
        , a = localStorage[atob(P.c)]
        , r = a
        , i = (null == r ? void 0 : r.split("-")) || [];
    i.pop();
    var o, c = null == n ? void 0 : n.split("-").slice(2).join("-");
    
    function h_g(e) {
        for (var t = e.split("-").reduce((function (e, t) {
                return e + t[0] + t[t.length - 1]
            }
        ), ""), n = "", a = 0; a < t.length; a++)
            n += 1 ^ t[a];
        return n
    }
    
    function O_a(e, t, n) {
        return t in e ? Object.defineProperty(e, t, {
            value: n,
            enumerable: !0,
            configurable: !0,
            writable: !0
        }) : e[t] = n,
            e
    }
    
    get_requestid = function () {
        var n = (new Date).getTime()
        a = function () {
            for (var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 12, t = "".concat("ABCDEFGHIJKLMNOPQRSTUVWXYZ").concat("0123456789"), n = "", a = 0; a < e; a++)
                n += t[Math.floor(Math.random() * t.length)];
            return n
        }(12)
        r = "".concat(a, "-").concat(n);
        return r
    }
    
    get_t = function () {
        t = {}
        Object(O_a)(t, atob(P.f), "".concat(Object(h_g)(i.join("-")) + "-" + Object(h_g)(n) + "-" + c))
        Object(O_a)(t, atob(P.e), a)
        t['requestId'] = get_requestid()
        return t
    }
    """
zzz = execjs.compile(js_fn)
t = zzz.call('get_t')
# print(t)
o_dancheng = {
    "adultCount": 1,
    "arrival": "HAN",  # 到达
    "childCount": 0,
    "currency": "USD",  # 货币
    "daysAfterDeparture": 0,
    "daysBeforeDeparture": 0,
    "departureDate": "2023-03-31",  # 离开时间
    "departurePlace": "SGN",  # 出发地
    "infantCount": 0,
    "oneway": 1,  # 往返为0 单向为1
    "requestId": t['requestId'],
    "sessionId": None,
    "user-agent-ls-data": t["user-agent-ls-data"],
    "x-power-web-s-d": t["x-power-web-s-d"],
}
o_wangfan = {
    "currency": "USD",  # 货币
    "departureDate": "2023-03-29",  # 离开时间
    "daysBeforeDeparture": 0,
    "daysAfterDeparture": 0,
    "departurePlace": "SGN",  # 出发地
    "arrival": "BMV",  # 到达
    "oneway": 0,  # 往返为0 单向为1
    "adultCount": 1,
    "childCount": 0,
    "infantCount": 0,
    "returnDate": "2023-04-21",  # 返回时间
    "daysBeforeReturn": 0,
    "daysAfterReturn": 0,
    "requestId": t['requestId'],
    "sessionId": None,
    "x-power-web-s-d": t["x-power-web-s-d"],
    "user-agent-ls-data": t["user-agent-ls-data"],
}


def get_full_o(o):
    index = open('get_full_o.js', 'r', encoding='utf-8')
    js = execjs.compile(index.read())
    o = js.call('get_full_o', o)
    return o


headers = {
    "content-language": "zh-cn",
    # "accept-language": "zh-cn",
    # "content-type": "application/json",
    # "accept": "application/json",
    # "cache-control":"no-cache",
    # "content-length":"1040",
    # "accept-encoding":"gzip, deflate, br",
    # "origin":"https://www.vietjetair.com",
    # "pragma":"no-cache",
    # "referer":"https://www.vietjetair.com/",
    # "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}


def get_encrypted(s):
    rpc_url = "http://127.0.0.1:5620/business-demo/invoke"
    rpc_params = {
        "group": "rpc-test",
        "action": "action",
        "data": s,
    }
    res = requests.get(rpc_url, params=rpc_params).json()
    # print(res)
    return res['getencrypted']


data = get_full_o(o_dancheng)  # 单程
# data = get_full_o(o_wangfan)  # 往返








import rsa
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
#rsa加密，通常对加密结果进行base64编码

def handle_pub_key(key):
    """
    处理公钥
    公钥格式pem，处理成以-----BEGIN PUBLIC KEY-----开头，-----END PUBLIC KEY-----结尾的格式
    :param key:pem格式的公钥，无-----BEGIN PUBLIC KEY-----开头，-----END PUBLIC KEY-----结尾
    :return:
    """
    start = '-----BEGIN PUBLIC KEY-----\n'
    end = '-----END PUBLIC KEY-----'
    result = ''
    # 分割key，每64位长度换一行
    divide = int(len(key) / 64)
    divide = divide if (divide > 0) else divide + 1
    line = divide if (len(key) % 64 == 0) else divide + 1
    for i in range(line):
        result += key[i * 64:(i + 1) * 64] + '\n'
    result = start + result + end
    print(result)
    return result


def get_param(message, public_key, N):
    """
    处理长消息 不经过 这个处理回报下面error
    OverflowError: 458 bytes needed for message, but there is only space for 117
    :param message 消息
    :param public_key 公钥
    :return:
    """
    # pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(public_key)
    # crypto = b''
    # divide = int(len(message) / 117)
    # divide = divide if (divide > 0) else divide + 1
    # line = divide if (len(message) % 117 == 0) else divide + 1
    # for i in range(line):
    #     crypto += rsa.encrypt(message[i * 117:(i + 1) * 117].encode(), pubkey)

    # N = 245
    # N = 190
    # N = 166
    pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(public_key)
    crypto = b''
    divide = int(len(message) / N)
    print(divide)
    divide = divide if (divide > 0) else divide + 1
    print(divide)
    line = divide if (len(message) % N == 0) else divide + 1
    print(line)
    for i in range(line):
        print(message[i * N:(i + 1) * N])
        crypto += rsa.encrypt(message[i * N:(i + 1) * N].encode(), pubkey)

    crypto1 = base64.b64encode(crypto)
    return crypto1.decode()

public_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAok58IrYXjeFjb6hPgrcvKis43ARDVIqowS2AJKivDp4+8uKDCWnjzBZTsuVvwKPzvVCxBzON2/DPpHU3wnRtdKSVzWju7HMKhuLxe04FsVw8+xvZTmguBj4jTczNLSLjK13lQr46J8j7JrmVUlPqGxIL/Bd3HNAIFuarZQkDsgx5fvdNrMbmT4edr1b3A8wRkhfo9tuE5Tmlx0YVUwybzcI6hgLggCfNwwaClXyBt08NbGSIBcKYKjiQErND0EOnWcGyto7EhkpgGRfAeESo3hbmsiabThLd4t9iOWVHFSl+7B0q+1IGFjSo9qkvNdMUI4ZYdIKq+nCHufpuFMl7SwIDAQAB"
print(json.dumps(data))
public_key = handle_pub_key(public_key)
for N in range(166, 245):
    encrypted = get_param(json.dumps(data), public_key, N)

    # encrypted = get_encrypted(json.dumps(data))
    # encrypted = "A" * 1024
    print(encrypted)
    params = {"encrypted": encrypted}
    url = 'https://vietjet-api.vietjetair.com/booking/api/v1/search-flight'
    response = requests.patch(url, headers=headers, data=params)
    if response.status_code != 400:
        print(response.text)

encrypted = get_encrypted(json.dumps(data))
print(encrypted)
params = {"encrypted": encrypted}
url = 'https://vietjet-api.vietjetair.com/booking/api/v1/search-flight'
response = requests.patch(url, headers=headers, data=params)
if response.status_code != 400:
    print(response.text)