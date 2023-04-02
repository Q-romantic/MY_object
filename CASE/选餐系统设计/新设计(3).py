import copy
import csv
import pandas as pd
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from PIL import Image, ImageTk

filename_c = r'C:\Y\Case\选餐系统设计\选餐数据.csv'  # 文件路径
filename_s = r'C:\Y\Case\选餐系统设计\学生登录密码.csv'  # 文件路径
filename_t = r'C:\Y\Case\选餐系统设计\教师登录密码.csv'  # 文件路径
students_num = sum(1 for _ in open(filename_s)) - 1
teachers_num = sum(1 for _ in open(filename_t)) - 1


# 基本界面（窗口）
class Base:
    def __init__(self, window):
        self.window = window

        self.window.title('配餐系统')
        # self.window.iconbitmap(icon_file)  # icon_file就是一个.ico的图标文件，使用绝对或相对路径
        self.window.attributes('-topmost', True)  # 窗口置顶
        self.window.resizable(False, False)  # 窗口尺寸固定
        # window.overrideredirect(True)   # 隐藏窗口外部，会导致无标题栏，且不能选择最小化最大化关闭按钮，慎用！！！
        # window.attributes("-alpha", 0.6)    # 设置透明度

        # 窗口 宽、高
        w, h = 1100, 482 - 28  # 调试后得知或自定义
        self.centerWindow(self.window, w, h)

        SelectIdentityFace(self.window)

    # 屏幕居中
    def centerWindow(self, window, width, height):  # 窗口 宽、高
        # 获取屏幕 宽、高
        ws = window.winfo_screenwidth()  # 1920
        hs = window.winfo_screenheight()  # 1080
        # 计算 x, y 位置
        x = (ws / 2) - (width / 2)  # 左右1:1
        y = (hs / 4) - (height / 4)  # 上下1:3
        window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def getPeoplesAndFlags(self, filename):
        flag = '学生' if '学生登录密码.csv' in filename else '教师' if '教师登录密码.csv' in filename else None
        people_num = sum(1 for _ in open(filename)) - 1
        return flag, people_num


# 身份选择界面
class SelectIdentityFace:
    def __init__(self, window):
        # 生成身份选择界面
        self.window = window
        self.Pilimage = Image.open(r"封面.jpg")
        self.image = ImageTk.PhotoImage(image=self.Pilimage)
        self.selectIdentityFace = tk.Frame(self.window, width=1100, height=434, background="palegoldenrod")
        self.selectIdentityFace.pack()
        coverImage = tk.Label(self.selectIdentityFace, image=self.image)
        coverImage.place(relx=0.4, rely=0.5, anchor='center')
        titleLabel = tk.Label(self.selectIdentityFace, text="您的身份", font=('黑体', 20))
        titleLabel.place(relx=0.9, rely=0.3, anchor='center')
        teacherButton = tk.Button(self.selectIdentityFace, text="老师", font=('楷体', 18),
                                  command=self.teacherLoginFace)
        teacherButton.place(relx=0.85, rely=0.5, anchor='center')
        studentButton = tk.Button(self.selectIdentityFace, text="学生", font=('楷体', 18),
                                  command=self.studentLoginFace)
        studentButton.place(relx=0.95, rely=0.5, anchor='center')

        # 添加菜单
        menubar = tk.Menu(self.selectIdentityFace)
        functionMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="菜单", menu=functionMenu)
        functionMenu.add_command(label="exit", command=exit)
        self.window.config(menu=menubar)

    # 跳转到老师登录界面
    def teacherLoginFace(self):
        self.selectIdentityFace.destroy()
        PublicLoginFace(self.window, filename_t)

    # 跳转到学生登录界面
    def studentLoginFace(self):
        self.selectIdentityFace.destroy()
        PublicLoginFace(self.window, filename_s)


