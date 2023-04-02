# -*- coding: utf-8 -*-
"""
@Time    : 2023/1/6  006 下午 17:57
@Author  : Jan
@File    : url_to_doc.py
"""
import execjs
import pandas as pd


# # file = open('教师登录密码.csv', 'w', newline='', encoding='utf8')
# filename = r'C:\Y\Case\选餐系统设计\学生登录密码.csv'  # 文件路径
# people_num = sum(1 for lines in open(filename)) - 1
# # print('The total lines is ', teachers_num, type(teachers_num))
# # table = pd.read_csv(filename, dtype='str')
# # names = {table.iloc[i, 1] for i in range(0, teachers_num)}
# # print(names)
# name = '2'
# tabel = pd.read_csv(filename, dtype='str')
#
# names = {tabel.iloc[i, 1]: i for i in range(0, people_num)}
# tabel.loc[names[name], :] = [names[name], name, 'aaaaa']
# print(tabel)
# # file = open(filename, 'a', newline='', encoding='utf8')
# # Passwords = csv.writer(file)
# # Passwords.writerow(tabel)
#
# df = tabel.to_csv(filename, index=False)


def convertCurrency(a):
    index = open(r'C:\Y\Case\working\music\index.js', 'r', encoding='utf-8')
    js = execjs.compile(index.read())
    a = js.call('convertCurrency', a)
    return a
def fun(rmb):
    # rmb = input().split(".")
    rmb = rmb.split(".")
    n = rmb[0]
    m = rmb[1]

    x = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    y = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
    z = ["元", "拾", "佰", "仟", "万", "拾", "佰", "仟", "亿", "拾", "佰", "仟", "万亿", "拾", "佰", "仟"]
    t = ["角", "分"]

    result_b = ""
    for i in range(len(m)):
        if m[i] == "0":
            continue
        b = y[int(m[i])] + t[i]
        result_b += b

    result_a = "人民币"
    n = n[::-1]
    for i in range(len(n))[::-1]:
        if n[i] == "0":
            result_a += "零"
        else:
            a = y[int(n[i])] + z[i]
            result_a += a

    s = result_a
    s = s.replace("零零", "零")
    s = s.replace("人民币零", "人民币")
    s = s.replace("壹拾", "拾")
    if result_b:
        return s + result_b
    else:
        return s + "整"

if __name__ == '__main__':
    M = '1-4'  # 控制位数
    N = 2
    l = []
    r = []
    li = []
    dic = {}
    for i in range(2 ** int(M[-1])):
        l.append(bin(i).replace('0b', '').replace('1', '3'))
    for i in range(2 ** N):
        r.append(bin(i).replace('0b', '').replace('1', '3'))
    for i in l:
        for j in r:
            li.append(i + '.' + j)
    for i in li:
        result = fun(i)[3:]
        result2 = convertCurrency(i)
        if '整' in result:
            result = result[:-1]
        if '整' in result2:
            result2 = result2[:-1]
        # if result == result2:
        #     pass
        # else:
        print(result == result2, '人民币-' + result, i, result2)

