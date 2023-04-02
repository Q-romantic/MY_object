# -*- coding: utf-8 -*-
"""
@Time    : 2023/1/4  004 下午 16:10
@Author  : Jan
@File    : biji.py
"""
import base64
import copy
import json

import math
import time

import cv2
import numpy as np
import requests

""" {} """

# class test:
#     def __init__(self, xxx, p=([],)):
#         if p[0]:
#             pass
#             print(xxx)
#         else:
#             p[0].append(1)
#             print(p, 'init', xxx)
#         pass
#
#     def ppp(self):
#         test.iii(self, '123------')
#         test(555).iii(123)
#         print(666)
#
#     def iii(self, a):
#         print(777, a)


# t = test(1)
# t.ppp()
# print('----')
# test(2).ppp()
# print('----')
# test(3).ppp()
# print('----')
# test(3).iii(444)

pass

# import cv2
# from PIL import Image
# from io import BytesIO
#
# # PIL转二进制: img ---> data
# img = Image.open('C:/Users/11390/Desktop/1.png')
# print(img, type(img))  # <class 'PIL.PngImagePlugin.PngImageFile'>
#
# bytesIO = BytesIO()
# img.save(bytesIO, format='PNG')  # format='JPEG'，实际未保存
# data = bytesIO.getvalue()
# print(data, type(data))  # <class 'bytes'>
#
# data = np.asarray(bytearray(data), dtype="uint8")
# image = cv2.imdecode(data, cv2.IMREAD_COLOR)
# print(image, type(image))  # <class 'numpy.ndarray'>
#
# # numpy矩阵转二进制（数组转二进制）: image ---> data
# data = cv2.imencode('.jpg', image)[1].tobytes()
# print(data, type(data))  # <class 'bytes'>
#
# # 二进制转PIL: data --> img
# img = Image.open(BytesIO(data))
# print(img, type(img))
#
# image = cv2.imread('C:/Users/11390/Desktop/1.png')
# print(image, type(image))  # <class 'numpy.ndarray'>
#
# cv2.imwrite('C:/Users/11390/Desktop/1122.png', image)
# img.save('C:/Users/11390/Desktop/1133.png')

pass

# def fn(a):
#     li = []
#     for i in a:
#         b = copy.deepcopy(a)
#         b.remove(i)
#         li.extend([b])
#     return li
#
#
# a = [1, 2, 3, 4, 5, 6]
# print(fn(a))

pass

# from working.ok.tools import excel_col_to_num_version_original
#
# print(excel_col_to_num_version_original('KZ'))
# print(excel_col_to_num_version_original('FM'))

pass

# for line in sys.stdin:
#     a = map(int, line.split())
#     print(a)
#     print(list(a))
#
# while 1:
#     a = map(int, input().split())
#     print(a)
#     print(list(a))

pass

# a = [1, 2, 3, 4, 5, 6]
# for i in a:
#     b=copy.deepcopy(a)
#     b.remove(i)
#     for j in b:
#         c = copy.deepcopy(b)
#         c.remove(j)
#         for k in c:
#             d = copy.deepcopy(c)
#             d.remove(k)
#             for l in d:
#                 print((i,j,k,l),end=' ')

pass

# # 方法一：
# from PIL import Image
#
# file_path = 'C:\\Users\\11390\\Desktop\\2.jpg'
#
# img = Image.open(file_path)
# imgSize = img.size  # 大小/尺寸
# w = img.width  # 图片的宽
# h = img.height  # 图片的高
# f = img.format  # 图像格式
#
# print(imgSize)
# print(w, h, f)

# # 方法二：
# import cv2
# import requests
# import numpy as np
# response = requests.get(url, headers=headers)
# data = response.content
# data = np.asarray(bytearray(data), dtype="uint8")
# img = cv2.imdecode(data, cv2.IMREAD_COLOR)
# y, x = img.shape[0:2]  # 高，宽
# print(x, y)

pass

# # 折弯列表，舍弃某个区间(即舍弃个数x)再返回
# def ring(a: list, x: int) -> list:
#     y, x = divmod(abs(x), len(a))
#     return [] if y > 0 and x == 0 else [a[i + x:] + a[:i] for i in range(len(a) - x)]
#
#
# a = [1, 2, 3, 4, 5, 6]
# for i in range(-27, 28):
#     print(i, ring(a, i))

pass

# while 1:
#     a, b, c = input().split()
#     print(a, b, c)
#
# import sys
#
# for line in sys.stdin:
#     a = line.split()
#     print(len(a[-1]))

pass

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [0, 1, 2, 3, 4, 5, 6, 7]
#
# print(list(filter(None, c)))
# print(list(filter(lambda x: x > 3, c)))
# print(list(map(lambda x, y: (x, y), a, b)))
# print(list(zip(a, b)))
#
# # for i in map(None, a, b):   # python3 之后已舍弃
# #     print(i)

pass

# n = 5
# x = 2
# from functools import reduce
#
# print(reduce(lambda x, y: x * y, range(1, n + 1), x))  # x * n!

pass

# import json
# import dill
# import inspect
#
# source = inspect.getsource(json.dumps)
# print(source)
# source = dill.source.getsource(json.dumps)
# print(source)
# cache = {}
# cache['MD5'] = cache['md5'] = '_md5.md5'
# print(cache)

