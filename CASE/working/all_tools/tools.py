# -*- coding: utf-8 -*-
"""
@Time    : 2022/6/30  030 下午 16:47
@Author  : Jan
@File    : tools.py
"""
import base64
import glob
import random
import pprint
import os
import shutil
import threading
import requests
import pandas as pd
import xlrd
import xlwt
from xlutils.copy import copy
from fontTools.ttLib import TTFont
from PIL import ImageFont, Image, ImageDraw
from io import BytesIO
import ddddocr
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from subcase.tkinter.tool import get_ips

""" {} """


# UserAgent在线生成工具 https://gongjux.com/userAgentGenerator/
def get_ua():
    os_type = ["windows"]
    os_version = lambda: random.choice(['10.0; Win64; x64', '10.0', '6.3; Win64; x64', '6.3', '6.2; Win64; x64', '6.2', '6.1; Win64; x64', '6.1'])
    browser_type = lambda: random.choice(['Safari', 'Edg'])
    browser_version = lambda: random.choice(
        ['87.0.4280.63', '87.0.4280.60', '87.0.4280.47', '86.0.4240.198', '86.0.4240.193', '86.0.4240.183', '86.0.4240.111', '86.0.4240.75', '85.0.4183.121',
         '85.0.4183.83', '84.0.4147.135', '84.0.4147.125', '84.0.4147.105', '84.0.4147.89', '83.0.4103.116', '83.0.4103.106', '83.0.4103.97', '83.0.4103.61',
         '81.0.4044.138', '81.0.4044.129', '81.0.4044.122', '81.0.4044.113', '81.0.4044.92', '80.0.3987.163', '80.0.3987.162', '80.0.3987.149', '80.0.3987.132',
         '80.0.3987.122', '80.0.3987.116', '80.0.3987.106', '80.0.3987.100', '80.0.3987.87', '79.0.3945.130', '79.0.3945.117', '79.0.3945.88', '79.0.3945.79',
         '78.0.3904.108', '78.0.3904.97', '78.0.3904.87', '78.0.3904.70', '77.0.3865.120', '77.0.3865.90', '77.0.3865.75', '76.0.3809.132', '76.0.3809.100',
         '76.0.3809.87', '75.0.3770.142', '75.0.3770.100', '75.0.3770.90', '75.0.3770.80', '74.0.3729.169', '74.0.3729.157', '74.0.3729.131', '74.0.3729.108',
         '73.0.3683.103', '73.0.3683.86', '73.0.3683.75', '72.0.3626.121', '72.0.3626.119', '72.0.3626.109', '72.0.3626.96', '72.0.3626.81', '71.0.3578.98',
         '71.0.3578.80', '70.0.3538.110', '70.0.3538.102', '70.0.3538.77', '70.0.3538.67', '69.0.3497.100', '69.0.3497.81', '68.0.3440.106', '68.0.3440.84',
         '68.0.3440.75', '67.0.3396.99', '67.0.3396.87', '67.0.3396.79', '67.0.3396.62', '66.0.3359.181', '66.0.3359.170', '66.0.3359.139', '66.0.3359.117',
         '65.0.3325.181', '65.0.3325.162', '65.0.3325.146', '64.0.3282.186', '64.0.3282.140', '64.0.3282.119', '63.0.3239.132', '63.0.3239.108', '63.0.3239.84',
         '62.0.3202.94', '62.0.3202.89'])
    return f"Mozilla/5.0 ({os_type[0]} NT {os_version()}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser_version()} {browser_type()}/537.36"


# 获取随机ip代理
def get_ip():
    # with open(f'C:\Y\Case\subcase\疫情大数据\ip.txt', mode='r') as f:
    #     iplist = f.readlines()
    ips = get_ips().json()["data"]["proxy_list"][0].split(",")[0]
    # proxy = "18875066946:hioyv9yu@" + proxy     # 非必须
    return ips


