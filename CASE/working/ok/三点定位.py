# from itertools import combinations, permutations
#
# r = 30
# x = 115.542246
# y = 39.642543
# a = []
# for i in range(r):
#     a.append(i)
# for i in range(r):
#     a.append(i)
# # a = [0, 1, 2, 0, 1, 2]
# c = list(sorted(set(combinations(a, 2))))
# # print(c)
# # print(len(c))
# for i in c:
#     print('[{}][lon]'.format(i)+str(x+i[0]/10)+'[/lon][lat]'+str(y+i[1]/10)+'[/lat]')

#
# import numpy as np
# import math
#
# import sympy
# from matplotlib.pyplot import plot
# from matplotlib.pyplot import show
# import matplotlib.pyplot as plt
#
#
# def triposition(xa, ya, da, xb, yb, db, xc, yc, dc):
#     x, y = sympy.symbols('x, y')
#     f1 = 2 * x * (xa - xc) + np.square(xc) - np.square(xa) + 2 * y * (ya - yc) + np.square(yc) - np.square(ya) - (
#                 np.square(dc) - np.square(da))
#     f2 = 2 * x * (xb - xc) + np.square(xc) - np.square(xb) + 2 * y * (yb - yc) + np.square(yc) - np.square(yb) - (
#                 np.square(dc) - np.square(db))
#     result = sympy.solve([f1, f2], [x, y])
#     locx, locy = result[x], result[y]
#     return [locx, locy]
#
#
# '''
# [-----天安门东-----][lon]116.40625[/lon][lat]39.91045[/lat]
# [-----   国贸-----][lon]116.46692[/lon][lat]39.91116[/lat]
# [-----大红门南-----][lon]116.40605[/lon][lat]39.839395[/lat]
# '''
# a1 = 4
# b1 = 1
# d1 = 1
#
# a2 = 2
# b2 = 1
# d2 = 1
#
# a3 = 3
# b3 = 0
# d3 = 1
#
# print(triposition(a1, b1, d1, a2, b2, d2, a3, b3, d3))


# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:50:29 2018
@author: dag
"""
import sympy
import numpy as np
import math
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import matplotlib.pyplot as plt
import matplotlib

# 解决无法显示中文问题，fname是加载字体路径，根据自身pc实际确定，具体请百度
zhfont1 = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simkai.ttf')

# 随机产生3个参考节点坐标
maxy = 1000
maxx = 1000
cx = maxx * np.random.rand(3)
cy = maxy * np.random.rand(3)
dot1 = plot(cx, cy, 'k^')

# 生成盲节点，以及其与参考节点欧式距离
mtx = maxx * np.random.rand()
mty = maxy * np.random.rand()
plt.show()
dot2 = plot(mtx, mty, 'go')
da = math.sqrt(np.square(mtx - cx[0]) + np.square(mty - cy[0]))
db = math.sqrt(np.square(mtx - cx[1]) + np.square(mty - cy[1]))
dc = math.sqrt(np.square(mtx - cx[2]) + np.square(mty - cy[2]))


# 计算定位坐标
def triposition(xa, ya, da, xb, yb, db, xc, yc, dc):
    x, y = sympy.symbols('x y')
    f1 = 2 * x * (xa - xc) + np.square(xc) - np.square(xa) + 2 * y * (ya - yc) + np.square(yc) - np.square(ya) - (
                np.square(dc) - np.square(da))
    f2 = 2 * x * (xb - xc) + np.square(xc) - np.square(xb) + 2 * y * (yb - yc) + np.square(yc) - np.square(yb) - (
                np.square(dc) - np.square(db))
    result = sympy.solve([f1, f2], [x, y])
    locx, locy = result[x], result[y]
    return [locx, locy]


# 解算得到定位节点坐标
[locx, locy] = triposition(cx[0], cy[0], da, cx[1], cy[1], db, cx[2], cy[2], dc)
print([locx, locy])
plt.show()
dot3 = plot(locx, locy, 'r*')

# 显示脚注
x = [[locx, cx[0]], [locx, cx[1]], [locx, cx[2]]]
y = [[locy, cy[0]], [locy, cy[1]], [locy, cy[2]]]
for i in range(len(x)):
    plt.plot(x[i], y[i], linestyle='--', color='g')
plt.title('三边测量法的定位', fontproperties=zhfont1)
plt.legend(['参考节点', '盲节点', '定位节点'], loc='lower right', prop=zhfont1)
plt.show()
derror = math.sqrt(np.square(locx - mtx) + np.square(locy - mty))
print(derror)
