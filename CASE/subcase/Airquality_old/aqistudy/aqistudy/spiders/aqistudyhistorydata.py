# -*- coding: utf-8 -*-
import base64
import pprint
import random
import re
import sys
import time
import hashlib
import urllib.parse
import execjs
import scrapy
import json
from jsmin import jsmin
from scrapy import Spider, Request, cmdline, FormRequest
from full_city_info import get_citys_urls, user_agent_list

# from ..items import AqistudyItem
# from subcase.Airquality_old.aqistudy.aqistudy.items import AqistudyItem


class AqistudyhistorydataSpider(scrapy.Spider):
    name = 'aqistudyhistorydata'
    allowed_domains = ['aqistudy.cn']
    # start_urls = [
    #     'https://www.aqistudy.cn/historydata/daydata.php?city=神农架林区&month=202112',
    #     'https://www.aqistudy.cn/historydata/daydata.php?city=神农架林区&month=202201',
    # ]
    # start_urls = get_citys_urls()

    def start_requests(self):
        start_urls = [
            'https://www.aqistudy.cn/historydata/daydata.php?city=神农架林区&month=202112',
            'https://www.aqistudy.cn/historydata/daydata.php?city=神农架林区&month=202201',
        ]
        for url in start_urls:
            yield scrapy.Request(
                url=url,
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36"},
                callback=self.parse,
                dont_filter=True
            )

    def parse(self, response):
        print(response.url)
        info = re.findall('city=(.*?)&month=(.*)', response.url)[0]
        add_params = {}
        add_params['city'] = urllib.parse.unquote(info[0])
        add_params['month'] = info[1]
        data = response.text
        # print(add_params)
        head_url = 'https://www.aqistudy.cn/historydata/'
        main_js_urls = re.findall('<script type="text/javascript" src="(.*?)"></script>', data)  # xpath:'/html/body/script[2]'
        # print(main_js_urls)
        main_js_url = head_url + main_js_urls[1]
        headers = {"User-Agent": random.choice(user_agent_list)}
        yield Request(main_js_url, headers=headers, callback=self.parse_next_1, cb_kwargs=add_params, dont_filter=True)

    def parse_next_1(self, response, city, month):
        data = response.text
        data = data.replace('eval', '')
        data = execjs.eval(data)
        # print(data)
        if 'dweklxde(' in data:
            str_count = data.count('dweklxde')
            # print(str_count)
            data = re.findall("\'(.*?)\'", data)[0]
            # print(data)
            while str_count:
                data = base64.b64decode(data)
                str_count -= 1
            data = jsmin(data.decode())
        params_name = re.search('data:\{(.*?):(.*?)\},', data)
        params_key = params_name.group(1)
        params_value = params_name.group(2)
        encode_fn_name = re.findall('if\(!.*?\)\{var .*?=(.*?)\(', data)[0]

        method = "GETDAYDATA"
        str_object = {"city": city, "month": month}
        with open('1.js', mode='r') as f1:
            data1 = f1.read()
        data = data1 + data
        params = {
            params_key: execjs.compile(data).call(encode_fn_name, method, str_object)
        }
        print(params)
        # print(params_key, params_value, encode_fn_name)

        name = re.findall('success:function\((.*?)\)\{', data)[0]
        decode_fn_name = re.findall(f'success:function\({name}\).*{name}=(.*?)\({name}\);', data)[0]
        # print(name)
        # print(decode_fn_name)

        add_params = {}
        add_params['data'] = data
        add_params['decode_fn_name'] = decode_fn_name
        add_params['city'] = city
        data_url = 'https://www.aqistudy.cn/historydata/api/historyapi.php'
        # self.headers['Referer'] = data_url + f'?city={self.city}&month={self.month}'  # 不更改也可以
        headers = {"User-Agent": random.choice(user_agent_list)}
        yield FormRequest(data_url, method='post', headers=headers, formdata=params, callback=self.parse_next_2, cb_kwargs=add_params)
        pass

    def parse_next_2(self, response, data, decode_fn_name, city):
        last_data = response.text
        print(last_data)
        last_data = execjs.compile(data).call(decode_fn_name, last_data)
        last_data = json.loads(last_data)
        pprint.pprint(last_data)
        # for i in last_data['result']['data']['items']:
        #     i['city'] = city
        #     print(i)
        #     item = AqistudyItem(
        #         time_point=i['time_point'],
        #         aqi=i['aqi'],
        #         quality=i['quality'],
        #         pm2_5=i['pm2_5'],
        #         pm10=i['pm10'],
        #         co=i['co'],
        #         so2=i['so2'],
        #         no2=i['no2'],
        #         o3=i['o3'],
        #         city=i['city'],
        #         rank=i['rank'],
        #     )
        #     yield item


if __name__ == '__main__':
    # cmdline.execute("scrapy crawl aqistudyhistorydata -s LOG_FILE=all.log".split())
    cmdline.execute("scrapy crawl aqistudyhistorydata --nolog".split())
