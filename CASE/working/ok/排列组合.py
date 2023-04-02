# -*- coding: utf-8 -*-
"""
@Time    : 2023/1/30  030 下午 17:39
@Author  : Jan
@File    : 排列组合.py
"""

""" { 排列组合 } """

import copy
from itertools import combinations
from itertools import permutations
from itertools import product


# 装饰器，统计返回列表长度
def length(function):
    def inner(*args, **kwargs):
        res = function(*args, **kwargs)
        return res if kwargs.get('flag') else (f"共有: {len(res)} 种", res)

    return inner


# 组合，方法一：仅限每2个组合
@length
def combination(li: list) -> list:
    def combin(a, li):
        return [(a,) + (i,) for i in li]

    res = []
    for i in range(len(li) - 1):
        # t = combin(li.pop(0), li)  # li = copy.copy(li) ，缺陷：会修改原列表
        t = combin(li[i], li[i + 1:])  # 优化上一条缺陷
        res.extend(t)
    return res


# 全排列，方法一：
@length
def permutation(li: list, *args, **kwargs) -> list:
    res = []
    start, end = 0, len(li) - 1

    def fn(li, start, end, res):
        if start == end:
            res.append(copy.copy(li))
        for i in range(start, end + 1):
            li[start], li[i] = li[i], li[start]  # 将第i个元素与首位元素交换
            fn(li, start + 1, end, res)  # 子序列进行全排列
            li[start], li[i] = li[i], li[start]  # 将i个元素放回原位置，准备下一个元素的交换

    fn(li, start, end, res)
    return [tuple(i) for i in res]


# 组合,不限元素个数，列表中元素不允许重复出现
@length
def allCombinations(li: list, n: int = -1) -> list:
    choice = [()] if n == 0 else []  # 装指定选择的 n 个数
    res = [()]  # 默认列出所有组合
    resall = [()]  # 默认列出所有组合并排列
    for i in li:
        tmp = []
        for j in res:  # 把之后的每一个元素与 res 组合
            t = j + (i,)
            if len(t) == n:
                choice.append(t)
            tt = permutation(list(t), flag=True)  # 设置一个开关，不对其内部调用结果装饰
            resall += tt
            tmp.append(t)
        res += tmp
    return resall if n < -1 else res if n == -1 else choice


# 折弯列表，舍弃某个区间(即舍弃个数x)再返回
@length
def ring(a: list, x: int = 0) -> list:
    y, x = divmod(abs(x), len(a))
    return [] if y > 0 and x == 0 else [a[i + x:] + a[:i] for i in range(len(a) - x)]


if __name__ == '__main__':
    m = 2
    li = [1, 2, 3, 4]

    # 使用系统模块
    print((lambda x: (f"共有: {len(x)} 种", x))(list(combinations(li, m))))  # 组合,不限元素个数，列表中元素不允许重复出现，通式：math.comb(n, m)
    print((lambda x: (f"共有: {len(x)} 种", x))(list(permutations(li, m))))  # 排列，列表中元素不允许重复出现，通式：math.perm(n, m)
    print((lambda x: (f"共有: {len(x)} 种", x))(list(product(li, repeat=m))))  # 排列，列表中元素可以重复出现，通式：[C(n, 1)]**m = n**m

    # 自定义算法
    print(combination(li))  # 组合，仅限2个，不推荐
    print(permutation(li))  # 全排列，通式：A(n, n) = n!，挑选 m 个进行排列，通式：A(n, m) = n!/(n-m)!
    print(allCombinations(li))  # 任意不重复组合不排列，所有可能，可以是 0 个或 n 个，通式：C(n, 0) ... + ... C(n, n) = 2**n
    print(allCombinations(li, m))  # 任意不重复组合不排列，挑选 m 个组合，通式：C(n, m) = n!/(n-m)!/m!
    print(allCombinations(li, -2))  # 任意不重复组合并排列，所有可能，通式：C(n, 0)*A(0, 0) ... + C(n, r)*A(r, r) + ... C(n, n)*A(n, n) = ???

    # 列表配对
    a = [1, 2, 3, 4]
    b = [6, 7, 8, 9]
    result = [(i, j) for i in a for j in b if i != j]
    print((lambda x: (f"共有: {len(x)} 种", x))(result))  # 通式：a * b

    # 环形列表
    print(ring(li))
