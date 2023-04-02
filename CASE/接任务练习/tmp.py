# -*- coding: utf-8 -*-
"""
@Time    : 2022/11/9  009 上午 10:38
@Author  : Jan
@File    : url_to_doc.py
"""
import copy
import pprint
import time

import parsel
import pysnooper
import requests

""" {} """

headers = {
    "cookie": "lastCity=101010100; wd_guid=d5acd83c-4117-47fb-be86-efbdff15f84c; historyState=state; _bl_uid=q1l4IbjadkXatLcevmR34aqvj6Fg; __zp_seo_uuid__=9357ac16-ae0d-43bd-ab76-a2939b00471a; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1673429481,1674450671; boss_login_mode=app; wt2=DRaDczAo0MC17-8Cz7MvUgX9_j_tkm0p1skDGjftc9Kp4xO7H_b7JAaft_-LgLx4pmmLiGTdUIv3fJwCN6IlrwQ~~; wbg=0; __l=r=https%3A%2F%2Fwww.so.com%2Flink%3Fm%3DbYLUfDTIY%252FhlB7jNkchhcBx9aJK2TOWaFDeSnGZCNjVgKCDVF6yHk2UEJZab7fYucYQJkFI35D10OkP9z5pHQf6Uux5RyzQ9O8nUGGybkCP1KTkZjFH4rrtY6Zk8mtoKNCcz6ps89hee1tBZSEFxGM4KnZqQal6%252BSL9cY5w%253D%253D&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D&s=3&g=&friend_source=0&s=3&friend_source=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1674450701; __zp_stoken__=3f6deWzQZbBhqEmY2KFJtAFgYdl5ebHwrLwEYLXsoSWxjSyM3BnwRDHVLclBKQHd0NldNXUh6ZQQlZgxnOnN9WzI7V15QC20MPxpMKBk7b2IWMFwJRXoeCgozKlVLFCtqdG5%2FPEcOEA1yVnw%3D; __c=1674450671; __a=76476689.1670318154.1673429481.1674450671.27.4.17.20; geek_zp_token=V1Q9MnFuT03lhgXdNuyxkdLCOz6jPXwA~~",
    # "cookie": "lastCity=101010100; wd_guid=d5acd83c-4117-47fb-be86-efbdff15f84c; historyState=state; _bl_uid=q1l4IbjadkXatLcevmR34aqvj6Fg; __zp_seo_uuid__=9357ac16-ae0d-43bd-ab76-a2939b00471a; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1673429481,1674450671; boss_login_mode=app; wt2=DRaDczAo0MC17-8Cz7MvUgX9_j_tkm0p1skDGjftc9Kp4xO7H_b7JAaft_-LgLx4pmmLiGTdUIv3fJwCN6IlrwQ~~; wbg=0; __l=r=https%3A%2F%2Fwww.so.com%2Flink%3Fm%3DbYLUfDTIY%252FhlB7jNkchhcBx9aJK2TOWaFDeSnGZCNjVgKCDVF6yHk2UEJZab7fYucYQJkFI35D10OkP9z5pHQf6Uux5RyzQ9O8nUGGybkCP1KTkZjFH4rrtY6Zk8mtoKNCcz6ps89hee1tBZSEFxGM4KnZqQal6%252BSL9cY5w%253D%253D&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D&s=3&g=&friend_source=0&s=3&friend_source=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1674450701; __zp_stoken__=3f6deWzQZbBhqEmY2KFJtAFgYdl5ebHwrLwEYLXsoSWxjSyM3BnwRDHVLclBKQHd0NldNXUh6ZQQlZgxnOnN9WzI7V15QC20MPxpMKBk7b2IWMFwJRXoeCgozKlVLFCtqdG5%2FPEcOEA1yVnw%3D; __c=1674450671; __a=76476689.1670318154.1673429481.1674450671.27.4.17.20; geek_zp_token=V1Q9MnFuT03lhgXdNuyxkdLim36zjezQ~~",
    # "pragma":"no-cache",
    # "referer":"https://www.zhipin.com/web/geek/chat?id=7f0cf42596bb9cd11HZ92d26E1s~",
    # "sec-fetch-dest":"empty",
    # "sec-fetch-mode":"cors",
    # "sec-fetch-site":"same-origin",
    # "token":"4G0coA5G9VD6ptJ",
    # "traceid":"E53BB15F-00C5-4CB6-AA5D-51671B5160EC",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    # "x-requested-with":"XMLHttpRequest",
    # "zp_token":"V1Q9MnFuT03lhgXdNuyxkdLCOz6jPXwA~~"
}


