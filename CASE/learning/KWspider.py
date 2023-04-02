import requests
from jsonpath import jsonpath  # pip install jsonpath
# from urllib import parse
import time
import os
import math
import re

'''
思维流程：
1，分析歌曲列表页的详情信息的数据包，发起请求，将歌手名，歌曲名 歌曲总数，歌曲Id获取下来
        --http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key=%E6%9E%97%E4%BF%8A%E6%9D%B0&pn=1&rn=30&httpsStatus=1&reqId=d76e88d0-ff64-11eb-8430-95975dd1a0f8
2，分析歌曲播放数据包，发起请求，拿到目标url后缀为.mp3的播放链接
        --http://www.kuwo.cn/url?format=mp3&rid=180150337&response=url&type=convert_url3&br=128kmp3&from=web&t=1629209414119&httpsStatus=1&reqId=d7703680-ff64-11eb-8430-95975dd1a0f8
        --https://cc-sycdn.kuwo.cn/81f3482b0a8169a504c80af5e993d7e0/611bc345/resource/n1/73/70/2683167142.mp3
3，再次向歌曲后缀为.mp3的url发请求，获取二进制数据
4，保存
5，爬取任意歌手的任意数据：
    -- 找到歌手歌曲总数  total
    -- 计算页码数
    --  for page in range(1, page_number + 1):  # 1,2 ....202
        data['pn'] = page  # 通过字典拿建名改键值   
    --重新再次发请求，拿到每页歌曲信息及其播放信息
'''

name = input("请输入你要下载的歌手名：")
url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord'
head = {
    'Cookie': '_ga=GA1.2.605549104.1629290912; _gid=GA1.2.102742997.1629290912; channel_from_id=1001008053; '
              'userid=1632236011; websid=3249347696; liveCheck=1; watched=549760885; gid=56759a48-666e-4cbd-8f41-9423806dffd9; '
              'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1629290912,1629345664; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1629345664; kw_token=BHLKWLM4C9',
    # 夸站请求伪造
    'csrf': 'BHLKWLM4C9',
    'Host': 'www.kuwo.cn',
    'Referer': 'http://www.kuwo.cn/search/list',
    # 'Referer': 'http://www.kuwo.cn/search/list?key=%E9%82%A3%E8%8B%B1',
    # 'Referer': 'http://www.kuwo.cn/search/list?key=那英',   # 这里key参数可以省略，且网页复制值自动转换中文不能运行
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73',
}
data = {
    'key': name,
    'pn': 1,  # 页码  # 1 2 3 4 ...
    'rn': '30',  # 当页歌曲总数
    'httpsStatus': '1',  # http状态请求码
    # 'reqId': '7abef800-ff59-11eb-9332-7be0ac7938da',
}


# 请求站点
def get_data(urls, headers, params=None):
    response = requests.get(urls, headers=headers, params=data)
    if response.status_code == 200:
        # print(response.json())
        return response.json()
    return None


# 解析网页数据  只拿有用的数据
def parse_json():
    json_data = get_data(url, head, data)
    # $表示从根节点开始  ..表示跳过任意层级
    song_sum = jsonpath(json_data, '$..total')[0]  # 歌曲总数
    # 计算页码数量
    page_number = math.ceil(int(song_sum) / 30)  # math.ceil() 向上取整
    # print(song_sum)
    # print(page_number)
    for page in range(1, page_number + 1):  # 1,2 ....202
        # print(page)
        data['pn'] = page  # 通过字典拿键名改键值
        data_json = get_data(url, head, data)  # 对每一页数据包发起请求

        singer_name = jsonpath(data_json, '$..artist')  # 歌手名
        song_name = jsonpath(data_json, '$..name')  # 歌曲名
        song_id = jsonpath(data_json, '$..rid')  # 歌曲id
        
        x = 1

        for singer_names, song_names, song_ids in zip(singer_name, song_name, song_id):
            print('==========\033[1;31m已下载<{}>首歌曲\033[0m，正在下载第{}页{}首歌曲，'
                  '歌名是\033[1;32m《{}》\033[0m'.format(30*(page-1)+x-1, page, x, song_names))
            print(singer_names)
            print(song_names)
            print(song_ids)
            # print('---' * 10)
            s = int(time.time() * 1000)  # 时间戳
            # 歌曲播放的数据包链接
            song_url = 'http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&' \
                       'from=web&t={}&httpsStatus=1&reqId=917ad600-ff5d-11eb-87ce-03542e2aef11'.format(song_ids, s)
            # 再次发送请求 获得歌曲播放数据
            song_data = requests.get(song_url, headers=head).json()['url']
            # print(song_data)  # 歌曲链接
            # 再次请求song_data  获取歌曲二进制数据
            song_mp3 = requests.get(song_data).content
            # print(song_mp3)
            save_data(name, song_names, song_mp3)

            x += 1
            print(song_data, "\n")


# 保存数据
def save_data(singer_name, song_names, mp3data):
    path = './酷我/{}/'.format(singer_name)
    # []过滤里面任意字符
    song_names = re.sub('[\/:*?"<>|]', '-', song_names)
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + '{}.mp3'.format(song_names), 'wb')as f:
        f.write(mp3data)


if __name__ == '__main__':
    parse_json()
