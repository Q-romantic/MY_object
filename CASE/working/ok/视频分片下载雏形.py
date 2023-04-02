'''
几乎所有网站视频下载流程:
    1.拿到548121-1-1. htmL的页面源代码
    2.从源代码中提取到m3u8的url
    3.下载m3u8
    4.读取m3u8文件，下载视频
    5.合并视频
'''

import re
import requests

url = 'https://www.91kanju2.com/vod-play/62655-1-1.html'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29',
}


def get_m3u8():
    resp = requests.get(url, headers=headers)
    obj1 = re.compile(r"<title>《(?P<name>.*?)》高清在线观看－91看剧网</title>", re.S)
    obj2 = re.compile(r"url: '(?P<url>.*?)',", re.S)
    video_name = obj1.search(resp.text).group('name')
    m3u8_url = obj2.search(resp.text).group('url')
    resp.close()
    print(m3u8_url, video_name)

    resp2 = requests.get(m3u8_url, headers=headers)
    filename = 'video/' + video_name + '.m3u8'
    with open(filename, mode='wb') as f:
        f.write(resp2.content)
    resp2.close()
    return filename


filename = get_m3u8()
n = 1
with open(filename, mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        # print(line)
        # 下载视频片段
        # resp3 = requests.get(line, headers=headers)
        # f = open(f"video/{n}.ts", mode="wb")
        # f.write(resp3.content)
        # f.close()
        # resp3.close()
        print(line)
        n += 1
        if n == 11:
            break