def get_historyMsg(bossId, securityId):
    url = 'https://www.zhipin.com/wapi/zpchat/geek/historyMsg'
    params = {
        "bossId": bossId,
        "groupId": bossId,
        "maxMsgId": "0",
        "c": "20",
        "page": "1",
        "src": "0",
        "securityId": securityId,
        "loading": "true",
        "_t": int(time.time() * 1000)
    }
    resp = requests.get(url, headers=headers, params=params)
    # print(resp.status_code)
    # pprint.pprint(resp.json())
    messages = resp.json()['zpData']['messages'][:-1]
    for message in messages:
        try:
            pushText = message['pushText']
            if '徐先生' in pushText:
                # print("|", '{:{}>{width}}'.format(pushText, chr(12288), width=50), "|")  # 靠右对齐
                print("|", pushText.rjust(50, chr(12288)), "|")  # 靠右对齐
            else:
                print("|", pushText.ljust(50, chr(12288)), "|")
        except:
            pass


# params = {'page': 1}
# url = 'https://www.zhipin.com/wapi/zprelation/friend/getGeekFriendList.json'
# resp = requests.get(url, headers=headers, params=params)
# for result in resp.json()['zpData']['result']:
#     avatar = result['avatar']
#     brandName = result['brandName']  # 重要
#     encryptBossId = result['encryptBossId']  # 重要
#     encryptJobId = result['encryptJobId']  # 重要
#     encryptUid = result['encryptUid']  # 重要
#     filterReasonList = result['filterReasonList']
#     filtered = result['filtered']
#     friendSource = result['friendSource']
#     goldGeekStatus = result['goldGeekStatus']
#     isFiltered = result['isFiltered']
#     isTop = result['isTop']
#     itemType = result['itemType']
#     jobId = result['jobId']
#     jobSource = result['jobSource']
#     lastMessageInfo = result['lastMessageInfo']
#     lastMsg = result['lastMsg']
#     lastTS = result['lastTS']
#     lastTime = result['lastTime']
#     name = result['name']  # 重要
#     relationType = result['relationType']
#     securityId = result['securityId']  # 重要
#     sourceTitle = result['sourceTitle']
#     sourceType = result['sourceType']
#     tinyUrl = result['tinyUrl']
#     title = result['title']
#     uid = result['uid']
#     unreadMsgCount = result['unreadMsgCount']
#     # print(brandName, name, encryptBossId, securityId, sep='\n')
#     if encryptBossId == '738bb00a0457633b0X162tq8F1s~':
#         get_historyMsg(encryptBossId, securityId)
#         break
#     else:
#         pass

"""
盘锦人瑞 
陈女士 
f48763a2d410e4c31HF909y4GVs~ 
kZBoG6FwTrdJY-s1-mU6a149R3nXIcnhvukZ2WUCFmrkFk-3oMQulxyY0oOhJBj1wREYLIX6wtrOomHnbuThg-LXY6yjS_yZGyCJV-9yqVaxc28yh-P4tD6t08qOBarbR6Fhlq5toEfjjP1qtRcEoH-P-iyYbF3hw_bebMRKjsz7FJM9yKFV-rCQJGPEqNJtogxLNSTsSQzV0siP0wKxsvEEfcWVX4oqoIIANLavWAavduGLhiC2CdDPmbwg7lfavjIYW2_iI4j4vL4ct7mkpwUdh5Iny37qk5y_Qv74jQoEowHFp1eaBAhFuolU4qSMkBhKEIlv2wadszJRdtnrJGMf9PrN2xuzV19tX25OK8C5jgjF6-Hv-EKO99phL_8L59hL-URA_TBTYyycqLXzYKDhp5jeNnipkrNP_oKyWnQG7aZEx03RpY6qdgsTfVaBl1ex692aToz3cmxlJfdhL7mbWWf_DG8g7I68IflM_SMqdIz9vpKFIjL7lRphMz-wSmms
"""
url = 'https://www.zhipin.com'

