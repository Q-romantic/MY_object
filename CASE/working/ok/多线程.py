from threading import Thread


# 方法一，推荐
class MyThread(Thread):
    def __init__(self, a, b):
        Thread.__init__(self)
        self.a = a
        self.b = b
    def run(self):
        for i in range(10):
            print('子线程', self.a, self.b, i)


if __name__ == '__main__':
    t1 = MyThread('a', 'b')
    t1.start()
    t2 = MyThread('c', 'd')
    t2.start()
    for i in range(10):
        print('主线程', i)

# 方法二
# def func1(name):
#     for i in range(10):
#         print(name, i)
# def func2(name1, name2):
#     for i in range(10):
#         print(name1, name2, i)
#
# if __name__ == '__main__':
#     t1 = Thread(target=func1, args=('abc',))  # 带一个参数，均以元祖传参
#     t1.start()
#     t2 = Thread(target=func2, args=('aaa', 'bbb'))    # 带多个参数
#     t2.start()
#     for i in range(10):
#         print('main', i)