# 公共注册界面
class PublicRegisterFace:
    def __init__(self, window, filename):
        #  生成注册界面
        self.window = window
        self.filename = filename
        self.flag, self.people_num = Base.getPeoplesAndFlags(self.window, filename)

        self.Pilimage = Image.open(r"封面.jpg")
        self.image = ImageTk.PhotoImage(image=self.Pilimage)
        self.publicRegisterFace = tk.Frame(self.window, width=1100, height=434, background="palegoldenrod")
        self.publicRegisterFace.pack()
        coverImage = tk.Label(self.publicRegisterFace, image=self.image)
        coverImage.place(relx=0.65, rely=0.5, anchor='center')
        titleLabel = tk.Label(self.publicRegisterFace, text="用户注册", font=('黑体', 20))
        titleLabel.place(relx=0.165, rely=0.1, anchor='center')
        userNameLabel = tk.Label(self.publicRegisterFace, text="姓名", font=('楷体', 18))
        userNameLabel.place(relx=0.055, rely=0.3, anchor='center')
        self.varUserName = tk.StringVar()
        userNameEntry = tk.Entry(self.publicRegisterFace, textvariable=self.varUserName, show=None,
                                 font=('楷体', 18), justify='center')
        userNameEntry.place(relx=0.22, rely=0.3, anchor='center')
        PasswordLabel1 = tk.Label(self.publicRegisterFace, text="密码", font=('楷体', 18))  # 密码
        PasswordLabel1.place(relx=0.055, rely=0.5, anchor='center')
        self.varPassword1 = tk.StringVar()
        PasswordEntry = tk.Entry(self.publicRegisterFace, textvariable=self.varPassword1, show='*',
                                 font=('楷体', 18))
        PasswordEntry.place(relx=0.22, rely=0.5, anchor='center')
        PasswordLabel2 = tk.Label(self.publicRegisterFace, text="确认密码", font=('楷体', 18))  # 确认密码
        PasswordLabel2.place(relx=0.055, rely=0.7, anchor='center')
        self.varPassword2 = tk.StringVar()
        newPasswordEntry = tk.Entry(self.publicRegisterFace, textvariable=self.varPassword2, show='*',
                                    font=('楷体', 18))
        newPasswordEntry.place(relx=0.22, rely=0.7, anchor='center')
        confrimLabel = tk.Button(self.publicRegisterFace, text="确认", font=('楷体', 18),
                                 command=self.judge)
        confrimLabel.place(relx=0.16, rely=0.9, anchor='center')

        # 添加菜单
        menubar = tk.Menu(self.publicRegisterFace)
        functionMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="菜单", menu=functionMenu)
        functionMenu.add_command(label="注册", command=self.publicRegisterFaces)
        functionMenu.add_command(label="切换身份", command=self.SelectIdentityFace)
        functionMenu.add_separator()  # 插入分隔符(上下分隔线)
        functionMenu.add_command(label="exit", command=exit)
        self.window.config(menu=menubar)

    # 判断 学生 or 教师，跳转至各自登录主页
    def userFunctionFaces(self, flag, name, password):
        if flag == '教师':
            self.teacherFunctionFace(name, password)
        elif flag == '学生':
            self.studentFunctionFace(name, password)
        else:
            tkinter.messagebox.showinfo(title="提示", message="出错啦！")

    # 判断姓名和密码
    def judge(self):
        userName = self.varUserName.get()
        password1 = self.varPassword1.get()
        password2 = self.varPassword2.get()

        if userName:
            if password1:
                if password1 == password2:
                    tabel = pd.read_csv(self.filename, dtype='str')
                    names = {tabel.iloc[i, 1]: i for i in range(0, self.people_num)}
                    self.newPassword = password1
                    if userName in names:
                        msg = tkinter.messagebox.askyesnocancel(title="提示", message="用户已存在，是否更新密码")
                        if msg:
                            # 方法一：推荐（修改指定行）
                            tabel.loc[names[userName], :] = [names[userName], userName, self.newPassword]
                            tabel.to_csv(self.filename, index=False)

                            # 方法二：
                            pass
                            # file = open(self.filename, 'w', newline='', encoding='utf8')
                            # header = ['序号', '姓名', '密码']
                            # Passwords = csv.writer(file)
                            # Passwords.writerow(header)
                            # for i in range(0, self.people_num):
                            #     password = []
                            #     if tabel.iloc[i, 1] == userName:
                            #         password.append(i + 1)
                            #         password.append(userName)
                            #         password.append(self.newPassword)
                            #         Passwords.writerow(password)
                            #     else:
                            #         password.append(i + 1)
                            #         password.append(tabel.iloc[i, 1])
                            #         password.append(tabel.iloc[i, 2])
                            #         Passwords.writerow(password)
                            tkinter.messagebox.showinfo(title="提示", message="修改成功！")
                            self.userFunctionFaces(self.flag, userName, self.newPassword)
                        else:
                            pass
                    else:
                        file = open(self.filename, 'a', newline='', encoding='utf8')
                        self.people_num += 1
                        insertInfo = [self.people_num, userName, password1]
                        info = csv.writer(file)
                        info.writerow(insertInfo)
                        tkinter.messagebox.showinfo(title="提示", message="注册成功！")
                        self.userFunctionFaces(self.flag, userName, self.newPassword)
                else:
                    tkinter.messagebox.showinfo(title="提示", message="确认密码和密码不一致，请重试！")
            else:
                tkinter.messagebox.showinfo(title="提示", message="密码不能为空")
        else:
            tkinter.messagebox.showinfo(title="提示", message="请输入您的姓名")

    # 跳转到注册界面
    def publicRegisterFaces(self):
        self.publicRegisterFace.destroy()
        PublicRegisterFace(self.window, self.filename)

    # 跳转到身份选择界面
    def SelectIdentityFace(self):
        self.publicRegisterFace.destroy()
        SelectIdentityFace(self.window)

    # 跳转到老师首页,跳过登录步骤
    def teacherFunctionFace(self, name, password):
        self.publicRegisterFace.destroy()
        TeacherFunctionFace(self.window, name)

    # 跳转到学生首页,跳过登录步骤
    def studentFunctionFace(self, name, password):
        self.publicRegisterFace.destroy()
        StudentFunctionFace(self.window, name)


