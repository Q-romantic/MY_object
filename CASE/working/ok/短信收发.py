# -*- coding: utf-8 -*-
"""
@Time    : 2023/1/24  024 下午 18:27
@Author  : Jan
@File    : 短信收发.py
"""

""" {} """

import requests
import time


def sendMessage(phone: [int, str], content: str) -> str:
    statusStr = {
        '0': '短信发送成功',
        '-1': '参数不全',
        '-2': '服务器空间不支持,请确认支持curl或者fsocket,联系您的空间商解决或者更换空间',
        '30': '密码错误',
        '40': '账号不存在',
        '41': '余额不足',
        '42': '账户已过期',
        '43': 'IP地址限制',
        '50': '内容含有敏感词'
    }
    url = f'https://api.smsbao.com/sms?u=jianxu&p=65066e65c29b4fd2a5c1e69df471b791&m={phone}&c={content}'
    resp = requests.get(url)
    status = statusStr[resp.text]
    print(status)
    return status


def receiveMessage(phone: [int, str], content: str) -> str:
    url = 'http://您的域名/接收参数的文件?m=PHONE&c=CONTENT'
    resp = ''
    return resp


def sendMessage2(phone: [int, str], content: str) -> str:
    url = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'
    values = {
        'account': 'C82396473',
        'password': '5211a8de9e5a8d454200acfe9246748c',
        'mobile': phone,
        'content': content,
        'format': 'json',
    }

    resp = requests.post(url, data=values)
    print(resp.text)
    return resp.json()


def receiveMessage2() -> list:
    url = 'https://user.ihuyi.com/new/api/sms/records/reply_list'
    user_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjcyNDI0MywiYXVkIjoiIiwiZXhwIjoxNjc0NjAyMzQ2LCJpYXQiOjE2NzQ1NTkxNDYsImlzcyI6IiIsImp0aSI6IjE2MmMwODI1NzI4OWU2NGM1MzVhYzFjZWExNzE5ZjQ1IiwibmJmIjoxNjc0NTU5MTQ2LCJzdWIiOiIifQ.Gl1Fzs963tto4aAwVHNftDP-Tk7KzB67b5DnofkshOA"
    headers = {"authorization": f"bearer {user_token}"}
    params = {
        # "page": "1",
        # "pagesize": "20",
        # "s_time": "2022-12-25",
        # "e_time": "2023-01-24",
        # "timeStamp": str(time.time() * 1000)
    }
    resp = requests.get(url, headers=headers, params=params)
    li = []
    for i in resp.json()['data']['list']:
        date_create = i['date_create']
        mobilephone = i['mobilephone']
        content = i['content']
        li.append(f"{date_create} ----- {mobilephone} ----- {content}")
    return li


if __name__ == '__main__':
    phone = "18875066946, "  # 可以群发
    content = """this is a test"""
    # sendMessage(phone=phone, content=content)
    # sendMessage2(phone=phone, content=content)

    message = receiveMessage2()
    # print(message[0])
    print(message)
