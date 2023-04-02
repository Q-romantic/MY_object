# -*- coding: utf-8 -*-
"""
@Time    : 2022/10/25  025 下午 17:20
@Author  : Jan
@File    : ibox.py
"""
import random

import requests
import json
import time
from Crypto.Cipher import AES
import httpx
import snappy  # pip install python-snappy
import execjs

# print(execjs.get().name)

js_method = """
var y = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
function base64ToArrayBuffer(e) {
            for (var t = function(e) {
                var t = String(e).replace(/=+$/, "")
                  , r = "";
                if (t.length % 4 == 1)
                    throw new Error('"atob" failed');
                for (var n = 0, i = void 0, o = void 0, a = 0; o = t.charAt(a++); ~o && (i = n % 4 ? 64 * i + o : o,
                n++ % 4) ? r += String.fromCharCode(255 & i >> (-2 * n & 6)) : 0)
                    o = y.indexOf(o);
                return r
            }(e), r = t.length, n = new Uint8Array(r), i = 0; i < r; i++)
                n[i] = t.charCodeAt(i);
            return new Uint8Array(n)
        }
"""
loader = execjs.compile(js_method)

def get_bytes(secret_key):
    secret_key = "zjHUHzZssTRStT3Z4RxKkg=="
    result = loader.call('base64ToArrayBuffer', secret_key)
    print(secret_key)
    print(result)
    arr = []
    for k, v in result.items():
        arr.append(v)
    secret_key_bytes = bytes(arr)
    return secret_key_bytes


# if __name__ == '__main__':
#     result = get_bytes("zkXsdQURgkDefISbA6prjw==")
#     print(result)


key_url = 'https://web-001.cloud.servicewechat.com/wxa-qbase/jsoperatewxdata'


def get_headers(timestamp):
    headers_2 = {
        "X-WX-ENCRYPTION-VERSION": "2",
        "X-WX-ENCRYPTION-TIMESTAMP": str(timestamp),
        "X-WX-COMPRESSION": "snappy",
        "X-WX-USER-TIMEOUT": "30000",
        "X-WX-LIB-BUILD-TS": "1655460325335",
        "X-WX-RESPONSE-CONTENT-ACCEPT-ENCODING": "PB, JSON",
        "Content-Type": "application/octet-stream",
        "X-WX-REQUEST-CONTENT-ENCODING": "JSON"
    }
    return headers_2


def parse_compress_data():
    headers_list = []
    headers = {
        "X-WX-EXCLUDE-CREDENTIALS": "unionid, cloudbase-access-token, openid",
        "X-WX-REGION": "ap-beijing",
        "X-WX-GATEWAY-ID": "gw-1-1g2n1gd143d56b56",
        "HOST": "api-h5-tgw.ibox.art",
        "Accept-Language": "zh-CN",
        "IB-DEVICE-ID": "dfb3dd84aa254ea0920f11cf964ec43d",
        "IB-TRANS-ID": "d0d27b251d1546788f359750e81d5556",  # 可能会变
        "x-cloudbase-phone": "",
        "IB-PLATFORM-TYPE": "web",
        "content-type": "application/json",
        "User-Agent": "",
        "X-WX-ENV": "ibox-3gldlr1u1a8322d4",
        "X-WX-CALL-ID": "0.02830912142312636_1666694470058",  # 随机数_13位时间戳
        "X-WX-RESOURCE-APPID": "wxa2d0710b1323fd96",
        "X-WX-CONTAINER-PATH": "/nft-mall-web/v1.1/nft/user/getUserInfo",
    }
    call_id = f"{random.random()}_{str(int(time.time() * 1000))}"
    for k, v in headers.items():
        k = k.lower()
        if 'x-wx-call-id' == k:
            v = call_id
        headers_list.append({'key': k, 'value': v})
    header_body = {
        "method": "GET",
        "header": headers_list,
        "body": "undefined",
        "call_id": call_id
    }
    # header_body_arr = bytes(json.dumps(header_body).encode('utf-8'))
    # header_body_c = snappy.compress(header_body_arr)
    # return header_body_c
    e = '{"method":"GET","header":[{"key":"x-wx-exclude-credentials","value":"unionid, cloudbase-access-token, openid"},{"key":"x-wx-region","value":"ap-beijing"},{"key":"x-wx-gateway-id","value":"gw-1-1g2n1gd143d56b56"},{"key":"host","value":"api-h5-tgw.ibox.art"},{"key":"accept-language","value":"zh-CN"},{"key":"ib-device-id","value":"11582baf51704c07af7b0a987ed57ef5"},{"key":"ib-trans-id","value":"31f05583772f4f47b74b2c31dba7b943"},{"key":"x-cloudbase-phone","value":""},{"key":"ib-platform-type","value":"web"},{"key":"content-type","value":"application/json"},{"key":"user-agent","value":""},{"key":"x-wx-env","value":"ibox-3gldlr1u1a8322d4"},{"key":"x-wx-call-id","value":"0.6687688655669655_1668490037198"},{"key":"x-wx-resource-appid","value":"wxb5b2c81edbd4cf69"},{"key":"x-wx-container-path","value":"/nft-mall-web/nft/contentList"}],"body":"undefined","call_id":"0.6687688655669655_1668490037198"}'

    vv = []
    # for i in json.dumps(header_body):
    for i in e:
        x = ord(i)
        vv.append(x)
        # print(x)
        # break
    print(vv)