# 公共登录界面
class PublicLoginFace:
    def __init__(self, window, filename):
        # 生成登录界面
        self.window = window
        self.filename = filename
        self.flag, self.people_num = Base.getPeoplesAndFlags(self.window, filename)

        self.Pilimage = Image.open(r"封面.jpg")
        self.image = ImageTk.PhotoImage(image=self.Pilimage)
        self.publicLoginFace = tk.Frame(self.window, width=1100, height=434, background="palegoldenrod")
        self.publicLoginFace.pack()
        coverImage = tk.Label(self.publicLoginFace, image=self.image)
        coverImage.place(relx=0.35, rely=0.5, anchor='center')
        titleLabel = tk.Label(self.publicLoginFace, text=f"{self.flag}登录", font=('黑体', 20))
        titleLabel.place(relx=0.85, rely=0.2, anchor='center')
        teacherNameLabel = tk.Label(self.publicLoginFace, text="姓名", font=('楷体', 18))
        teacherNameLabel.place(relx=0.73, rely=0.4, anchor='center')
        self.varUserName = tk.StringVar()
        teacherNameEntry = tk.Entry(self.publicLoginFace, textvariable=self.varUserName, show=None,
                                    font=('楷体', 18))
        teacherNameEntry.place(relx=0.88, rely=0.4, anchor='center')
        passwordLabel = tk.Label(self.publicLoginFace, text="密码", font=('楷体', 18))
        passwordLabel.place(relx=0.73, rely=0.6, anchor='center')
        self.varPassword = tk.StringVar()
        passwordEntry = tk.Entry(self.publicLoginFace, textvariable=self.varPassword, show='*', font=('楷体', 18))
        passwordEntry.place(relx=0.88, rely=0.6, anchor='center')
        loginLabel = tk.Button(self.publicLoginFace, text="登录", font=('楷体', 18), command=self.judge)
        loginLabel.place(relx=0.85, rely=0.8, anchor='center')

        # 添加菜单
        menubar = tk.Menu(self.publicLoginFace)
        functionMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="菜单", menu=functionMenu)
        functionMenu.add_command(label="注册", command=self.publicRegisterFace)
        functionMenu.add_command(label="切换身份", command=self.publicSelectIdentityFace)
        functionMenu.add_separator()  # 插入分隔符(上下分隔线)
        functionMenu.add_command(label="exit", command=exit)
        self.window.config(menu=menubar)

    # 判断姓名和密码是否正确
    def judge(self):
        tabel = pd.read_csv(self.filename, dtype='str')
        userName = self.varUserName.get()
        password = self.varPassword.get()
        for i in range(0, self.people_num):  # xx登录密码.csv文件中的人数
            if tabel.iloc[i, 1] == userName and tabel.iloc[i, 2] == password:  # 读取序号为i的信息，序号、姓名、密码
                self.publicLoginFace.destroy()
                PublicRegisterFace(self.window, self.filename).userFunctionFaces(self.flag, userName, password)
                break
            elif i == self.people_num - 1:
                tkinter.messagebox.showinfo(title="提示", message="姓名或密码不正确！")
            else:
                continue

    # 判断 学生 or 教师，跳转至各自注册页面
    def userRegisterFaces(self, flag):
        if flag == '教师':
            PublicRegisterFace(self.window, filename_t)
        elif flag == '学生':
            PublicRegisterFace(self.window, filename_s)
        else:
            tkinter.messagebox.showinfo(title="提示", message="出错啦！")

    # 跳转到注册界面
    def publicRegisterFace(self):
        self.publicLoginFace.destroy()
        self.userRegisterFaces(self.flag)

    # 跳转到身份选择界面
    def publicSelectIdentityFace(self):
        self.publicLoginFace.destroy()
        SelectIdentityFace(self.window)


