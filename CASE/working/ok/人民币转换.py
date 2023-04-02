# -*- coding: utf-8 -*-
"""
@Time    : 2023/1/17  017 下午 16:00
@Author  : Jan
@File    : 人民币转换.py
"""
import re

import execjs

"""
{看了各位小伙伴，貌似或多或少有点问题，或者说仅限通过测试，没起到统用性，并且我觉得这不应该涉及用计算方式，所以整理了如下方法，
纯粹的字符列表的映射关系，排除掉一些特殊情况也许是为了可读性，在拼接的时候有反转情况。另外“壹拾”写成“拾”貌似有争议，
参考网页公开使用版本并没有去掉“壹”，还有就是小数点后有零的情况也是有争议（注释处已带标记？？？），也许是两种读法吧，也不纠结它了。
欢迎小伙伴们任意抽测，我测试过10位数以下都没问题，想来算法是ok的，所以可以是任意数值}
"""


class NumToRMB:
    def __init__(self, num):
        if "." in num:
            self.left, self.right = num.split(".")
        else:
            self.left, self.right = num, ""
        self.a, self.b = divmod(len(self.left), 4)
        self.x = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
        # self.x = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.p = ["仟", "佰", "拾", "元"]  # 公共部分
        self.y = ["垓", "京", "兆", "亿", "万", "元"]  # 整数进位部分  扩展时向此列表前添加即可  百度百科 “数字”
        # self.y = ['古戈尔普勒克斯', '古戈尔', '无觉', '无想', '无感', '无知', '无数', '无等', '无边', '大数', ' 无量', '不可思议', '那由他', '阿僧祗', '恒河沙', '极', '载', '正', '涧', '沟', '穰', '秭', '垓', '京', ' 兆', '亿', '万', '元']  # 整数进位部分  扩展时向此列表前添加即可
        self.z = ["角", "分", "厘", "毛"]  # 小数部分
        # self.z = ["角", '分', '厘', '毛', '糸', '忽', '微', '纤', '沙', '尘', '埃', '渺', '漠', '模糊', '逡巡', '须臾', '瞬息', '弹指', '刹那', '六德', '虚空', '清净', '阿赖耶', '阿摩罗', '涅槃寂静']  # 小数部分

    def get_li(self, left: str) -> list:
        li = []
        if left[: self.b] != "":
            li.append(left[: self.b])
        for i in range(self.a):
            s = left[self.b:][(i * 4): (i * 4) + 4]
            li.append(s)
        return li

    def numToRMB_1(self, num: str, p: list, y: str) -> str:
        tmp = []
        l = len(num)
        index = p[-l:]  # 只取后 l 位真实值需要用到的单位 p = ['仟', '佰', '拾', '元']
        y = "" if y == "元" else y
        for i, j in zip(num, index):
            if i == "0" or (i != "0" and j == "元"):  # 对应位置为 0 不写入单位，并且默认末尾为 “元” 时也不记录，方便后面组合时拼接进位单位
                tmp.append(self.x[int(i)])
            else:
                tmp.append(self.x[int(i)] + j)
        res = "".join(tmp)
        res = re.sub(r"0{2,}|零{2,}", self.x[0], res)  # 单个片段间有 相邻 2 个以上合并为 1 个
        if res[-1] == "0" or res[-1] == "零":
            res = re.sub(r"0$|零$", f"{y}零", res)  # 特殊情况 0万 0亿，此时读作 万0 亿0，所以要对其反向
            res = re.sub(r"0{2,}|零{2,}", self.x[0], res)  # 特殊情况 反向后可能也会出现有 相邻 2 个以上再次合并为 1 个
        else:
            res = res + y  # 拼接进位单位
        return res

    def resultLeft(self, left: str, p: list, y: list) -> str:
        l0 = []
        li = self.get_li(left)  # 对 left 分组，每后四位一组
        y = [y[-i] for i in range(len(li), 0, -1)]  # 调整 整数进位部分单位 y = ['垓', '京', '兆', '亿', '万', '元']
        for i, j in zip(li, y):
            res = self.numToRMB_1(i, p, j)  # 每组调用公共单位 p = ['仟', '佰', '拾', '元']
            l0.append(res)
        res = "".join(l0)
        res = re.sub(r"0{2,}|零{2,}", self.x[0], res)  # 有相邻 2 个以上合并为 1 个
        for i in range(len(y) - 2):
            # a, b = y[-3 - i], y[-2 - i]     # 倒着取便于递归替换，按先生成先替换，更合理
            a, b = y[0], y[i + 1]  # 顺着取替换，也合理
            res = re.sub(f"{a}" + r"(0|零){0,1}" + f"{b}", a, res)  # 特殊情况  兆亿 亿万 ... 兆0亿 亿0万 ... 组合，需要循环替换保留进位最高位
        res = re.sub(r"0$|零$", "", res) + "元"  # 特殊情况 0 结尾
        res = re.sub(r"^元$|^元$", "零元", res)  # 特殊情况 0元

        # res = re.sub(r"(1|壹)拾", f"拾", res)  # 特殊情况 只为过测试，貌似有争议 ？？？

        return res

    # right = ['1','01','11','001','011','101','111','0001','0011','0111','0101','0101','1111','1001', '1101', '1011','00000001']
    def numToRMB_2(self, num: str, li: list) -> str:
        tmp = []
        try:
            while num[-1] == "0":  # 1000 情况，末尾有至少一个 0
                num = num[:-1]
        except:
            pass
        for i, j in zip(num, li):
            if i == "0":  # 对应位置数值为 0 时不加单位
                j = ""
            tmp.append(self.x[int(i)] + j)
        res = "".join(tmp)
        res = re.sub(r"0{2,}|零{2,}", f"{self.x[0]}", res)  # 0001 情况，合并 0
        # res = re.sub(r'(0|零){2,}', f'{self.x[0]}', res)  # 上下两种写法

        # res = re.sub(r"^0|^零", "", res)  # 特殊情况 只为过测试，貌似有争议 ？？？

        return res

    def main(self):
        resultLeft = self.resultLeft(self.left, self.p, self.y)
        resultRight = self.numToRMB_2(self.right, self.z)
        if self.right == "" or int(self.right) == 0:
            return resultLeft  # + "整"
        elif int(self.left) == 0:  # 0.01 情况
            return resultRight
        return resultLeft + resultRight


