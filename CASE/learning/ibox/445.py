# -*- coding: utf-8 -*-
"""
@Time    : 2022/11/19  019 下午 16:20
@Author  : Jan
@File    : 445.py
"""
import json
import random
import time

import execjs

""" {} """

import requests

session = requests.Session()

headers = {
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"zh-CN,zh;q=0.9",
    "cache-control":"no-cache",
    "cookie":"sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221847643cb422ca-075339f140436c8-977173c-2073600-1847643cb43d4e%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg0NzY0M2NiNDIyY2EtMDc1MzM5ZjE0MDQzNmM4LTk3NzE3M2MtMjA3MzYwMC0xODQ3NjQzY2I0M2Q0ZSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221847643cb422ca-075339f140436c8-977173c-2073600-1847643cb43d4e%22%7D",
    "pragma":"no-cache",
    "sec-ch-ua":"\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"document",
    "sec-fetch-mode":"navigate",
    "sec-fetch-site":"same-origin",
    "sec-fetch-user":"?1",
    "upgrade-insecure-requests":"1",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

params = {'id': '100515059'}

response = session.get('https://www.ibox.art/zh-cn/item/group/', headers=headers, params=params)
response.encoding = response.apparent_encoding
print(1, response.text)


headers = {
    'ib-platform-type': 'web',
    'accept-language': 'zh-CN',
    'sec-ch-ua-mobile': '?0',
    'accept': 'application/json, text/plain, */*',
    'x-cloudbase-phone': '',
    'ib-device-id': '11582baf51704c07af7b0a987ed57ef5',
    'ib-trans-id': 'cc209e87832647989bb19128262fb40b',
    'origin': 'https://www.ibox.art',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.ibox.art/',
}

response = session.get('https://api-public.ibox.art/nft-mall-web/nft/app/getConfig', headers=headers)
response.encoding = response.apparent_encoding
print(2, response.text)


headers = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "626",
    "Content-Type": "application/json",
    "Host": "web-001.cloud.servicewechat.com",
    "Origin": "https://www.ibox.art",
    "Pragma": "no-cache",
    "Referer": "https://www.ibox.art/",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
}

data = {"appid": "wxb5b2c81edbd4cf69",
        "data": {"qbase_api_name": "tcbapi_get_service_info", "qbase_req": "{\"client_random\":\"0.4005950284866038_1668951043745\",\"system\":\"\"}",
                 "qbase_options": {"identityless": True, "resourceAppid": "wxb5b2c81edbd4cf69", "resourceEnv": "ibox-3gldlr1u1a8322d4",
                                   "config": {"database": {"realtime": {"maxReconnect": 5, "reconnectInterval": 5000, "totalConnectionTimeout": "null"}}},
                                   "appid": "wxb5b2c81edbd4cf69", "env": "ibox-3gldlr1u1a8322d4"},
                 "qbase_meta": {"session_id": "1668951043752", "sdk_version": "wx-web-sdk/WEBDOMAIN_1.0.0 (1655460325000)", "filter_user_info": False},
                 "cli_req_id": "1668951044204_0.5436564336739025"}}


response = session.post('https://web-001.cloud.servicewechat.com/wxa-qbase/jsoperatewxdata', headers=headers, json=data)
response.encoding = response.apparent_encoding
print(3, response.text)
data = json.loads(response.json().get('data'))
token = data.get('token')
key = data.get('key')
timestamp = data.get('timestamp')


