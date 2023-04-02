# -*- coding: utf-8 -*-
"""
@Time    : 2022/10/30  030 下午 13:17
@Author  : Jan
@File    : 20221030_微博搜索.py
"""

import requests
from working.all_tools.tools import getip
from working.all_tools.tools import getua

""" {通过微博名称搜索其主页链接} """

headers = {
    "User-Agent": getua(),

}
proxies = {
    'http': 'http://' + getip(),
    'https': 'http://' + getip(),
}


def weiboname_to_url(searchname):
    # searchname = "微博环保"
    url = 'https://m.weibo.cn/api/container/getIndex'
    params = {
        "containerid": f"100103type=1&q={searchname}",
        "page_type": "searchall"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    # print(data)
    # print(data["data"]["cards"][0]["card_group"][0]["scheme"])
    profile_url = data["data"]["cards"][0]["card_group"][0]["user"]["profile_url"]
    # print(searchname, profile_url)
    # print(response)
    return profile_url


li = [
    "JDL京东物流",
    "联合国环境规划署",
    "摄影师李小月",
    "Thomas看看世界",
    "网护自然",
    "微博环保",
    "让候鸟飞",
    "D5_丁飞俊",
    "刘芳菲",
    "小林是李昀"
]
for i in li:
    print(i, weiboname_to_url(i))

# import xlrd
# from xlutils.copy import copy
#
# data = xlrd.open_workbook('1.xls')  # 打开xls文件
# table = data.sheets()[0]
# rows_old = table.nrows  # 获取表的行数
# new_workbook = copy(data)
# new_worksheet = new_workbook.get_sheet(0)
# for i in range(0, rows_old):
#     profile_url = weiboname_to_url(table.row_values(i)[0])
#     for j in range(1, 2):
#         new_worksheet.write(i, j, profile_url)  # 从第一行开始写
# new_workbook.save('2.xls')  # 保存工作簿