def check(num):
    num = num.replace(",", "")  # 去掉不相关字符
    num = re.sub(r"^0+", "", num)
    num = re.sub(r"^\.", "0.", num)
    try:
        flage = re.match(r"^((\d{1,3}(,\d{3})*(.((\d{3},)*\d{1,3}))?)|(\d+(.\d+)?))$", num)
        if flage.group(0) == num:
            return num
    except:
        pass


def convertCurrency(a):
    index = open(r'C:\Y\Case\working\music\index.js', 'r', encoding='utf-8')
    js = execjs.compile(index.read())
    a = js.call('convertCurrency', a)
    return a


M = '5-6'  # 控制数字位数 1~n
N = 2
l = []
r = []
nums = []
dic = {}
for i in range(2 ** int(M.split('-')[0]), 2 ** int(M.split('-')[1])):  # 小数点左边位数
    l.append(bin(i).replace('0b', '').replace('1', '1'))
for i in range(2 ** N):  # 小数点右边位数
    r.append(bin(i).replace('0b', '').replace('1', '1'))
for i in l:
    for j in r:
        nums.append(i + '.' + j)

# nums = ['151121.15', '101010.00',  '0.85', '0.40', '0.01', '4.00', '0.00', '532.00', '6007.14', '10', '110.00', '101001111', '30105000.00', '000123,340.00']
for num in nums:
    # num = '123456.79'
    num = check(num)
    result = NumToRMB(num).main()
    # print("人民币" + result)

    # 如下是测试比较部分
    try:
        result2 = convertCurrency(num)  # 同 JS 代码运行结果比较时需要注释掉以上带？？？有争议部分和末尾填“整”
        if '整' in result2:
            result2 = result2[:-1]
    except:
        result2 = num
    if result == result2:
        print("True", result)
    else:
        print('-----' * 3, result, num, result2)
