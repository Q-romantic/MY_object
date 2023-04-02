# -*- coding: utf-8 -*-
import base64
import requests
from login import login_headers

""" 找参数规律或通过js代码获取计算加密方式 """

url = 'https://match.yuanrenxue.com/api/match/12'

total = 0
for i, j in zip(range(1, 6), ['E=', 'I=', 'M=', 'Q=', 'U=']):
    params = {
        'page': i,
        'm': 'eXVhbnJlbnh1ZT' + j
    }
    response = requests.get(url, headers=login_headers, params=params)
    print(response.text)
    data = response.json()["data"]
    for d in data:
        total += d["value"]

print(total)


total = []
for i in range(1, 6):
    c = 'yuanrenxue' + str(i)
    params = {
        'page': i,
        'm': base64.encodebytes(c.encode('utf8'))  # 转为base64
        # 'm': base64.encodebytes(c.encode('utf8')).decode()  # 转为base64
    }
    response = requests.get(url, headers=login_headers, params=params)
    print(response.text)
    data = response.json()["data"]
    for d in data:
        total.append(d["value"])











s = """
accept: */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
cache-control: no-cache
cookie: Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1652606374,1652644142,1652851574,1652965759; no-alert3=true; tk=4874674831297904843; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1652580503,1652851573,1652965767; mz=TW96aWxsYSxOZXRzY2FwZSw1LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMS4wLjQ5NTEuNjQgU2FmYXJpLzUzNy4zNiBFZGcvMTAxLjAuMTIxMC40Nyxbb2JqZWN0IE5ldHdvcmtJbmZvcm1hdGlvbl0sdHJ1ZSwsW29iamVjdCBHZW9sb2NhdGlvbl0sOCx6aC1DTix6aC1DTixlbixlbi1HQixlbi1VUywwLFtvYmplY3QgTWVkaWFDYXBhYmlsaXRpZXNdLFtvYmplY3QgTWVkaWFTZXNzaW9uXSxbb2JqZWN0IE1pbWVUeXBlQXJyYXldLHRydWUsW29iamVjdCBQZXJtaXNzaW9uc10sV2luMzIsW29iamVjdCBQbHVnaW5BcnJheV0sR2Vja28sMjAwMzAxMDcsW29iamVjdCBVc2VyQWN0aXZhdGlvbl0sTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMS4wLjQ5NTEuNjQgU2FmYXJpLzUzNy4zNiBFZGcvMTAxLjAuMTIxMC40NyxHb29nbGUgSW5jLiwsW29iamVjdCBEZXByZWNhdGVkU3RvcmFnZVF1b3RhXSxbb2JqZWN0IERlcHJlY2F0ZWRTdG9yYWdlUXVvdGFdLDEwMzIsMCwwLDE5MjAsMjQsMTA4MCxbb2JqZWN0IFNjcmVlbk9yaWVudGF0aW9uXSwyNCwxOTIwLFtvYmplY3QgRE9NU3RyaW5nTGlzdF0sZnVuY3Rpb24gYXNzaWduKCkgeyBbbmF0aXZlIGNvZGVdIH0sLG1hdGNoLnl1YW5yZW54dWUuY29tLG1hdGNoLnl1YW5yZW54dWUuY29tLGh0dHBzOi8vbWF0Y2gueXVhbnJlbnh1ZS5jb20vbWF0Y2gvMTQsaHR0cHM6Ly9tYXRjaC55dWFucmVueHVlLmNvbSwvbWF0Y2gvMTQsLGh0dHBzOixmdW5jdGlvbiByZWxvYWQoKSB7IFtuYXRpdmUgY29kZV0gfSxmdW5jdGlvbiByZXBsYWNlKCkgeyBbbmF0aXZlIGNvZGVdIH0sLGZ1bmN0aW9uIHRvU3RyaW5nKCkgeyBbbmF0aXZlIGNvZGVdIH0sZnVuY3Rpb24gdmFsdWVPZigpIHsgW25hdGl2ZSBjb2RlXSB9; m=25deb4a187f65d57dbd91847ca4de2c5|1652974100000|13223792800000|1; sessionid=0wjq2kk4i5ns28f6xxtjgpp4u9850uj6; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1653018202; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1653018209
pragma: no-cache
referer: https://match.yuanrenxue.com/match/12
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47
x-requested-with: XMLHttpRequest
"""
def s_to_dic(headers_str):
    import re
    pattern = '^(.*?): (.*)$|^(.*?):(.*)$'
    h = {}
    for line in headers_str.splitlines():
        if line == '' or line.startswith('#'):
            continue
        if ': ' not in line:
            line.replace(':', ': ')
        # print(re.sub(pattern, "\'\\1\': \'\\2\',", line))
        s = re.sub(pattern, '{\'\\1\': \'\\2\'}', line)
        h.update(eval(s))
    return h


headers = s_to_dic(s)

answer = sum(total)
print(answer)
url = 'https://match.yuanrenxue.com/api/answers'
params = {'answer': answer, 'id': 12}
resq = requests.get(url, headers=headers, params=params)
data = resq.json()
print(data)

""" 答案固定：41782
"""