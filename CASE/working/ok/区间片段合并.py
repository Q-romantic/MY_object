# -*- coding: utf-8 -*-
"""
@Time    : 2023/1/22  022 下午 19:15
@Author  : Jan
@File    : 区间片段合并.py
"""

""" { 区间片段合并，或在指定偏差值范围内合并 } """

import pysnooper

# 比较有意思的对象转换
# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b
#
#
# a = Interval(11, 22)
# print(a.start, a.end)
# li = [[1, 10], [15, 20], [18, 30], [33, 40]]
# li = list(map(lambda x: Interval(*x), li))
# print(li)
# print(li[0].start)
# li = list(map(lambda x: [x.start, x.end], li))
# print(li)


pass


# 判断两组片段是否满足合并条件
# @pysnooper.snoop()
def judg(a: list, b: list, z=[]) -> list:
    x = b[0] - a[1]
    if b[0] <= a[1] and a[1] <= b[1] or x in z:
        return [[a[0], b[1]]]
    elif a[0] <= b[0] and b[1] <= a[1]:
        return [a]  # 前者包含后者 注意：后面会根据返回长度判断是否已合并，所以必须多加一层 []
    else:
        return [a, b]  # 不满足原样输出


# 方法二
# @pysnooper.snoop()
def combine(li: list, z=[]) -> list:
    li = sorted(li, key=lambda x: x[0])  # 规整列表，排除乱序情况
    i = 1
    res = [li[0]]
    while i < len(li):
        tmp = judg(res[-1], li[i], z)
        if len(tmp) == 1:
            res[-1][1] = tmp[0][-1]
        else:
            res.append(tmp[1])
        i += 1
    return res


# 方法一：
def merge(li, z=[]):
    if not li:
        return []
    li.sort(key=lambda x: x[0])
    res = [li[0]]
    for i in li[1:]:
        x = i[0] - res[-1][1]
        if i[0] <= res[-1][1] and res[-1][1] < i[1] or x in z:
            res[-1][1] = i[1]
        elif res[-1][1] < i[0]:
            res.append(i)
        else:
            pass
    return res


# 输入样例：
# [1, 10], [15, 20], [18, 30], [33, 40]
# [5, 4, 3, 2]
# li = eval("[" + input() + "]")
# z = eval(input())

li = [[1, 10], [15, 20], [18, 30], [33, 40]]
z = [5, 4, 3, 2]  # 指定的偏差值范围

print(li)
print(combine(li))  # 合并有重叠的区域
print(combine(li, z))  # 拼接间距存在 z 列表值，方法二
print(merge(li, z))  # 拼接间距存在 z 列表值，方法一
