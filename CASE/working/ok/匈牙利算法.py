# -*- coding: utf-8 -*-
"""
@Time    : 2023/1/20  020 下午 17:20
@Author  : Jan
@File    : 匈牙利算法.py
"""

""" {匈牙利算法，主要解决指派问题} """

import copy
import numpy as np
from scipy.optimize import linear_sum_assignment

"""
需要解决的问题：一份说明书需要翻译成 ABCD 四种语言，现有 甲乙丙丁 四人去做四种语言的翻译所需要的时间见下表，需要求得的是如何指派任务使完成翻译工作需要的工时最少。
"""


# 二维列表行列转置
def transpose(array):
    # arr = list(map(lambda x: list(x), zip(*array)))
    # arr = list(map(list, zip(*array)))
    # arr = [list(i) for i in zip(*array)]
    # 方法四
    arr = [[] for _ in range(len(array))]
    for i in array:
        for j in range(len(i)):
            arr[j].append(i[j])
    return arr


def juge(array, flag=True):  # 判断每行每列是否存在唯一圈 0 ，即每行每列只存在 'o'
    for i in array:
        if i.count('o') == 1:
            flag = True
        else:
            flag = False
            return flag
    for i in transpose(array):
        if i.count('o') == 1:
            flag = True
        else:
            flag = False
            return flag
    return flag


def replace_o_to_0(array):  # 将圈 0 位置 'o' 全部替换回 0
    for index, i in enumerate(array):
        for index_col, j in enumerate(i):
            if j == 'o':
                array[index][index_col] = 0
    return array


def only_o_to_1(array):  # 最后将圈 0 位置 'o' 全部替换成 1 ，其余替换成 0
    for index, i in enumerate(array):
        for index_col, j in enumerate(i):
            if j == 'o':
                array[index][index_col] = 1
            else:
                array[index][index_col] = 0
    return array


def run(array):
    for index_row, i in enumerate(array):
        mi = min(i)  # 每行中最小值
        for index_col, j in enumerate(i):
            array[index_row][index_col] -= mi  # 每行元素减去该行最小值
    for index_col, i in enumerate(transpose(array)):
        if 0 not in i:  # 不包含 0 的列
            mi = min(i)  # 每列中最小值
            for index_row, j in enumerate(i):
                array[index_row][index_col] -= mi  # 每列元素减去该行最小值
    while 1:
        if juge(array):
            break
        array = replace_o_to_0(array)
        for index_row, i in enumerate(array):
            try:
                index_col = i.index(0)
                array[index_row][index_col] = 'o'  # 找到每行第一个 0 标记为 'o'
                for index_r, j in enumerate(transpose(array)[index_col]):
                    if j == 0:
                        array[index_r][index_col] = '0'  # 再将标记为 'o' 行所在列其余值 0 划去，我标记为 '0'
            except:
                for index_col, ii in enumerate(i):  # 如上操作完后可能找不到值为 0 的情况
                    if '0' in i:
                        if ii == '0':
                            array[index_row][index_col] = 0
                            for index_ro, iii in enumerate(transpose(array)[index_col]):
                                if iii == 'o':
                                    array[index_ro][index_col] = 0
                                    for index_co, iiii in enumerate(array[index_ro]):
                                        array[index_ro][index_co] -= 1
                                array[index_ro][index_col] += 1
                        array[index_row][index_col] -= 1
            finally:
                pass
    return array


""" ############################################################################################# """


# 系数矩阵
# """第一步进行行变换和列变换"""
def preprocessing(C):
    # 行规约
    row_change = np.min(C, axis=1)
    row_change = row_change.reshape(row_change.shape[0], 1)
    C = C - row_change
    # 列规约
    column_change = np.min(C, axis=0)
    C = C - column_change
    return C


# """ 找到独立零元素 """
def find_independent_zeros(C):
    # 将系数矩阵中的0提取出来，若该位置为0，则标号1，否则为0
    zeroArray = np.zeros((C.shape[0], C.shape[1]))
    for i in range(C.shape[0]):
        num = 0
        for j in range(C.shape[1]):
            if C[i, j] == 0:
                num = 1
                zeroArray[i, j] = num
    # print('标记零元素的矩阵',zeroArray)
    M = []  # 已经找到了独立0元素的行
    for j in range(5):
        '找到最少0值所在的行'
        countZero = np.count_nonzero(zeroArray == 1, axis=1)  # 统计每一行的零元素的个数
        # 如果某一行已经确定了独立零元素，或者没有零元素，那么将计数列表提高一个极大数
        for i in range(len(countZero)):
            if countZero[i] == 0 or i in M:
                countZero[i] = 10000
        temp = np.argmin(countZero)  # 确定最少零元素个数的行索引
        M.append(temp)
        column = np.where(zeroArray[temp, :] == 1)[0]  # 一行中0元素的所有列索引

        # 这里将同一行多余的0，提前设置为-1
        p = 0
        for i in column:
            '第一个0不改变'
            if p == 0:
                p += 1
            else:
                zeroArray[temp, i] = -1

        # 这里将同一列多余0，设置为-1
        for k in range(C.shape[0]):
            if zeroArray[k, column[0]] == 1 and k not in M:
                zeroArray[k, column[0]] -= 2
        # print('确定某一行独立零元素后的矩阵',zeroArray)
    return zeroArray


