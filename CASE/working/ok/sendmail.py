# -*- coding: utf-8 -*-
"""
@Time    : 2023/1/3  003 下午 15:30
@Author  : Jan
@File    : sendmail.py
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

""" {批量发送邮件} """

class SendMail:
    def __init__(self):
        # 多附件邮件基本思路，首先用MIMEMultipart()来标识这个邮件由多个部分组成
        # 然后通过Header方法，定义邮件的发送人、接收人、邮件标题；MIMEtext构造邮件正文
        # 然后再用attach（）方法将各部分内容分别加入到MIMEMultipart容器内
        message = MIMEMultipart()
        self.message = message
        message['Subject'] = Header('带附件的邮件测试', 'utf-8')  # 邮件主题
        message['From'] = Header("python程序", 'utf-8')  # 发件人别名或描述信息
        # message['To'] = Header("徐健1<1139011728@qq.com>;徐健2<1044030729@qq.com>", 'utf-8')
        # message['Cc'] = Header("徐健2<1044030729@qq.com>", 'utf-8')
        message['To'] = Header('; '.join(receivers), 'utf-8')
        if cc:
            message['Cc'] = Header('; '.join(cc), 'utf-8')
        message.attach(MIMEText(body, 'plain', 'utf-8'))

    def load_attachment(self, att, filename):
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = f'attachment; filename={filename}'
        # att.add_header('content-disposition', 'attachment', filename=filename)
        self.message.attach(att)

    def classified(self, path):
        """
        Content-Disposition激活附件下载对话框。Content-Disposition有两种属性：inline 和 attachment
        inline:默认值，将文件内容直接显示在页面；
        attachment：弹出对话框，让用户下载
        filename：定义下载文件的文件名。
        """
        filename = path.split('/')[-1] if '/' in path else path.split('\\')[-1]
        key = filename.split('.')[-1]
        if key == 'txt':  # 通过MIMEText构造附件1文本
            att = MIMEText(open(path, 'rb').read(), 'base64', 'utf-8')  # r方式可能会表编码问题
            self.load_attachment(att, filename)
        elif key == ('png' or 'jpg' or 'jpeg'):  # 通过MIMEImage构造附件2图片
            att = MIMEImage(open(path, 'rb').read())
            self.load_attachment(att, filename)
        elif key == 'mp3':  # 通过MIMEAudio构造附件3。MEMEAudio需要定义音频类型
            att = MIMEAudio(open(path, 'rb').read(), 'audio')
            self.load_attachment(att, filename)
        else:  # 其他类型通过MIMEApplication构造附件4
            att = MIMEApplication(open(path, 'rb').read())
            self.load_attachment(att, filename)

    def send(self):
        for path in attachments:
            self.classified(path)
        # 链接SMTP服务器
        # [开通QQ邮箱SMTP服务，获取授权码]
        smtp = smtplib.SMTP()
        smtp.connect('smtp.qq.com')
        smtp.login(sender, password)
        all_receivers = receivers + cc if cc else receivers
        smtp.sendmail(sender, all_receivers, self.message.as_string())
        print("邮件发送成功！！！")
        smtp.quit()


if __name__ == '__main__':
    # 定义发送人、接收人、抄送人(密送)邮箱
    sender = '1139011728@qq.com'
    password = 'alojfoglmrdybabg'
    receivers = ['1139011728@qq.com', '1044030729@qq.com']
    # cc = ['1044030729@qq.com', '1044030729@qq.com']
    cc = []  # 无抄送选择

    # 需要发送的邮件内容
    body = '''尊敬的xx：
        您好！
    这是一封测试邮件！
    1、这是用Python编写的邮件发送程序……
    2、这是用Python编写的邮件发送程序……
    3、这是用Python编写的邮件发送程序……
    '''

    # 需要发送的附件路径
    attachments = [
        'C:\\Users\\11390\\Desktop\\Snipaste_2022-10-29_20-09-25.png',
        'C:/Users/11390/Desktop/tmp.html',
        'C:/Users/11390/Desktop/test.txt',
    ]
    # s = SendMail()
    # s.send()
