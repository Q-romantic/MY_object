# -*- coding: utf-8 -*-
import requests
import re  # 正则表达式
import pprint
import json
import subprocess
# from working.IP_Headers_Proxies import headers
from working.IP_Headers_Proxies import proxies


headers = {
    # 'Host': 'www.bilibili.com',
    # 'referer': 'https://www.bilibili.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
}

def send_request(url):
    response = requests.get(url=url, headers=headers, proxies=proxies)
    return response


def get_video_data(html_data):
    """解析视频数据"""

    # 提取视频的标题
    title = re.findall('<span class="tit">(.*?)</span>', html_data)[0]
    # print(title)

    # 提取视频对应的json数据
    json_data = re.findall('<script>window\.__playinfo__=(.*?)</script>', html_data)[0]
    # print(json_data)  # json_data 字符串
    json_data = json.loads(json_data)
    pprint.pprint(json_data)

    # 提取音频的url地址
    audio_url = json_data['data']['dash']['audio'][0]['backupUrl'][0]
    print('解析到的音频地址:', audio_url)

    # 提取视频画面的url地址
    video_url = json_data['data']['dash']['video'][0]['backupUrl'][0]
    print('解析到的视频地址:', video_url)

    return [title, audio_url, video_url]


def save_data(file_name, audio_url, video_url):
    # 请求数据
    print('正在请求音频数据')
    audio_data = send_request(audio_url).content
    print('正在请求视频数据')
    video_data = send_request(video_url).content
    with open(file_name + '.mp3', mode='wb') as f:
        f.write(audio_data)
        print('正在保存音频数据')
    with open(file_name + '.mp4', mode='wb') as f:
        f.write(video_data)
        print('正在保存视频数据')


def merge_data(video_name):
    print('视频合成开始:', video_name)
    # ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -strict experimental output.mp4
    COMMAND = f'ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -c:v copy -c:a aac -strict experimental output.mp4'
    subprocess.Popen(COMMAND, shell=True)
    print('视频合成结束:', video_name)


if __name__ == '__main__':
    url = 'https://www.bilibili.com/video/BV1qS4y1w7tP'
    html_data = send_request(url).text
    video_data = get_video_data(html_data)
    save_data(video_data[0], video_data[1], video_data[2])
