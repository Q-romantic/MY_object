# -*- coding: utf-8 -*-
"""
@Time    : 2022/7/9  009 下午 15:38
@Author  : Jan
@File    : win_proxy.py
"""
import time

import requests

""" {} """

# headers = {
#     "User-Agent": getua(),
#
# }
# proxies = {
#     'http': 'http://' + getip(),
#     # 'https': 'https://' + getip(),
# }
#
# url = ''
#
#
#
# response = requests.get(url, headers=headers, params={}, data={}, proxies=proxies)
# data = response.text
# print(data)
# print(response)

'''Sets Windows' proxy configurations easily.

This script allows user to update Windows proxy settings easily,
by using predefined values assigned to proxies identified by
keywords.

Note that it'll also refresh your system to guarantee that all
settings take effect.  Although in the tests it seemed unnecessary
(Windows 8.1), it's considered just a guarantee.

Of course, you must reload all pages after running this script, but
the first thing you gotta do before running it is to setup the PROXIES
variable, creating an ID for each proxy in your environment, so you
can refer to it by using that ID as a parameter.

The "default" and "off" words are reserved, one for your proxy default
settings and the 拼多多 to disable proxy --remember to set up the 
"default" keyword properly.  Running this script without parameters
will print the current proxy settings on screen.

Usage examples:
$ python winproxy.py
$ python winproxy.py off
$ python winproxy.py proxyid

Based on: https://bitbucket.org/canassa/switch-proxy
'''

# import ctypes
# from sys import argv
# from winreg import OpenKey, QueryValueEx, SetValueEx
# from winreg import HKEY_CURRENT_USER, KEY_ALL_ACCESS
# from subcase.疫情大数据.tools import getip
#
# PROXIES = {
#     'default': {
#         'enable': 1,
#         'override': u'127.0.0.1;localhost;<local>',
#         'server': u'10.0.0.5:8080'
#     },
#     'off': {
#         'enable': 0,
#         'override': u'-',
#         'server': u'-'
#     },
#     'proxyid': {
#         'enable': 1,
#         'override': u'127.0.0.1;localhost;<local>',
#         'server': f'{getip()}'
#     },
# }
#
# INTERNET_SETTINGS = OpenKey(HKEY_CURRENT_USER,
#                             r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
#                             0, KEY_ALL_ACCESS)
#
#
# def set_key(name, value):
#     SetValueEx(INTERNET_SETTINGS, name, 0,
#                QueryValueEx(INTERNET_SETTINGS, name)[1], value)
#
#

#
#
# if __name__ == '__main__':
#
#     while 1:
#         try:
#             proxy = "off"
#             set_key('ProxyEnable', PROXIES[proxy]['enable'])
#             set_key('ProxyOverride', PROXIES[proxy]['override'])
#             set_key('ProxyServer', PROXIES[proxy]['server'])
#         except IndexError:
#             print(f'Enable....: {QueryValueEx(INTERNET_SETTINGS, "ProxyEnable")[0]}')
#             print(f'Server....: {QueryValueEx(INTERNET_SETTINGS, "ProxyServer")[0]}')
#             print(f'Exceptions: {QueryValueEx(INTERNET_SETTINGS, "ProxyOverride")[0]}')
#             # exit(0)
#
#         proxy_ip = get_ip()
#         with open(f'C:\Y\Case\subcase\疫情大数据\ip.txt', mode='w') as f:
#             f.write(proxy_ip)
#         print(proxy_ip)
#
#         # try:
#         #     proxy = "proxyid"
#         #     set_key('ProxyEnable', PROXIES[proxy]['enable'])
#         #     set_key('ProxyOverride', PROXIES[proxy]['override'])
#         #     set_key('ProxyServer', PROXIES[proxy]['server'])
#         #
#         #     # granting the system refresh for settings take effect
#         #     internet_set_option = ctypes.windll.Wininet.InternetSetOptionW
#         #     internet_set_option(0, 37, 0, 0)  # refresh
#         #     internet_set_option(0, 39, 0, 0)  # settings changed
#         # except KeyError:
#         #     print(f'Registered proxies: {PROXIES.keys()}')
#         #     exit(1)
#         exit(0)
#
#         time.sleep(60)


import winreg


def edit_system_proxy(open_or_close, proxy):
    """
    修改注册表使用代理
    :param open_or_close:
    :param proxy:
    :return:
    """

    root = winreg.HKEY_CURRENT_USER
    proxy_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
    kv_Enable = [
        (proxy_path, "ProxyEnable", 1, winreg.REG_DWORD),
        (proxy_path, "ProxyServer", proxy, winreg.REG_SZ),
    ]

    kv_Disable = [
        (proxy_path, "ProxyEnable", 0, winreg.REG_DWORD),
        # (proxy_path, "ProxyServer", proxy, winreg.REG_SZ),
    ]
    if open_or_close:
        kv = kv_Enable
    else:
        kv = kv_Disable
    for keypath, value_name, value, value_type in kv:
        hKey = winreg.CreateKey(root, keypath)
        winreg.SetValueEx(hKey, value_name, 0, value_type, value)


def get_ip():
    api_url = "http://v2.api.juliangip.com/dynamic/getips?num=1&pt=1&result_type=text&split=1&trade_no=1727174320704510&sign=d3f8576b7d8bd5a0aeb186fbdda12bba"
    ip = requests.get(api_url).text
    # res = requests.get('http://icanhazip.com/', proxies={'http': f'http://{proxy_ip}'})
    # print(res.text)
    return ip


if __name__ == '__main__':
    edit_system_proxy(False, "-")
    while True:
        proxy = get_ip()
        with open(f'C:\Y\Case\subcase\疫情大数据\ip.txt', mode='w') as f:
            f.write(proxy)
        print(proxy)
        edit_system_proxy(True, proxy)
        time.sleep(60)
