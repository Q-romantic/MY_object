# -*- coding: utf-8 -*-
"""
@Time    : 2023/1/18  018 下午 22:23
@Author  : Jan
@File    : 智力题.py
"""
import types

""" {经典智力题：N 人就餐分座位，每桌3人剩2人，每桌5人剩4人，每桌7人剩6人，每桌9人剩8人，每桌11人正好。} """
pass
"""
######################### 如下是基础模型
######################### 如下是基础模型
"""
pass
# 假设如下两行代表某个数 N 的除数和余数，求其 N 最小值，或者满足条件的递推公式
# 例如： 注意：统一按 a < c 从上往下排序，后面对这个顺序有点点小要求，没有对它做判断
a, b = [3, 1]  # 其余数可以是 1-2
c, d = [7, 6]  # 其余数可以是 1-6


# 1、常规思路，从可能的最小值挨个尝试，直到找到符合条件值，缺点：输出个数不可控
def general(a, b, c, d):
    for N in range(d, 300):
        if N % a == b:
            if N % c == d:
                print(N, end=',')


general(a, b, c, d)
print('----------1')


# 2、变通思路，将两个条件合并成一个条件，再用 1、常规办法
# @pysnooper.snoop()
def advanced(a, b, c, d, k=0):  # k 是自增变量(如下 m-n 的值)，可取值 0 - n ，直到满足条件
    # 原理是假设各自商为 m,n ,对各自乘以对方的除数，得到新除数为二者最小公倍数，故得知 acm+bc=cN,acn+ad=aN ,再带入其求差计算出 N 的通式
    x, y = divmod(a * c * k + b * c - a * d, c - a)
    if y == 0 and x > 0:
        return x
    else:
        return advanced(a, b, c, d, k + 1)


# 2.1、合并后再一般思路
aa, bb = a * c, advanced(a, b, c, d)
general(aa, bb, 1, 0)  # general(1, 0, aa, bb) 前后耗时好像没什么区别
print('----------2.1')

# 3、升级，优点：输出个数可控
N1 = advanced(a, b, c, d)
for i in range(20):
    N = a * c * i + N1
    print(N, end=',')
print('----------3')

# 3.1、合并后再升级思路
N1 = advanced(1, 0, aa, bb)  # 可能会导致递归深度受限，不推荐
for n in range(20):
    N = aa * n + N1
    print(N, end=',')
print('----------3.1')

"""
######################### 如下是扩展升级、优化、测试等
######################### 如下是扩展升级、优化、测试等
"""
pass
# 4.1、检测经典智力题：N 人就餐分座位，每桌3人剩2人，每桌5人剩4人，每桌7人剩6人，每桌9人剩8人，每桌11人正好。
# a0, b0 = [3, 2] # 因为下面有是 9 的倍数，已包含是 3 的倍数，故忽略
a, b = [5, 4]
c, d = [7, 6]
e, f = [9, 8]
g, h = [11, 0]
x, y = a * c, advanced(a, b, c, d)
x, y = e * x, advanced(e, f, x, y)
N1 = advanced(g, h, x, y)
for n in range(20):
    N = g * x * n + N1
    print(N, end=',')
print('----------4.1')

# 4.1.1 不推荐
# sys.setrecursionlimit(3000)  # 修改默认递归深度
# x, y = g * x, advanced(g, h, x, y)
# N1 = advanced(1, 0, x, y)  # 理论上没问题，但此方法不推荐 1、超默认递归深度，2、堆栈溢出
# for n in range(1):
#     N = 1 * x * n + N1
#     print(N, end=',')
print('----------4.1.1')


# 4.1.2 优化上述情况，使用 “尾递归 + 生成器” 彻底解决堆栈溢出
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


x, y = a * c, f_recursive_wapper2(advanced, a, b, c, d)  # 使用 “尾递归 + 生成器” 彻底解决堆栈溢出
x, y = e * x, f_recursive_wapper2(advanced, e, f, x, y)
x, y = g * x, f_recursive_wapper2(advanced, g, h, x, y)
N1 = f_recursive_wapper2(advanced, 1, 0, x, y)
for n in range(20):
    N = 1 * x * n + N1
    print(N, end=',')
print('----------4.1.2')

pass


# 4.2、首先系统有默认递归深度限制，可用下面方法修改。但又引发另一个问题 Process finished with exit code -1073741571 (0xC00000FD)
# 意思是堆栈溢出。递归限制仅指示递归调用的深度，但它不会改变堆栈大小。每次递归调用都会将帧添加到堆栈中，最终您将达到极限。
# 如果你真的想深入到递归，你必须用threading.stack_size()改变堆栈大小并创建一个新的线程。    # 还未测试
# 新方法：改递归为 while 循环
def perfect(a, b, c, d, k=-1):
    def advanced(a, b, c, d, k=0):  # k 是自增变量(如下 m-n 的值)，可取值 0 - n ，直到满足条件
        # 原理是假设各自商为 m,n ,对各自乘以对方的除数，得到新除数为二者最小公倍数，故得知 acm+bc=cN,acn+ad=aN ,再带入其求差计算出 N 的通式
        x, y = divmod(a * c * k + b * c - a * d, c - a)
        return x, y, a, b, c, d, k

    while True:
        x, y, a, b, c, d, k = advanced(a, b, c, d, k + 1)
        if y == 0 and x > 0:
            break
    return x


x, y = a * c, perfect(a, b, c, d)
x, y = e * x, perfect(e, f, x, y)
x, y = g * x, perfect(g, h, x, y)
N1 = perfect(1, 0, x, y)
for n in range(20):
    N = 1 * x * n + N1
    print(N, end=',')
print('----------4.2')

# 常规思路结题笨方法：直观理解
for N in range(11, 70000):
    if N % 3 == 2:
        if N % 5 == 4:
            if N % 7 == 6:
                if N % 9 == 8:
                    if N % 11 == 0:
                        print(N, end=',')
print('----------0')

# 合并后的常规解题方法，为了做对比，总结得出递推公式 N = 3465 * (n - 1) + 2519
for N in range(11, 70000):
    if N % 1 == 0:
        if N % 3465 == 2519:
            print(N, end=',')
print('----------0.1')
