# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/4  004 下午 22:17
@Author  : Jan
@File    : DOC88.COM_v3.py
"""
import os
import time
import img2pdf
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from lxml import etree

""" {} """

chromeOptions = webdriver.ChromeOptions()
dir_path = os.getcwd() + '\道客巴巴文档'
path = dir_path + '\data'
options = Options()
# 判断文件夹是否存在，不存在创建文件夹
is_exists = os.path.exists(path)
if not is_exists:
    os.mkdir(path)

# 指定浏览器下载文件夹
prefs = {
    "profile.default_content_settings.popups": 0,
    "download.default_directory": path,
    "profile.default_content_setting_values.automatic_downloads": 1,  # 取消下载多个文件的弹窗，直接自动下载多个文件
}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])  # 消除警告提示"Chrome 正在受自动化测试软件控制的控制。"
options.add_argument('--start-maximized')  # 界面窗口最大化
options.add_argument('--headless')  # 设置chrome浏览器无界面模式(设置无头浏览器)
browser = webdriver.Chrome(options=options)


def main(url):
    # 指定网页链接
    # url = 'https://m.doc88.com/p-05429759423388.html'
    # browser.get('https://www.doc88.com/p-5969904068700.html')  #论文
    browser.get(url)
    # 网页源代码

    text = browser.page_source
    html = etree.HTML(text)
    page_num = html.xpath("//li[@class='text']/text()")[0]
    name = html.xpath("//div[@class='doctopic']/h1/@title")[0]
    # 获取总页码数
    page_num = int(page_num.replace('/ ', ''))
    print(f'共{page_num}页')

    # 等待网页加载
    time.sleep(3)
    # 等待按钮
    # print(EC.visibility_of_element_located((By.XPATH, "//div[@id='continueButton']")))
    element = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='continueButton']")))
    element.click()

    # browser.find_element_by_xpath("//div[@id='continueButton']").click()

    js = "return action=document.body.scrollHeight"
    # 初始化现在滚动条所在高度为0
    height = 0
    # 当前窗口总高度
    new_height = browser.execute_script(js)
    k = 0

    while k <= page_num:
        for i in range(height, new_height, 3000):
            k += 1
            browser.execute_script(f'window.scrollTo(0, {i})')
            time.sleep(1)
            a = f"downloadPages({k}, {k})"
            # 中间需要手动点一下运行下载多个文件，已解决
            js_fn = \
                """
                function downloadPages(from, to) {
                    for (i = from; i <= to; i++) {
                        const pageCanvas = document.getElementById('page_' + i);
                        if (pageCanvas === null) break;
                        pageNo_ = i >= 10 ? '' + i : '0' + i;
                        const pageNo = pageNo_;
                        pageCanvas.toBlob(
                            blob => {
                                const anchor = document.createElement('a');
                                anchor.download = 'page_' + pageNo + '.png';
                                anchor.href = URL.createObjectURL(blob);
                                anchor.click();
                                URL.revokeObjectURL(anchor.href);
                            }
                            //, 'image/jpeg' // (*)
                            //, 0.9          // (*)
                        );
                    }
                };
                """
            browser.execute_script(js_fn + a)
    return name


if __name__ == '__main__':
    url = 'https://m.doc88.com/p-05429759423388.html'
    name = main(url)

    # 方法一：
    from os import walk

    names = next(walk(path), (None, None, []))[2]

    # # 方法二：
    # from os import listdir
    # from os.path import isfile, join
    # names = [f for f in listdir(path) if isfile(join(path, f))]
    # print(names)

    # li = []
    # # 定义pdf的格式：是以A4纸格式定义的
    # a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
    # # 应用
    # layout_fun = img2pdf.get_layout_fun(a4inpt)
    # for i in names:
    #     with open(path + '\\' + i, mode='rb') as f:
    #         data = f.read()
    #         li.append(data)
    # with open(dir_path + '\\' + 'name' + '.pdf', 'wb') as f:
    #     f.write(img2pdf.convert(li, layout_fun=layout_fun))

    # 删除文件夹
    import shutil

    shutil.rmtree(path)
