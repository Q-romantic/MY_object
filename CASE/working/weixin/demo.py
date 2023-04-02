# -*- coding: utf-8 -*-
import json
import pprint
import re
import time
import parsel
import requests

""" 解释参考：https://zhuanlan.zhihu.com/p/257833704 """
""" https://github.com/wnma3mz/wechat_articles_spider/blob/master/docs/使用的微信公众号接口.md """

# url = 'https://mapi.guazi.com/car-source/carList/pcList'
# for page in range(1, 6):
#     params = {
#         'page': page,
#         'pageSize': '20',
#         'city_filter': '12',
#         'city': '12',
#         'guazi_city': '12',
#         'deviceId': 'd4500b77-400c-44bd-8f79-cbded611069a',
#     }
#     response = requests.get(url, headers=headers, params=params)
#     pprint.pprint(response.json())

url = 'https://mp.weixin.qq.com/mp/profile_ext'

headers = {
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5',
    # 'cache-control': 'no-cache',
    'cookie': 'rewardsn=; wxtokenkey=777; wxuin=720440125; lang=zh_CN; appmsg_token=1170_dcRZFyNIaQw5aN2sKD_2jHILZvbflD4HjlEa0rB6kvtmPgInG2bh0cpf4neHtlyMjeOi9p1NU4A2suGy; devicetype=iPhoneiOS15.3.1; version=18001729; pass_ticket=leGdSyltPQnsqEbDqgN2OsN3ExrKx7/o1WcEO5U06V23blj65f48zotOSgaqYLK; wap_sid2=CL2WxNcCEooBeV9ISXFuQ3hROUlnR3piUUtaNG45Tlo3OEpfVHVOa20tRkFIM0gtZnRSNmtVZi1RajBsek1Ma19sRGd6dXVOWDZzdjFKOTByUTdHeERFUjhkZmZGTFNaYU1MT25qVm9UMkg0RklxSS1SdlJsM21TNGxKNFBYWlNDQXBKR2JmV1o4cjQyOFNBQUF+MIzjppUGOA1AlU4=',
    # 'cookie': 'fqm_pvqid=59145f96-c8fd-405f-baa1-c13a9ffa2e23; pgv_pvid=3524282308; tvfe_boss_uuid=656089f518af6f33; RK=65e4yxS0Tt; ptcz=13ecf9647a609268b8bfb54b2996bc0d4cea49ab02ea188de55ffa743391eff0; pgv_info=ssid=s5190590572; video_omgid=1fc07a1f063abab5; vversion_name=8.2.95; _qpsvr_localtk=0.4159291322884666; rewardsn=; wxtokenkey=777; wxuin=720440125; lang=zh_CN; wwapp.vid=; wwapp.cst=; wwapp.deviceid=; ua_id=F3pAoe5J2TJIpoSqAAAAAJN6i1N72buXok6tGjiw2K0=; devicetype=iPhoneiOS15.3.1; version=18001729; pass_ticket=leGdSyltPQnsqEbDqgN2OsN3ExrKx7/o1WcEO5U06V23blj65f48zotOSgaqYLK; wap_sid2=CL2WxNcCEooBeV9IR2RJYmxlcmV5TThWTEVSQUxQOEVtWUZBVEg5QnplbHhFb1B3bWRmUmVkTkd3ZUREb2xNLTI2cjN1ci1NZEEwckdaalYzcE10TkdrOENCMnVHQlFOc0o2OVNIT09RcDdnVnY4RVpfbEVnOVdxR2NhR0hyRDNxYlVpMHJPa0J2WW1XOFNBQUF+MM2XpZUGOA1AlU4=; uuid=e498ee752175a61de2e3647927a3c57c; appmsg_token=1169_NZjXnqa+Wln7d+1EuXMfnMNzbmnyLdHMgqC4r0hCsQWKEnM9mlriFpc7TzxRAMqnJ2NnLMqo-FLAlHRD',
    # 'pragma': 'no-cache',
    # 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Microsoft Edge";v="102"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'sec-fetch-dest': 'document',
    # 'sec-fetch-mode': 'navigate',
    # 'sec-fetch-site': 'none',
    # 'sec-fetch-user': '?1',
    # 'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',

}


def get_detail_info(url):
    response = requests.get(url)
    # print(response.text)
    jpeg_url = re.findall('data-type="jpeg" data-w="1080" data-src="(.*?)"', response.text)
    print(jpeg_url)


