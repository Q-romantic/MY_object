import requests,csv
from jsonpath import jsonpath

dic = {
    '蔬菜': [1186, {
        '水菜': 1199,
        '特菜': 1200}],

    '水果': [1187, {
        '进口果': 1201,
        '干果': 1202}],

    '肉禽蛋': [1189, {
        '猪肉类': 1205,
        '牛肉类': 1206,
        '羊肉类': 1207,
        '禽蛋类': 1208}],

    '水产': [1190, {
        '淡水鱼': 1209,
        '海水鱼': 1210,
        '其他类': 1211}],

    '粮油': [1188, {
        '米面类': 1212,
        '杂粮类': 1213,
        '食用油': 1214}],

    '豆制品': [1203, {'x': ''}],
    '调料': [1204, {'x': ''}]
}

url = 'http://www.xinfadi.com.cn/getPriceData.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36',
}
with open('data.csv', mode='w', encoding='utf-8', newline='') as f:
    csvwriter = csv.writer(f)
    T = ['prodid', '一级分类', '二级分类', '品名', '最低价', '平均价', '最高价', '规格', '产地', '单位', '发布日期']
    csvwriter.writerow(T)
    for i in dic:
        for j in dic[i][1]:
            # print(dic[i][0], dic[i][1][j])
            data = {
                'limit': 100,
                'current': 1,
                'pubDateStartTime': '2002/01/01',     # 查询开始时间
                'pubDateEndTime': '2022/12/31',       # 查询结束时间
                'prodPcatid': dic[i][0],                # 一级大分类
                # 'prodCatid': dic[i][1][j],              # 二级小分类
                'prodName': '',
            }
            response = requests.post(url, headers=headers, data=data)
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
                li_sub = [prodid, prodCat, prodPcat, prodName, lowPrice, avgPrice, highPrice, specInfo, place, unitInfo, pubDate]
                # print(li_sub)
                csvwriter.writerow(li_sub)
                # break
    print('Done')