# print(resp.status_code)
# print(resp.text)


url = 'https://www.zhipin.com/wapi/zppassport/get/zpToken'
headers = {
    "cookie": "wt2=DRaDczAo0MC17-8Cz7MvUgX9_j_tkm0p1skDGjftc9Kp4xO7H_b7JAaft_-LgLx4pmmLiGTdUIv3fJwCN6IlrwQ~~",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76",
}
# params = {'v': int(time.time()*1000)}
# resp = requests.get(url, headers=headers, params=params)
# print(resp.text)
# token = resp.json()['zpData']['token']
# print(token)
# for i in range(20):
#     params = {'v': int(time.time() * 1000)}
#     resp = requests.get(url, headers=headers, params=params)
#     token = resp.json()['zpData']['token']
#     print(token)
url = 'https://www.zhipin.com/wapi/zpgeek/recommend/job/list.json'
headers = {
     # "cookie":"lastCity=101010100; wd_guid=d5acd83c-4117-47fb-be86-efbdff15f84c; historyState=state; _bl_uid=q1l4IbjadkXatLcevmR34aqvj6Fg; __zp_seo_uuid__=9357ac16-ae0d-43bd-ab76-a2939b00471a; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1673429481,1674450671; boss_login_mode=app; wt2=DRaDczAo0MC17-8Cz7MvUgX9_j_tkm0p1skDGjftc9Kp4xO7H_b7JAaft_-LgLx4pmmLiGTdUIv3fJwCN6IlrwQ~~; wbg=0; __l=r=https%3A%2F%2Fwww.so.com%2Flink%3Fm%3DbYLUfDTIY%252FhlB7jNkchhcBx9aJK2TOWaFDeSnGZCNjVgKCDVF6yHk2UEJZab7fYucYQJkFI35D10OkP9z5pHQf6Uux5RyzQ9O8nUGGybkCP1KTkZjFH4rrtY6Zk8mtoKNCcz6ps89hee1tBZSEFxGM4KnZqQal6%252BSL9cY5w%253D%253D&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D&s=3&g=&friend_source=0&s=3&friend_source=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1674542833; __c=1674450671; __a=76476689.1670318154.1673429481.1674450671.35.4.25.29; __zp_stoken__=3ea8eAExZMw1ZISNgWXwocgxMXUBFYmsfYCsdazR8Jj8pf3xMZFBVNhx6BCU1WWA6R25lBjAwMB0MdwAfIUpmIUgHMmkEQj5gLQNeUBQ2PxpkCSFtKUhMaTtaBTYqAwNxBVdXZz9OTxhBZXw%3D; geek_zp_token=V1Q9MnFuT03lhgXdNuyxgcKi6z6j3Qww~~",
    "cookie":"lastCity=101010100; wd_guid=d5acd83c-4117-47fb-be86-efbdff15f84c; historyState=state; _bl_uid=q1l4IbjadkXatLcevmR34aqvj6Fg; __zp_seo_uuid__=9357ac16-ae0d-43bd-ab76-a2939b00471a; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1673429481,1674450671; boss_login_mode=app; wt2=DRaDczAo0MC17-8Cz7MvUgX9_j_tkm0p1skDGjftc9Kp4xO7H_b7JAaft_-LgLx4pmmLiGTdUIv3fJwCN6IlrwQ~~; wbg=0; __l=r=https%3A%2F%2Fwww.so.com%2Flink%3Fm%3DbYLUfDTIY%252FhlB7jNkchhcBx9aJK2TOWaFDeSnGZCNjVgKCDVF6yHk2UEJZab7fYucYQJkFI35D10OkP9z5pHQf6Uux5RyzQ9O8nUGGybkCP1KTkZjFH4rrtY6Zk8mtoKNCcz6ps89hee1tBZSEFxGM4KnZqQal6%252BSL9cY5w%253D%253D&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D&s=3&g=&friend_source=0&s=3&friend_source=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1674542998; __c=1674450671; __a=76476689.1670318154.1673429481.1674450671.36.4.26.32; __zp_stoken__=3ea8eAExZMw1ZIS5ALTBqcgxMXUBVPysKdVEdazR8JmIDVHYcZFBVNhx6MVReRlc6R25lBjAwMB0IIGcfIi1eUSkAbiQJcwRbLFpkUBQ2PxpkCSFaNiM9XDtaBTYqAwNxBVdXZz9OTxhBZXw%3D; geek_zp_token=V1Q9MnFuT03lhgXdNuyxgcKiK36DzTwQ~~",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",

}