pass

# print(math.comb(4, 2))
# print(math.perm(4, 2))

pass

# import itsdangerous
#
# salt = 'sdaf'  # 加盐，加调料，即密钥
# t = itsdangerous.TimedJSONWebSignatureSerializer(salt, expires_in=600)  # 过期时间600秒
# info = {'username': 'yangfan', 'user_id': 1}  # 加密的数据
#
# # =========加密token============
# token = t.dumps(info).decode()  # 指定编码格式
# print(token)  # 生成以 eyJ 开头加密数据
#
# print(token)
# # =========解密token============
# res = t.loads(token)
# print(t.secret_key)
# print(res)
# # 当超时或值有误则会报错

pass

# from functools import partial
#
#
# def add(x, y):
#     print(x, y)
#     return x + y
#
#
# add_y = partial(add, 3)  # add_y 是一个新的函数
# add_y(4)  # 7

pass

# # 单例模式，主要功能是减少多次实例化调用运行内存(通过类私有变量赋值，下次调用被覆盖)和特殊方法在初始化时只运行一次的情况
# class Solution:
#     # 定义类变量
#     # 记录第一个被创建对象的引用，代表着类的私有属性
#     _instance = None
#     # 记录是否执行过初始化动作
#     init_flag = False
#
#     def __init__(self, name, data):
#         self.name = name
#         self.data = data
#         # 使用类名调用类变量,不能直接访问。
#         if Solution.init_flag:
#             return
#         self.xml_load(self.data)
#         # 修改类属性的标记
#         Solution.init_flag = True
#
#     def __new__(cls, *args, **kwargs):
#         # 判断该类的属性是否为空；对第一个对象没有被创建，我们应该调用父类的方法，为第一个对象分配空间
#         if cls._instance == None:
#             # 把类属性中保存的对象引用返回给python的解释器
#             cls._instance = object.__new__(cls)
#         # 如果cls._instance不为None,直接返回已经实例化了的实例对象
#         return cls._instance
#
#     def xml_load(self, data):
#         print("初始化init", self.name, data)
#
#     def Parser(self):
#         print("解析完成finish", self.name)
#
#
# a = Solution("A11", 10)  # 第一次实例化对象地址，后面创建都是在该地址上进行的
# a.Parser()
# b = Solution("A12", 20)  # b把a覆盖掉
# b.Parser()
# print(id(a))
# print(id(b))
# print(a.name)
# print(b.name)
#
# xxx = 123456
#
# import _ctypes
#
# # 通过_ctypes的api进行对内存地址寻找对象
# obj = _ctypes.PyObj_FromPtr(id(xxx))
# # 打印出来通过内存地址寻找到的对象
# print(obj)
# obj = _ctypes.PyObj_FromPtr(id(b))
# obj.Parser()

pass

# from PIL import Image
# im = Image.open("C:/Users/11390/Desktop/2.jpg")
# im.rotate(45).show()


# import jwt
# data={
#     'iss': '45z6lwBVohUEGSZyF7ZDJH8WYA6vnRVr',
#     'iat': 1675799397,
#     # 'aud': 'pwa-search',
#     'exp': 1675802997,
#     'sub': '8bf131fb-382a-4a88-9c1e-9494cd787ebf'
#
# }
# key='secret-key'
# encoded_jwt = jwt.encode(data, key, algorithm='HS256')
# print(encoded_jwt)
# print(jwt.decode(encoded_jwt, key, algorithms='HS256'))


# import json
# from selenium import webdriver
# import time
#
# caps = {
#     'browserName': 'chrome',
#     'goog:loggingPrefs': {
#         'browser': 'ALL',
#         'driver': 'ALL',
#         'performance': 'ALL',
#     }
# }
# driver = webdriver.Chrome(desired_capabilities=caps)  # 增加;浏览器console记录???
#
# driver.get('https://partner.oceanengine.com/union/media/login/')
# # 必须等待一定的时间，不然会报错提示获取不到日志信息，因为絮叨等所有请求结束才能获取日志信息
# # time.sleep(1)
#
# request_log = driver.get_log('performance')
# # print(request_log)
#
# logs = [json.loads(log['message'])['message'] for log in request_log]
# for i in logs:
#     print(i)
#     # requestId = ''
#     # response_dict = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': requestId})
#     # body = response_dict["body"]
#     # # print(body)
#     # break

pass

# import jwt
# import json
# from datetime import datetime, timedelta
#
# payload = {
#     'iss': '45z6lwBVohUEGSZyF7ZDJH8WYA6vnRVr',
#     'aud': 'pwa-search',
#     'exp': str(time.mktime((datetime.now() + timedelta(minutes=30)).timetuple())),  # 令牌过期时间
#     'sub': '8bf131fb-382a-4a88-9c1e-9494cd787ebf'
# }
# s = 'ew0KCSJhbGciIDogIk5vbmUiLA0KCSJ0eXAiIDogImp3dCINCn0.' + base64.b64encode(json.dumps(payload).encode()).decode().replace('=', '')
# print(s)

pass

# from fake_useragent import UserAgent
# ua = UserAgent() ????????
# print(ua.chrome)
# url = 'useragentstring.com'