data = {"appid": "wxb5b2c81edbd4cf69", "data": {"qbase_api_name": "tcbapi_call_container",
                                                "qbase_req": "{\"method\":\"POST\",\"headers\":[{\"k\":\"X-WX-EXCLUDE-CREDENTIALS\",\"v\":\"unionid, cloudbase-access-token, openid\"},{\"k\":\"X-WX-REGION\",\"v\":\"ap-beijing\"},{\"k\":\"X-WX-GATEWAY-ID\",\"v\":\"gw-1-1g2n1gd143d56b56\"},{\"k\":\"HOST\",\"v\":\"api-h5-tgw.ibox.art\"},{\"k\":\"Accept-Language\",\"v\":\"zh-CN\"},{\"k\":\"IB-DEVICE-ID\",\"v\":\"11582baf51704c07af7b0a987ed57ef5\"},{\"k\":\"IB-TRANS-ID\",\"v\":\"11f3be94aa0048b08e34a138654abbe4\"},{\"k\":\"x-cloudbase-phone\",\"v\":\"\"},{\"k\":\"IB-PLATFORM-TYPE\",\"v\":\"web\"},{\"k\":\"content-type\",\"v\":\"application/json\"},{\"k\":\"User-Agent\",\"v\":\"\"},{\"k\":\"X-WX-ENV\",\"v\":\"ibox-3gldlr1u1a8322d4\"},{\"k\":\"X-WX-CONTAINER-PATH\",\"v\":\"/nft-mall-web/v1.1/nft/user/getUserInfo\"}],\"data\":\"{\\\"encryptKey\\\":\\\"drho+l8UXkJHWQyzxNruNPUnEnnHTqN7M2QFM03RsOdsgeDBWnlX+TAwzkgHqsjoEEPXCWNe1GqWIazjihhUCir4PTng66htqxTYe/ohmVwwsEUiJDAIB8/mqQlrZ/F6R/yJetL8bD4V/5zRfLvpzJAm44tFmuBp8MsHPFiGBKA=\\\",\\\"data\\\":\\\"EepdBQXpTfdw_BtpRgmK5Q==\\\"}\",\"data_type\":0,\"action\":1,\"retryType\":0,\"call_id\":\"1668951044261-0.21807169786683667\",\"user_timeout\":30000}",
                                                "qbase_options": {"identityless": True, "resourceAppid": "wxb5b2c81edbd4cf69",
                                                                  "resourceEnv": "ibox-3gldlr1u1a8322d4", "config": {"database": {
                                                        "realtime": {"maxReconnect": 5, "reconnectInterval": 5000, "totalConnectionTimeout": "null"}}},
                                                                  "appid": "wxb5b2c81edbd4cf69", "env": "ibox-3gldlr1u1a8322d4"},
                                                "qbase_meta": {"session_id": "1668951043752", "sdk_version": "wx-web-sdk/WEBDOMAIN_1.0.0 (1655460325000)",
                                                               "filter_user_info": False}, "cli_req_id": "1668951044262_0.41760144666688803"}}
response = session.post('https://web-001.cloud.servicewechat.com/wxa-qbase/jsoperatewxdata', headers=headers, json=data)
response.encoding = response.apparent_encoding
print(4, response.text)


headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua-mobile': '?0',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'script',
    'Referer': 'https://www.ibox.art/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = {
    'captcha_id': '32727fa8d208a82e46754c2e5055a679',
    'challenge': 'cce38ad5-2f1d-42a7-9317-cb97ce40043a',
    'client_type': 'web',
    'lang': 'zh-cn',
    # 'callback': 'geetest_1668951045167',
}

response = session.get('https://gcaptcha4.geetest.com/load', headers=headers, params=params)
response.encoding = response.apparent_encoding
print(5, response.text)

resp = response.text
data = json.loads(resp[1:-1])['data']
lot_number = data['lot_number']
payload = data['payload']
process_token = data['process_token']
datetime = data['pow_detail']['datetime']
# pprint.pprint(data)

headers = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cache-Control":"no-cache",
    "Connection":"keep-alive",
    "Content-Length":"232",
    "Content-Type":"application/json",
    "Host":"web-001.cloud.servicewechat.com",
    "Origin":"https://www.ibox.art",
    "Pragma":"no-cache",
    "Referer":"https://www.ibox.art/",
    "sec-ch-ua":"\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"cross-site",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
params = {'token': token}

data = {"report_info_list":[{"log_id":22601,"version":9,"user_log_list":",1668951044204,1668951044516,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,im,,312,0,,/nft-mall-web/v1.1/nft/user/getUserInfo,web_sdk,,1655460325335,,,,,,1668951044260,,"}]}