# PIL 进行图片的读取、处理、保存
def read_filename(file_name):
    square = Image.open(file_name)  # 打开指定文件图片
    # square.show()  # 进行图片显示

    squarel = square.filter(ImageFilter.CONTOUR)  # 进行轮廓效果——素描处理
    # squarel.show()

    squarell = squarel.filter(ImageFilter.SMOOTH)  # 平滑处理
    # squarell.show()

    squarelll = squarell.filter(ImageFilter.EDGE_ENHANCE)  # 锐化处理
    # squarelll.show()

    enh_col = ImageEnhance.Color(squarelll)  # 进行对比度处理
    color = 1.5
    squarellll = enh_col.enhance(color)
    # squarellll.show()

    square_l = ImageEnhance.Brightness(squarellll)
    square_ll = square_l.enhance(0.8)  # 改变亮度
    square_ll.show()

    path = r"C:\Y\Case\验证码\图片\000.jpg"  # 保存路径

    # try:
    #     square_ll.save(path, quality=95)  # quality为图片质量，65为最低，95为最高
    #     print('图片保存成功，保存在' + path + "\n")
    # except:
    #     print('图片保存失败')


# 表格字母列号转数字，方法一
def convert_to_number(letter: str, columnA=1) -> int:  # ('A' -> 1)
    ab = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    w = 0
    for _ in letter.upper():
        w *= 26
        w += ab.find(_)
    return w - 1 + columnA


# 表格数字转字母列号，方法一
def convert_to_letter(number: int, columnA=1) -> str:  # 1 -> 'A'
    ab = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = number - columnA
    x = n % 26
    if n >= 26:
        n = int(n / 26)
        return convert_to_letter(n, 1) + ab[x + 1]
    else:
        return ab[x + 1]


# 表格字母列号转数字，方法二
def excel_col_to_num_version_original(col: str) -> int:  # ('A' -> 1)
    dict0 = {}
    for i in range(26):
        dict0[chr(ord('A') + i)] = i + 1
    num = 0
    for i in range(len(col)):
        num = num * 26 + dict0[col[i]]
    return num


# 表格数字转字母列号，方法二
def num_to_excel_col_version_original(num: int) -> str:  # 1 -> 'A'
    if not 1 <= num <= 18278:  # 官方给出的 excel 列最大到 "ZZZ"（18278）
        raise ValueError("Invalid column index {0}".format(num))
    excel_col_name = ""
    while num > 0:
        num, remainder = divmod(num, 26)
        if remainder == 0:
            remainder = 26
            num -= 1
        excel_col_name = chr(remainder + 64) + excel_col_name
    return excel_col_name


# 查找质数因子，最优方案
def FindPrimeNumber(num):
    li = []
    i = 2  # 从 2 开始除 num
    while num != 1:  # 商不等 1 时
        if num % i == 0:
            li.append(i)  # 如果能整除,记录下这个除数 i
            num //= i  # 更新 num,num = 商
        else:  # 如果 num 除以 i 除不尽
            if i > int(num ** 0.5):  # 当 i 大于根号 num 时，说明 num 的质因子只有它本身,此时结束循环
                li.append(num)
                break
            else:
                i += 1  # 除数 i+1
    print(*li)


# 指定位数分隔字符串，可选正向或反向
def parse_int(num, flag: int = 3, direction: int = 1) -> str:  # """ print(format(num, ',')) """  # 纯数字转金额表示
    # 方法一：
    # def run(s):
    #     if len(s) > flag:
    #         tmp.append(s[0 - flag:][::direction])
    #         return run(s[:0 - flag])
    #     else:
    #         tmp.append(s[::direction])
    tmp = []
    # 方法二：
    run = lambda s: tmp.append(s[::direction]) if len(s) <= flag else [tmp.append(s[0 - flag:][::direction]), run(s[:0 - flag])]
    # run = lambda s: [tmp.append(s[0 - flag:][::direction]), run(s[:0 - flag])] if len(s) > flag else tmp.append(s[::direction])
    direction = 1 if direction >= 0 else -1
    run(str(num)[::direction])
    return ','.join(tmp[::-1][::direction])


