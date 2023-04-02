# -*- coding: utf-8 -*-
import requests
import re
import parsel
import pdfkit  # 结合安装软件，下载地址 https://wkhtmltopdf.org/downloads.html
import imgkit  # 结合安装软件，下载地址 https://wkhtmltopdf.org/downloads.html
# from working.IP_Headers_Proxies import headers
import img2pdf



html_str = \
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    {article}
    </body>
    </html>
    """


def new_name(name):
    name = re.sub('[\/:*?"<>|]', '-', name)
    return name


# 将wkhtmltopdf.exe程序绝对路径传入config对象
path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)


def url_to_pdf(url, to_file):
    """ 将网页url生成pdf文件 """
    # 生成pdf文件，to_file为文件路径
    pdfkit.from_url(url, to_file, configuration=config)


def html_to_pdf(html, to_file):
    """ 将html文件生成pdf文件 """
    pdfkit.from_file(html, to_file, configuration=config)


def str_to_pdf(string, to_file):
    """ 将字符串生成pdf文件 """
    pdfkit.from_string(string, to_file, configuration=config)


# 将wkhtmltoimage.exe程序绝对路径传入config对象
path_wkhtmltoimage = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe'
conf = imgkit.config(wkhtmltoimage=path_wkhtmltoimage)


def url_to_img(url, to_file):
    """ 将网页url生成图片文件 """
    # 生成pdf文件，to_file为文件路径
    imgkit.from_url(url, to_file, config=conf)


def html_to_img(html, to_file):
    """ 将html文件生成图片文件 """
    imgkit.from_file(html, to_file, config=conf)


def str_to_img(string, to_file):
    """ 将字符串生成图片文件 """
    imgkit.from_string(string, to_file, config=conf)


def main():
    url_to_pdf(r'https://blog.csdn.net/weixin_45682261/article/details/125117124', 'out_0.pdf')
    url_to_pdf(r'https://zhuanlan.zhihu.com/p/69869004', 'out_1.pdf')
    # html_to_pdf('sample.html', 'out_2.pdf')
    str_to_pdf('This is test!', 'out_3.pdf')

    # 获取网页局部内容
    url = 'https://blog.csdn.net/weixin_45682261/article/details/125117124'
    response = requests.get(url, headers=headers)
    # print(response.text)
    selector = parsel.Selector(response.text)
    title = selector.css('#articleContentId::text').get()
    article = selector.css('#mainBox > main > div.blog-content-box > article').get()
    title = new_name(title) + '.pdf'
    article = html_str.format(article=article)
    # 方法一：
    str_to_pdf(article, title)
    # print(article)

    # 方法二：
    # html_path = title + '.html'
    # pdf_path = title + '.pdf'
    # with open(html_path, mode='w', encoding='utf-8') as f:
    #     f.write(article)
    # config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    # pdfkit.from_file(html_path, pdf_path, configuration=config)
    # print('Down')





if __name__ == '__main__':
    # main()

    url_to_pdf(r'https://mathsfans.github.io/Euclidea/v1/', 'Euclidea2.pdf')

    # html_to_img('大数据学习路线总结.html', '1.png')
    # str_to_img('大数据学习路线总结.html', '2.jpg')
    # url_to_img('https://zhuanlan.zhihu.com/p/69869004', '3.png')

    # file1 = r'1.png'
    # file2 = r'2.jpg'
    # file3 = r'3.png'
    # imglist = [file1, file2, file3]
    # # 多个图片合成一个pdf文件
    # with open(r'1.pdf', 'wb') as f:
    #     f.write(img2pdf.convert(imglist))
    pass
