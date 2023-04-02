import json
import winreg
from tkinter import *
from tkinter import scrolledtext
from threading import Thread
import time
import inspect
import ctypes
import requests

# 默认不保存代理详细信息
# flag_save_ip = False
flag_save_ip = False
# 代理 ip 切换频率默认使用自带失效时间
# flag_ip_remain = 0
flag_ip_remain = 0


def get_ips():
    # api_url = "http://v2.api.juliangip.com/dynamic/getips?num=1&pt=1&result_type=text&split=1&trade_no=1727174320704510&sign=d3f8576b7d8bd5a0aeb186fbdda12bba"
    api_url = "http://v2.api.juliangip.com/dynamic/getips?city_code=1&city_name=1&filter=1&ip_remain=1&num=1&pt=1&result_type=json&trade_no=1727174320704510&sign=611c92295f7a001bbecaedf800064d33"
    data = requests.get(api_url)
    # res = requests.get('http://icanhazip.com/', proxies={'http': f'http://{data[0]}'})   # 查看当前使用代理IP地址
    # print(res.text)
    return data


class Application(Frame):
    def __init__(self, master=None):
        self.x = 800
        self.y = 600
        self.a = 560
        self.b = 100
        self.root = master
        self.root.geometry(f'{self.x}x{self.y}+{self.a}+{self.b}')
        self.root.title('测试')
        self.root.attributes('-topmost', True)  # 窗口置顶
        self.root.resizable(width=False, height=False)  # 设置窗口大小不可变,禁止改变窗口大小
        # self.root.bind("<Motion>", self.call_back)

        self.frm1 = Frame(self.root)
        self.frm2 = Frame(self.root)
        self.frm3 = Frame(self.root)
        self.frm4 = Frame(self.root)

        super(Application, self).__init__(master)
        self.grid()
        self.place(x=(self.x - 65) / 2 + 12, y=(self.y - 118) / 2)  # 按钮位置
        self.data = self.createpage()
        self.bttn_clicks = 0
        self.bttn_clicks_proxy = 0
        self.count = 0
        self.flag_Thread = False
        self.create_widget(self.data)
        self.create_widget_proxy(self.data)

    def create_widget_proxy(self, data):
        self.bttn_proxy = Button(self.root)
        self.bttn_proxy.place(x=(self.x - 65) / 2 + 12, y=(self.y + 30) / 2 + 150)
        self.bttn_proxy['text'] = '代理\nNO'
        self.bttn_proxy['height'] = 3
        self.bttn_proxy['width'] = 4
        self.bttn_proxy['command'] = lambda: self.update_count_proxy(data)

    def _async_raise(self, tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

    def stop_thread(self, thread):
        self._async_raise(thread.ident, SystemExit)

    def edit_system_proxy(self, open_or_close, proxy):
        """
        修改注册表使用代理
        :param open_or_close:
        :param proxy:
        :return:
        """

        root = winreg.HKEY_CURRENT_USER
        proxy_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
        kv_Enable = [
            (proxy_path, "ProxyEnable", 1, winreg.REG_DWORD),
            (proxy_path, "ProxyServer", proxy, winreg.REG_SZ),
        ]

        kv_Disable = [
            (proxy_path, "ProxyEnable", 0, winreg.REG_DWORD),
            # (proxy_path, "ProxyServer", proxy, winreg.REG_SZ),
        ]
        if open_or_close:
            kv = kv_Enable
        else:
            kv = kv_Disable
        for keypath, value_name, value, value_type in kv:
            hKey = winreg.CreateKey(root, keypath)
            winreg.SetValueEx(hKey, value_name, 0, value_type, value)

    def run(self, data):
        self.edit_system_proxy(False, "-")
        while True:
            try:
                if self.flag_Thread == True:
                    break
                self.info = get_ips()
                proxy_detail_info = self.info.json()["data"]["proxy_list"][0]
                proxy_info = proxy_detail_info.split(",")
                ip = proxy_info[0]
                ip_remain = proxy_info[-1]
                if flag_save_ip:
                    with open(r'C:\Y\Case\subcase\疫情大数据\ip_detail.txt', mode='a', encoding='utf-8') as f:
                        f.write(proxy_detail_info)
                        f.write("\n")
                    with open(r'C:\Y\Case\subcase\疫情大数据\ip.txt', mode='w', encoding='utf-8') as f:
                        f.write(ip)
                data[2].insert(INSERT, f"# {ip}\t---> {ip_remain}s\n")
                self.edit_system_proxy(True, f"http://{ip}")  # 本地使用代理开关
                self.count += 1
                if flag_save_ip:
                    time.sleep(flag_save_ip)  # 测试，不宜过长
                else:
                    time.sleep(int(ip_remain) - 10)

            except:
                self.edit_system_proxy(False, "-")
                data[2].insert(INSERT, f"# {self.info.text}\n")
                break
            if self.count % 10 == 0:
                self.count = 0
                data[2].delete(1.0, END)

    def update_count_proxy(self, data):
        self.bttn_clicks_proxy += 1
        if self.bttn_clicks_proxy % 2 == 1:
            self.flag_Thread = False
            data[2].insert(INSERT, f"# 已开启代理\n")
            self.bttn_proxy['text'] = "代理\nOFF"
            self.t1 = Thread(target=self.run, args=(data,))
            self.t1.setDaemon(True)
            self.t1.start()
        else:
            self.bttn_proxy['text'] = "代理\nNO"
            # self.stop_thread(self.t1)  # 在这里貌似没起作用
            self.flag_Thread = True
            self.edit_system_proxy(False, "-")
            data[2].insert(INSERT, f"# 已关闭代理\n")

    def create_widget(self, data):
        self.bttn = Button(self)
        self.bttn['text'] = ">>>\nGO\n>>>"
        self.bttn['height'] = 3
        self.bttn['width'] = 4
        self.bttn['command'] = lambda: self.update_count(data)
        self.bttn.grid()

    def update_count(self, data):
        if self.bttn_clicks % 2 == 0:
            self.getTextInput(data)
            self.bttn['text'] = "<<<\n清除\n<<<"

        else:
            self.textClear(data)
            self.bttn['text'] = ">>>\nGO\n>>>"
        self.bttn_clicks += 1

    def call_back(self, event):
        print('现在的位置是：', event.x_root, event.y_root)

    # 第6步，获取文本框输入
    def getTextInput(self, data):
        # Tkinter 文本框控件中第一个字符的位置是 1.0，可以用数字 1.0 或字符串"1.0"来表示。
        # "end"表示它将读取直到文本框的结尾的输入。我们也可以在这里使用 tk.END 代替字符串"end"。
        data[3].delete(1.0, END)  # 清除文本输入框的内容

        def s_to_dic(title, s):
            s = s.replace(': \n', ': ').replace(':\n', ': ')
            dic = dict([line.split(': ' if " " in line else ':', 1) for line in s.split("\n") if line != '' and "#" not in line])
            tmp = json.dumps(dic, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
            data[3].insert(INSERT, f"\n{title} = {tmp}\n")

        s = data[0].get(1.0, END)  # 获取文本输入框的内容
        s_to_dic('headers', s)

        s = data[1].get(1.0, END)  # 获取文本输入框的内容
        s_to_dic('params', s)

        s = data[2].get(1.0, END)  # 获取文本输入框的内容
        s_to_dic('data', s)

    def textClear(self, data):
        data[0].delete(1.0, END)  # 清除文本输入框的内容
        data[1].delete(1.0, END)  # 清除文本输入框的内容
        data[2].delete(1.0, END)  # 清除文本输入框的内容
        # data[3].delete(1.0, END)  # 清除文本输入框的内容

    def textCopy(self, text):
        data = text.get(1.0, 'end')

        def one():
            import pyperclip
            pyperclip.copy(data)
            pyperclip.paste()

        def two():
            import clipboard
            clipboard.copy(data)  # now the clipboard content will be string "abc"
            text = clipboard.paste()  # text will have the content of clipboard

        def three():
            from tkinter import Tk
            r = Tk()
            r.withdraw()
            r.clipboard_clear()
            r.clipboard_append(data)
            r.update()  # now it stays on the clipboard after the window is closed
            r.destroy()

        def four():
            import pandas as pd
            df = pd.DataFrame([data])
            df.to_clipboard(index=False, header=False)

        # one()
        # two()
        three()
        # four()  # 不佳，粘贴带有引号
        pass

    def createpage(self):
        # menu = Menu(self.root)
        # self.root.config(menu=menu)
        # filemenu = Menu(menu)
        # menu.add_cascade(label='测试1', menu=filemenu)
        # filemenu.add_command(label='1')
        # filemenu.add_command(label='2')
        # filemenu.add_command(label='3')
        # onemenu = Menu(menu)
        # menu.add_cascade(label='测试2', menu=onemenu)
        # onemenu.add_command(label='1')
        # onemenu.add_command(label='2')
        # onemenu.add_command(label='3')

        self.frm1.config(height=(self.y - 14) / 3, width=(self.x - 65) / 2)
        Label(self.frm1, text='headers').place(anchor=NW)
        self.frm1.place(x=10, y=5)
        # frm1下的控件
        text1 = scrolledtext.ScrolledText(self.frm1, highlightcolor='red', highlightthickness=1.5)
        text1.place(x=0, y=23, height=(self.y - 14) / 3 - 23, width=(self.x - 65) / 2)

        self.frm2.config(height=(self.y - 14) / 3, width=(self.x - 65) / 2)
        Label(self.frm2, text='params').place(in_=self.frm2, anchor=NW)
        self.frm2.place(x=10, y=(self.y - 14) / 3 + 7)
        # frm2下的控件
        text2 = scrolledtext.ScrolledText(self.frm2, highlightcolor='red', highlightthickness=1.5)
        text2.place(x=0, y=23, height=(self.y - 14) / 3 - 23, width=(self.x - 65) / 2)

        self.frm3.config(height=(self.y - 14) / 3, width=(self.x - 65) / 2)
        Label(self.frm3, text='data').place(in_=self.frm3, anchor=NW)
        self.frm3.place(x=10, y=2 * (self.y - 14) / 3 + 9)
        # frm3下的控件
        self.text3 = scrolledtext.ScrolledText(self.frm3, highlightcolor='red', highlightthickness=1.5)
        self.text3.place(x=0, y=23, height=(self.y - 14) / 3 - 23, width=(self.x - 65) / 2)

        self.frm4.config(height=self.y - 10, width=(self.x - 65) / 2)
        Label(self.frm4, text='full').place(in_=self.frm4, anchor=NW)
        self.frm4.place(x=(self.x - 65) / 2 + 55, y=5)
        # frm4下的控件
        text4 = scrolledtext.ScrolledText(self.frm4, highlightcolor='red', highlightthickness=1.5)
        text4.place(x=0, y=23, height=self.x - 10 - 23, width=(self.x - 65) / 2)

        # Button(self.root, text='GO', height=3, width=4,
        #        command=lambda: self.getTextInput([text1, text2, text3, text4])).place(x=375, y=233)
        # Button(self.root, text='清除', height=3, width=4, command=lambda: self.textClear([text1, text2, text3, text4])).place(x=375, y=307)
        # Button(self.frm4, text='copy', height=3, width=6, command=lambda: self.textCopy(text4)).place(x=170, y=265)

        Button(self.root, text='复制', height=3, width=4, command=lambda: self.textCopy(text4)).place(
            x=(self.x - 65) / 2 + 12, y=(self.y + 30) / 2)

        return [text1, text2, self.text3, text4]

        # frm3下的Label
        # Label(self.frm3, text='Label Test Test',
        #       fg='red', font='Verdana 10 bold').place(x=300, y=10)
        # frm2下的Button
        # for i in range(9):
        #     Button(self.frm2, text='Button%d' % i).place(x=20, y=20+i*50, width=100)


if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()
    app.edit_system_proxy(False, "-")
