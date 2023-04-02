import requests
import csv
import re

url1 = 'http://www.xinfadi.com.cn/priceDetail.html'
url2 = 'http://www.xinfadi.com.cn/getChildCat.html'
url3 = 'http://www.xinfadi.com.cn/getPriceData.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36',
}


class BeiJingXinFaDi(object):

    def list_Big_class(self):
        a = []
        response = requests.get(url1, headers=headers)
        page_content = response.text
        # print(page_content)
        result = re.findall(r'<li class="lis" ><a href="javascript:cat(?P<id>.*?)">(?P<name>.*?)</a></li>',
                            page_content,
                            re.S)
        for it in result:
            # print(it[1], it[0].strip('(').strip(')'))
            # print({it[1]: it[0][1:-1]})
            a.append(it[0][1:-1])
        return a

    def list_Small_class(self, li):
        b = []
        for i in li:
            b.append(self.Small_class(i))
        return b

    def Small_class(self, id):
        c = []
        data1 = {
            'prodCatid': id,
        }
        response = requests.post(url2, headers=headers, data=data1)
        page_content = response.json()
        if page_content == []:
            c.append((id, ''))
        else:
            for i in page_content:
                # print(id, i['names'], i['id'])
                c.append((id, i['id']))
        return c

    def get_data(self, tuple_data):
        data2 = {
            'limit': 100,  # 单页显示行数
            'current': 1,
            # 'pubDateStartTime': '2002/01/01',  # 查询开始时间
            # 'pubDateEndTime': '2022/12/31',  # 查询结束时间
            'prodPcatid': tuple_data[0],  # 一级大分类
            'prodCatid': tuple_data[1],  # 二级小分类
            'prodName': '',
        }
        response = requests.post(url3, headers=headers, data=data2)
        page_content = response.json()
        # print(page_content)

        for k in page_content['list']:
            prodid = k['id']
            prodName = k['prodName']
            prodCatid = k['prodCatid']
            prodCat = k['prodCat']
            prodPcatid = k['prodPcatid']
            prodPcat = k['prodPcat']
            lowPrice = k['lowPrice']
            highPrice = k['highPrice']
            avgPrice = k['avgPrice']
            place = k['place']
            specInfo = k['specInfo']
            unitInfo = k['unitInfo']
            pubDate = k['pubDate']
            status = k['status']
            userIdCreate = k['userIdCreate']
            userIdModified = k['userIdModified']
            userCreate = k['userCreate']
            userModified = k['userModified']
            gmtCreate = k['gmtCreate']
            gmtModified = k['gmtModified']
            # li_all = [prodid, prodName, prodCatid, prodCat, prodPcatid, prodPcat, lowPrice, highPrice, avgPrice, place, specInfo, unitInfo, pubDate, status, userIdCreate, userIdModified, userCreate, userModified, gmtCreate, gmtModified]
            li_sub = [prodid, prodCat, prodPcat, prodName, lowPrice, avgPrice, highPrice, specInfo, place, unitInfo,
                      pubDate]
            # print(li_sub)
            return li_sub


with open('data.csv', mode='w', encoding='utf-8', newline='') as f:
    csvwriter = csv.writer(f)
    TT = ['prodid', '一级分类', '二级分类', '品名', '最低价', '平均价', '最高价', '规格', '产地', '单位', '发布日期']
    csvwriter.writerow(TT)
    X = BeiJingXinFaDi()
    ll = X.list_Big_class()
    for i in X.list_Small_class(ll):
        for j in i:
            li = X.get_data(j)
            print(li)
            csvwriter.writerow(li)
print('Done')