# # 老师登录界面
# class TeacherLoginFace:
#     def __init__(self, window):
#         # 生成老师登录界面
#         self.window = window
#         self.Pilimage = Image.open(r"封面.jpg")
#         self.image = ImageTk.PhotoImage(image=self.Pilimage)
#         self.teacherLoginFace = tk.Frame(self.window, width=1100, height=434, background="palegoldenrod")
#         self.teacherLoginFace.pack()
#         coverImage = tk.Label(self.teacherLoginFace, image=self.image)
#         coverImage.place(relx=0.35, rely=0.5, anchor='center')
#         titleLabel = tk.Label(self.teacherLoginFace, text="用户登录", font=('黑体', 20))
#         titleLabel.place(relx=0.85, rely=0.2, anchor='center')
#         teacherNameLabel = tk.Label(self.teacherLoginFace, text="姓名", font=('楷体', 18))
#         teacherNameLabel.place(relx=0.73, rely=0.4, anchor='center')
#         self.varTeacherName = tk.StringVar()
#         teacherNameEntry = tk.Entry(self.teacherLoginFace, textvariable=self.varTeacherName, show=None,
#                                     font=('楷体', 18))
#         teacherNameEntry.place(relx=0.88, rely=0.4, anchor='center')
#         passwordLabel = tk.Label(self.teacherLoginFace, text="密码", font=('楷体', 18))
#         passwordLabel.place(relx=0.73, rely=0.6, anchor='center')
#         self.varPassword = tk.StringVar()
#         passwordEntry = tk.Entry(self.teacherLoginFace, textvariable=self.varPassword, show='*', font=('楷体', 18))
#         passwordEntry.place(relx=0.88, rely=0.6, anchor='center')
#         loginLabel = tk.Button(self.teacherLoginFace, text="登录", font=('楷体', 18), command=self.judge)
#         loginLabel.place(relx=0.85, rely=0.8, anchor='center')
#
#         # 添加菜单
#         menubar = tk.Menu(self.teacherLoginFace)
#         functionMenu = tk.Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="菜单", menu=functionMenu)
#         functionMenu.add_command(label="注册", command=self.teacherRegisterFace)
#         functionMenu.add_command(label="切换身份", command=self.teacherSelectIdentityFace)
#         functionMenu.add_separator()  # 插入分隔符(上下分隔线)
#         functionMenu.add_command(label="exit", command=exit)
#         self.window.config(menu=menubar)
#
#     # 判断姓名和密码是否正确
#     def judge(self):
#         tabel = pd.read_csv('教师登录密码.csv', dtype='str')
#         global teacherName
#         teacherName = self.varTeacherName.get()
#         password = self.varPassword.get()
#         for i in range(0, teachers_num):  # 教师登录密码.csv文件中的人数限制
#             if tabel.iloc[i, 1] == teacherName and tabel.iloc[i, 2] == password:  # 读取序号为i的信息，序号、姓名、密码
#                 self.teacherFunctionFaces()
#                 break
#             elif i == teachers_num - 1:
#                 tkinter.messagebox.showinfo(title="提示", message="姓名或密码不正确！")
#             else:
#                 continue
#
#     # 跳转到老师注册界面
#     def teacherRegisterFace(self):
#         self.teacherLoginFace.destroy()
#         PublicRegisterFace(self.window, filename_t)
#
#     # 跳转到老师功能选择界面
#     def teacherFunctionFaces(self):
#         self.teacherLoginFace.destroy()
#         TeacherFunctionFace(self.window, teacherName)
#
#     # 跳转到身份选择界面
#     def teacherSelectIdentityFace(self):
#         self.teacherLoginFace.destroy()
#         SelectIdentityFace(self.window)
#
#
# # 学生登录界面
# class StudentLoginFace:
#     def __init__(self, window):
#         #  生成登录界面
#         self.window = window
#         self.Pilimage = Image.open(r"封面.jpg")
#         self.image = ImageTk.PhotoImage(image=self.Pilimage)
#         self.studentLoginFace = tk.Frame(self.window, width=1100, height=434, background="palegoldenrod")
#         self.studentLoginFace.pack()
#         coverImage = tk.Label(self.studentLoginFace, image=self.image)
#         coverImage.place(relx=0.35, rely=0.5, anchor='center')
#         titleLabel = tk.Label(self.studentLoginFace, text="用户登录", font=('黑体', 20))
#         titleLabel.place(relx=0.85, rely=0.2, anchor='center')
#         studentNameLabel = tk.Label(self.studentLoginFace, text="姓名", font=('楷体', 18))
#         studentNameLabel.place(relx=0.73, rely=0.4, anchor='center')
#         self.varStudentName = tk.StringVar()
#         studentNameEntry = tk.Entry(self.studentLoginFace, textvariable=self.varStudentName, show=None,
#                                     font=('楷体', 18))
#         studentNameEntry.place(relx=0.88, rely=0.4, anchor='center')
#         passwordLabel = tk.Label(self.studentLoginFace, text="密码", font=('楷体', 18))
#         passwordLabel.place(relx=0.73, rely=0.6, anchor='center')
#         self.varPassword = tk.StringVar()
#         passwordEntry = tk.Entry(self.studentLoginFace, textvariable=self.varPassword, show='*', font=('楷体', 18))
#         passwordEntry.place(relx=0.88, rely=0.6, anchor='center')
#         loginLabel = tk.Button(self.studentLoginFace, text="登录", font=('楷体', 18), command=self.judge)
#         loginLabel.place(relx=0.85, rely=0.8, anchor='center')
#
#         # 添加菜单
#         menubar = tk.Menu(self.studentLoginFace)
#         functionMenu = tk.Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="菜单", menu=functionMenu)
#         functionMenu.add_command(label="注册", command=self.studentRegisterFace)
#         functionMenu.add_command(label="切换身份", command=self.studentSelectIdentityFace)
#         functionMenu.add_separator()  # 插入分隔符(上下分隔线)
#         functionMenu.add_command(label="exit", command=exit)
#         self.window.config(menu=menubar)
#
#     # 判断姓名和密码是否正确
#     def judge(self):
#         tabel = pd.read_csv('学生登录密码.csv', dtype='str')
#         global studentName
#         studentName = self.varStudentName.get()
#         password = self.varPassword.get()
#         for i in range(0, students_num):
#             if tabel.iloc[i, 1] == studentName and tabel.iloc[i, 2] == password:
#                 self.studentFunctionFace()
#                 break
#             elif i == students_num - 1:
#                 tkinter.messagebox.showinfo(title="提示", message="姓名或密码不正确！")
#             else:
#                 continue
#
#     # 跳转到学生注册界面
#     def studentRegisterFace(self):
#         self.studentLoginFace.destroy()
#         PublicRegisterFace(self.window, filename_s)
#
#     # 跳转到学生功能选择界面
#     def studentFunctionFace(self):
#         self.studentLoginFace.destroy()
#         StudentFunctionFace(self.window, studentName)
#
#     # 跳转到身份选择界面
#     def studentSelectIdentityFace(self):
#         self.studentLoginFace.destroy()
#         SelectIdentityFace(self.window)

pass

