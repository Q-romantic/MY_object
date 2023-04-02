# -*- coding: utf-8 -*-
import os
import execjs
import requests
import re
import subprocess
from login import login_headers

""" ? """


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


head = """
accept: */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
pragma: no-cache
referer: https://match.yuanrenxue.com/match/14
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36
x-requested-with: XMLHttpRequest
"""


def get_sojson(a):
    index = open('get_sojson_for_index_14.js', 'r', encoding='utf-8')
    js = execjs.compile(index.read())
    a = js.call('get_sojson', a)
    return a


headers = s_to_dic(head)

cookies = {
    'mz': 'TW96aWxsYSxOZXRzY2FwZSw1LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMS4wLjQ5NTEuNjcgU2FmYXJpLzUzNy4zNixbb2JqZWN0IE5ldHdvcmtJbmZvcm1hdGlvbl0sdHJ1ZSwsW29iamVjdCBHZW9sb2NhdGlvbl0sOCx6aC1DTix6aC1DTix6aCwwLFtvYmplY3QgTWVkaWFDYXBhYmlsaXRpZXNdLFtvYmplY3QgTWVkaWFTZXNzaW9uXSxbb2JqZWN0IE1pbWVUeXBlQXJyYXldLHRydWUsW29iamVjdCBQZXJtaXNzaW9uc10sV2luMzIsW29iamVjdCBQbHVnaW5BcnJheV0sR2Vja28sMjAwMzAxMDcsW29iamVjdCBVc2VyQWN0aXZhdGlvbl0sTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMS4wLjQ5NTEuNjcgU2FmYXJpLzUzNy4zNixHb29nbGUgSW5jLiwsW29iamVjdCBEZXByZWNhdGVkU3RvcmFnZVF1b3RhXSxbb2JqZWN0IERlcHJlY2F0ZWRTdG9yYWdlUXVvdGFdLDEwMzIsMCwwLDE5MjAsMjQsMTA4MCxbb2JqZWN0IFNjcmVlbk9yaWVudGF0aW9uXSwyNCwxOTIwLFtvYmplY3QgRE9NU3RyaW5nTGlzdF0sZnVuY3Rpb24gYXNzaWduKCkgeyBbbmF0aXZlIGNvZGVdIH0sLG1hdGNoLnl1YW5yZW54dWUuY29tLG1hdGNoLnl1YW5yZW54dWUuY29tLGh0dHBzOi8vbWF0Y2gueXVhbnJlbnh1ZS5jb20vbWF0Y2gvMTQsaHR0cHM6Ly9tYXRjaC55dWFucmVueHVlLmNvbSwvbWF0Y2gvMTQsLGh0dHBzOixmdW5jdGlvbiByZWxvYWQoKSB7IFtuYXRpdmUgY29kZV0gfSxmdW5jdGlvbiByZXBsYWNlKCkgeyBbbmF0aXZlIGNvZGVdIH0sLGZ1bmN0aW9uIHRvU3RyaW5nKCkgeyBbbmF0aXZlIGNvZGVdIH0sZnVuY3Rpb24gdmFsdWVPZigpIHsgW25hdGl2ZSBjb2RlXSB9'
}
from login import login_cookies

cookies.update(login_cookies)
total = 0
for page in range(1, 6):
    # 解析window[v14]和window[v142]的值
    response = requests.get('https://match.yuanrenxue.com/api/match/14/m', cookies=cookies)

    # 方法一：
    # encode_file_path = 'C:\\Y\\Case\\working\\猿人学\\tmp1.js'
    # decode_file_path = 'C:\\Y\\Case\\working\\猿人学\\tmp2.js'
    # with open(encode_file_path, 'w') as f:
    #     f.write(response.text)
    # # print(response.text)
    #
    # # v14 = 'z34qar8ywp'
    # # v142 = '34476880564'
    #
    # # 执行m.js，得到加密后的m值
    # # p = subprocess.Popen(['node', '.\index_14.js', win_value[0], win_value[1], str(page)], stdout=subprocess.PIPE).stdout.read().decode()
    # out = subprocess.Popen(['node', 'get_sojson_for_index_14.js', encode_file_path, decode_file_path], stdout=subprocess.PIPE).stdout.read().decode()
    # os.remove(encode_file_path)
    # os.remove(decode_file_path)

    # 方法二：
    out = get_sojson(response.text)

    v14 = re.findall('window\.v14 = \"(.*?)\";', out, re.S)[0]
    v142 = re.findall('window\.v142 = \"(.*?)\";', out, re.S)[0]
    print(v14, v142)
    with open('index_14.js', mode='r', encoding='utf-8') as f:
        jsdata = f.read()
    m = execjs.compile(jsdata).call('get_m', v14, v142, page)
    m = m.split(';')[0].split('=')[-1]
    print(m)
    cookies['m'] = m
    # print(cookies)

    # 带上cookie信息请求数据页api
    url = 'https://match.yuanrenxue.com/api/match/14?page=' + str(page)
    response = requests.get(url, cookies=cookies, headers={'User-Agent': 'yuanrenxue.project'})
    print(response.text)
    data = response.json()["data"]
    for d in data:
        total += d["value"]
    # break