response = session.post('https://web-001.cloud.servicewechat.com/wxa-qbase/report', headers=headers, params=params, json=data)
response.encoding = response.apparent_encoding
print(6, response.text)











headers = {
    'X-WX-USER-TIMEOUT': '30000',
    'X-WX-LIB-BUILD-TS': '1655460325335',
    'X-WX-ENCRYPTION-TIMESTAMP': str(timestamp),
    'X-WX-REQUEST-CONTENT-ENCODING': 'JSON',
    # 'Content-Type': 'application/octet-stream',
    'X-WX-RESPONSE-CONTENT-ACCEPT-ENCODING': 'PB, JSON',
    'X-WX-ENCRYPTION-VERSION': '2',
    # 'X-WX-COMPRESSION': 'snappy',
}
#
# params = {'token': token}
#
# data = {?????????????????????}
#
# response = session.post('https://web-001.cloud.servicewechat.com/wxa-qbase/container_service', headers=headers, params=params, data=data)
def get_params(a, b):
    index = open('index.js', 'r', encoding='utf-8')
    js = execjs.compile(index.read())
    arr = js.call('get_sss_to_L', a, b)
    # print(arr)
    # asii = []
    # for i in arr:
    #     x = chr(int(i))
    #     asii.append(x)
    #     # break
    # arr = ''.join(asii)
    return arr


def get_sss():
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
    return json.dumps(header_body)


