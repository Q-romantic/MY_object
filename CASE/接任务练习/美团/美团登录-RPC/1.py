# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/14  014 上午 10:50
@Author  : Jan
@File    : 1.py
"""
import base64

import execjs
import parsel
import requests
import rsa
from binascii import b2a_hex, a2b_hex
from urllib.parse import urlencode

""" {} """

# https://cloud.tencent.com/developer/article/1947238


# headers = {"User-Agent": get_ua()}
# proxies = (lambda ips: {'http': r'http://' + ips, 'https': r'http://' + ips})(get_ip())

# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
# proxies = {}
#
#
#
# url = ''
# response = requests.get(url, headers=headers, params={}, data={}, proxies=proxies)
# data = response.text
# print(data)
# print(response)
# sel = parsel.Selector(response.text)
# a = sel.xpath('//div[@id="u1"]/a/text()').getall()
# print(a)
# xml = etree.HTML(response.text)
# a = xml.xpath('//div[@id="s-top-left"]/a/@target')
# print(a)
# sel = fromstring(resp.text)
# a = sel.xpath('//div[@id="u1"]/a/text()')
# print(a)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

js_fn = \
    """
    function X(e) {
        for (var n = ""; n.length < e;)
            n += Math.random().toString(36).substr(2, 1);
        return escape(n)
    }
    """
z = execjs.compile(js_fn)
f = lambda x: z.call('X', x)
logan_session_token = f(20)

js_fn = \
    """
    function ir() {
        for (var t = +new Date, e = 0; t === +new Date && e < 200;)
            e++;
        return t.toString(16) + e.toString(16)
    }
    screen = {
        availHeight: 1032,
        availLeft: 0,
        availTop: 0,
        availWidth: 1920,
        colorDepth: 24,
        height: 1080,
        pixelDepth: 24,
        width: 1920,
    }
    r = (screen.height * screen.width).toString(16)
    get__lxsdk_cuid = function (ua) {
        le = ua;
        _lxsdk_cuid = "".concat(ir(), "-").concat(Math.random().toString(16).replace(".", ""), "-").concat(function () {
            var t, e, i = [], n = 0;
        
            function r(t, e) {
                for (var n = 0, r = 0; r < e.length; r++)
                    n |= i[r] << 8 * r;
                return t ^ n
            }
        
            for (t = 0; t < le.length; t++)
                e = le.charCodeAt(t),
                    i.unshift(255 & e),
                4 <= i.length && (n = r(n, i),
                    i = []);
            return (n = 0 < i.length ? r(n, i) : n).toString(16)
        }(), "-").concat(r, "-").concat(ir())
        
        return _lxsdk_cuid
    }
    """
zz = execjs.compile(js_fn)
f = lambda x: zz.call('get__lxsdk_cuid', x)
_lxsdk_cuid = f(headers.get('User-Agent'))

js_fn = \
    """
    qn = function () {
    return Math.random()
    }

    function or() {
        return Math.floor(1 + 65535 * qn()).toString(16).substring(1)
    }

    function ar() {
        var t = []
            , e = +new Date;
        return t.push(e.toString(16)),
            t.push(or()),
            t.push(or()),
            t.push(or()),
            t.join("-")
    }

    get__lxsdk_s = function (x) {
        _lxsdk_s = [ar(), "%7C", "%7C", x].join("")
        return _lxsdk_s
    }
    """
zzz = execjs.compile(js_fn)
_lxsdk_s = lambda x: zzz.call('get__lxsdk_s', x)

url = 'https://passport.meituan.com/account/unitivelogin'
response = requests.get(url, headers=headers)
sel = parsel.Selector(response.text)
csrf = sel.xpath('//div[@class="form-field form-field--ops"]/input[2]/@value').get()
# print(csrf)

cookies = response.cookies
# print(cookies)
uuid = dict(cookies)['uuid']
# cookies.update({"logan_session_token": logan_session_token})
# cookies.update({"SERV.sig": "rbfHkMpolNSrIgwXH32sJOs81O8"})
# cookies.update({"LREF.sig": "WlMS4JoDHBUvp6jSCTzPexQlQew"})
# cookies.update({"mtcdn": "K"})
# cookies.update({"_lxsdk_s": _lxsdk_s(12)})
# cookies.update({"_lxsdk_cuid": _lxsdk_cuid})


params = {
    "risk_partner": "0",
    "risk_platform": "1",
    "risk_app": "-1",
    "uuid": uuid,
    "token_id": "DNCmLoBpSbBD6leXFdqIxA",
    "service": "www",
    # "continue": "https%3A%2F%2Fwww.meituan.com%2Faccount%2Fsettoken%3Fcontinue%3Dhttps%253A%252F%252Fwww.meituan.com",
    "continue": "https://www.meituan.com/account/settoken?continue=https%3A%2F%2Fwww.meituan.com"
}


def get_h5Fingerprint_and_password(s):
    url = "https://passport.meituan.com" + "/account/unitivelogin"
    # 将字典转成URL请求参数
    result = urlencode(params)
    # print(result)
    rpc_url = "http://127.0.0.1:5620/business-demo/invoke"
    rpc_params = {
        "group": "rpc-test",
        "action": "action",
        "url": url + "?" + result,
        "password": s,
    }
    res = requests.get(rpc_url, params=rpc_params).json()
    # print(res)
    clientId = res['clientId']
    h5Fingerprint = res['getH5fingerprint']
    password = res['getpassword']
    # print(clientId)
    # print(h5Fingerprint)
    # print(password)
    return h5Fingerprint, password


# 方法一：加密方法改写
def get_password(s):
    def rsa_encrypt(data, pubkey):  # 加密
        ciphertext = rsa.encrypt(data.encode(), pubkey)
        return b2a_hex(ciphertext).decode()

    pubkey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCRD8YahHualjGxPMzeIWnAqVGMIrWrrkr5L7gw+5XT55iIuYXZYLaUFMTOD9iSyfKlL9mvD3ReUX6Lieph3ajJAPPGEuSHwoj5PN1UiQXK3wzAPKcpwrrA2V4Agu1/RZsyIuzboXgcPexyUYxYUTJH48DeYBGJe2GrYtsmzuIu6QIDAQAB"
    pubkey = f'-----BEGIN PUBLIC KEY-----\n{pubkey}\n-----END PUBLIC KEY-----'
    pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(pubkey.encode())
    ency_text = rsa_encrypt(s, pubkey)
    password = base64.b64encode(bytes.fromhex(ency_text)).decode()
    return password


password = '123'
h5Fingerprint, password = get_h5Fingerprint_and_password(password)
# password = get_password("123")


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    # "X-CSRF-Token": csrf,
    "X-Requested-With": "XMLHttpRequest"
}

data = {
    "countrycode": "86",
    "email": "13688888888",
    "password": password,
    "origin": "account-login",
    "csrf": csrf,
    # "requestCode": requestCode,
    "requestCode": "",
    "responseCode": "",
    # "responseCode": responseCode,
    "h5Fingerprint": h5Fingerprint,
    "device_name": "",
    "device_type": "Chrome",
    "device_os": "Window",
    "sdkType": "pc"
}

url = 'https://passport.meituan.com/account/unitivelogin'
response = requests.post(url, headers=headers, params=params, data=data, cookies=cookies)
data = response.text
print(data)
print(response)
