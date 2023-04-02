# -*- coding: utf-8 -*-
import random

import execjs

index = open('index.js', 'r', encoding='utf-8')
js = execjs.compile(index.read())


def link_js_a(a):  # 生成指定a位数且指定字符集随机数
    a = js.call('a', a)
    # print(a)
    return a


def link_js_b():
    b = js.call('b')
    # print(b)
    return b


# for i in range(10):
#     print(link_js_b())
# print(len(link_js_b()))


################ 方法二
js_fn = \
    """
    function w(){
        return 6
    }
    function a(a, x, y) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
                e = Math.floor(e),
                c += b.charAt(e);
        return [c, x, y+w()] // 生成指定位数且指定字符集随机数
    }
    """
x = execjs.compile(js_fn)
z = x.call('a', 16, 1, 2)
print(z)  # execjs.compile用于执行更复杂的js代码

funcName = 'a(16, 1, 2)'
z2 = x.eval(funcName)
print(z2)

print(random.random())


