# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/23  023 上午 11:57
@Author  : Jan
@File    : 优酷作者主页.py
"""

""" {} """

import requests, time, execjs, json, hashlib, re
from jsonpath import jsonpath

# 此处可自定义
init = {
    # 'homepage': 'https://www.youku.com/profile/index/?spm=a2h0c.8166622.PhoneSokuUgc_8.1&uid=UNTc2MjIzNDYyNA==',
    'homepage': 'https://www.youku.com/profile/index?spm=a2hcb.profile.app.5~5!2~5~5!2~5!2~5!2~5~5~5!2~A&uid=UODI5MTE3MjU2OA==',
    'keyword': "小",
    'pg': 1,
    "pz": 20,
}
now = lambda: str(int(time.time() * 1000))
jsonpIncPrefix = now()
response = requests.get(init.get("homepage"))
data = response.text
ytid = re.search(',"ytid":"(.*?)",', data).group(1)


# https://g.alicdn.com/youku-node/pc-pages-v2/1.4.4/static/js/profile.chunk.js --> aaid
def get_aaid(a):
    index = open('1.js', 'r', encoding='utf-8')
    js = execjs.compile(index.read())
    a = js.call('get_aaid', a)
    return a


utdId = "H+98HE4ddVwCAT0w0m6bwJ8n"  # 其内容可有可无，来自 getCookie("cna")
aaid = get_aaid(now() + utdId)
# print(aaid, jsonpIncPrefix, now())
g = "23774304"
token = ""
data = {"searchType": 1, "pg": init["pg"], "pz": init["pz"], "site": 1, "appCaller": "pc_user", "appScene": "user_page_search", "sdkver": 315,
        "aaid": aaid, "utdId": utdId, "searchFrom": 1, "sourceFrom": "home",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36", "userType": "guest",
        "userId": "", "keyword": init["keyword"], "sceneContentId": ytid}

# https://g.alicdn.com/mtb/lib-mtop/2.4.2/mtop.js --> sign
def get_sign(token, i):
    s = token + "&" + i + "&" + g + "&" + json.dumps(data)
    m = hashlib.md5(s.encode('utf-8'))
    return m.hexdigest()


params = lambda token, time, B: {
    "jsv": "2.4.2",
    "appKey": g,
    "t": time,
    "sign": get_sign(token, time),
    "api": "mtop.youku.soku.yksearch",
    "v": "2.0",
    "dataType": "jsonp",
    "jsonpIncPrefix": jsonpIncPrefix,
    "type": "jsonp",
    # "callback": f"mtopjsonp{jsonpIncPrefix}{B}",  # 此处为无效参数，可忽略
    "data": json.dumps(data)
}
path = "https://acs.youku.com/h5/mtop.youku.soku.yksearch/2.0/"
js_fn = \
    """
    function f(a) {
    var b = [];
    for (var c in a)
        a[c] && b.push(c + "=" + encodeURIComponent(a[c]));
    return b.join("&")
    }
    """
z = execjs.compile(js_fn)
f = lambda x: z.call('f', x)
params1 = params(token, now(), 2)
url_1 = path + "?" + f(params1)

response = requests.get(url_1)
cookies = response.cookies
# print(cookies)
# https://g.alicdn.com/mtb/lib-mtop/2.4.2/mtop.js --> a.token.split("_")
token = cookies.get('_m_h5_tk').split('_')[0]
# print(token)

params2 = params(token, now(), 3)
url_2 = path + "?" + f(params2)
response = requests.get(url_2, cookies=cookies)
# print(response.text)
res = json.loads(response.text[10:-1])
# print(res)
# for node in res['data']['nodes'][0]['nodes']:
#     for data in node[0]:
#     break

titles = jsonpath(res, '$..displayName')
srcs = jsonpath(res, '$..videoId')
imgs = jsonpath(res, '$..newImgInfo.thumbUrl')
longtimes = jsonpath(res, '$..rightBottomText')
publishTimes = jsonpath(res, '$..publishTime')
for title, src, img, longtime, publishTime in zip(titles, srcs, imgs, longtimes, publishTimes):
    src = f"https://v.youku.com/v_show/id_{src}.html"
    print(title)
    print(src)
    print(img)
    print(longtime)
    print(publishTime)
    print('---' * 30)