# 公共首页 ????????????????????????后面再改
# class PublicFunctionFace:
#     def __init__(self, window, filename):
#         #  生成功能选择界面
#         self.window = window
#         self.filename = filename
#         
#         self.window.title('配餐系统')
#         self.Pilimage1 = Image.open(r"封面.jpg")
#         self.image1 = ImageTk.PhotoImage(image=self.Pilimage1)
#         self.Pilimage2 = Image.open(r"二维码.jpg")
#         self.image2 = ImageTk.PhotoImage(image=self.Pilimage2)
#         self.publicFunctionFace = tk.Frame(self.window, width=1100, height=434, background="palegoldenrod")
#         self.publicFunctionFace.pack()
#         coverImage1 = tk.Label(self.publicFunctionFace, image=self.image1)
#         coverImage1.place(relx=0.66, rely=0.5, anchor='center')
#         coverImage2 = tk.Label(self.publicFunctionFace, image=self.image2)
#         coverImage2.place(relx=0.18, rely=0.5, anchor='center')
#         text = tk.Label(self.publicFunctionFace, text="欢迎扫码关注！", font=('楷体', 20))
#         text.place(relx=0.18, rely=0.94, anchor='center')
# 
#         # 添加菜单
#         menubar = tk.Menu(self.publicFunctionFace)
#         functionMenu = tk.Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="菜单", menu=functionMenu)
#         functionMenu.add_command(label="修改登录密码", command=self.publicChangePasswordFaces)
#         functionMenu.add_command(label="进行点餐", command=self.studentOrderFaces)
#         functionMenu.add_separator()
#         functionMenu.add_command(label="返回主页", command=self.publicFunctionFaces)
#         functionMenu.add_command(label="退出系统", command=self.publicLoginFaces)
#         self.window.config(menu=menubar)
#         
#     # 跳转到学生修改密码界面
#     def publicChangePasswordFaces(self):
#         self.publicFunctionFace.destroy()
#         publicChangePasswordFace(self.window, self.username)
# 
#     # 跳转到学生点餐界面
#     def studentOrderFaces(self):
#         self.publicFunctionFace.destroy()
#         StudentOrderFace(self.window, self.username)
# 
#     # 跳转到学生主页
#     def publicFunctionFaces(self):
#         self.publicFunctionFace.destroy()
#         publicFunctionFace(self.window, self.username)
# 
#     # 跳转到登录界面
#     def publicLoginFaces(self):
#         self.publicFunctionFace.destroy()
#         publicLoginFace(self.window)

pass


# 老师功能选择界面,老师主页
class TeacherFunctionFace:
    def __init__(self, window, name):
        #  生成功能选择界面
        global username
        username = name
        self.window = window
        self.Pilimage1 = Image.open(r"封面.jpg")
        self.image1 = ImageTk.PhotoImage(image=self.Pilimage1)
        self.Pilimage2 = Image.open(r"二维码.jpg")
        self.image2 = ImageTk.PhotoImage(image=self.Pilimage2)
        self.teacherFunctionFace = tk.Frame(self.window, width=1100, height=434, background="palegoldenrod")
        self.teacherFunctionFace.pack()
        coverImage1 = tk.Label(self.teacherFunctionFace, image=self.image1)
        coverImage1.place(relx=0.66, rely=0.5, anchor='center')
        coverImage2 = tk.Label(self.teacherFunctionFace, image=self.image2)
        coverImage2.place(relx=0.18, rely=0.5, anchor='center')
        text = tk.Label(self.teacherFunctionFace, text="欢迎扫码关注！", font=('楷体', 20))
        text.place(relx=0.18, rely=0.94, anchor='center')

        # 添加菜单
        menubar = tk.Menu(self.teacherFunctionFace)
        functionMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="菜单", menu=functionMenu)
        functionMenu.add_command(label="修改登录密码", command=self.teacherChangePasswordFaces)
        functionMenu.add_command(label="查看学生信息", command=self.teacherLookStudentFaces)
        functionMenu.add_separator()
        functionMenu.add_command(label="返回主页", command=self.teacherFunctionFaces)
        functionMenu.add_command(label="退出系统", command=self.teacherLoginFaces)
        self.window.config(menu=menubar)

    # 跳转到老师修改登录密码界面
    def teacherChangePasswordFaces(self):
        self.teacherFunctionFace.destroy()
        TeacherChangePasswordFace(self.window, username)

    # 跳转到查看学生信息的界面
    def teacherLookStudentFaces(self):
        self.teacherFunctionFace.destroy()
        TeacherLookStudentFace(self.window, username)

    # 跳转到老师主页
    def teacherFunctionFaces(self):
        self.teacherFunctionFace.destroy()
        TeacherFunctionFace(self.window, username)

    # 跳转到登录界面
    def teacherLoginFaces(self):
        self.teacherFunctionFace.destroy()
        PublicLoginFace(self.window, filename_t)