for page in range(0, 200, 10):
    params = {
        'action': 'getmsg',
        '__biz': 'MzU0MzU4OTY2NQ==',
        'offset': page,
        'count': '20',
        # 'is_ok': '1',
        # 'scene': '',
        # 'uin': '777',
        # 'key': '777',
        # 'pass_ticket': '',
        # 'wxtoken': '',
        # 'appmsg_token': '1169_5tbEwfU4O2HfZYOB1wvq7fS1bvENpylYpXcQxw~~',
        'appmsg_token': '1170_yA1%2FjZPMjWAK31t10X1NvboVti97t_j6Ay0YdA~~',  # 注意：cookie和这个参数有失效时间，可重新抓包获取
        # 'x5': '0',
        'f': 'json',
    }
    response = requests.get(url, headers=headers, params=params)
    print(response.text)
    print(response.url)
    data = response.json()['general_msg_list']
    data = json.loads(data)['list']
    # pprint.pprint(data[1])
    for index in data:
        content_url_1 = index['app_msg_ext_info']['content_url']
        title_1 = index['app_msg_ext_info']['title']
        datetime = index['comm_msg_info']['datetime']
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(datetime)))
        print(title_1, content_url_1)
        for multi_app_msg_item_list in index['app_msg_ext_info']['multi_app_msg_item_list']:
            content_url = multi_app_msg_item_list['content_url']
            title = multi_app_msg_item_list['title']
            print(title, content_url)
            # get_detail_info(content_url)
        #     break
        # break
    print(len(data))
    break















"""
统一请求部分
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
}
输入账号密码的url
https://mp.weixin.qq.com/cgi-bin/bizlogin?action=startlogin

# 使用post方法
# headers 需要添加host、origin、referer
data = {
    "username": username,
    "userlang": "zh_CN",
    "token": "",
    "pwd": pwd,
    "lang": "zh_CN",
    "imgcode": "",
    "f": "json",
    "ajax": "1"
}
获取登录二维码的url
https://mp.weixin.qq.com/cgi-bin/loginqrcode?action=getqrcode&param=4300&rd=928

# 使用get方法
# 直接请求，用二进制进行读写操作
获取token的url
https://mp.weixin.qq.com/cgi-bin/bizlogin?action=login

# 使用post方法
# headers需要更改referer
referer = "https://mp.weixin.qq.com/cgi-bin/bizlogin?action=validate&lang=zh_CN&account={}".format(
username)
data = {
    "userlang": "zh_CN",
    "token": "",
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
}
# token截取
token = res["redirect_url"].split("=")[-1]
获取公众号信息
https://mp.weixin.qq.com/cgi-bin/searchbiz

# 返回的json
{
    'alias': 公众号别名,
    'fakeid': 公众号唯一id,
    'nickname': 公众号名称,
    'round_head_img': 公众号头像的url,
    'service_type': 1公众号性质
}
获取公众号文章信息
https://mp.weixin.qq.com/cgi-bin/appmsg

# 请求方法为get, 具体请求参数见代码
{
    'app_msg_cnt': # 公众号发文章总数,
    'app_msg_list': 　# 一个数组(参看GetArticles),
    'base_resp': {
    'err_msg': 'ok',
    'ret': 0
    }
    'list': [
        {
            'aid': '2650949647_1',
            'appmsgid': 2650949647,
            'cover': # 封面的url
            'digest': # 文章摘要,
            'itemidx': 1,
            'link': # 文章的url,
            'title': # 文章标题,
            'update_time': # 更新文章的时间戳
        },
    ]
}
获取文章评论信息
https://mp.weixin.qq.com/mp/appmsg_comment

# 请求方法为get, 具体参数见代码，不需要cookie和appmsg_token，但是需要comment_id,获取方法见下
{
    "base_resp": {
        "errmsg": "ok", 
        "ret": 0
    }, 
    "elected_comment": [
        {
            "content": # 用户评论文字, 
            "content_id": "6846263421277569047", 
            "create_time": 1520098511, 
            "id": 3, 
            "is_from_friend": 0, 
            "is_from_me": 0, 
            "is_top": 0, # 是否被置顶
            "like_id": 10001, 
            "like_num": 3, 
            "like_status": 0, 
            "logo_url": "http://wx.qlogo.cn/mmhead/OibRNdtlJdkFLMHYLMR92Lvq0PicDpJpbnaicP3Z6kVcCicLPVjCWbAA9w/132", 
            "my_id": 23, 
            "nick_name": # 评论用户的名字, 
            "reply": {
                "reply_list": [ ]
            }
        }
    ], 
    "elected_comment_total_cnt": 3, # 评论总数
    "enabled": 1, 
    "friend_comment": [ ], 
    "is_fans": 1, 
    "logo_url": "http://wx.qlogo.cn/mmhead/Q3auHgzwzM6GAic0FAHOu9Gtv5lEu5kUqO6y6EjEFjAhuhUNIS7Y2AQ/132", 
    "my_comment": [ ], 
    "nick_name": 当前用户名, 
    "only_fans_can_comment": false
}
获取comment_id
直接请求文章的url

```python
# 请求方法为post
# 请求data参数如下，可以无需cookie
data = {
    "is_only_read": "1",
    "is_temp_url": "0",
}
# 获取返回的text, 使用正则进行过滤。具体见代码
``` 
获取文章点赞数和阅读数
https://mp.weixin.qq.com/mp/getappmsgext

# 请求方式为post, 请求data参数同上，params参数和具体的请求见代码。需要appmsg_token和cookie
{
    'advertisement_info': [],
    'advertisement_num': 0,
    'appmsgstat': {'is_login': True,
    'like_num': 12, # 点赞数
    'liked': False,
    'read_num': 288,  # 阅读数
    'real_read_num': 0,
    'ret': 0,
    'show': True},
    'base_resp': {'wxtoken': 2045685972},
    'reward_head_imgs': []
}
"""