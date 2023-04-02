# import requests
# from login import headers

from threading import Thread

#
# # 方法一，推荐
# class MyThread(Thread):
#     def __init__(self, url, x):
#         Thread.__init__(self)
#         self.url = url
#         self.x = x
#     def run(self):
#         for i in range(10000, 1000000):
#             params1 = {'answer': i, 'id': self.x}
#             resq = requests.get(self.url, headers=headers, params=params1)
#             data = resq.json()
#             print(data)
#             if data['info'] == 'success':
#                 print('---' * 30, 'success', f'answer={i}')
#                 break
#             # params2 = {'answer': i, 'id': '18'}
#             # resq = requests.get(url, headers=headers, params=params2)
#             # data = resq.json()
#             # print(data)
#             # if data['info'] == 'success':
#             #     print('---' * 30, 'success', f'answer={i}')
#             #     break
#
#
# if __name__ == '__main__':
#     url = 'https://match.yuanrenxue.com/api/answer'
#     t1 = MyThread(url, 14)
#     t1.start()
#     t2 = MyThread(url, 18)
#     t2.start()
#     # for i in range(10):
#     #     print('主线程', i)



import sys
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fn(i, url, x, y):
    params1 = {'answer': i, 'id': x}
    # resq = requests.get(url, headers=headers, params=params1)
    # data = resq.json()
    print(i)
    if i == 100:
        print('---' * 30, 'success', f'answer={i}')
        sys.exit()
    params2 = {'answer': i, 'id': y}
    # resq = requests.get(url, headers=headers, params=params2)
    # data = resq.json()
    print(i)
    if i == 120:
        print('---' * 30, 'success', f'answer={i}')
        sys.exit()
    pass


if __name__ == '__main__':
    # 创建线程池
    url = 'https://match.yuanrenxue.com/api/answer'
    with ThreadPoolExecutor(10) as t:
        # for i in range(11190, 100000):
        for i in range(1, 300):
            t.submit(fn, i, url, 8, 18)
    # 等待线程池中的任务全部执行完毕。才继续执行(守护)
    print("123")











"""
a14 = {"status": "1", "state": "success",
       "data": [{"value": -3974}, {"value": -3628}, {"value": -2144}, {"value": 617}, {"value": -1687}, {"value": -571},
                {"value": -3526}, {"value": 3849}, {"value": -3756}, {"value": -800}]}
b14 = {"status": "1", "state": "success",
       "data": [{"value": 2125}, {"value": -1005}, {"value": -2283}, {"value": 1717}, {"value": 187}, {"value": 4903},
                {"value": 4238}, {"value": 1509}, {"value": -345}, {"value": -1015}]}
c14 = {"status": "1", "state": "success",
       "data": [{"value": 3616}, {"value": 441}, {"value": 457}, {"value": 5044}, {"value": -4040}, {"value": -44},
                {"value": 4652}, {"value": 482}, {"value": -2789}, {"value": 3036}]}
a18 = {"status": "1", "state": "success",
       "data": [{"value": 4838}, {"value": 458}, {"value": 3093}, {"value": 4305}, {"value": -2295}, {"value": -2048},
                {"value": -3975}, {"value": -708}, {"value": -3991}, {"value": -287}]}
b18 = {"status": "1", "state": "success",
       "data": [{"value": 1077}, {"value": 3873}, {"value": 1801}, {"value": 1783}, {"value": 3426}, {"value": 969},
                {"value": -143}, {"value": 5129}, {"value": 295}, {"value": -1955}]}
c18 = {"status": "1", "state": "success",
       "data": [{"value": 1930}, {"value": 4369}, {"value": 4370}, {"value": 5548}, {"value": -1504}, {"value": 5674},
                {"value": -554}, {"value": 4832}, {"value": 4086}, {"value": -3756}]}

li = []
for i in a14['data']:
    li.append(i['value'])
print(li)
print(sum(li), '---1')
for i in b14['data']:
    li.append(i['value'])
print(li)
print(sum(li), '---2')
for i in c14['data']:
    li.append(i['value'])
print(li)
print(sum(li), '---3')

print('---'*30)

li = []
for i in a18['data']:
    li.append(i['value'])
print(li)
print(sum(li), '---1')
for i in b18['data']:
    li.append(i['value'])
print(li)
print(sum(li), '---2')
for i in c18['data']:
    li.append(i['value'])
print(li)
print(sum(li), '---3')
"""