# 需要补位，str不是16的倍数那就补足为16的倍数
def add_to_16_byte(value):
    while len(value) % 16 != 0:
        value += b'\0'
    return value


def aes_encrypt(key_bytes, text):
    # 增加vi向量
    aes = AES.new(key_bytes, AES.MODE_CBC, key_bytes)
    bytes = aes.encrypt(add_to_16_byte(text))
    return bytes


def get_key_token():
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '626',
        'Content-Type': 'application/json',
        'Host': 'web-001.cloud.servicewechat.com',
        'Origin': 'https://www.ibox.art',
        'Pragma': 'no-cache',
        'Referer': 'https://www.ibox.art/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    data = {
        "appid": "wxe77e91c2fdb64e85",
        "data": {
            "qbase_api_name": "tcbapi_get_service_info",
            "qbase_req": "{\"client_random\":\"0.2826657173143865_1657318155306\",\"system\":\"\"}",
            "qbase_options": {
                "identityless": "true",
                "resourceAppid": "wxe77e91c2fdb64e85",
                "resourceEnv": "ibox-3gldlr1u1a8322d4",
                "config": {
                    "database": {
                        "realtime": {
                            "maxReconnect": 5,
                            "reconnectInterval": 5000,
                            "totalConnectionTimeout": "null"
                        }
                    }
                },
                "appid": "wxe77e91c2fdb64e85",
                "env": "ibox-3gldlr1u1a8322d4"
            },
            "qbase_meta": {
                # "session_id": str(int(time.time() * 1000)),
                "sdk_version": "wx-web-sdk/WEBDOMAIN_1.0.0 (1655460325000)",
                "filter_user_info": False
            },
            # "cli_req_id": str(int(time.time() * 1000)) + "_0.5101258021009685"
        }
    }
    response = requests.post(url=key_url, headers=headers, json=data)
    content = json.loads(response.content)
    if content:
        data = json.loads(content.get('data'))
        token = data.get('token')
        key = data.get('key')
        timestamp = data.get('timestamp')
        return key, token, timestamp


def get_request():
    base_url = "https://web-001.cloud.servicewechat.com/wxa-qbase/container_service?token="
    key, token, timestamp = get_key_token()
    print(token)
    base_url += token

# "http://localhost:12080/go?group=group&name=name&action=func_1&param=1"




    # data = parse_compress_data()
    # print(data, "ssssssss")
    key_bytes = get_bytes(key)
    print(key_bytes)
    # aes_data = aes_encrypt(key_bytes, data)


    # print(aes_data)
    # headers = get_headers(timestamp)
    # with httpx.Client(http2=True) as client:
    #     response = client.post(base_url, headers=headers, content=aes_data)
    #     print(response.content)
    #
    # resp = requests.post(base_url, headers=headers, data=aes_data)
    # print(resp.content)


if __name__ == '__main__':
    get_request()
