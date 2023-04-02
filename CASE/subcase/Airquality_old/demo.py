# -*- coding: utf-8 -*-
import time

import requests

"""
猿急送：https://www.yuanjisong.com/
外包大师：http://www.waibaodashi.com/
人人开发：http://www.rrkf.com/
码易：https://www.mayigeek.com
开源众包：https://zb.oschina.net/
智筹：http://zhichou.com/
开发邦：https://www.kaifabang.com/
码市：https://codemart.com/
猪八戒：https://luoyang.zbj.com/
程序猿客栈：http://www.proginn.com
"""

headers = {
    # "Host":"www.vmgirls.com",
    # "Connection":"keep-alive",
    # "Pragma":"no-cache",
    # "Cache-Control":"no-cache",
    # "sec-ch-ua":"\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
    # "sec-ch-ua-mobile":"?0",
    # "sec-ch-ua-platform":"\"Windows\"",
    # "Upgrade-Insecure-Requests":"1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    # "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "Sec-Fetch-Site":"same-origin",
    # "Sec-Fetch-Mode":"navigate",
    # "Sec-Fetch-User":"?1",
    # "Sec-Fetch-Dest":"document",
    # "Referer":"https://www.vmgirls.com/13344.html",
    # "Accept-Encoding":"gzip, deflate, br",
    # "Accept-Language":"zh-CN,zh;q=0.9",
    # "Cookie":"__51uvsct__JfW3k9jZFIZNmhsN=1; __51vcke__JfW3k9jZFIZNmhsN=35c5cdc2-625d-53bc-b8eb-86eb960753fd; __51vuft__JfW3k9jZFIZNmhsN=1656054923252; __gads=ID=ab7793903c3eca41-2238bd0800d300e1:T=1656054942:RT=1656054942:S=ALNI_MYmF806o_hxhYR5UnwdRrjNX2wDRQ; __gpi=UID=0000062a6db68699:T=1656054942:RT=1656054942:S=ALNI_MYDh2P-uxNHS94t5uV8xZTNF2hNzw; __vtins__JfW3k9jZFIZNmhsN=%7B%22sid%22%3A%20%2215a455c7-2d2f-5fe1-a802-351b96c9f5ea%22%2C%20%22vd%22%3A%208%2C%20%22stt%22%3A%201493716%2C%20%22dr%22%3A%2093338%2C%20%22expires%22%3A%201656058216965%2C%20%22ct%22%3A%201656056416965%7D"
}

# url = 'https://www.vmgirls.com/13404.html'
#
# response = requests.get(url, headers=headers)
# print(response)
# data = response.text
# print(data)
#


# from selenium import webdriver
#
# option = webdriver.ChromeOptions()
# # option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
# driver = webdriver.Chrome(executable_path="C:/Python39/Scripts/chromedriver.exe", options=option)
# driver.get('https://www.aqistudy.cn/historydata/monthdata.php?city=成都&month=2022-06')
#
# data = driver.page_source
# time.sleep(1)
# print(data)

# url = 'https://www.aqistudy.cn/historydata/monthdata.php?city=成都&month=2022-06'
# response = requests.get(url, headers=headers)
# data = response.text
# print(response)
# print(data)


from selenium import webdriver
from selenium.webdriver import ChromeOptions

# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# option.add_experimental_option('useAutomationExtension', False)
# # option.add_argument('--headless')
# browser = webdriver.Chrome(options=option)
# browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
#     'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
# })
#
# url = 'https://www.aqistudy.cn/historydata/monthdata.php?city=成都&month=2022-06'
# browser.get(url)
# data = browser.page_source
# print(data)
#
# 'https://www.aqistudy.cn/historydata/daydata.php?city=%E6%88%90%E9%83%BD&month=2022-06'
# 'view-source:https://www.aqistudy.cn/historydata/daydata.php?city=%E6%88%90%E9%83%BD&month=2022-06'
#
#