# headers = {
#     "accept":"application/json, text/javascript, */*; q=0.01",
#     "accept-encoding":"gzip, deflate, br",
#     "accept-language":"zh-CN,zh;q=0.9",
#     "cache-control":"no-cache",
#     "cookie":"lastCity=101010100; wd_guid=d5acd83c-4117-47fb-be86-efbdff15f84c; historyState=state; _bl_uid=q1l4IbjadkXatLcevmR34aqvj6Fg; __zp_seo_uuid__=9357ac16-ae0d-43bd-ab76-a2939b00471a; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1673429481,1674450671; boss_login_mode=app; wt2=DRaDczAo0MC17-8Cz7MvUgX9_j_tkm0p1skDGjftc9Kp4xO7H_b7JAaft_-LgLx4pmmLiGTdUIv3fJwCN6IlrwQ~~; wbg=0; __l=r=https%3A%2F%2Fwww.so.com%2Flink%3Fm%3DbYLUfDTIY%252FhlB7jNkchhcBx9aJK2TOWaFDeSnGZCNjVgKCDVF6yHk2UEJZab7fYucYQJkFI35D10OkP9z5pHQf6Uux5RyzQ9O8nUGGybkCP1KTkZjFH4rrtY6Zk8mtoKNCcz6ps89hee1tBZSEFxGM4KnZqQal6%252BSL9cY5w%253D%253D&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D&s=3&g=&friend_source=0&s=3&friend_source=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1674542833; __c=1674450671; __a=76476689.1670318154.1673429481.1674450671.35.4.25.28; __zp_stoken__=3ea8eAExZMw1ZISNgWXwocgxMXUBFYmsfYCsdazR8Jj8pf3xMZFBVNhx6BCU1WWA6R25lBjAwMB0MdwAfIUpmIUgHMmkEQj5gLQNeUBQ2PxpkCSFtKUhMaTtaBTYqAwNxBVdXZz9OTxhBZXw%3D; geek_zp_token=V1Q9MnFuT03lhgXdNuyxgcKi6z6j3Qww~~",
#     "pragma":"no-cache",
#     "referer":"https://www.zhipin.com/",
#     "sec-fetch-dest":"empty",
#     "sec-fetch-mode":"cors",
#     "sec-fetch-site":"same-origin",
#     "token":"4G0coA5G9VD6ptJ",
#     "traceid":"6C035E65-C65A-4615-A5D5-0E9336812B3B",
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
#     "x-requested-with":"XMLHttpRequest",
#     "zp_token":"V1Q9MnFuT03lhgXdNuyxgcKi6z6j3Qww~~"
# }
params = {
    "expectId":"e92b76ed731e9bbd1HJ90t60EVpZ",
    "pk":"cpc_job_index",
    "sortType":"1",
    "page":"1",
    "salary":"",
    "payType":"",
    "degree":"",
    "experience":"",
    "stage":"",
    "scale":"",
    "districtCode":""
}
resp = requests.get(url, headers=headers, params=params)
try:
    jobLists = resp.json()['zpData']['jobList']
    for jobList in jobLists:
        name = jobList['bossName']  # 重要
        brandName = jobList['brandName']  # 重要
        securityId = jobList['securityId']  # 重要
        encryptBossId = jobList['encryptBossId']  # 重要
        encryptJobId = jobList['encryptJobId']  # 重要
        encryptBrandId = jobList['encryptBrandId']  # 重要
        print(name, brandName, securityId)
        break
except:
    print(resp.status_code)
    print(resp.text)







