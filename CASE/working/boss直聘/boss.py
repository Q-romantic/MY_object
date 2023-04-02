# -*- coding: utf-8 -*-
"""
@Time    : 2022/7/5  005 下午 13:18
@Author  : Jan
@File    : boss.py
"""
import parsel
import requests

""" {} """

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "cookie": "lastCity=101010100; "
              "wd_guid=d5acd83c-4117-47fb-be86-efbdff15f84c; "
              "historyState=state; "
              "_bl_uid=q1l4IbjadkXatLcevmR34aqvj6Fg; "
              "wt2=DqGMf0HanmBkdZ4PsRel6AUe9ykcZ5SQswlCatNFNyk_qoE2Nj2QHFpCB4HGCnieyVLSqHMnuOC5EmfLgnPwnLw~~; "
              "wbg=0; "
              "__zp_seo_uuid__=1c32644e-5ea8-40a6-a7e3-b97cf17a837e; "
              "__l=r=https%3A%2F%2Fwww.so.com%2Flink%3Fm%3DbdW%252BQYgfnRgWA%252BsNz3Nul%252FWMmOi5hMfu30%252BQISIrK%252FX2b%252FoqH9bI63StzzSHCubQrdNEkrTC3LjFlCk6zZLPH4Wo0IM3XUdXkNO8KqC4%252B72PkbHs0eZ9uus5wQj2PPwQXeRYDzbq30nW3T8Qret0%252FHTIMDocEMhxz0UoaIA%253D%253D&l=%2Fcitysite%2Fbeijing%2F&s=1; "
              "Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1678184101,1678712819; "
              "Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1678712821; "
              "__c=1678712821; "
              "__g=-; "
              "__a=76476689.1670318154.1678184101.1678712821.60.6.1.53; "
              "__zp_stoken__=f933eWCRUUS9CaWRjXCgNXWZVVzdZNF8tXDx9Omh4RmhnSTwpfCoAMnFjDAxmcwRWR0dNXjg%2BH1AtQmZABAADTjNRRFRMMHhQEC0lDzgFMBR%2BIAkqTCZBRhgNJkdtVHgdBX5%2FPzhfNFVgfhY%3D"
}
proxies = {}

url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json'
params = {
    "scene": "1",
    "query": "python",
    "city": "101010100",
    "experience": "",
    "degree": "",
    "industry": "",
    "scale": "",
    "stage": "",
    "position": "",
    "salary": "",
    "multiBusinessDistrict": "",
    "page": "1",
    "pageSize": "30"
}

response = requests.get(url, headers=headers, params=params, data={}, proxies=proxies)
data = response.json()
print(data)
# print(response)
for job in data["zpData"]["jobList"]:
    securityId = job["securityId"]
    encryptJobId = job["encryptJobId"]
    encryptBrandId = job["encryptBrandId"]
    lid = job["lid"]

    jobName = job["jobName"]  # 职位名称
    salaryDesc = job["salaryDesc"]  # 职位薪资
    jobLabels = job["jobLabels"]  # 工作经历+学历
    areaDistrict = [job["areaDistrict"], job["businessDistrict"]]  # 所在区域+附近区域
    brandNameAndScaleName = [job["brandName"], job["brandScaleName"]]  # 公司名称+公司人数
    bossNameAndTitle = [job["bossName"], job["bossTitle"]]  # 招聘人+招聘人职位

    company_url = f"https://www.zhipin.com/gongsir/{encryptBrandId}.html?ka=company-jobs"
    headers["referer"] = f"https://www.zhipin.com/gongsi/{encryptBrandId}.html?ka=job-cominfo"
    response = requests.get(company_url, headers=headers, params={}, data={}, proxies=proxies)
    data = response.text
    selector = parsel.Selector(data)
    num = selector.xpath('//div[@class="company-tab"][1]/a[2]/text()').get()

    detail_url = f"https://www.zhipin.com/job_detail/{securityId}.html?lid={lid}&securityId={securityId}"
    response = requests.get(detail_url, headers=headers, params={}, data={}, proxies=proxies)
    data = response.text
    selector = parsel.Selector(data)
    jobDetail = selector.xpath('//div[@class="text"]//text()').getall()



    print(jobName, salaryDesc, jobLabels, areaDistrict, brandNameAndScaleName, bossNameAndTitle, num, jobDetail)
    break








"""
import parsel
import requests
import pprint
from subcase.疫情大数据.tools import getip
from subcase.疫情大数据.tools import getua
from selenium import webdriver
from selenium.webdriver import ChromeOptions


url = "https://www.zhipin.com/gongsir/ee6a1eb8c53f8a020nJ729q6.html"

def get_value():
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    # option.add_argument('--no-sandbox')
    # option.add_argument('--disable-dev-shm-usage')
    # option.add_argument("--window-size=1920,1080")
    option.add_argument(f'--proxy-server=https://{getip()}')
    option.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'")
    browser = webdriver.Chrome(options=option)
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    })
    browser.get(url)
    # data = browser.page_source
    data = browser.get_cookies()
    for i in data:
        try:
            if i["name"] == "__zp_stoken__":
                value = i["value"]
                # print(value)
                return value
        except:
            continue

headers = {
    "User-Agent": getua(),
    "cookie": f"__zp_stoken__={get_value()}"
}
proxies = {
    'http': 'http://' + getip(),
    # 'https': 'https://' + getip(),
}


detail_url = f"https://www.zhipin.com/job_detail/a50dc26513d6d81e1XZ53d68FlpR.html"
response = requests.get(detail_url, headers=headers, params={}, data={}, proxies=proxies)
data = response.text
# print(data)
selector = parsel.Selector(data)
jobDetail = selector.xpath('//div[@class="text"]//text()').getall()
print(jobDetail)

"""


























