# 线程池:一次性开辟一些线程。我们用户直接给线程池子提交任务。线程任务的调度交给线程池来完成

# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
#
#
# def fn(name):
#     print(name)
#     pass
#
#
# if __name__ == '__main__':
#     # 创建线程池
#     with ThreadPoolExecutor(20) as t:
#         for i in range(100):
#             t.submit(fn, name=f"线程{i}")
#     # 等待线程池中的任务全部执行完毕。才继续执行(守护)
#     print("123")




# 例子：



import requests
import csv
import time
from lxml import etree
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

f = open('data.csv', mode='w', encoding='utf-8', newline='')
csvwriter = csv.writer(f)
# f1 = open('data1.csv', mode='w', encoding='utf-8', newline='')
# csvwriter1 = csv.writer(f1)
# f2 = open('data1.csv', mode='w', encoding='utf-8', newline='')
# csvwriter2 = csv.writer(f2)
# f3 = open('data1.csv', mode='w', encoding='utf-8', newline='')
# csvwriter3 = csv.writer(f3)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36',
}
def download_one_page(url):
    resp = requests.get(url,headers=headers)
    resp.encoding = 'utf-8'
    # print(resp.text)
    html = etree.HTML(resp.text)
    ul = html.xpath('/html/body/div[4]/div[2]/div[1]/ul')[0]

    # lis = ul.xpath('./li')[1:]  # 去掉首行
    # lis = ul.xpath('./li[position()>1]')    # 去掉首行
    lis = ul.xpath('./li')
    for li in lis:
        txt = li.xpath('./h2/a/text()')[0]
        link = url[:20] + li.xpath('./h2/a/@href')[0]
        print(link, txt)
        # a.append(link)
        # a.append(txt)
        # a.append('\n')
        csvwriter.writerow([link, txt])
    pass


if __name__ == '__main__':
    # 创建线程池
    s = time.time()
    with ThreadPoolExecutor(50) as t:
        for i in range(50):
            url = f'https://www.yhdmp.cc/list/?order=更新时间&pagesize=24&pageindex={i}'
            t.submit(download_one_page, url)
    # 等待线程池中的任务全部执行完毕。才继续执行(守护)
    f.close()
    e = time.time()
    print(e - s)
    print("123")


    # s = time.time()
    # for i in range(1):
    #     url = f'https://www.yhdmp.cc/list/?order=更新时间&pagesize=24&pageindex={i}'
    #     download_one_page(url)
    # e = time.time()
    # print(e-s)