# 字符串转字典
def str_to_dic(s: str = '', flags: [bool, int] = 0) -> dict:
    import re
    # pattern = '^(.*?):\s{0,}(.*)$'    # 上下等价
    pattern = '^(.*?):\s*(.*)$'
    h = {}
    s = s.replace(': \n', ': ').replace(':\n', ': ')
    for line in s.splitlines():
        if line == '' or line.startswith('#'):
            continue
        s = re.sub(pattern, '{\'\\1\': \'\\2\'}', line)
        h.update(eval(s))
        if flags:
            print(re.sub(pattern, "\'\\1\': \'\\2\',", line))
    return h


# 对文件内容按行去重
def get_single(file_name):
    list01 = []
    for i in open(file_name):
        if i in list01:
            continue
        list01.append(i)
    with open('tmp.txt', 'w') as handle:
        handle.writelines(list01)
    os.remove(file_name)
    os.rename('tmp.txt', file_name)


# def save_to_xls(filename: [int, str], values: list = None, sheet="Sheet1"):
def save_to_xls(filename: any, values: list = None, sheet="Sheet1"):
    current_path = os.getcwd()
    file_path = current_path + f"/{filename}.xls"
    if not os.path.exists(file_path):
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个worksheet
        workbook.add_sheet(sheet)
        workbook.save(file_path)

    workbook = xlrd.open_workbook(file_path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格

    if sheet not in sheets:
        new_workbook = copy(workbook)
        new_worksheet = new_workbook.add_sheet(sheet)
        rows_old = 0
    else:
        index = sheets.index(sheet)  # 获取sheet索引
        # index = [x for x, y in enumerate(sheets) if y == sheet][0]  # 获取sheet索引
        worksheet = workbook.sheet_by_name(sheet)  # 获取工作簿中所有表格中的的第一个表格
        rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
        new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
        new_worksheet = new_workbook.get_sheet(index)  # 指定写入子sheet

    for i in range(0, len(values)):
        if isinstance(values[0], dict):
            for j, k in zip(range(0, len(values[i])), values[i].keys()):
                new_worksheet.write(i + rows_old, j, values[i][k])  # 追加写入数据，注意是从i+rows_old行开始写入
        else:
            for j in range(0, len(values[i])):
                new_worksheet.write(i + rows_old, j, values[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(file_path)  # 保存工作簿
    pass


# 二进制字体文件转字典
def identify_word(data: [bytes, any]) -> dict:
    """识别ttf字体结果"""
    # 由于TTFont接收一个文件类型
    # BytesIO(bin_data) 把二进制数据当作文件来操作
    if isinstance(data, bytes):
        woff_file = BytesIO(data)
    else:
        woff_file = data

    def font_to_img(_code, filename):
        """将字体画成图片"""
        img_size = 1024
        img = Image.new('1', (img_size, img_size), 255)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(filename, int(img_size * 0.7))
        txt = chr(_code)
        x, y = draw.textsize(txt, font=font)
        draw.text(((img_size - x) // 2, (img_size - y) // 2), txt, font=font, fill=0)
        return img

    dic = {}
    font = TTFont(woff_file)
    ocr = ddddocr.DdddOcr()
    for cmap_code, glyph_name in font.getBestCmap().items():
        bytes_io = BytesIO()
        pil = font_to_img(cmap_code, woff_file)
        pil.save(bytes_io, format="PNG")
        word = ocr.classification(bytes_io.getvalue())  # 识别字体
        # print(cmap_code, glyph_name, word)
        dic[glyph_name] = word
    # print(dic)
    return dic


# 包含 \u 或 uni 开头的字体编码列表转明文
def font_encoding(li: list, dic: dict):
    s = str(li).replace("\\u", "uni")
    ll = []
    for i in eval(s):
        if "uni" in i:
            i = i.upper().replace("UNI", "uni")
            i = dic[i]
        ll.append(i)
    s = "".join(ll)
    return s


# 根据滑动距离生成滑动轨迹
def get_slide_track(distance: int) -> list:
    """
    :param distance: 需要滑动的距离
    :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
        x: 已滑动的横向距离
        y: 已滑动的纵向距离, 除起点外, 均为0
        t: 滑动过程消耗的时间, 单位: 毫秒
    """

    def __ease_out_expo(sep):
        return 1 if sep == 1 else 1 - pow(2, -10 * sep)

    if not isinstance(distance, int) or distance < 0:
        raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
    # 初始化轨迹列表
    slide_track = [
        [random.randint(-50, -10), random.randint(-50, -10), 0],
        [0, 0, 0],
    ]
    # 共记录count次滑块位置信息
    count = 30 + int(distance / 2)
    # 初始化滑动时间
    t = random.randint(50, 100)
    # 记录上一次滑动的距离
    _x = 0
    _y = 0
    for i in range(count):
        # 已滑动的横向距离
        x = round(__ease_out_expo(i / count) * distance)
        # 滑动过程消耗的时间
        t += random.randint(10, 20)
        if x == _x:
            continue
        slide_track.append([x, _y, t])
        _x = x
    slide_track.append(slide_track[-1])
    return slide_track


# 将一个excel文件中的多个sheet分离出来并且以csv格式保存
def excel2csv(excel_file):  # 若报错不支持降指定版本 python39 -m pip install xlrd==1.2.0
    """
    :param excel_file: r'C:\\Y\\Case\\123.xlsx'
    :return:
    """
    # 打开excel文件
    workbook = xlrd.open_workbook(excel_file)
    # 获取所有sheet名字
    sheet_names = workbook.sheet_names()
    for worksheet_name in sheet_names:
        # 遍历每个sheet并用Pandas读取
        data_xls = pd.read_excel(excel_file, worksheet_name, index_col=None)
        # 获取excel当前目录
        dir_path = os.path.abspath(os.path.dirname(excel_file))
        # 转换成csv并保存到excel所在目录下的csv文件夹中
        csv_path = dir_path + '\\csv\\'
        if not os.path.exists(csv_path):
            os.mkdir(csv_path)
        data_xls.to_csv(csv_path + worksheet_name + '.csv', index=False, encoding='utf-8')

    # 将分离出来csv格式的文件合并成一个表
    def hebin(dir_path):
        csv_list = glob.glob(dir_path + '*.csv')
        # print(u'共发现%s个CSV文件' % len(csv_list))
        # print(u'正在处理')
        for i in csv_list:  # 循环读取同文件夹下的csv文件
            data = open(i, 'rb').read()
            with open('all.csv', 'ab') as f:  # 将结果保存为all.csv
                f.write(data)
        # print(u'合并完毕！')

    # hebin(r'C:\\Y\\Case\\csv\\')
    # shutil.rmtree(r'C:\\Y\\Case\\csv\\')    # 递归删除文件夹，即：删除非空文件夹


# 可选重复或带参数，多线程并发
def start_thread(**kwargs):
    """
    start_thread(func=func, num=2)  # 重复执行func()用法
    start_thread(func=func, params=i)   # 传参执行func(i)用法
    :param kwargs:
    :return:
    """

    def run_func(*args):
        return kwargs['func'](args) if 'params' in kwargs else kwargs['func']()

    for i in range(kwargs['num'] if 'num' in kwargs else 1):
        thread_name = threading.Thread(target=run_func, args=(kwargs['params'],)) if 'params' in kwargs else threading.Thread(target=run_func)
        thread_name.start()


def base64_to_hex(payload_base64):
    bytes_out = base64.b64decode(payload_base64)
    str_out = bytes_out.hex()
    return str_out


def hex_to_base64(payload_hex2):
    bytes_out = bytes.fromhex(payload_hex2)
    str_out = base64.b64encode(bytes_out)
    print("hex_to_base64:", str_out)
    return str_out


def strToBase64(s):
    strEncode = base64.b64encode(s.encode('utf8'))
    return str(strEncode, encoding='utf8')


def base64ToStr(s):
    strDecode = base64.b64decode(bytes(s, encoding='gbk'))
    return str(strDecode, encoding='gbk')


# ASE-CBC加密
def AESEncrypt(text: str, key, iv):
    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    encrypt_text = aes.encrypt(pad(text.encode('utf-8'), AES.block_size, style='zero'))  # 自定义新增Padding58-59
    encrypt_text = str(base64.encodebytes(encrypt_text), encoding='utf-8').replace("\n", "")
    return encrypt_text


# ASE-CBC解密
def AESDecrypt(text, key, iv):  # base64 格式
    decode_encrypt_text = base64.b64decode(text)
    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    decrypt_text = aes.decrypt(decode_encrypt_text).decode('utf8')
    decrypt_text = decrypt_text.replace(b'\x00'.decode(), "")
    return decrypt_text


# 防伪查询
def cha12315(code):
    import ddddocr

    ocr = ddddocr.DdddOcr()
    session = requests.Session()
    url = 'http://www.cha12315.com/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    session.get(url, headers=headers)
    url = 'http://www.cha12315.com/api/checkcode.aspx'
    res = session.get(url).content
    res = ocr.classification(res)
    data = {
        "checkcode": res,
        # "code": "1106183443534989",   # 例子：防伪码
        "code": code,
        "info": "111.193.138.229",
        "area": "北京市",
        "address": ""
    }
    url = 'http://www.cha12315.com/api/localquery.ashx?action=query'

    resp = session.post(url, data=data)
    resp.encoding = resp.apparent_encoding
    print(resp.text)
    return resp.text


# 学历信息查询
def xueli_check(num):
    """ 例子：
    xueli_check("65500118133031258")
    xueli_check("141735201606000368")
    :param num: 学历证书编号
    :return:
    """
    url = "http://www.abcbh.cn/18.asp"
    data = {"num": num, }
    response = requests.post(url, data=data)
    response.encoding = response.apparent_encoding
    data = response.text.split('\n')[0]
    for i in data.split('<br>'):
        print(i)
    print()


# curl to python
def curl_to_python(curl: str, flag: [bool, int] = 0, run: [bool, int] = 1):
    headers = []
    params = []
    curl = curl.strip('\n')
    li = curl.split('\n')
    if "?" in li[0]:
        url, param = li[0][6:-3].split('?')
        for p in param.split('&'):
            key, value = p.strip('^').split('=')
            params.append(f'\n\t\'{key}\': \'{value}\',')
    else:
        url = li[0][6:-3]
    for line in li[1:]:
        if '-H ' in line:
            key, value = line[6:-3].split(': ')
            headers.append(f'\n\t\'{key}\': \'{value.replace("^", "")}\',')
        else:
            continue
    out_pub = f"""import requests
    import parsel
    url = '{url}'
    headers = {{{''.join(headers)}
    }}
    params = {{{''.join(params)}
    }}
"""
    out_byte = f"""
def func():
    {out_pub}
    resp = requests.get(url, headers=headers, params=params)
    print(resp.status_code)
    return resp.content  
"""
    out_txt = f"""
def func():
    {out_pub}
    resp = requests.get(url, headers=headers, params=params)
    print(resp.status_code)
    resp.encoding = resp.apparent_encoding
    eg = '''
    # sel = parsel.Selector(resp.text)
    # names = sel.xpath('//div[@id="s-top-left"]/a/text()').getall()
    # print(names)
    '''
    # print(resp.text)
    print(eg)
    return resp.text
    
    
"""
    if flag:
        func_str = out_byte
    else:
        func_str = out_txt
    if run:
        ret = func_str
    else:
        namespace = {}
        fun = compile(func_str, '<string>', 'exec')
        exec(fun, namespace)
        ret = namespace['func']()
    return ret


if __name__ == '__main__':
    value1 = [
        ["用户1", "影评1"],
        ["用户2", "影评2"],
        ["用户3", "影评3"]
    ]
    value2 = [
        {"用户1": 1, "影评1": 2},
        {"用户1": 2, "影评1": 4},
        {"用户1": 3, "影评1": 6},
        {"用户1": 4, "影评1": 8},
    ]
    # save_to_xls(filename="test", values=value1, sheet="Sheet1")  # 列表嵌套列表形式
    # save_to_xls(filename="test", values=value2, sheet="Sheet1")  # 字典嵌套字典形式

    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36"}
    # url = 'http://api.shenlongip.com/ip?key=stsq8dal&pattern=txt&count=200&protocol=1'
    # response = requests.get(url, headers=headers, params={}, data={}, proxies={})
    # data = response.text
    # print(data)
    # print(response)