def get_key_token():
    url = 'https://web-001.cloud.servicewechat.com/wxa-qbase/jsoperatewxdata'
    headers = {
        "Host": "web-001.cloud.servicewechat.com",
        "Referer": "https://www.ibox.art/zh-cn/item/group/?id=100515155",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    data = {
        "appid": "wxb5b2c81edbd4cf69",
        "data": {
            "qbase_api_name": "tcbapi_get_service_info",
            "qbase_req": "{\"client_random\":\"0.9378987950086999_1668574874529\",\"system\":\"\"}",
            "qbase_options": {
                "identityless": True,
                "resourceAppid": "wxb5b2c81edbd4cf69",
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
                "appid": "wxb5b2c81edbd4cf69",
                "env": "ibox-3gldlr1u1a8322d4"
            },
            "qbase_meta": {
                "session_id": "1668574874536",
                "sdk_version": "wx-web-sdk/WEBDOMAIN_1.0.0 (1655460325000)",
                "filter_user_info": False
            },
            "cli_req_id": "1668574874835_0.9932751746305886"
        }
    }
    response = requests.post(url, headers=headers, json=data)
    data = json.loads(response.json().get('data'))
    token = data.get('token')
    key = data.get('key')
    timestamp = data.get('timestamp')
    # print(key, token, timestamp)
    return key, token, timestamp


def get_headers(timestamp):
    headers = {
        "X-WX-ENCRYPTION-VERSION": "2",
        "X-WX-ENCRYPTION-TIMESTAMP": str(timestamp),
        "X-WX-COMPRESSION": "snappy",
        "X-WX-USER-TIMEOUT": "30000",
        "X-WX-LIB-BUILD-TS": "1655460325335",
        "X-WX-RESPONSE-CONTENT-ACCEPT-ENCODING": "PB, JSON",
        "Content-Type": "application/octet-stream",
        "X-WX-REQUEST-CONTENT-ENCODING": "JSON"
    }

    return headers


def get_request():
    base_url = "https://web-001.cloud.servicewechat.com/wxa-qbase/container_service?token="
    # key, token, timestamp = get_key_token()
    base_url += token
    sss = get_sss()
    aes_data = get_params(sss, key)
    # headers = get_headers(timestamp)
    # print(base_url, key, token, timestamp, sss, aes_data, headers)

    resp = session.post(base_url, headers=headers, files={"files": bytes(aes_data)})
    print(resp.status_code)
    print(7, resp.content)

get_request()













# headers = {
#     'Connection': 'keep-alive',
#     'Pragma': 'no-cache',
#     'Cache-Control': 'no-cache',
#     'sec-ch-ua': '^\\^',
#     'sec-ch-ua-mobile': '?0',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
#     'sec-ch-ua-platform': '^\\^Windows^\\^',
#     'Accept': '*/*',
#     'Sec-Fetch-Site': 'cross-site',
#     'Sec-Fetch-Mode': 'no-cors',
#     'Sec-Fetch-Dest': 'script',
#     'Referer': 'https://www.ibox.art/',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
# }
#
# def get_s():
#     """生成随机16位字符串"""
#
#     def _():
#         return str(hex((int((1 + random.random()) * 65536) | 0)))[3:]
#
#     return _() + _() + _() + _()
#
# guid = get_s()
#
# pow_msg = f"1|4|md5|{datetime}|32727fa8d208a82e46754c2e5055a679|{lot_number}||{guid}"
# e = {
#     # "device_id": "1130585e23f605ac8beab2fa0aab12b0",  # 二选一 or 随机 ？？？
#     "device_id": "5d25317d91fd2c612ee3c2ec316f90b0",
#     "lot_number": lot_number,
#     "pow_msg": pow_msg,
#     "pow_sign": hashlib.md5(pow_msg.encode('utf-8')).hexdigest(),
#     "geetest": "captcha",
#     "lang": "zh",
#     "ep": "123",
#     "qca4": "1909887014",
#     "em": {
#         "ph": 0,
#         "cp": 0,
#         "ek": "11",
#         "wd": 1,
#         "nt": 0,
#         "si": 0,
#         "sc": 0
#     }
# }
# e = json.dumps(e)
#
# def get_param_w(a, b):
#     index = open('66.js', 'r', encoding='utf-8')
#     js = execjs.compile(index.read())
#     a = js.call('get_w', a, b)
#     return a
#
#
#
# # e = '{"device_id":"5d25317d91fd2c612ee3c2ec316f90b0","lot_number":"1edd2a57d0e84a0986a5764355353bf5","pow_msg":"1|4|md5|2022-11-20T16:18:15.805813+08:00|32727fa8d208a82e46754c2e5055a679|1edd2a57d0e84a0986a5764355353bf5||e24baa56b2e73772","pow_sign":"0b94428c077f0761983eb1c100fdaed0","geetest":"captcha","lang":"zh","ep":"123","qca4":"1909887014","em":{"ph":0,"cp":0,"ek":"11","wd":1,"nt":0,"si":0,"sc":0}}'
# # guid = "94f422eec3054d0d"
# w = get_param_w(e, guid)
# # print(w)
#
# params = (
#     ('captcha_id', '32727fa8d208a82e46754c2e5055a679'),
#     ('client_type', 'web'),
#     ('lot_number', lot_number),
#     ('payload', payload),
#     ('process_token', process_token),
#     ('payload_protocol', '1'),
#     ('pt', '1'),
#     # ('w', w),
#     ('w', 'e523973db4274a57cc32ac688a12e42993136ad08666b334edf83ea400f9f9ef0f6cbd67c86905c12dee458b74b5b37e897ee890b941bc7a33eb762f9d6a0aec08ea0f17e1adef58e36593cfc27bd64a2793444954a47ff3669ac2223eb9e094deb128774c90ac665c4cb83dc00362f33fd595e314bd5fd822b95e5a271413ebffc92c3ab11d1a6c66180f891196906e935d348d5c7435526b020179ad49bda85cb59d0bc90e5b2b1ebabeaef4f74a2ac9cf6a4c0265cb622e30936687366c92757c85a385af3064a0996a74ac0db005ebd72446ec99b9bb39b65edd81dda34bd62b55863fcaeb66cad6e55c2f8075dfcf78d0f33fca4fd4cd491d58eea23f240f117d6030e5bdc6a1b81c3b2f8b74630ac604ee0b7651243118b4bc02ac7fda22f7e964524bd61d51a97f8529450a81aaf150243d3eb4bcc85946280284176c47e4f24e726aa5f038f2933cd715100fcba53e48532960ee6f3409412704141940c715b4f5c5128a1dba2f38689ecf75336b68e45b80f4137d33d1c3b41d469ca0c1dd8c9d1a1d1f2e72efdf010576449e40226c0b2ef45e16fd189a6b3c22a41cb2db026ad0d4fad576a30543b377033b106dd15062f79f639d9cbabc21eb37cfa99ed894a48c89eb1fb9f0617242f4114828eaaa4d3286fc126fb8b94f50e4eeefe77b4c3660696f606cd8ef2f6a3490f28ebf0f9a36b2446ac722c456689f60c0f3983758d5a341dc746bca900366c162d54dd846d678a06702688d46e6f9'),
#     # ('callback', 'geetest_1668951049757'),
# )
#
# response = session.get('https://gcaptcha4.geetest.com/verify', headers=headers, params=params)
# response.encoding = response.apparent_encoding
# # print(response.text)
#
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
# #     'Referer': 'https://www.ibox.art/',
# #     "cookie": "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221847643cb422ca-075339f140436c8-977173c-2073600-1847643cb43d4e%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg0NzY0M2NiNDIyY2EtMDc1MzM5ZjE0MDQzNmM4LTk3NzE3M2MtMjA3MzYwMC0xODQ3NjQzY2I0M2Q0ZSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221847643cb422ca-075339f140436c8-977173c-2073600-1847643cb43d4e%22%7D; acw_tc=ddcc172816689308154652400e2e51db05f712c47d40b0243d92ebf47a"
# # }
# #
# # params = {
# #     'captcha_id': '32727fa8d208a82e46754c2e5055a679',
# #     'client_type': 'web',
# #     'lot_number': lot_number,
# #     'payload': payload,
# #     'process_token': process_token,
# #     'payload_protocol': '1',
# #     'pt': '1',
# #     'w': w,
# #     # 'w': '4426350bfdda7cc2c6355f1165551c739a7a074b9bfc48549016a98ed45924c0055cd2a8cd361fb60c43016536e3429a98ce75b78b53232d583140d1dbb41d01c5e1c246ca8129350b749d61bd4b0efcfa6109eb252fd246216c2b607ad042d074a2b15c666b928937e31c5d1dc79a2f394891544bd6c7152797b9237c2ac8507a8c5bc502fd604202ccd07060505bd44558f2138229709f19ba4d0dd113ea61b292409bfab20ca299ca4a0f61df267511899c9ca703208ef1cb1858d89bbf262429e6543b5f519856ce624e9ca451a40cda08653d23027eb00348b96132e19b057d8db6cd319eb436294d02d24faadb030ed86439ca13437cd653661e0eaa4e00ae8a97482cb9452f5ecb399a3ed41208cc9a59d10303745afa9b2ded07b96ab266fe65277923f8cc9c11c10f158e23721d50c0b04915b86d404c2cf733f67c074fdf30c2affb688a7f78fcd39a55cdbd2f6c19f69c806fa02fb2096741f588a32d894a0f6e53b84bb31fe8755c9d8cef6d5fa856ebe8b54cf3adbf4202bb7d2bdc0b8e33b5752ba36d6adecd7a6f8eed79924bbee16e81f84ebcb790302516310ac084ddba3a9d15ac81f69945279d84e4f61459808bc9ca3532d3ac07e6ae3ec056871556909c49ee4b1b99a353e0ae9b54e36038372d3ae7f4e7d3e3490872b404dde04b60194265539f262f55e536c09a4b078d18f163dd4ed6f35eed62f5be06d188e59dbf891a7aa956ac0884f820708ff480733647b0ad3f7d24141c',
# #     # 'w': "a4f21e1b3a35ab9321d5e3703a02c68bf52662f3872de38f1cd38f79597c1932751d47d432438465f30e7c993fa64c609cae82384af61b3a6bf241c969c99642aed502b321d97d7d1785e1e49098cf9e6f3f3341150c4052990d766eb8028a6cafd1ef53e6ad6480da817141ec849c6af55dd86dfc9a9405c8a6f375b465189dde09fea00617b2e8d1e37c1ea27d4e8744977a99f8e5c6e5b9d7812c011a6e413e3fac7755fb8a8e198e2f3c78c2d2a2b0cd71b9bd3d0f4de99752197978c49ef7beeed40b21343dcc1788981e533cc8f938de1e0975397f7521391ee4a2124f91655fae00afd1d801a4a444672228e1640b784a25338202bd7c5f9e5257c68945423feddbd1261f83b5b4f64a79fe74e697fc129989323f1ca19759eec03b05bbd724b20c9c1dafeabd5a82d506a15c8e4d32f712f8568c3ee1d97a2c921a73fc999dd0a17ece67420b15cd0a9f3398471b974cabb05ddbb753c57c7f7e65fdf49e07ad4f8e2f10b37a173d5bf96edec90b7ab2d90741e6f2baa9eb276b712ae8a93a7472680a3bd085a08a244b368c042b4aefa452df57ef3e8e28c87c3161ad2f930df0ced88b6289343a9867ca6d8ffe5162e4b602790ec415d728a7b720e06baf61dd27ee4e6f97d430a60b3842b52aba560aeaaa83a055c16b1571772ef7d3a7a95171e7ce17cd4ea3f8ff70b0eafac0ea6aa33c873088f557a5369416fdd86b2b785f8e85f4cedcd11ce8b13aba2b9548592f11c7ccde21b660ca77b3",
# #     # 'w': "24a4c5e7d6e8d67d35aea28c6ac05c3513a4e673da646a30f2c337c222dc843ce8179ee5db6fb27af6cb0f4b9f5313734ee1d787fa76f3cd7d182e40697762829535b563cf656fce6cca06f07269a58e7320dbc732d6ae46e90b40df74e6f1ef5c0bc43dc7ce4e17b8c03f93d481be3a77589a7b0b8ebb380080a38a8e1131e9c415dba0a67de1b37f3fbfdf5e36b00075a1f7e7dc4b176009f762cfc414218fc790e1e0fc43d2c22dc39314c4668a4cabb6787e394e0858854aa1322d9d694d1c68f495786803bb5c0cb7a7b383abd8fe0b26f28def450e3d8c0c1978bcaa358524e32b84f6dc020a83f356d07897dd7d81fe7db515540ac354e978862d745f14ce3d25b3023aa81ff1507204c8d36efbec4d15f65d4d443c7990e3728fa05b843dc6ceec9af921be6a5ab37dbdc5ed9db4bf238e7ad795a280923d62e00d4186bbe77e69749354cbdd470425b150105b1149b1407a94d6acf4b883111c75d3093cc1ddfa3fb271f4727df920e3ca12fbe82c93a6107a6b89b56cb5349c811913b8456ebbf7a3b2ced53d95f3a15e2ca86b61254d124de0e71bcef9a67b92ac5749a505bd69c1b7bf1599eae72d1983eec9b0b35756b03eb3dd8400ab9cf7deb2058b0d4e594bfe3f8bf60b5eb5ff9967cad3e95c51dd91563abab3f74bcf345d56799dd4937c3a64a539d60047c835802af7db30b112c633fabe85c0ade84473edb84bc7d117997713c8f1a31adf4aaad5328df11245bd290c658bcd48f676",
# #     # 'callback': 'geetest_1668845512522',
# # }
# #
# # resp = session.get('https://gcaptcha4.geetest.com/verify', headers=headers, params=params).text
# # print(resp, "-----------------------")
#
#
# resp = response.text
# data = json.loads(resp[1:-1])['data']
# # pprint.pprint(data)
#
# payload = data['payload']
# process_token = data['process_token']
# captcha_id = data['seccode']['captcha_id']
# captcha_output = data['seccode']['captcha_output']
# gen_time = data['seccode']['gen_time']
# lot_number = data['seccode']['lot_number']
# pass_token = data['seccode']['pass_token']
# data = {
#     "page": "1",
#     "pageSize": "50",
#     "albumId": "100515059",
#     "onSale": "1",
#     "order": "1",
#     "lot_number": lot_number,
#     "captcha_output": captcha_output,
#      "pass_token": pass_token,# 变化
#     "gen_time": gen_time,   # 变化
#     "captcha_id": "32727fa8d208a82e46754c2e5055a679",# 不变化
#     "captcha_key": "2290891d5795f250f4befbe5712efc85",# 不变化
# }
# url = "https://api-h5-tgw.ibox.art/nft-mall-web/v1.2/nft/product/getProductListByAlbumId"
# headers = {
#     "X-WX-EXCLUDE-CREDENTIALS": "unionid, cloudbase-access-token, openid",
#     "X-WX-REGION": "ap-beijing",
#     "X-WX-GATEWAY-ID": "gw-1-1g2n1gd143d56b56",
#     "HOST": "api-h5-tgw.ibox.art",
#     "Accept-Language": "zh-CN",
#     "IB-DEVICE-ID": "11582baf51704c07af7b0a987ed57ef5",
#     "IB-TRANS-ID": "8ceb539dcf3641dd86e61bedb4854478",
#     "x-cloudbase-phone": "",
#     "IB-PLATFORM-TYPE": "web",
#     "content-type": "application/json",
#     "User-Agent": "",
# }
# # resp = session.get(url,headers=headers,params=data)
# # print(resp.status_code)
# # print(resp.text)
#
#
#
# headers = {
#     'Connection': 'keep-alive',
#     'Pragma': 'no-cache',
#     'Cache-Control': 'no-cache',
#     'X-WX-USER-TIMEOUT': '30000',
#     'X-WX-LIB-BUILD-TS': '1655460325335',
#     'X-WX-ENCRYPTION-TIMESTAMP': '1668951044188',
#     'X-WX-REQUEST-CONTENT-ENCODING': 'JSON',
#     'sec-ch-ua-mobile': '?0',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
#     'Content-Type': 'application/octet-stream',
#     'X-WX-RESPONSE-CONTENT-ACCEPT-ENCODING': 'PB, JSON',
#     'X-WX-ENCRYPTION-VERSION': '2',
#     'X-WX-COMPRESSION': 'snappy',
#     'sec-ch-ua': '^\\^',
#     'sec-ch-ua-platform': '^\\^Windows^\\^',
#     'Accept': '*/*',
#     'Origin': 'https://www.ibox.art',
#     'Sec-Fetch-Site': 'cross-site',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Dest': 'empty',
#     'Referer': 'https://www.ibox.art/',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
# }
#
# params = (
#     ('token', token),
# )
#
# data = {
#   '^^\x9E^\xFE^\xC5^\xDB^\x88^\n\nm^\x01^\xC5^]^\xB1^\xFF^\xCB^\x9Ccn^\xEB^\x05i^\xD0\xA0\x0B^\xAD^\xF1^\xBCTFx^\x1B^\xEA^\x98USL^\xE4^\xE3^\xB0^\xE5^\xB8': '^\b^\xA3^\xCC^\x83^\x1APE^\xACuh^\xF2^\x8A^\xA5v3^\xB6^\x96^\xB3^\x0E\'^\xF2^\xAE/b^]oOa^\xA3^\x19^\xCD?r^\xBBWD^\xC1^\xC0^\x95^\xD1^\x16^\xE2^\x02^\xBF ^\xF6^\xDC;gl^\x0F^\x87^\x8F/Z5^\xDC^$j0I^\xEA;/H^\xDC^\x98^$^\x81^\xD2^\x9D^\x80^\xF8^\x88^^^\xF9^\x1C=^\x8FjB^\x9Ei^< ^\x0F^\xA2/^$^\x8C^\x18^\xBD^\xD1^\x1D^[^\xE7^{^\x07Q^\xEC^\xDE\t^\x94T^\x01^\x9F^\xCC^\xCA^\xFE ^\x96^\xFBp7-^\xB5^'
# }
#
# response = session.post('https://web-001.cloud.servicewechat.com/wxa-qbase/container_service', headers=headers, params=params, data=data)
# resp = response
# print(resp.status_code)
# print(resp.content)

