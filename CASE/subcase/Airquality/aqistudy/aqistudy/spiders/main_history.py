import base64
import os
import re
import urllib.parse
import execjs
import requests
import scrapy
import json
from jsmin import jsmin
from scrapy import Request, cmdline, FormRequest
from full_city_info import get_citys_urls
from working.all_tools.tools import getua

# from ..items import AqistudyItem
from subcase.Airquality.aqistudy.aqistudy.items import AqistudyItem

start_urls = get_citys_urls()
# print(start_urls)
class MainHistorySpider(scrapy.Spider):
    name = 'main_history'
    allowed_domains = ['aqistudy.cn']
    start_num = 0
    if os.path.exists('start_num.txt'):
        with open('start_num.txt', mode='r') as f:
            start_num = len(start_urls) - int(f.read())

    def start_requests(self):
        # start_urls = [
        #     'https://www.aqistudy.cn/historydata/daydata.php?city=神农架林区&month=202112',
        #     # 'https://www.aqistudy.cn/historydata/daydata.php?city=神农架林区&month=202201',
        #     # 'https://www.aqistudy.cn/historydata/daydata.php?city=神农架林区&month=202202',
        #     # 'https://www.aqistudy.cn/historydata/daydata.php?city=神农架林区&month=202203',
        #     # 'https://www.aqistudy.cn/historydata/daydata.php?city=神农架林区&month=202204',
        # ]
        # start_urls = get_citys_urls()
        for url in start_urls[self.start_num:]:
            yield scrapy.Request(
                url=url,
                headers={"User-Agent": getua()},
                callback=self.parse,
                dont_filter=True,
            )

    def parse(self, response):
        # print(response)
        print(response.url)
        info = re.findall('city=(.*?)&month=(.*)', response.url)[0]
        headers = {"User-Agent": getua()}
        add_params = {}
        add_params['city'] = urllib.parse.unquote(info[0])
        add_params['month'] = info[1]
        add_params['headers'] = headers

        data = response.text
        # print(add_params)
        head_url = 'https://www.aqistudy.cn/historydata/'
        main_js_urls = re.findall('<script type="text/javascript" src="(.*?)"></script>', data)  # xpath:'/html/body/script[2]'
        # print(main_js_urls)
        main_js_url = head_url + main_js_urls[1]

        yield Request(main_js_url, headers=headers, callback=self.parse_next_1, cb_kwargs=add_params, dont_filter=True)

    def parse_next_1(self, response, city, month, headers):
        # print(response)
        # print(response.url)
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
        # print(params)   # 加密的请求参数
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
        yield FormRequest(data_url, method='post', headers=headers, formdata=params, callback=self.parse_next_2, cb_kwargs=add_params, dont_filter=True)
        pass

    def parse_next_2(self, response, data, decode_fn_name, city):
        # print(response)
        # print(response.url)
        last_data = response.text
        # print(last_data)    # 加密的数据
        try:
            last_data = execjs.compile(data).call(decode_fn_name, last_data)
            last_data = json.loads(last_data)
            # pprint.pprint(last_data)
            for i in last_data['result']['data']['items']:
                i['city'] = city
                print(i)
                item = AqistudyItem(
                    time_point=i['time_point'],
                    aqi=i['aqi'],
                    quality=i['quality'],
                    pm2_5=i['pm2_5'],
                    pm10=i['pm10'],
                    co=i['co'],
                    so2=i['so2'],
                    no2=i['no2'],
                    o3=i['o3'],
                    city=i['city'],
                    rank=i['rank'],
                )
                yield item
            self.start_num += 1
            with open("start_num.txt", mode="w", encoding="utf-8") as f:
                f.write(str(len(start_urls) - self.start_num))

        except:

            print("error")
            # self.crawler.engine.close_spider(self, 'no data')
            # print("close_spider ok")



if __name__ == '__main__':
    api_url = "http://v2.api.juliangip.com/dynamic/getips?num=1&pt=1&result_type=text&split=1&trade_no=1727174320704510&sign=d3f8576b7d8bd5a0aeb186fbdda12bba"
    proxy_ip = requests.get(api_url).text
    res = requests.get('http://icanhazip.com/', proxies={'http': f'http://{proxy_ip}'})
    print(res.content)
    with open(f'C:\Y\Case\subcase\疫情大数据\ip.txt', mode='w') as f:
        f.write(proxy_ip)

    # cmdline.execute("scrapy crawl main_history -s LOG_FILE=all.log".split())
    cmdline.execute("scrapy crawl main_history --nolog".split())


