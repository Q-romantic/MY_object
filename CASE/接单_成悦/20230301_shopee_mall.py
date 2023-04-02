# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/1  001 下午 17:07
@Author  : Jan
@File    : 20230301_shopee_mall.py
"""
import execjs

""" {} """

import requests
from lxml import etree
import pprint
import parsel
import random
from working.all_tools.tools import get_ua
from working.all_tools.tools import get_ip

# from working.all_tools.tools import curl_to_python

""" {} """

# headers = {"User-Agent": get_ua()}
# proxies = (lambda ips: {'http': r'http://' + ips, 'https': r'http://' + ips})(get_ip())

# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
proxies = {}

params = {
    "itemid": "17611169935",
    "shopid": "24681653"
}

js_fn = \
    """
    // https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg//assets/bundle.334209968403acb9.js
    // "X-CSRFToken": V(r, n)
    H_A8 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    csrftoken = function (e, t = H_A8) {
        let n = "";
        for (let r = 0; r < e; r++) {
            const e = Math.floor(Math.random() * t.length);
            n += t.substring(e, e + 1)
        }
        return n
    }(32)
    // console.log(csrftoken)
    
    Ta = function () {
        return new Date(Date.now())
    }
    Ua = function () {
        return Ta().getTime()
    }
    b = Math.round(2147483647 * Math.random())
    ts = Math.round(Ua() / 1E3)
    _gcl_au = "1.1." + [String(b), ts].join(".")
    // console.log(_gcl_au)
    
    _ga_CB0044GVTM = "GS1.1." + ts + ".1.0." + ts + ".60.0.0"
    // console.log(_ga_CB0044GVTM)
    
    b = Math.round(2147483647 * Math.random())
    _ga = "GA1.1." + [String(b), Math.round(Ua() / 1E3)].join(".")
    // console.log(_ga)
    
    
    get_cookies = function () {
        cookies = {
            "csrftoken": csrftoken,
            "_gcl_au": _gcl_au,
            "_ga_CB0044GVTM": _ga_CB0044GVTM,
            "_ga": _ga,
        }
        return cookies
    }
    // console.log(get_cookies())
    """
z = execjs.compile(js_fn)
Cookies = z.call('get_cookies')
url = 'https://shopee.ph/api/v4/itemcard/set/elements?set_ids=1'
response = requests.get(url)
cookies = dict(response.cookies)
cookies.update(Cookies)

# cookies.update({"_QPWSDCXHZQA": "8b3e5adb-dce0-44a1-c565-7979a6cd7401"}) ??? js代码混淆严重，后续分析

headers = {
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5",
    "af-ac-enc-dat": "AAcyLjUuMy0yAAABhpxvi00AAAw4AoAAAAAAAAAAAsd6dMgubQZggd7b95AjwU6tLynmCw1e2zkbICMjy+cYi27Y0+a5OMQi1EvLALu2hfxigpXCxc01hPIrcdLMIahX/gFdRyR+f9qpnYRQEwLc++Ab9b7bUTZsY/iWdlBElO+vdLLi0npRYQN/Vdf9bl98mKNnRyR+f9qpnYRQEwLc++Ab9dLR0iVpSnVbQkfWXM2rAcijPFs13SwHHQaeeumHIvrCXKo8sCf4Rf8zqP+fZJAzmCJYpQy8lG5fkeEDlEX2WdDwZa/TgisZHMMNnFYD1FdWBayVwSyGafNOD4lT/5qnVgOF6D1bJu4NzJZPTNA5Z1mJmPbv+lH8SwOfhVz5/VPn0RySdhyhKzToeXrsCr/7VtvXqTHiAIOhfdRSDm1pQOHHCY88UtccsTm1/h2/nuAs/s8k66IJxjEzQchTdxzMI6djBDNOoqYIPfEGkdJ9lDEyiC4+C0k5JZzLdJ6g57SDgcCXowjhsliz3Z/Fs4l3dpf/NhMnw8f21UXD2mkb2JuyyLCD+z6tPHxk5FqNW+djihhDfBJbeJC9W8Le/FVyxfm5zHMDo/4eXEjxrR7QQhOX/zYTJ8PH9tVFw9ppG9ibQhok4rnhZ2Is+jDlbRCpcvfrFVbQcvMfLxtsud6f16CxzZdt91zaCm3/5olQ6pU8f5ESVUgGfkx5dL8vIvGMqe9HHSiJmzO9FlD4WCi4pVZSbzV4gJfhPFy2nqwdOqlWc/bUKf8jA3zBJLKT0OHdDU9eMQYZbLcMxVW6RkoOz7YUharmI1FtSVfSR7XL6+ZyPioIt5ly3B8R21NMbHwxt1tOBrNBWNVzJsqY1qg8wr2wXTv/RktVgQjJUnm3r7Ar",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "referer": "https://shopee.ph/product/24681653/17611169935",
    "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Microsoft Edge\";v=\"110\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57",
    "x-api-source": "pc",
    "x-csrftoken": Cookies.get('csrftoken'),
    "x-requested-with": "XMLHttpRequest",
    "x-shopee-language": "en"
}

url = 'https://shopee.ph/api/v4/item/get'
response = requests.get(url, headers=headers, params=params, cookies=cookies, proxies=proxies)
data = response.text
print(data)
print(response)
# print(response.url)
# sel = parsel.Selector(response.text)
# a = sel.xpath('//div[@id="u1"]/a/text()').getall()
# print(a)
# xml = etree.HTML(response.text)
# b = xml.xpath('//div[@id="s-top-left"]/a/@target')
# print(b)













'''
商品链接：https://shopee.com.my/product/264070136/5637247041
'''
# "if-none-match-" = "55b03-" + md5("55b03" + md5(url.split('?')[-1]) + "55b03" )
# def get_xiapi_matche(url):
#     import hashlib
#     data = url.split('?')[-1]
#     str_request = f"55b03{hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()}55b03"
#     if_none_match = f"55b03-{hashlib.md5(str_request.encode(encoding='UTF-8')).hexdigest()}"
#     return if_none_match
# url = 'https://shopee.com.my/api/v4/product/get_shop_info?shopid=264070136'
# headers = {
#     "if-none-match-":get_xiapi_matche(url),
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57",
# }
# response = requests.get(url, headers=headers, params=params, cookies=cookies, proxies=proxies)
# data = response.text
# print(data)
# print(response)