answer = total
print(answer)
url = 'https://match.yuanrenxue.com/api/answers'
params = {'answer': answer, 'id': 14}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)

"""答案：42686
t8q96du45o 12296087627
e9532cf78154f22664254fae6f7a28fe|1652974741000|13223797928000|1
{"status": "1", "state": "success", "data": [{"value": -3974}, {"value": -3628}, {"value": -2144}, {"value": 617}, {"value": -1687}, {"value": -571}, {"value": -3526}, {"value": 3849}, {"value": -3756}, {"value": -800}]}
z5rogjmd 53023052794
9b9a58f00c499f484a18206f477ca743|1652974742000|13223797936000|2
{"status": "1", "state": "success", "data": [{"value": 2125}, {"value": -1005}, {"value": -2283}, {"value": 1717}, {"value": 187}, {"value": 4903}, {"value": 4238}, {"value": 1509}, {"value": -345}, {"value": -1015}]}
iybkjrvq 43401920329
c98a1a65df1f425d42ca9c7d534f39fc|1652974744000|13223797952000|3
{"status": "1", "state": "success", "data": [{"value": 3616}, {"value": 441}, {"value": 457}, {"value": 5044}, {"value": -4040}, {"value": -44}, {"value": 4652}, {"value": 482}, {"value": -2789}, {"value": 3036}]}
3a9oqpgjy1 20497131503
fcf060ec57f5697c95cf4e412c30e9ca|1652974746000|13223797968000|4
{"status": "1", "state": "success", "data": [{"value": 5225}, {"value": 1872}, {"value": 1290}, {"value": -10}, {"value": 328}, {"value": 224}, {"value": -2160}, {"value": 1950}, {"value": 2014}, {"value": -1562}]}
n52gyxbh 14708768981
e86e4cde2a1b56bd314fa5e61fa35683|1652974748000|13223797984000|5
{"status": "1", "state": "success", "data": [{"value": 5193}, {"value": -218}, {"value": 3626}, {"value": 4382}, {"value": 5021}, {"value": 4050}, {"value": 4385}, {"value": 2875}, {"value": -1547}, {"value": 482}]}
"""

# # -*- coding:utf-8 -*-
# from lxml import etree
# from selenium import webdriver
#
#
# def get_data():
#     page_data = driver.page_source
#     # print(page_data)
#     xml = etree.HTML(page_data)
#     data = xml.xpath('/html/body/div/div[2]/table/tbody/tr/td/text()')
#     print(data)
#
#
# option = webdriver.ChromeOptions()
# option.add_experimental_option("excludeSwitches", ["enable-automation"])  # 规避检测
# # prefs = {"profile.managed_default_content_settings.images": 2}              # 不显示图片提高代码速度，貌似没用，反而慢
# # option.add_experimental_option("prefs", prefs)
# option.add_experimental_option('useAutomationExtension', False)
# option.add_argument("--user-agent=xxxxxx")  # 替换UA
# option.add_argument('--headless')  # 设置chrome浏览器无界面模式(设置无头浏览器)
# # driver = webdriver.Chrome(executable_path='C:\Python39\Scripts\chromedriver', options=option)
# driver = webdriver.Chrome(options=option)
# driver.maximize_window()  # 窗口最大化
# driver.get("https://match.yuanrenxue.com/api/login")  # 必须有个登录或其他页面才可以往后加cookie
#
# url = 'https://match.yuanrenxue.com/api/login'
# data = {'username': 'Jan9360', 'password': 'Q-romantic20'}
# resp = requests.post(url, data=data)
# sessionid = resp.cookies.items()[0][1]
# driver.add_cookie({'name': 'sessionid', 'value': sessionid})  # 手动添加cookie
#
# # driver.add_cookie({'name': 'sessionid', 'value': '4yw685m38n7i8se0tgety4k6q5zeaxiv'})  # 手动添加cookie，并且一次只能添加一个值
# driver.get(f"http://match.yuanrenxue.com/match/14")
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/button[2]').click()  # 关闭弹窗
# get_data()
# for i in range(2):
#     driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div/nav/ul/li[7]/a').click()  # 翻页
#     get_data()
#
# # input()
# # driver.close()
