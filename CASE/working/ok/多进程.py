from multiprocessing import Process


# 方法一，推荐
class MyProcess(Process):
    def run(self):
        for i in range(100):
            print('子进程', i)


if __name__ == '__main__':
    t = MyProcess()
    t.start()
    for i in range(100):
        print('主进程', i)

# 方法二
# def func():
#     for i in range(100):
#         print('func', i)
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()
#     for i in range(100):
#         print('main', i)
