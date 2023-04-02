# -*- coding: utf-8 -*-
import os
import re
import json
import random
import string
import binascii
import requests
# from crypto.Cipher import AES     # 可能需要安装pip install pycryptodome
from Crypto.Cipher import AES  # 通过验证考察，修改模块位置文件名'crypto'为大写首字母
from base64 import b64encode
from jsonpath import jsonpath
from bs4 import BeautifulSoup

""" https://music.163.com """

url = "https://music.163.com/song?id=1937451510"  # 歌曲详情链接

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36',
    'cookie': '_ntes_nnid=462ec0f891be2c48b95aca103d574225,1626612719661; _ntes_nuid=462ec0f891be2c48b95aca103d574225; NMTID=00OyKled4RF_BvWH01rqBpnkSeoq80AAAF6uaxgqw; WEVNSM=1.0.0; WNMCID=bvbofo.1626612720132.01.0; WM_TID=axrappbUKPxEABAFFEZ%2ByduGnLB4YmqX; __root_domain_v=.163.com; _qddaz=QD.405231961583572; __remember_me=true; __snaker__id=Iy8gZPyZvN8OYTrt; gdxidpyhxdE=8rvarJocN43xxlRZITQY0QeCmKsgvGrNmZCMxykEwHq%2FPy2Yq9Ku8Jc44j3jxHUBRkE54ZQPZ93V5%2BMmPty%5C42AbnvCUNQRy2DJ13T3IEznB716Ud2DU%2FyrG8%2BbgjRI9ZoAmVf1DDXsGUsL5D%5ChTIrskINR8pO3g5lGWvRLDxmliaVvz%3A1650012326835; _9755xjdesxxd_=32; __csrf=3b22ffdba6751b48cd024dc4865f1b04; MUSIC_U=1c4319c630a22bfd8f8dfe45bec8fdbc59a1787e4f530c18fc65f5870d95a3cc993166e004087dd3a0a45ddac48826c95abbc7d25df9292a46b14e3f0c3f8af929f5e126cc9926cbc3061cd18d77b7a0; ntes_kaola_ad=1; _iuqxldmzr_=32; WM_NI=7NkyTySyfCVSx%2Bte77c8O%2FgbcQlHpVQLXkHFUMe3hpNEa2d%2Fa6ztiT%2F%2F7re7LLux52pVauyfsKBTf4EZi3BnN4Q77YyZRWuV3uxyROBOghdZCdLEjcNS7ukqpYpopVMdV3o%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeaece5fba9ca6a7d97c9bb88aa6c14b938a9fadd44f98bcfb89ae72bc8ba9b0c92af0fea7c3b92af592a59ad77391a7aaa4d559bcf5bc86b63da1e881d0e66aa18fa4a9f35e9394988ccb4e9793abd4eb7c8e9bafd3e725a3eab695ec60edf1f993e83d9094bb99b83ab48aaf96fc6eb1958eb5e5408786a7d4c1668eec9fd8b653bb869eb8f85ef1abb89ad1458291a989e75281bc84a6e9698e8df996ea7bb487c090f35e8fbc9ad4ee37e2a3; JSESSIONID-WYYY=OlYH9lIH%2BUyNiqWTq8UdtsT0O%5CKxjWbTfyagCKTHpfJncrZYfGa6wmOt9QsPVT8X0S1lPK34VYYDROFXeYqeS%2BoWXI81UXPBtWzh25NhPnrP0eWkXBQW4fze1SkvEIQFS%2BEPR1dhgUZx5K%5Cg5fYm7W%5CPrKrsZX3D9ae6pWR%5CzVXJ0F2K%3A1650724225387',
}

e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
# i = "0000000000000000"    # 随机字母+数字组合16位
i = ''.join(random.sample(string.ascii_letters + string.digits, 16))


def get_encSecKey(x):
    x = int(binascii.hexlify(x[::-1].encode('utf-8')), 16)
    return str(hex(pow(x, 65537, int(f, 16))))[2:]


