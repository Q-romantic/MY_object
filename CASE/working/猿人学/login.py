# -*- coding: utf-8 -*-
import requests

url = 'https://match.yuanrenxue.com/api/login'

data = {'username': 'Jan9360', 'password': 'Q-romantic20'}

resp = requests.post(url, data=data)
login_cookies = dict(resp.cookies)
cookie = ""
for k, v in login_cookies.items():
    cookie += f'{k}={v}; '
login_headers_no_cookies = {'User-Agent': 'yuanrenxue.project'}
login_headers = {'User-Agent': 'yuanrenxue.project', 'cookie': cookie.strip()}

if __name__ == '__main__':
    print(resp.text)
    print(login_headers_no_cookies, login_cookies)
    print(login_headers)
    # import 猿人学_01
    # import 猿人学_02
    # import 猿人学_03
    # import 猿人学_04
    # import 猿人学_05
    # import 猿人学_06
    # import 猿人学_07
    # import 猿人学_08
    # import 猿人学_09
    # import 猿人学_10
    # import 猿人学_11
    # import 猿人学_12
    # import 猿人学_13
    # import 猿人学_14
    # import 猿人学_15
    # import 猿人学_16
    # import 猿人学_17
    # import 猿人学_18
    # import 猿人学_19
    # import 猿人学_20

