# -*- coding: utf-8 -*-
"""
@Time    : 2023/1/28  028 下午 20:48
@Author  : Jan
@File    : 装饰器.py
"""
import time

""" { 常用装饰器 } """


# 实例化
def instantiation(function):
    return function()


# 计时
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print(stop - start)
        return res

    return wrapper


""" 如下是使用方法：例子 """


@instantiation  # 普通装饰器
class B:

    @staticmethod
    # @instantiation    # 加上此行，如下可以这样不带括号调用 @B.instantiation
    def instantiation(x=1):
        def inner(function):
            print(x)
            return function()

        return inner


@B.instantiation()  # 调用类装饰器 或 带参数的装饰器
class A:
    class C:
        @classmethod  # 不加此行时需要这样调用 A.C().say3()
        def say3(self):
            A.say2(8)  # 类与类间调用
            print("say3...")

    @classmethod  # 加不加都可以调用
    def say1(self):
        self.say2(6)
        print("say1...")

    @staticmethod
    def say2(x):
        print(x ** 2)


if __name__ == '__main__':
    pass
    # A.say1()  # 正常需要 A().say1() 调用，有装饰器后，在调用时就对其实例化了
    # A.say2(5)
    A.C.say3()