# coding=utf-8
from selenium import webdriver
# import pymysql
import pandas as pd
import time
import requests
import re
from bs4 import BeautifulSoup
# from sqlalchemy.exc import IntegrityError

def get_date(url):
    response = requests.get(url, headers=headers)
    # print(response.text)
    dates = []
    try:
        if response.status_code ==200:
            response = response.text
            soup = BeautifulSoup(response, 'lxml')
            dates_ = soup.find_all('li')
            for i in dates_:
                if i.a:  # 去除空值
                    li = i.a.text  # 提取li标签下的a标签
                    date = re.findall('[0-9]*', li)  # ['2019', '', '12', '', '']
                    year = date[0]
                    month = date[2]
                    if month and year:  # 去除不符合要求的内容
                        date_new = '-'.join([year, month])
                        dates.append(date_new)
            return dates
    except:
        print('数据获取失败！')
def spider(url):
    browser.get(url)
    df = pd.read_html(browser.page_source, header=0)[0]  # 返回第一个Dataframe
    time.sleep(1.5)
    if not df.empty:
        # print(df)
        # df.to_csv('data.csv', mode='a', index=None)
        print(url+'数据爬取已完成')
        return df
    else:
        return spider(url)  # 防止网络还没加载出来就爬取下一个url
if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/monthdata.php?city=%E5%8C%97%E4%BA%AC'
    base_url = 'https://www.aqistudy.cn/historydata/daydata.php?city='
    # 声明浏览器对象
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option("useAutomationExtension", False)
    browser = webdriver.Chrome(options=option)
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",{
        'source':'''Object.defineProperty(navigator, 'webdriver', {
        get: () =>false'''
    })
    city = [
        '北京',
            ]
    # conn = pymysql.connect(host='localhost', user='root', db='weatherdata', passwd='12345678', charset='utf8')  # 连接数据库
    # cursor = conn.cursor()  # 获取cursor游标
    dates = get_date(url)[1:]
    print(dates)
    list_data = []
    list_row = []
    for ct in range(len(city)):
        for date in dates:
            url = base_url + city[ct] + '&month=' + date
            df = spider(url)
            print(df)
            time.sleep(1.5)
            df['city'] = city[ct]  # 添加一列
            for i in range(0, df.shape[0]):  # 行
                for j in range(df.shape[1]):  # 列
                    data = df.iloc[i, j]
                    list_row.append(data)
                list_data.append(list_row)
                list_row = []
            print(list_data)
            break
        for n in range(len(list_data)):
            li = (list_data[n][0], (list_data[n][1]), list_data[n][2],
                (list_data[n][3]),(list_data[n][4]),(list_data[n][5]),(list_data[n][6]),
                        (list_data[n][7]),(list_data[n][8]),list_data[n][9])
            print(li)
            # sql = 'insert ignore into aqidata (DATE,AQI,GRADE,PM25,PM10,SO2,CO,NO2,O3_8h,CITY)' \
            #       ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            # try:
            #     x = cursor.execute(sql, (list_data[n][0], float(list_data[n][1]), list_data[n][2],
            #     float(list_data[n][3]),float(list_data[n][4]),float(list_data[n][5]),float(list_data[n][6]),
            #             float(list_data[n][7]),float(list_data[n][8]),list_data[n][9]))
            # except IntegrityError:
            #     print('IntegrityError happened!')
    #         conn.commit()
    # cursor.close()  # 关闭cursor
    # conn.close()  # 关闭连接
    browser.close()
    # aqidata = pd.DataFrame(list_data,
    #             columns=['日期', 'AQI', '质量等级', 'PM2.5', 'PM10', 'SO2', 'CO', 'NO2', 'O3_8h', 'city'])
    # print('所有数据爬取已完成！\n', aqidata)

url = 'https://www.aqistudy.cn/historydata/daydata.php?city=成都&month=2022-06'

'/html/body/script[2]'


data_url = 'https://www.aqistudy.cn/historydata/api/historyapi.php'
city_url = 'https://www.aqistudy.cn/historydata/'
params = {

}