# """ 划线操作 """
def draw_line(zeroArray, C):
    notZeroRow = []  # 没有独立零元素的行，并打✔
    for i in range(zeroArray.shape[0]):
        if 1 not in zeroArray[i, :]:
            notZeroRow.append(i)

    deletaZeroColumn = []  # 非独立零元素的列打✔
    for i in notZeroRow:
        for j in range(zeroArray.shape[0]):
            if zeroArray[i, j] == -1:
                deletaZeroColumn.append(j)

    # 在已经✔的列中，对独立零元素的行打✔
    for i in deletaZeroColumn:
        for j in range(zeroArray.shape[0]):
            if zeroArray[j, i] == 1:
                notZeroRow.append(j)

    # '划线操作'
    lineListRow = [i for i in range(zeroArray.shape[0]) if i not in notZeroRow]
    lineListColumn = deletaZeroColumn
    findMin = copy.deepcopy(C)
    # 将画线部分的值变为一个极大数
    for i in lineListRow:
        findMin[i, :] = 100000
    for i in lineListColumn:
        findMin[:, i] = 100000
    minIndex = np.where(findMin == np.min(findMin))
    for i in notZeroRow:
        C[i, :] -= findMin[minIndex[0][0], minIndex[1][0]]
    # 消除负数元素
    for i in notZeroRow:
        for j in range(C.shape[0]):
            if C[i, j] < 0:
                C[:, j] += findMin[minIndex[0][0], minIndex[1][0]]
                break
    return C


def main(array):
    C = np.array(array)
    # C = np.array([[4, 8, 7, 15, 12], [7, 9, 17, 14, 10], [6, 9, 12, 8, 7], [6, 7, 14, 6, 10], [6, 9, 12, 10, 6]])
    C_matrix = copy.deepcopy(C)
    '系数矩阵归一化处理'
    C_matrix = preprocessing(C_matrix)
    # 确定独立零元素和划线操作
    while True:
        zeroArray = find_independent_zeros(C_matrix)
        if np.count_nonzero(zeroArray == 1) == C.shape[0]:  # 当独立零元素的个数等于系数方阵时，找到最优解
            break
        C_matrix = draw_line(zeroArray, C_matrix)
    '结果输出'
    result = np.where(zeroArray == 1)
    out(array, result)
    return result


def out(array, result):
    arrayAddHeaders(array, result)
    C = np.array(array)
    cost = []
    for i in range(C.shape[0]):
        value = C[result[0][i], result[1][i]]
        cost.append(value)
        print('事件', chr(ord('@') + result[1][i] + 1), '分配给工人', str(result[0][i] + 1))
    print(f'最佳值为：{" + ".join(map(str, cost))} =', sum(cost))


def arrayAddHeaders(array, result):
    arr = [
        [f'人{_}' if i == 0 else ' ' for i in range(len(array[0]) + 1)] if _ != 0 else [chr(ord('@') + j) if j != 0 else " \\" for j in range(len(array[0]) + 1)]
        for _ in range(len(array) + 1)]
    for i in result[0]:
        j = result[1][i]
        arr[i + 1][j + 1] = str(array[i][j])
    for i in arr:
        print(i)
    return arr


""" ############################################################################################# """


def pair(events, tmp=[], total=[]):
    for i in events:
        tmp.append(i)
        b = copy.deepcopy(events)
        b.remove(i)
        if b == []:
            total.append(copy.deepcopy(tmp))
        pair(b, tmp=tmp, total=total)
        tmp.pop()
    return total


def master(workers, events, array):
    dic = {}
    for worker, i in zip(workers, range(len(array))):
        dic[worker] = {key: value for key, value in zip(events, array[i])}
    data = {}
    for i in pair(events, total=[]):  # 此处有个小陷阱，该函数单次运行 2 次以上会出现结果累加。 解决办法是指定 total=[]
        t = 0
        for index, j in zip(workers, i):
            t += dic[index][j]
        data[''.join(i)] = t
        # data[str(i)] = t
    data = sorted(data.items(), key=lambda x: x[1])
    return data


if __name__ == '__main__':
    array = [
        # ['A', 'B', 'C', 'D']
        [6, 7, 11, 2],  # 甲
        [4, 5, 9, 8],  # 已
        [3, 1, 10, 4],  # 丙
        [5, 9, 8, 2],  # 丁
    ]
    # 0、我的暴力破解，完美递归找所有情况，排序输出
    workers = ['甲', '乙', '丙', '丁']
    events = ['A', 'B', 'C', 'D']
    data = master(workers, events, array)
    for i in data:
        print(i)
    # 1、我的方法，此处有漏洞
    # a = run(array)
    # a = only_o_to_1(a)
    # for i in a:
    #     print(i)
    print('-----' * 8)
    pass
    """ ############################################################################################# """
    # 2、网友算法细分
    # array = transpose(array)    # 行列转置
    result = main(array)
    print(result)
    print('-----' * 8)
    pass
    """ ############################################################################################# """
    # 3、运用模块
    cost = np.array(array)
    result = linear_sum_assignment(cost)
    print(result)
    out(array, result)
    print('-----' * 8)
    # 3.1、此处是最大化指派问题，需要找出阵列最大值，再用这个数减去其它每个值后，再用标准形式指派求解，即：array = 11 - array
    array2 = [
        [5, 4, 0, 9],
        [7, 6, 2, 3],
        [8, 10, 1, 7],
        [6, 2, 3, 9],
    ]
    cost = np.array(array2)
    result = linear_sum_assignment(cost)
    print(result)
    out(array, result)
    print('-----' * 8)
