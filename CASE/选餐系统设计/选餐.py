import csv
import tkinter as tk
import tkinter.messagebox


class chooseMeal:
    def __init__(self, window, name):
        self.root = window
        self.username = name
        self.root.title("信息输入框")

        # 获取屏幕 宽、高
        ws = self.root.winfo_screenwidth()  # 1920
        hs = self.root.winfo_screenheight()  # 1080
        # 获取窗口 宽、高
        # w, h = 366, 488 - 28  # 调试后得知或自定义,按钮竖向排列（title高28不计算）
        w, h = 366, 345 - 28  # 调试后得知或自定义,按钮横向排列（title高28不计算）
        # 计算 x, y 位置
        x = (ws / 2) - (w / 2)  # 左右1:1
        y = (hs / 4) - (h / 4)  # 上下1:3
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # 用于调试测量窗口大小
        # self.root.after(0, self.root.update())
        # w = self.root.winfo_width()
        # h = self.root.winfo_height()
        # print(w, h)

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
            # tk.Button(self.root, text="点击确定", command=get_click).pack()
            # tk.Label(self.root, text="").pack()  # 添加无描述空行
            # tk.Button(self.root, text="点击结束", command=exit).pack()
            # tk.Label(self.root, text="\n").pack()  # 添加无描述空行

            # 2个按钮左右排列
            tk.Label(self.root, text="").pack()  # 添加无描述空行
            self.frame = tkinter.Frame(self.root)
            self.frame.pack()
            tk.Button(self.frame, text="点击确定", command=get_click).pack(side='left')
            tk.Label(self.frame, text="   ").pack(side='left')  # 添加无描述空行
            tk.Button(self.frame, text="点击结束", command=exit).pack(side='left')
            tk.Label(self.root, text="").pack()  # 添加无描述空行

            self.root.mainloop()


if __name__ == '__main__':
    window = tk.Tk()
    name = '1'
    chooseMeal(window, name)