def get_params(data):  # 加密2次
    def to_16(data):
        pad = 16 - len(data) % 16
        data += chr(pad) * pad
        return data

    def enc_params(data, key):
        iv = '0102030405060708'
        data = to_16(data)
        aes = AES.new(key=key.encode('utf-8'), iv=iv.encode('utf-8'), mode=AES.MODE_CBC)  # 注意指定编码方式
        bs = aes.encrypt(data.encode('utf-8'))
        return str(b64encode(bs), 'utf-8')

    first = enc_params(data, g)
    second = enc_params(first, i)
    return second


def get_song_name(url):
    url = url.replace('/#', '')
    response = requests.get(url, headers=headers)
    obj = re.compile('<title>(?P<name>.*?) - 单曲 - 网易云音乐</title>')
    title = obj.search(response.text).group('name')
    strinfo = re.compile(r'[/:*?"<>|\\]')
    name = strinfo.sub('-', title)
    return name


def download_song(url):
    sid = url.split('=')[-1]
    url_song = "https://music.163.com/song/media/outer/url?id=" + sid  # 歌曲音频链接
    print(url_song)
    resp = requests.get(url_song, headers=headers)
    filename = get_song_name(url) + '.mp3'
    os_mkdir_path = os.getcwd() + '/歌曲/'
    if not os.path.exists(os_mkdir_path):
        os.mkdir(os_mkdir_path)
    with open(os_mkdir_path + filename, 'wb') as ff:
        ff.write(resp.content)


def download_lyric(url):
    sid = url.split('=')[-1]
    data_lyric = {  # 歌词内容请求传参加密前参数
        'id': sid,
        'lv': -1,
        'tv': -1,
    }
    data_lyric_params = {  # 歌词内容请求传参（加密后参数）
        'params': get_params(json.dumps(data_lyric)),
        'encSecKey': get_encSecKey(i),
    }
    csrf_token = (''.join(random.sample(string.ascii_letters + string.digits, 32))).lower()  # 32位随机数
    url_lyric = 'https://music.163.com/weapi/song/lyric?csrf_token=' + csrf_token  # 歌词链接
    print(url_lyric)
    resp = requests.post(url_lyric, headers=headers, data=data_lyric_params)
    lyric = resp.json()['lrc']['lyric']
    # print(lyric)
    # strinfo = re.compile('[/:*?"<>|\\\\]')  # 注意用4个\\\\来替换\
    # strinfo = re.compile(r'[/:*?"<>|\\]')  # 加r,2个\即可
    strinfo = re.compile('\[.*?\]')
    d3 = strinfo.sub('', lyric)
    filename = get_song_name(url) + '.lrc'
    os_mkdir_path = os.getcwd() + '\\歌曲\\'
    if not os.path.exists(os_mkdir_path):
        os.mkdir(os_mkdir_path)
    with open(os_mkdir_path + filename, 'w', encoding='utf-8') as ff:
        ff.write(d3)
    print(get_song_name(url))
    print(d3)


def get_comments_data(url):
    url = url.replace('/#', '')
    sid = url.split('=')[-1]
    data_comments = {  # 评论内容请求传参加密前参数
        "csrf_token": "",
        "cursor": "-1",
        "offset": "0",
        "orderType": "1",
        "pageNo": "1",
        # "pageSize": "1024",
        "pageSize": 10,  # 可调节页面接收字节大小
        "rid": "R_SO_4_" + sid,
        "threadId": "R_SO_4_" + sid,
    }
    data_comments_params = {  # 评论内容请求传参（加密后参数）
        'params': get_params(json.dumps(data_comments)),
        'encSecKey': get_encSecKey(i),
    }
    # url_comments = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token=" + csrf_token
    url_comments = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="  # 评论链接
    print(url_comments)
    resp = requests.post(url_comments, headers=headers, data=data_comments_params)
    user_link = 'https://music.163.com/#/user/home?id='
    userId = jsonpath(resp.json(), '$..userId')
    nickname = jsonpath(resp.json(), '$..nickname')
    content = jsonpath(resp.json(), '$..content')
    for user_id, user_name, user_content in zip(userId, nickname, content):
        print(user_name, user_link + str(user_id), user_content)
    # print(len(userId))    # 方便统计获取评论数量


if __name__ == '__main__':
    print(url)
    print(get_song_name(url))  # 获取歌曲名
    # download_song(url)  # 下载歌曲
    download_lyric(url)  # 获取歌词
    get_comments_data(url)  # 获取评论