"""
nickname: "Jan","finish_time": "2022-05-06T22:23:15","challenge_number": 17
nickname: "\u4eca\u665a\u65e9\u70b9\u7761","finish_time": "2022-05-04T21:42:23","challenge_number": 19
nickname: "ForGao","finish_time": "2022-04-13T15:05:08","challenge_number": 17
nickname: "\u67e0\u6aac\u82cf\u6253ss","finish_time": "2022-04-05T23:10:19","challenge_number": 18
nickname: "\u884c\u8d70\u7684\u81ea\u884c\u8f66","finish_time": "2022-03-25T23:28:33","challenge_number": 20
nickname: "\u6d2a\u594e","finish_time": "2022-03-20T01:46:39","challenge_number": 17
nickname: "igufei","finish_time": "2022-03-11T18:59:39","challenge_number": 19
nickname: "\u65f6\u5149","finish_time": "2022-03-10T14:34:54","challenge_number": 18
nickname: "\u5929\u7a7a\u5bab\u9619","finish_time": "2022-02-16T14:03:38","challenge_number": 19
nickname: "\u5f13\u592b\u6563\u4eba","finish_time": "2022-01-30T16:15:08","challenge_number": 18
nickname: "xiaoji","finish_time": "2022-01-28T15:44:50","challenge_number": 17
nickname: "0.0","finish_time": "2022-01-11T15:58:34","challenge_number": 17
nickname: "\u4e00\u53ea\u5c0f\u722c\u866b","finish_time": "2021-12-24T22:29:31","challenge_number": 17
nickname: "\u8bc1\u660e\u81ea\u5df1","finish_time": "2021-12-15T11:50:17","challenge_number": 19
nickname: "wzy","finish_time": "2021-12-07T15:50:58","challenge_number": 17
nickname: "\u5f20\u4e09","finish_time": "2021-12-05T17:13:56","challenge_number": 18
nickname: "jia666","finish_time": "2021-11-30T15:09:03","challenge_number": 17
nickname: "\u900d\u9065\u4e00\u4ed9","finish_time": "2021-11-29T15:35:41","challenge_number": 19
nickname: "andy","finish_time": "2021-11-27T11:27:15","challenge_number": 18
nickname: "\u5c0f\u94c1","finish_time": "2021-11-25T19:24:17","challenge_number": 19
nickname: "\u5927\u8170\u5b50","finish_time": "2021-11-25T18:25:21","challenge_number": 19
nickname: "\u75be\u98ce\u4ea6\u6709\u5f52\u9014","finish_time": "2021-11-25T16:27:46","challenge_number": 17
nickname: "\u8fa3\u6912\u4fa0","finish_time": "2021-08-27T13:18:03","challenge_number": 16
nickname: "\u65f6\u738b","finish_time": "2021-07-28T22:07:18","challenge_number": 16
nickname: "\u6635\u79f0123","finish_time": "2021-05-21T15:58:03","challenge_number": 16
nickname: "\u90aa\u7d2b\u682a","finish_time": "2021-03-09T18:46:00","challenge_number": 16
nickname: "\u5b89\u6f9c","finish_time": "2021-02-02T10:24:00","challenge_number": 16
nickname: "\u4e8c\u6b21\u84dd","finish_time": "2021-01-09T19:03:00","challenge_number": 16
nickname: "York","finish_time": "2021-01-05T15:20:00","challenge_number": 17


0: {nickname: "行走的自行车", finish_time: "2022-03-25T23:28:33", challenge_number: 20}
1: {nickname: "大腰子", finish_time: "2021-11-25T18:25:21", challenge_number: 19}
2: {nickname: "小铁", finish_time: "2021-11-25T19:24:17", challenge_number: 19}
3: {nickname: "逍遥一仙", finish_time: "2021-11-29T15:35:41", challenge_number: 19}
4: {nickname: "证明自己", finish_time: "2021-12-15T11:50:17", challenge_number: 19}
5: {nickname: "天空宫阙", finish_time: "2022-02-16T14:03:38", challenge_number: 19}
6: {nickname: "igufei", finish_time: "2022-03-11T18:59:39", challenge_number: 19}
7: {nickname: "今晚早点睡", finish_time: "2022-05-04T21:42:23", challenge_number: 19}
8: {nickname: "andy", finish_time: "2021-11-27T11:27:15", challenge_number: 18}
9: {nickname: "张三", finish_time: "2021-12-05T17:13:56", challenge_number: 18}
10: {nickname: "弓夫散人", finish_time: "2022-01-30T16:15:08", challenge_number: 18}
11: {nickname: "时光", finish_time: "2022-03-10T14:34:54", challenge_number: 18}
12: {nickname: "柠檬苏打ss", finish_time: "2022-04-05T23:10:19", challenge_number: 18}
13: {nickname: "York", finish_time: "2021-01-05T15:20:00", challenge_number: 17}
14: {nickname: "疾风亦有归途", finish_time: "2021-11-25T16:27:46", challenge_number: 17}
15: {nickname: "jia666", finish_time: "2021-11-30T15:09:03", challenge_number: 17}
16: {nickname: "wzy", finish_time: "2021-12-07T15:50:58", challenge_number: 17}
17: {nickname: "一只小爬虫", finish_time: "2021-12-24T22:29:31", challenge_number: 17}
18: {nickname: "0.0", finish_time: "2022-01-11T15:58:34", challenge_number: 17}
19: {nickname: "xiaoji", finish_time: "2022-01-28T15:44:50", challenge_number: 17}
20: {nickname: "洪奎", finish_time: "2022-03-20T01:46:39", challenge_number: 17}
21: {nickname: "ForGao", finish_time: "2022-04-13T15:05:08", challenge_number: 17}
22: {nickname: "Jan", finish_time: "2022-05-06T22:23:15", challenge_number: 17}
23: {nickname: "二次蓝", finish_time: "2021-01-09T19:03:00", challenge_number: 16}
24: {nickname: "安澜", finish_time: "2021-02-02T10:24:00", challenge_number: 16}
25: {nickname: "邪紫株", finish_time: "2021-03-09T18:46:00", challenge_number: 16}
26: {nickname: "昵称123", finish_time: "2021-05-21T15:58:03", challenge_number: 16}
27: {nickname: "时王", finish_time: "2021-07-28T22:07:18", challenge_number: 16}
28: {nickname: "辣椒侠", finish_time: "2021-08-27T13:18:03", challenge_number: 16}
"""
