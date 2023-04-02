import requests, re, csv

url = 'https://movie.douban.com/top250'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36',
}

response = requests.get(url, headers=headers)
page_content = response.text
# 解析数据
obj = re.compile(r'<span class="title">(?P<name>.*?)</span>.*?'
                 r'<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<num>.*?)人评价</span>', re.S)
# 开始匹配，方法1
result1 = obj.finditer(page_content)
f1 = open('data1.csv', mode='w', encoding='utf-8', newline='')
csvwriter = csv.writer(f1)
for it in result1:
    # print(it.group("name"))
    # print(obj.search(page_content).group('name'))     # 用search可以减少使用for循环
    # print(it.group("year").strip())
    # print(it.group("score"))
    # print(it.group("num"))
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    # print(dic.values())
    csvwriter.writerow(dic.values())
f1.close()
print('over1!')


# 开始匹配，方法2
result2 = re.findall(r'<span class="title">(?P<name>.*?)</span>.*?'
                     r'<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                     r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                     r'<span>(?P<num>.*?)人评价</span>', page_content, re.S)

with open('data2.csv', mode='w', encoding='utf-8', newline='') as f2:
    csvwriter = csv.writer(f2)
    for it in result2:
        it = list(it)
        it[1] = it[1].strip()
        csvwriter.writerow(it)
print('over2!')


# 开始匹配，方法3
result3 = obj.finditer(page_content)
with open('data3.csv', mode='w', encoding='utf-8', newline='') as f3:
    csvwriter = csv.writer(f3)
    for it in result3:
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())  # csvwriter是按列表一次性写入
print('over3!')
