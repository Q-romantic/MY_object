# -*- coding: utf-8 -*-
"""
@Time    : 2023/1/19  019 下午 16:31
@Author  : Jan
@File    : 递归深度和堆栈溢出.py
"""
import sys
import math
import types
import pysnooper

""" {如下共四种解决办法} """


class TailRecurseException(BaseException):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):
    """
    This function decorates a function with tail call
    optimization. It does this by throwing an exception
    if it is it&#39;s own grandparent, and catching such
    exceptions to fake the tail call optimization.

    This function fails if the decorated5
    function recurses in a non-tail context.
    """

    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func


# 方法一：
# 尾递归优化，默认不带装饰器会超系统默认递归深度 1000
# sys.setrecursionlimit(3000)  # 可以修改默认递归深度
# threading.stack_size(12000000)  # 修改堆栈大小时需要单开进程，并且要结合上面递归深度一起设置才有效
@tail_call_optimized  # 使用时有个条件是返回递归函数外部不能带有计算表达式
def f0(i, res=0):
    if i == 0:
        return res + i
    return f0(i - 1, res + i)


result = f0(9999)
print(result, '----f0')


# 方法二：
# 用 while 循环代替
def f1(i, res=0):
    while i >= 0:
        res += i
        i -= 1
    return res


result = f1(9999)
print(result, '----f1')


# 方法三：
# 使用 “尾递归 + 生成器” 彻底解决堆栈溢出
def f_recursive(i, res=1):
    if i == 1:
        yield res
    yield f_recursive(i - 1, res + i)


def f_recursive_wapper(generator, i):
    gen = generator(i)
    while isinstance(gen, types.GeneratorType):
        gen = gen.__next__()
    return gen


result = f_recursive_wapper(f_recursive, 9999)
print(result, '----f_recursive')


# 应用测试效果
def advanced(a, b, c, d, k=0):  # k 是自增变量(如下 m-n 的值)，可取值 0 - n ，直到满足条件
    # 原理是假设各自商为 m,n ,对各自乘以对方的除数，得到新除数为二者最小公倍数，故得知 acm+bc=cN,acn+ad=aN ,再带入其求差计算出 N 的通式
    x, y = divmod(a * c * k + b * c - a * d, c - a)
    if y == 0 and x > 0:
        yield x
    else:
        yield advanced(a, b, c, d, k + 1)


def f_recursive_wapper2(generator, a, b, c, d):
    gen = generator(a, b, c, d)
    while isinstance(gen, types.GeneratorType):
        gen = gen.__next__()
    return gen


a, b = [5, 4]
c, d = [7, 6]
e, f = [9, 8]
g, h = [11, 0]
x, y = a * c, f_recursive_wapper2(advanced, a, b, c, d)
x, y = e * x, f_recursive_wapper2(advanced, e, f, x, y)
x, y = g * x, f_recursive_wapper2(advanced, g, h, x, y)
N1 = f_recursive_wapper2(advanced, 1, 0, x, y)
for n in range(20):
    N = 1 * x * n + N1
    print(N, end=',')
print('----------4.1.1')

# @tail_call_optimized
# def fibonacci(i, a=0, b=1):
#     print(a, end=',')
#     if i == 0:
#         return a
#     else:
#         return fibonacci(i - 1, b, a + b)
# res = fibonacci(20)
# print(res)

pass

# # @pysnooper.snoop()
# def fibonacci(i, a=0, b=1):
#     def run(i, a=0, b=1):
#         return i - 1, b, a + b
#
#     while i > 0:
#         i, a, b = run(i, a, b)
#         print(a, end=' ')
#     print()
# fibonacci(20)

pass


# 跳 n 级台阶跳法有多少种，每次最多跳 2 个台阶
def jumpFloor_1(number: int) -> int:
    a = b = 1
    for i in range(number):
        a, b = b, a + b
    return a


def jumpFloor_2(number: int) -> set:  # 使用 yield 生成器，此处期望返回数据类型不可以是 int、float、bool
    a = b = 1
    for i in range(number):
        yield a
        a, b = b, a + b


# 此类问题均归结为斐波那契序列，其通项公式表示为：
def general(n: int) -> int:
    return int((math.pow((1 + math.sqrt(5)) / 2, n) - math.pow((1 - math.sqrt(5)) / 2, n)) / math.sqrt(5))


n = 21
print(1, end=' ')
for i in range(1, n):
    print(jumpFloor_1(i), end=' ')
print()
for i in jumpFloor_2(n):
    print(i, end=' ')
print()
for i in range(1, n + 1):
    print(general(i), end=' ')
