# -*- coding: utf-8 -*-
import time

import requests
import filetype
from collections import OrderedDict
import json

while True:
    # p_ip = requests.get('https://proxypool.scrape.center/random').text
    p_ip = '52.90.182.59:16133'
    proxies = {'http': f'http://{p_ip}', 'https': f'http://{p_ip}'}
    print(proxies)
    if p_ip.endswith(':80') or p_ip.endswith(':8080'):
        continue
    else:
        break

filename = 'C:/Users/11390/Desktop/Snipaste_2022-04-02_10-03-56.png'
filename2 = 'C:/Users/11390/Desktop/1.png'
mime_type = filetype.guess(filename).mime  # 获取文件类型

url = 'https://www.alltoall.net/qfy-content/plugins/qfy-customize-cloudconvert/convert.php'
data_upload = {'action': 'upload'}
files_upload = {   # 适用于单文件提交
    # 'files[]': ['1.png', f'filename={filename}', 'image/png'],  # 上下两种方式传入均可
    'files[]': ['1.png', filename, mime_type],
}
session = requests.session()
# resp = requests.post(url, data=data_upload, files=files_upload)
resp = session.post(url, data=data_upload, files=files_upload, proxies=proxies)
print(resp.json())
# print('----' * 20)



time.sleep(5)
r0 = resp.json()
# r0 = {'files': [
#     '/var/www/html/qifeiye/websites/others/www.alltoall.net/qfy-content/uploads/alltoall/upload/www.alltoall.net_1_Ytyj8daDKC.png'],
#     'metas': [{'date': 'Wed, 25 May 2022 15:15:02 +0800', 'extension': 'png',
#                'file': '/var/www/html/qifeiye/websites/others/www.alltoall.net/qfy-content/uploads/alltoall/upload/www.alltoall.net_1_Ytyj8daDKC.png',
#                'name': 'www.alltoall.net_1_Ytyj8daDKC.png', 'old_name': '1', 'replaced': False, 'size': 55,
#                'size2': '0.05 KB', 'type': ['image', 'png']}],
#     'ext': 'png',
#     'ext_output': ['pdf', 'bmp', 'eps', 'gif', 'icns', 'ico', 'jpg', 'odd', 'png', 'ps', 'psd', 'tiff', 'webp'],
#     'success': True,
#     'recent_upload': 3,
#     'token': 'ee56a12b4d3cdc60f1d239b4145a9c24',
#     'file_name': 'www.alltoall.net_1_Ytyj8daDKC.png'}
data_output_1 = {
    'file_name': r0['file_name'],
    'token': r0['token'],
    'action': 'create',
    'input_type': r0['ext'],
    'output_type': 'pdf',
    # 可选输出类型['pdf', 'bmp', 'eps', 'gif', 'icns', 'ico', 'jpg', 'odd', 'png', 'ps', 'psd', 'tiff', 'webp']
}
resp = session.post(url, data=data_output_1)
print(resp.json(), '1111111111111111')
r1 = resp.json()
data_output_2 = {
    'file_name': r0['file_name'],
    'token': r0['token'],
    'action': 'process',
    'process_url': r1['process_url'],
    'file_url': 'http://www.alltoall.net/qfy-content/uploads/alltoall/upload/' + r0['file_name'],
    'output_type': 'pdf',
}
resp = session.post(url, data=data_output_2)
print(resp.json(), '2222222222222222')
time.sleep(5)
r2 = resp.json()
data_output_3 = {
    'file_name': r0['file_name'],
    'token': r0['token'],
    'action': 'status',
    'process_url': r1['process_url'],
}
time.sleep(1)
resp = session.post(url, data=data_output_3)
print(resp.json(), '33333333333333')
time.sleep(1)
resp = session.post(url, data=data_output_3)
print(resp.json(), '4444444444444444444')
url_download = ''



# files = [  # 据说适用于多文件提交，此网站只支持单个处理
#     # ('files[]', ('1.png', open(filename, 'rb'), 'image/png')),    # 可直接指定文件路径
#     ('files[]', ('1.png', filename, mime_type)),
# ]
# resp = requests.post(url, data=data, files=files, proxies=proxies)
# print(resp.status_code)
# print(resp.request.body.decode())
# print(resp.text)
# print('----' * 20)
