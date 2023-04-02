# -*- coding: utf-8 -*-
"""
@Time    : 2023/1/27  027 下午 14:56
@Author  : Jan
@File    : 矩阵螺旋线展开.py
"""

""" {} """


class MatrixTransform:
    def __call__(self, matrix, *args, **kwargs):
        print(self.clockwise(matrix))
        print(self.contrarotate(matrix))
        print(self.ltranspose(matrix))
        print(self.rtranspose(matrix))
        print(self.oglFlip(matrix))
        print(self.fliplr(matrix))

    # 顺时针旋转
    def clockwise(self, matrix):
        return [list(i)[::-1] for i in zip(*matrix)]

    # 逆时针旋转
    def contrarotate(self, matrix):
        return [list(i) for i in zip(*matrix)][::-1]

    # 左转置(对角线翻转)
    def ltranspose(self, matrix):
        return [list(i) for i in zip(*matrix)]

    # 右转置(对角线翻转)
    def rtranspose(self, matrix):
        return [list(i)[::-1] for i in zip(*matrix)][::-1]

    # 上下翻转
    def oglFlip(self, matrix):
        return matrix[::-1]

    # 左右翻转
    def fliplr(self, matrix):
        return [i[::-1] for i in matrix]

    # 二维转一维，顺时针螺旋展开
    @classmethod
    def spiralMatrix_1(self, matrix, k=0):
        options = {0: 0, 1: 1, 2: 2, 3: 3}
        if k not in options:
            res = """可选参数范围: 0 - 表从左上角开始
                1 - 表从右上角开始
                2 - 表从右下角开始
                3 - 表从左下角开始
            """
            return res
        res = []
        m = len(matrix)
        if m <= 0:
            return res
        n = len(matrix[0])
        x1, x2, y1, y2 = 0, n, 0, m
        while x1 < x2 and y1 < y2:
            for i in range(x1, x2):
                res.append(matrix[y1][i])
            y1 += 1
            for j in range(y1, y2 - 1):
                res.append(matrix[j][x2 - 1])
            x2 -= 1
            if y1 == y2:  # 针对单行情况，不左行
                break
            for i in range(x2, x1 - 1, -1):
                res.append(matrix[y2 - 1][i])
            y2 -= 1
            if x1 == x2:  # 针对单列情况，不上行
                break
            for j in range(y2 - 1, y1 - 1, -1):
                res.append(matrix[j][x1])
            x1 += 1
        return res[(n - 1) * options[k]:] + res[:(n - 1) * options[k]]

    # 二维转一维，逆时针螺旋展开
    @classmethod
    def spiralMatrix_2(self, matrix, k=0):
        options = {0: 0, 1: 1, 2: 2, 3: 3}
        if k not in options:
            res = """可选参数范围: 0 - 表从左上角开始
                1 - 表从左下角开始
                2 - 表从右下角开始
                3 - 表从右上角开始
            """
            return res
        res = []
        m = len(matrix)
        if m <= 0:
            return res
        n = len(matrix[0])
        x1, x2, y1, y2 = 0, n, 0, m
        while x1 < x2 and y1 < y2:
            for j in range(y1, y2):
                res.append(matrix[j][x1])
            x1 += 1
            for i in range(x1, x2 - 1):
                res.append(matrix[y2 - 1][i])
            y2 -= 1
            if x1 == x2:  # 针对单列情况，不上行
                break
            for j in range(y2, y1 - 1, -1):
                res.append(matrix[j][x2 - 1])
            x2 -= 1
            if y1 == y2:  # 针对单行情况，不左行
                break
            for i in range(x2 - 1, x1 - 1, -1):
                res.append(matrix[y1][i])
            y1 += 1
        return res[(n - 1) * options[k]:] + res[:(n - 1) * options[k]]


from 蛇形矩阵算法 import Clockwise as clockwise
from 蛇形矩阵算法 import Anticlockwise as anticlockwise

M = 4
N = 4
matrix1 = clockwise.clockwise_1(M, N, 11)
res = MatrixTransform.spiralMatrix_1(matrix1, 0)
print(res)

matrix2 = anticlockwise.anticlockwise_1(M, N, 11)
res = MatrixTransform.spiralMatrix_2(matrix2, 0)
print(res)