# 老师修改登录密码的界面
class TeacherChangePasswordFace():
    def __init__(self, window, name):
        #  生成修改登录密码界面
        global username
        username = name
        self.window = window
        self.Pilimage = Image.open(r"封面.jpg")
        self.image = ImageTk.PhotoImage(image=self.Pilimage)
        self.teacherChangePasswordFace = tk.Frame(self.window, width=1100, height=434, background="palegoldenrod")
        self.teacherChangePasswordFace.pack()
        coverImage = tk.Label(self.teacherChangePasswordFace, image=self.image)
        coverImage.place(relx=0.65, rely=0.5, anchor='center')
        titleLabel = tk.Label(self.teacherChangePasswordFace, text="修改登录密码", font=('黑体', 20))
        titleLabel.place(relx=0.163, rely=0.1, anchor='center')
        teacherNameLabel = tk.Label(self.teacherChangePasswordFace, text="姓名", font=('楷体', 18))
        teacherNameLabel.place(relx=0.04, rely=0.3, anchor='center')
        self.varTeacherName = tk.StringVar()
        teacherNameEntry = tk.Entry(self.teacherChangePasswordFace, textvariable=self.varTeacherName, show=None,
                                    font=('楷体', 18))
        teacherNameEntry.place(relx=0.188, rely=0.3, anchor='center')
        oldPasswordLabel = tk.Label(self.teacherChangePasswordFace, text="原密码", font=('楷体', 18))  # 旧密码
        oldPasswordLabel.place(relx=0.04, rely=0.5, anchor='center')
        self.varOldPassword = tk.StringVar()
        oldPasswordEntry = tk.Entry(self.teacherChangePasswordFace, textvariable=self.varOldPassword, show='*',
                                    font=('楷体', 18))
        oldPasswordEntry.place(relx=0.188, rely=0.5, anchor='center')
        newPasswordLabel = tk.Label(self.teacherChangePasswordFace, text="新密码", font=('楷体', 18))  # 新密码
        newPasswordLabel.place(relx=0.04, rely=0.7, anchor='center')
        self.varNewPassword = tk.StringVar()
        newPasswordEntry = tk.Entry(self.teacherChangePasswordFace, textvariable=self.varNewPassword, show='*',
                                    font=('楷体', 18))
        newPasswordEntry.place(relx=0.188, rely=0.7, anchor='center')
        confrimLabel = tk.Button(self.teacherChangePasswordFace, text="确认", font=('楷体', 18),
                                 command=self.successPassword)
        confrimLabel.place(relx=0.14, rely=0.9, anchor='center')

        #  添加菜单
        menubar = tk.Menu(self.teacherChangePasswordFace)
        functionMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="菜单", menu=functionMenu)
        functionMenu.add_command(label="修改登录密码", command=self.teacherChangePasswordFaces)
        functionMenu.add_command(label="查看学生信息", command=self.teacherLookStudentFaces)
        functionMenu.add_separator()
        functionMenu.add_command(label="返回主页", command=self.teacherFunctionFaces)
        functionMenu.add_command(label="退出系统", command=self.teacherLoginFaces)
        self.window.config(menu=menubar)

    #  修改成功并弹出提示信息
    def successPassword(self):
        teacherName = self.varTeacherName.get()
        oldPassword = self.varOldPassword.get()
        newPassword = self.varNewPassword.get()
        if teacherName == username:
            tabel = pd.read_csv("教师登录密码.csv", dtype='str')
            file = open('教师登录密码.csv', 'w', newline='', encoding='utf8')
            header = ['序号', '姓名', '密码']
            Passwords = csv.writer(file)
            Passwords.writerow(header)
            for i in range(0, teachers_num):
                password = []
                if tabel.iloc[i, 1] == teacherName:
                    password.append(i + 1)
                    password.append(teacherName)
                    password.append(newPassword)
                    Passwords.writerow(password)
                else:
                    password.append(i + 1)
                    password.append(tabel.iloc[i, 1])
                    password.append(tabel.iloc[i, 2])
                    Passwords.writerow(password)
            tkinter.messagebox.showinfo(title="提示", message="修改成功！")
        else:
            tkinter.messagebox.showinfo(title="提示", message="输入姓名有误！")

    #  跳转到老师修改登录密码界面
    def teacherChangePasswordFaces(self):
        self.teacherChangePasswordFace.destroy()
        TeacherChangePasswordFace(self.window, username)

    #  跳转到查看学生个人信息的界面
    def teacherLookStudentFaces(self):
        self.teacherChangePasswordFace.destroy()
        TeacherLookStudentFace(self.window, username)

    #  跳转到老师主页
    def teacherFunctionFaces(self):
        self.teacherChangePasswordFace.destroy()
        TeacherFunctionFace(self.window, username)

    #  跳转到登录界面
    def teacherLoginFaces(self):
        self.teacherChangePasswordFace.destroy()
        PublicLoginFace(self.window, filename_t)


# 老师查看学生信息的界面
class TeacherLookStudentFace():
    def __init__(self, window, name):
        #  生成学生个人信息界面
        #  仿照老师和学生查看信息的类编写
        global username
        username = name
        self.window = window
        self.teacherLookStudentFace = tk.Frame(self.window, background="palegoldenrod")
        self.teacherLookStudentFace.pack()
        #  添加菜单
        menubar = tk.Menu(self.teacherLookStudentFace)
        functionMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="菜单", menu=functionMenu)
        functionMenu.add_command(label="修改登录密码", command=self.teacherChangePasswordFaces)
        functionMenu.add_command(label="查看学生信息", command=self.teacherLookStudentFaces)
        # functionMenu.add_command(label="查看学生成绩", command=self.teacherLookInforFaces)
        functionMenu.add_separator()
        functionMenu.add_command(label="返回主页", command=self.teacherFunctionFaces)
        functionMenu.add_command(label="退出系统", command=self.teacherLoginFaces)
        self.window.config(menu=menubar)

        title = tk.Label(self.teacherLookStudentFace, text="您学生的个人信息如下表", font=('楷体', 20))
        title.grid(row=0, columnspan=3)
        # distrTabel = pd.read_csv('学生分配表.csv')
        studentTabels = pd.read_csv('学生登录密码.csv')
        header = ['序号', '姓名', '密码']
        studentTabel = ttk.Treeview(self.teacherLookStudentFace, columns=header, show="headings")
        for col in header:
            studentTabel.column(col, width=120)
            studentTabel.heading(col, text=col)
        studentTabel.grid(row=1, column=0, columnspan=2)
        # value = [username]
        for i in range(0, students_num):
            # if name == studentTabels.iloc[i, 1]:
            value = []
            for j in range(0, 3):
                value.append(studentTabels.iloc[i, j])
            studentTabel.insert("", "end", values=value)

    #  跳转到老师修改登录密码界面
    def teacherChangePasswordFaces(self):
        self.teacherLookStudentFace.destroy()
        TeacherChangePasswordFace(self.window, username)

    #  跳转到查看学生个人信息的界面
    def teacherLookStudentFaces(self):
        self.teacherLookStudentFace.destroy()
        TeacherLookStudentFace(self.window, username)

    #  跳转到老师主页
    def teacherFunctionFaces(self):
        self.teacherLookStudentFace.destroy()
        TeacherFunctionFace(self.window, username)

    #  跳转到登录界面
    def teacherLoginFaces(self):
        self.teacherLookStudentFace.destroy()
        PublicLoginFace(self.window, filename_t)


