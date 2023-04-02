# -*- coding: utf-8 -*-
import math
import sys


# a = int(sys.argv[1])
# b = int(sys.argv[2])

def dec(function):
    return function()


# 斜上顺序排列
@dec
class Down_up:
    def __call__(self, N):
        print("---" * 30, "斜上顺序排列")
        self.down_up_1(N)  # 方法一
        self.down_up_2(N)  # 方法二
        self.down_up_3(N)  # 方法三
        self.down_up_4(N)  # 方法四

    @classmethod
    def down_up_1(cls, N):
        return cls._down_up_1(N)

    @classmethod
    def down_up_2(cls, N):
        return cls._down_up_2(N)

    @classmethod
    def down_up_3(cls, N):
        return cls._down_up_3(N)

    @classmethod
    def down_up_4(cls, N):
        return cls._down_up_4(N)

    @staticmethod
    def _down_up_1(N):  # 方法一
        print("---" * 10, "斜上顺序排列-1")
        li = []
        ll = []
        for i in range(N):
            if i == 0:
                for j in range(N):
                    li.append((j + 1) * (j + 2) // 2)  # 第一行，
            else:
                li = [j - 1 for j in li[1:]]  # 后面几行，是前一行去掉第一个元素后，前一行元素减一
            print(li)
            ll += [li]
        return ll

    @staticmethod
    def _down_up_2(N):  # 方法二
        print("---" * 10, "斜上顺序排列-2")
        li = []
        for i in range(N):
            li.append([(i + 1) * (i + 2) // 2 - i])
            if i == 0:
                for j in range(N - i - 1):
                    li[i].append((j + 2) * (j + 3) // 2)
            else:
                [li[i].append(j - 1) for j in li[i - 1][2:]]
        for i in li:
            print(i)
        return li

    @staticmethod
    def _down_up_3(N):  # 方法三
        print("---" * 10, "斜上顺序排列-3")
        li = [[] for _ in range(N)]
        x = 1
        for r in range(N):
            for i in range(r, -1, -1):
                li[i].append(x)
                x += 1
        for i in li:
            print(i)
        return li

    @staticmethod
    def _down_up_4(N):  # 方法四
        print("---" * 10, "斜上顺序排列-4")
        m = 1
        ll = []
        for i in range(N):
            m += i
            k = m
            li = []
            for j in range(N - i):
                li.append(k)
                print(k, end=' ')
                k += i + 2 + j
            print()
            ll += [li]
        return ll


# 斜下顺序排列
# @dec  # 此处去掉装饰，下面改为 __new__ 方法也可，同上一个类效果一样，注意区别。貌似二者不可同时存在
class Up_down:
    def __new__(cls, N):
        print("---" * 30, "斜下顺序排列")
        cls.up_down_1(N)  # 方法一
        cls.up_down_2(N)  # 方法二
        cls.up_down_3(N)  # 方法三
        cls.up_down_4(N)  # 方法四

    @classmethod
    def up_down_1(cls, N):
        return cls._up_down_1(N)

    @classmethod
    def up_down_2(cls, N):
        return cls._up_down_2(N)

    @classmethod
    def up_down_3(cls, N):
        return cls._up_down_3(N)

    @classmethod
    def up_down_4(cls, N):
        return cls._up_down_4(N)

    @staticmethod
    def _up_down_1(N):  # 方法一
        print("---" * 10, "斜下顺序排列-1")
        li = []
        ll = []
        for i in range(N):
            if i == 0:
                for j in range(N):
                    li.append((j + 1) * (j + 2) // 2 - j)  # 第一行，
            else:
                li = [j + 1 for j in li[1:]]  # 后面几行，是前一行去掉第一个元素后，前一行元素减一
            print(li)
            ll += [li]
        return ll

    @staticmethod
    def _up_down_2(N):  # 方法二
        print("---" * 10, "斜下顺序排列-2")
        li = []
        for j in range(N):
            if j == 0:
                for e in range(N):
                    li.append([(e + 1) * (e + 2) // 2])
            else:
                if j - 1 == 0:
                    [li[j - 1].append(i) for i in [x[0] + 1 for x in li][:-j]]  # 第一列去掉最后一个 +1
                else:
                    [li[j - 1].append(i + 1) for i in li[j - 2][2:]]  # 上一行去掉第一个 +1
        for i in li:
            print(i)
        return li

    @staticmethod
    def _up_down_3(N):  # 方法三
        print("---" * 10, "斜下顺序排列-3")
        li = [[] for _ in range(N)]
        x = 1
        for r in range(N):
            for i in range(r + 1):
                li[i].append(x)
                x += 1
        for i in li:
            print(i)
        return li

    @staticmethod
    def _up_down_4(N):  # 方法四
        print("---" * 10, "斜下顺序排列-4")
        m = 0
        ll = []
        for i in range(N):
            m += i + 1
            k = m
            li = []
            for j in range(N - i):
                li.append(k)
                print(k, end=' ')
                k += i + j + 1
            print()
            ll += [li]
        return ll


# 竖螺旋顺序排序
def down_up_right_down(N):
    print("---" * 30, "竖螺旋顺序排序")
    a = [[] for _ in range(N)]
    x = 1
    for r in range(N):
        if r % 2 == 0:
            for i in range(r + 1):
                a[i].append(x)
                x += 1
        else:
            for i in range(r, -1, -1):
                a[i].append(x)
                x += 1
    for i in a:
        print(i)


# 横向螺旋顺序排序
def right_down_down_up(N):
    print("---" * 30, "横向螺旋顺序排序")
    li = [[] for _ in range(N)]
    x = 1
    for r in range(N):
        if r % 2 == 0:
            for i in range(r + 1):
                li[r - i].append(x)
                x += 1
        else:
            for i in range(r, -1, -1):
                li[r - i].append(x)
                x += 1
    for i in li:
        print(i)
    return li


# 横撇竖提螺旋
def first_to_end_1(N, x=111):
    print("---" * 30, "横撇竖提螺旋")
    a = [[] for _ in range(N)]
    for r in range(N):
        if r % 2 == 0:
            for i in range(r + 1):
                a[r - i].append(x)
                x += 1
        else:
            for i in range(r, -1, -1):
                a[r - i].append(x)
                x += 1
    for r in range(N - 1):
        if r % 2 ^ N % 2:
            for i in range(r + 1, N):
                a[i].append(x)
                x += 1
        else:
            for i in range(N - 1, r, -1):
                a[i].append(x)
                x += 1
    for i in a:
        print(i)


# 竖提横撇螺旋
def first_to_end_2(N, x=111):
    print("---" * 30, "竖提横撇螺旋")
    a = [[] for _ in range(N)]
    for r in range(N):
        if r % 2 == 0:
            for i in range(r, -1, -1):
                a[r - i].append(x)
                x += 1
        else:
            for i in range(r + 1):
                a[r - i].append(x)
                x += 1

    for r in range(N - 1):
        if N % 2 ^ r % 2:
            for i in range(N - 1, r, -1):
                a[i].append(x)
                x += 1
        else:
            for i in range(r + 1, N):
                a[i].append(x)
                x += 1
    for i in a:
        print(i)


# 蛇形下右上右
@dec
class Down_right_up_right:
    def __call__(self, a, b):
        print("---" * 30, "蛇形下右上右")
        self.down_right_up_right_1(a, b)
        self.down_right_up_right_2(a, b)

    @classmethod
    def down_right_up_right_1(cls, a, b):
        return cls._down_right_up_right_1(a, b)

    @classmethod
    def down_right_up_right_2(cls, a, b):
        return cls._down_right_up_right_2(a, b)

    @staticmethod
    def _down_right_up_right_1(a, b):  # 方法一
        print("---" * 10, "蛇形下右上右-1")
        li = []
        for i in range(1, a + 1):
            li.append([i])
            for j in range(2, b + 1):
                if j % 2 == 0:
                    li[i - 1].append(li[i - 1][j - 2] + 2 * a - 1 - (i - 1) * 2)
                else:
                    li[i - 1].append(li[i - 1][j - 2] + 1 + (i - 1) * 2)
            # break
        for i in li:
            print(i)
        return li

    @staticmethod
    def _down_right_up_right_2(a, b):  # 方法二
        print("---" * 10, "蛇形下右上右-2")
        li = [[[] for _ in range(b)] for _ in range(a)]
        x = 1
        for r in range(b):
            if r % 2 == 0:  # fill left
                for i in range(a):
                    li[i][r] = x
                    x = x + 1
            else:
                for i in range(a - 1, -1, -1):
                    li[i][r] = x
                    x = x + 1
        for i in li:
            print(i)
        return li


# 蛇形右下左下
@dec
class Right_down_left_down:
    def __call__(self, a, b):
        print("---" * 30, "蛇形右下左下")
        self.right_down_left_down_1(a, b)  # 方法一
        self.right_down_left_down_2(a, b)  # 方法二

    @classmethod
    def right_down_left_down_1(cls, a, b):
        return cls._right_down_left_down_1(a, b)

    @classmethod
    def right_down_left_down_2(cls, a, b):
        return cls._right_down_left_down_2(a, b)

    @staticmethod
    def _right_down_left_down_1(a, b):  # 方法一
        print("---" * 10, "蛇形右下左下-1")
        li = []
        for i in range(1, a + 1):
            if i % 2 == 0:
                li.append([i * b])
                for j in range(2, b + 1):
                    li[i - 1].append(li[i - 1][j - 2] - 1)
            else:
                li.append([(i - 1) * b + 1])
                for j in range(2, b + 1):
                    li[i - 1].append(li[i - 1][j - 2] + 1)
        for i in li:
            print(i)
        return li

    @staticmethod
    def _right_down_left_down_2(a, b):  # 方法二
        print("---" * 10, "蛇形右下左下-2")
        li = [[[] for _ in range(b)] for _ in range(a)]
        x = 1
        for r in range(a):
            if r % 2 == 0:
                for i in range(b):
                    li[r][i] = x
                    x = x + 1
            else:
                for i in range(b - 1, -1, -1):
                    li[r][i] = x
                    x = x + 1
        for i in li:
            print(i)
        return li


# 顺时针螺旋顺序排列，注意：当中心数唯一时会被替换两次（记得单独处理或规避）
@dec
class Clockwise:
    def __call__(self, a, b, x=111):
        print("---" * 30, "顺时针螺旋顺序排列")
        self.clockwise_1(a, b, x)  # 顺时针螺旋顺序排列-1-1-左上开始
        self.clockwise_2(a, b, x)  # 顺时针螺旋顺序排列-1-2-右上开始
        self.clockwise_3(a, b, x)  # 顺时针螺旋顺序排列-1-3-右下开始
        self.clockwise_4(a, b, x)  # 顺时针螺旋顺序排列-1-4-左下开始

    @classmethod
    def clockwise_1(cls, a, b, x=111):
        return cls._clockwise_1(a, b, x)

    @classmethod
    def clockwise_2(cls, a, b, x=111):
        return cls._clockwise_2(a, b, x)

    @classmethod
    def clockwise_3(cls, a, b, x=111):
        return cls._clockwise_3(a, b, x)

    @classmethod
    def clockwise_4(cls, a, b, x=111):
        return cls._clockwise_4(a, b, x)

    @staticmethod
    def _clockwise_1(a, b, x=111):
        print("---" * 30, "顺时针螺旋顺序排列-1-1-左上开始")
        p = [[[] for _ in range(b)] for _ in range(a)]  # 创建二维列表方式*4
        # p = [[0] * b for _ in range(a)]
        # p = [[0] * b] * a
        for r in range(2 * min(a, b) + 1):  # 最小循环次数
            if r % 4 == 0 and r < a * 2:  # fill up
                for i in range(r // 4, b - r // 4):
                    p[r // 4][i] = x
                    x = x + 1
            if r % 4 == 1 and r < b * 2:  # fill right
                for i in range(1 + r // 4, a - 1 - r // 4):
                    p[i][b - 1 - r // 4] = x
                    x = x + 1
            if r % 4 == 2 and r < a * 2:  # fill down
                for i in range(b - 2 - r // 4, r // 4 - 2, -1):
                    p[a - 1 - r // 4][i + 1] = x
                    x = x + 1
            if r % 4 == 3 and r < b * 2:  # fill left
                for i in range(a - r // 2, 1, -1):
                    p[i - 1 + r // 4][r // 4] = x
                    x = x + 1
        for i in p:
            print(i)
        return p

    @staticmethod
    def _clockwise_2(a, b, x=111):
        print("---" * 30, "顺时针螺旋顺序排列-1-2-右上开始")
        p = [[[] for _ in range(b)] for _ in range(a)]  # 创建二维列表方式*4
        # p = [[0] * b for _ in range(a)]
        # p = [[0] * b] * a
        for r in range(2 * min(a, b) + 1):  # 最小循环次数
            if r % 4 == 3 and r < a * 2:  # fill up
                for i in range(r // 4, b - 2 - r // 4):
                    p[r // 4][i + 1] = x
                    x = x + 1
            if r % 4 == 0 and r < b * 2:  # fill right
                for i in range(r // 4, a - r // 4):
                    p[i][b - 1 - r // 4] = x
                    x = x + 1
            if r % 4 == 1 and r < a * 2:  # fill down
                for i in range(b - 2 - r // 4, r // 4, -1):
                    p[a - 1 - r // 4][i] = x
                    x = x + 1
            if r % 4 == 2 and r < b * 2:  # fill left
                for i in range(a - r // 2, -1, -1):
                    p[i + r // 4][r // 4] = x
                    x = x + 1
        for i in p:
            print(i)
        return p

    @staticmethod
    def _clockwise_3(a, b, x=111):
        print("---" * 30, "顺时针螺旋顺序排列-1-3-右下开始")
        p = [[[] for _ in range(b)] for _ in range(a)]  # 创建二维列表方式*4
        # p = [[0] * b for _ in range(a)]
        # p = [[0] * b] * a
        for r in range(2 * min(a, b) + 1):  # 最小循环次数
            if r % 4 == 2 and r < a * 2:  # fill up
                for i in range(r // 4, b - r // 4):
                    p[r // 4][i] = x
                    x = x + 1
            if r % 4 == 3 and r < b * 2:  # fill right
                for i in range(1 + r // 4, a - 1 - r // 4):
                    p[i][b - 1 - r // 4] = x
                    x = x + 1
            if r % 4 == 0 and r < a * 2:  # fill down
                for i in range(b - 2 - r // 4, r // 4 - 2, -1):
                    p[a - 1 - r // 4][i + 1] = x
                    x = x + 1
            if r % 4 == 1 and r < b * 2:  # fill left
                for i in range(a - 1 - r // 2, 1, -1):
                    p[i - 1 + r // 4][r // 4] = x
                    x = x + 1
        for i in p:
            print(i)
        return p

    @staticmethod
    def _clockwise_4(a, b, x=111):
        print("---" * 30, "顺时针螺旋顺序排列-1-4-左下开始")
        p = [[[] for _ in range(b)] for _ in range(a)]  # 创建二维列表方式*4
        # p = [[0] * b for _ in range(a)]
        # p = [[0] * b] * a
        for r in range(2 * min(a, b) + 1):  # 最小循环次数
            if r % 4 == 1 and r < a * 2:  # fill up
                for i in range(r // 4, b - 2 - r // 4):
                    p[r // 4][i + 1] = x
                    x = x + 1
            if r % 4 == 2 and r < b * 2:  # fill right
                for i in range(r // 4, a - r // 4):
                    p[i][b - 1 - r // 4] = x
                    x = x + 1
            if r % 4 == 3 and r < a * 2:  # fill down
                for i in range(b - 2 - r // 4, r // 4, -1):
                    p[a - 1 - r // 4][i] = x
                    x = x + 1
            if r % 4 == 0 and r < b * 2:  # fill left
                for i in range(a - 1 - r // 2, -1, -1):
                    p[i + r // 4][r // 4] = x
                    x = x + 1
        for i in p:
            print(i)
        return p


# 逆时针螺旋顺序排列，注意：当中心数唯一时会被替换两次（记得单独处理或规避）
@dec
class Anticlockwise:
    def __call__(self, a, b, x=111):
        print("---" * 30, "逆时针螺旋顺序排列")
        self.anticlockwise_1(a, b, x)  # 逆时针螺旋顺序排列-2-1-左上开始
        self.anticlockwise_2(a, b, x)  # 逆时针螺旋顺序排列-2-2-右上开始
        self.anticlockwise_3(a, b, x)  # 逆时针螺旋顺序排列-2-3-右下开始
        self.anticlockwise_4(a, b, x)  # 逆时针螺旋顺序排列-2-4-左下开始

    @classmethod
    def anticlockwise_1(cls, a, b, x=111):
        return cls._anticlockwise_1(a, b, x)

    @classmethod
    def anticlockwise_2(cls, a, b, x=111):
        return cls._anticlockwise_2(a, b, x)

    @classmethod
    def anticlockwise_3(cls, a, b, x=111):
        return cls._anticlockwise_3(a, b, x)

    @classmethod
    def anticlockwise_4(cls, a, b, x=111):
        return cls._anticlockwise_4(a, b, x)

    @staticmethod
    def _anticlockwise_1(a, b, x=111):
        print("---" * 30, "逆时针螺旋顺序排列-2-1-左上开始")
        p = [[[] for _ in range(b)] for _ in range(a)]  # 创建二维列表方式*4
        # p = [[0] * b for _ in range(a)]
        # p = [[0] * b] * a
        for r in range(2 * min(a, b) + 1):  # 最小循环次数
            if r % 4 == 3 and r < a * 2:  # fill up
                for i in range(b - 2 - r // 4, r // 4, -1):
                    p[r // 4][i] = x
                    x = x + 1
            if r % 4 == 2 and r < b * 2:  # fill right
                for i in range(a - r // 4, r // 4, -1):
                    p[i - 1][b - 1 - r // 4] = x
                    x = x + 1
            if r % 4 == 1 and r < a * 2:  # fill down
                for i in range(r // 4, b - 2 - r // 4):
                    p[a - 1 - r // 4][i + 1] = x
                    x = x + 1
            if r % 4 == 0 and r < b * 2:  # fill left
                for i in range(a - r // 2):
                    p[i + r // 4][r // 4] = x
                    x = x + 1
        for i in p:
            print(i)
        return p

    @staticmethod
    def _anticlockwise_2(a, b, x=111):
        print("---" * 30, "逆时针螺旋顺序排列-2-2-右上开始")
        p = [[[] for _ in range(b)] for _ in range(a)]  # 创建二维列表方式*4
        # p = [[0] * b for _ in range(a)]
        # p = [[0] * b] * a
        for r in range(2 * min(a, b) + 1):  # 最小循环次数
            if r % 4 == 0 and r < a * 2:  # fill up
                for i in range(b - r // 4, r // 4, -1):
                    p[r // 4][i - 1] = x
                    x = x + 1
            if r % 4 == 3 and r < b * 2:  # fill right
                for i in range(a - 2 - r // 4, r // 4, -1):
                    p[i][b - 1 - r // 4] = x
                    x = x + 1
            if r % 4 == 2 and r < a * 2:  # fill down
                for i in range(r // 4, b - r // 4):
                    p[a - 1 - r // 4][i] = x
                    x = x + 1
            if r % 4 == 1 and r < b * 2:  # fill left
                for i in range(1, a - 1 - r // 2):
                    p[i + r // 4][r // 4] = x
                    x = x + 1
        for i in p:
            print(i)
        return p

    @staticmethod
    def _anticlockwise_3(a, b, x=111):
        print("---" * 30, "逆时针螺旋顺序排列-2-3-右下开始")
        p = [[[] for _ in range(b)] for _ in range(a)]  # 创建二维列表方式*4
        # p = [[0] * b for _ in range(a)]
        # p = [[0] * b] * a
        for r in range(2 * min(a, b) + 1):  # 最小循环次数
            if r % 4 == 1 and r < a * 2:  # fill up
                for i in range(b - 2 - r // 4, r // 4, -1):
                    p[r // 4][i] = x
                    x = x + 1
            if r % 4 == 0 and r < b * 2:  # fill right
                for i in range(a - r // 4, r // 4, -1):
                    p[i - 1][b - 1 - r // 4] = x
                    x = x + 1
            if r % 4 == 3 and r < a * 2:  # fill down
                for i in range(r // 4, b - 2 - r // 4):
                    p[a - 1 - r // 4][i + 1] = x
                    x = x + 1
            if r % 4 == 2 and r < b * 2:  # fill left
                for i in range(a + 1 - r // 2):
                    p[i + r // 4][r // 4] = x
                    x = x + 1
        for i in p:
            print(i)
        return p

    @staticmethod
    def _anticlockwise_4(a, b, x=111):
        print("---" * 30, "逆时针螺旋顺序排列-2-4-左下开始")
        p = [[[] for _ in range(b)] for _ in range(a)]  # 创建二维列表方式*4
        # p = [[0] * b for _ in range(a)]
        # p = [[0] * b] * a
        for r in range(2 * min(a, b) + 1):  # 最小循环次数
            if r % 4 == 2 and r < a * 2:  # fill up
                for i in range(b - 2 - r // 4, r // 4 - 2, -1):
                    p[r // 4][i + 1] = x
                    x = x + 1
            if r % 4 == 1 and r < b * 2:  # fill right
                for i in range(a - 2 - r // 4, r // 4, -1):
                    p[i][b - 1 - r // 4] = x
                    x = x + 1
            if r % 4 == 0 and r < a * 2:  # fill down
                for i in range(r // 4, b - r // 4):
                    p[a - 1 - r // 4][i] = x
                    x = x + 1
            if r % 4 == 3 and r < b * 2:  # fill left
                for i in range(1, a - r // 2):
                    p[i + r // 4][r // 4] = x
                    x = x + 1
        for i in p:
            print(i)
        return p


# 顺时针旋转排列 --- 网友算法可参考
def network_clockwise(N, num=1):
    print("---" * 30, "顺时针旋转排列 --- 网友算法可参考")
    import numpy

    # N = int(input("请输入一个整数:"))
    # N = 10
    Arr = numpy.zeros((N, N), dtype=numpy.int16)  # 先打印出N*N的0矩阵
    i = 0  # 记录行
    j = 0  # 记录列
    k = num  # 控制起始值
    times = N  # 记录循环次数
    while num <= N * N + k - 1:
        for _ in range(times):  # 向右，列的变化,不断增加
            Arr[i][j] = num  # 改变数组对应位置的值
            num += 1
            j += 1
        times -= 1
        j -= 1  # 循环结束时，行列的值需要相应的改变
        i += 1
        for _ in range(times):  # 向下，行的变化，不断增加
            Arr[i][j] = num
            num += 1
            i += 1
        i -= 1
        j -= 1
        for _ in range(times):  # 向左，列的变化,不断减少
            Arr[i][j] = num
            num += 1
            j -= 1
        times -= 1
        j += 1
        i -= 1
        for _ in range(times):  # 向上，行的变化，不断减少
            Arr[i][j] = num
            num += 1
            i -= 1
        i += 1
        j += 1

    print(Arr)


pass


# 有 n 个空水瓶，每 m 个空水瓶换一瓶(可以借)，通过规律得知结果为向下取整 int(n / (m - 1)) 或者 math.floor(n / (m - 1)) 或者 n // (m - 1)
# @pysnooper.snoop()
def drinkbottle(n, m=3):  # 可自定义大于 2 个空水瓶对换
    global k
    li = []
    k += 1  # 统计递归调用次数
    if n < m - 1:
        li.append(0)
    if n == m - 1:  # 满足可以借的条件
        li.append(1)  # 能借就能多一瓶，不能借就不添加
        # print(f'--- {i} 满足借--- {i} 是 {m - 1} 的整数倍')
    if n >= m:
        new_n = n // m + n % m
        li.append(n // m)
        drinkbottle(new_n, m)
    return sum(li)


# 例子：
# for i in range(1, 101):
#     k = 0
#     m = 7
#     result = drinkbottle(i, m)
#     print(i, k, result, int(i / (m - 1)), math.floor(i / (m - 1)), i // (m - 1))

pass


# 辗转相除求最大公约数
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)  # 最大公约数（短除法左侧除数的乘积）可用自带 math.gcd(a, b)


# 例子：
# num1, num2 = 15, 25
# # 最小公倍数 = 乘积 / 最大公约数
# print(num1 * num2 // gcd(num1, num2))  # 最小公倍数（短除法除数和商的乘积）可用自带 math.lcm(a, b)

pass


# """ 二分查找法升级，对任意有序无序序列查位置索引 """
def binarySearch(a: [str, list], target: [int, str]) -> int:
    index = sorted(range(len(a)), key=lambda x: a[x], reverse=False)  # 记录原序列位置索引
    a = sorted(a)  # 对原序列升序排序
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        midValue = a[mid]
        if midValue < target:
            left = mid + 1
        elif midValue > target:
            right = mid - 1
        else:
            return index[mid]  # 返回 index 对应位置索引值，即为原序列位置索引
    return -1


# """ 二分查找法，对去重列表查指定数据位置索引 """ 缺点输入序列必须是升序排列
def search(nums: list[int], target: int):
    N = 0
    if len(nums) > 0:
        left = 0
        right = len(nums) - 1
        while left <= right:
            N += 1  # 统计查询次数
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return [target, mid, N]  # 若存在返回：查询值，查询值位置索引，二分查找次数  最大值为：int(1 + math.log2(len(li)))，最小值为：1
    return -1, N  # 若不存在返回：-1，二分查找次数  最大值为：int(math.log2(1 + len(li))


# 例子：
# li = [-1, 0, 3, 4, 6, 10, 13, 14]
# for j in li:
#     o = search(li, 14)
#     print(o, '存在---最大查询次数：', int(1 + math.log2(len(li))))  # 查询数在列表最右侧，查询次数最大
#
# for k in li:
#     o = search(li, -1)
#     print(o, '不存在---最大查询次数：', int(math.log2(len(li) + 1)))  # 查询数在列表不存在，查询次数次于查询数在列表最右侧

pass


# """ 查找列表内所有峰值 """
def findPeakElement(nums: list[int]):
    li = set()
    if max(nums) == min(nums):
        li.add(0)
    else:
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                li.add(i)
        if max(nums) == nums[-1]:
            li.add(len(nums) - 1)
        if max(nums) == nums[0]:
            li.add(0)
    return li


# """ 木桶效应，盛水最多的容器 """
def maxArea(height: list) -> int:
    left, right = 0, len(height) - 1
    if right < 1:  # 特殊情况 n < 2
        return 0
    res = 0  # 记录容器的最大量
    while left < right:
        # right - left 表示宽度，min(height[left], height[right]) 表示高度，木桶效应，以最低那个为准
        x = (right - left) * min(height[left], height[right])
        res = max(res, x)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return res


if __name__ == '__main__':
    a = 12  # 行数
    b = 15  # 列数
    N = 16  # 行列等值
    start_num = 111  # 起点值，只为对齐美观

    Down_up(N)  # 斜上顺序排列
    Up_down(N)  # 斜下顺序排列
    down_up_right_down(N)  # 竖螺旋顺序排序
    right_down_down_up(N)  # 横向螺旋顺序排序
    first_to_end_1(N, start_num)  # 横撇竖提螺旋
    first_to_end_1(N + 1, start_num)  # 横撇竖提螺旋
    first_to_end_2(N, start_num)  # 竖提横撇螺旋
    first_to_end_2(N + 1, start_num)  # 竖提横撇螺旋

    Down_right_up_right(a, b)  # 蛇形下右上右
    Right_down_left_down(a, b)  # 蛇形右下左下
    Clockwise(a, b, start_num)  # 顺时针螺旋顺序排列，注意：当中心数唯一时会被替换两次（记得单独处理或规避）ok
    Anticlockwise(a, b, start_num)  # 逆时针螺旋顺序排列，注意：当中心数唯一时会被替换两次（记得单独处理或规避）ok
    network_clockwise(N, start_num)  # 网友算法可参考