# 学生功能选择界面,学生主页
class StudentFunctionFace:
    def __init__(self, window, name):
        #  生成功能选择界面
        self.username = name
        self.window = window
        self.window.title('配餐系统')
        self.Pilimage1 = Image.open(r"封面.jpg")
        self.image1 = ImageTk.PhotoImage(image=self.Pilimage1)
        self.Pilimage2 = Image.open(r"二维码.jpg")
        self.image2 = ImageTk.PhotoImage(image=self.Pilimage2)
        self.studentFunctionFace = tk.Frame(self.window, width=1100, height=434, background="palegoldenrod")
        self.studentFunctionFace.pack()
        coverImage1 = tk.Label(self.studentFunctionFace, image=self.image1)
        coverImage1.place(relx=0.66, rely=0.5, anchor='center')
        coverImage2 = tk.Label(self.studentFunctionFace, image=self.image2)
        coverImage2.place(relx=0.18, rely=0.5, anchor='center')
        text = tk.Label(self.studentFunctionFace, text="欢迎扫码关注！", font=('楷体', 20))
        text.place(relx=0.18, rely=0.94, anchor='center')

        # 添加菜单
        menubar = tk.Menu(self.studentFunctionFace)
        functionMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="菜单", menu=functionMenu)
        functionMenu.add_command(label="修改登录密码", command=self.studentChangePasswordFaces)
        functionMenu.add_command(label="进行点餐", command=self.studentOrderFaces)
        functionMenu.add_separator()
        functionMenu.add_command(label="返回主页", command=self.studentFunctionFaces)
        functionMenu.add_command(label="退出系统", command=self.studentLoginFaces)
        self.window.config(menu=menubar)

    # 交转到学生修改密码界面
    def studentChangePasswordFaces(self):
        self.studentFunctionFace.destroy()
        StudentChangePasswordFace(self.window, self.username)

    # 跳转到学生点餐界面
    def studentOrderFaces(self):
        self.studentFunctionFace.destroy()
        StudentOrderFace(self.window, self.username)

    # 跳转到学生主页
    def studentFunctionFaces(self):
        self.studentFunctionFace.destroy()
        StudentFunctionFace(self.window, self.username)

    # 跳转到登录界面
    def studentLoginFaces(self):
        self.studentFunctionFace.destroy()
        PublicLoginFace(self.window, filename_s)


# 学生修改登录密码界面
class StudentChangePasswordFace:
    def __init__(self, window, name):
        #  生成修改登录密码界面
        global username
        username = name
        self.window = window
        self.Pilimage = Image.open(r"封面.jpg")
        self.image = ImageTk.PhotoImage(image=self.Pilimage)
        self.studentChangePasswordFace = tk.Frame(self.window, width=1100, height=434, background="palegoldenrod")
        self.studentChangePasswordFace.pack()
        coverImage = tk.Label(self.studentChangePasswordFace, image=self.image)
        coverImage.place(relx=0.65, rely=0.5, anchor='center')
        titleLabel = tk.Label(self.studentChangePasswordFace, text="修改登录密码", font=('黑体', 20))
        titleLabel.place(relx=0.163, rely=0.1, anchor='center')
        studentNameLabel = tk.Label(self.studentChangePasswordFace, text="姓名", font=('楷体', 18))
        studentNameLabel.place(relx=0.04, rely=0.3, anchor='center')
        self.varStudentName = tk.StringVar()
        studentNameEntry = tk.Entry(self.studentChangePasswordFace, textvariable=self.varStudentName, show=None,
                                    font=('楷体', 18))
        studentNameEntry.place(relx=0.188, rely=0.3, anchor='center')
        oldPasswordLabel = tk.Label(self.studentChangePasswordFace, text="原密码", font=('楷体', 18))
        oldPasswordLabel.place(relx=0.04, rely=0.5, anchor='center')
        self.varOldPassword = tk.StringVar()
        oldPasswordEntry = tk.Entry(self.studentChangePasswordFace, textvariable=self.varOldPassword, show='*',
                                    font=('楷体', 18))
        oldPasswordEntry.place(relx=0.188, rely=0.5, anchor='center')
        newPasswordLabel = tk.Label(self.studentChangePasswordFace, text="新密码", font=('楷体', 18))
        newPasswordLabel.place(relx=0.04, rely=0.7, anchor='center')
        self.varNewPassword = tk.StringVar()
        newPasswordEntry = tk.Entry(self.studentChangePasswordFace, textvariable=self.varNewPassword, show='*',
                                    font=('楷体', 18))
        newPasswordEntry.place(relx=0.188, rely=0.7, anchor='center')
        confrimLabel = tk.Button(self.studentChangePasswordFace, text="确认", font=('楷体', 18),
                                 command=self.successPassword)
        confrimLabel.place(relx=0.14, rely=0.9, anchor='center')

        #  添加菜单
        menubar = tk.Menu(self.studentChangePasswordFace)
        functionMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="菜单", menu=functionMenu)
        functionMenu.add_command(label="返回主页", command=self.studentFunctionFaces)
        functionMenu.add_command(label="退出系统", command=self.studentLoginFaces)
        self.window.config(menu=menubar)

    #  修改成功并弹出提示信息
    def successPassword(self):
        studentName = self.varStudentName.get()
        oldPassword = self.varOldPassword.get()
        newPassword = self.varNewPassword.get()
        if studentName == username:
            tabel = pd.read_csv("学生登录密码.csv", dtype='str')
            file = open('学生登录密码.csv', 'w', newline='', encoding='utf8')
            header = ['序号', '姓名', '密码']
            Passwords = csv.writer(file)
            Passwords.writerow(header)
            for i in range(0, students_num):
                password = []
                if tabel.iloc[i, 1] == studentName:
                    password.append(i + 1)
                    password.append(studentName)
                    password.append(newPassword)
                    Passwords.writerow(password)
                else:
                    password.append(i + 1)
                    password.append(tabel.iloc[i, 1])
                    password.append(tabel.iloc[i, 2])
                    Passwords.writerow(password)
            tkinter.messagebox.showinfo(title="提示", message="修改成功！")
        else:
            tkinter.messagebox.showinfo(title="提示", message="输入姓名有误！")

    #  跳转到学生主页
    def studentFunctionFaces(self):
        self.studentChangePasswordFace.destroy()
        StudentFunctionFace(self.window, username)

    #  跳转到登录界面
    def studentLoginFaces(self):
        self.studentChangePasswordFace.destroy()
        PublicLoginFace(self.window, filename_s)


# 学生点餐界面
class StudentOrderFace:
    def __init__(self, window, name):
        self.window = window
        self.username = name

        self.root = tk.Toplevel(window)
        self.root.title("信息输入框")
        self.root.attributes('-topmost', True)  # 窗口置顶
        self.window.withdraw()  # 隐藏主窗口
        self.root.protocol("WM_DELETE_WINDOW", self.returnStudentFunctionFace)  # 意外关闭子窗口

        # 窗口 宽、高
        # w, h = 366, 488 - 28  # 调试后得知或自定义,按钮竖向排列（title高28不计算）
        w, h = 366, 345 - 28  # 调试后得知或自定义,按钮横向排列（title高28不计算）
        Base.centerWindow(self.window, self.root, w, h)

        self.main()

    def main(self):
        # 方法一：
        # input1 = tk.Label(self.root, text="输入姓名：").pack()
        # name_text = tk.Entry()
        # name_text.pack()

        # 方法二：
        input1 = tk.Label(self.root, text="\n输入姓名：").pack()
        name_text = tk.StringVar()
        name_text.set(self.username)
        name = tk.Entry(self.root, textvariable=name_text, justify='center').pack()

        input2 = tk.Label(self.root, text="\n输入宿舍号：").pack()
        dorm_text = tk.StringVar()
        dorm = tk.Entry(self.root, textvariable=dorm_text, justify='center').pack()

        input3 = tk.Label(self.root, text="\n\t\t正常餐(1为选择,0为不选)：\t\t      ").pack()
        normalfood_text = tk.StringVar()
        normalfood = tk.Entry(self.root, textvariable=normalfood_text, justify='center').pack()

        input4 = tk.Label(self.root, text="\n\t\t清真餐(1为选择,0为不选)：\t\t      ").pack()
        food_text = tk.StringVar()
        food = tk.Entry(self.root, textvariable=food_text, justify='center').pack()

        # 创建csv
        with open('选餐数据.csv', mode='a', newline='', encoding='utf-8') as f:
            write = csv.writer(f)

            def get_click():
                name = name_text.get()
                dorm = dorm_text.get()
                normalfood = normalfood_text.get()
                food = food_text.get()
                data = (name, dorm, normalfood, food)

                # 写入数据
                write.writerow(data)
                # 提示
                string = str("名字：%s ，宿舍号：%s ，正常餐：%s ，清真餐：%s  " % data)
                tkinter.messagebox.showinfo(title='aaa', message=string)
                print(string)
                print('成功写入csv文件！')

            # 2个按钮上下排列
            # tk.Label(self.root, text="").pack()  # 添加无描述空行
            # tk.Button(self.root, text="点击确定", command=get_click, ).pack()
            # tk.Label(self.root, text="").pack()  # 添加无描述空行
            # tk.Button(self.root, text="点击结束", command=self.returnStudentFunctionFace).pack()
            # tk.Label(self.root, text="").pack()  # 添加无描述空行

            # 2个按钮左右排列
            tk.Label(self.root, text="").pack()  # 添加无描述空行
            self.frame = tkinter.Frame(self.root)
            self.frame.pack()
            tk.Button(self.frame, text="点击确定", command=get_click).pack(side='left')
            tk.Label(self.frame, text="   ").pack(side='left')  # 添加无描述空行
            tk.Button(self.frame, text="点击结束", command=self.returnStudentFunctionFace).pack()
            # tk.Label(self.root, text="").pack()  # 添加无描述空行

            self.root.mainloop()

    # 跳转到学生主页
    def returnStudentFunctionFace(self):
        self.root.destroy()  # 销毁窗口
        self.window.deiconify()  # 显示主窗口
        StudentFunctionFace(self.window, self.username)


# 执行
if __name__ == "__main__":
    window = tk.Tk()
    Base(window)
    window.mainloop()
