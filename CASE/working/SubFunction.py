import time
import multiprocessing

"""装饰器调用及使用用法：
from working.SubFunction import clock
"""


def clock(func):
    @run
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("...Begin...")
        result = func(*args, **kwargs)
        end_time = time.time()
        print("...Finish...")
        # print("共耗时：%s秒" % round(end_time - start_time, 2))
        print("共耗时：%s秒" % (end_time - start_time))
        return result

    return wrapper


def run(func):
    def wrapper(*args, **kwargs):
        running_process = multiprocessing.Process(target=running)
        running_process.daemon = True  # 方法一：开始前设置守护主进程
        running_process.start()
        result = func(*args, **kwargs)
        # running_process.terminate()  # 方法二：结束时手动结束子进程
        return result

    return wrapper


def running():
    while True:
        print('...running...')
        time.sleep(0.1)


""" 如下是按类书写，功能同上 """


class SubFunction(object):

    def clock(self, func):
        @SubFunction().run
        def wrapper(*args, **kwargs):
            start_time = time.time()
            print("...Begin...")
            result = func(*args, **kwargs)
            end_time = time.time()
            print("...Finish...")
            # print("共耗时：%s秒" % round(end_time - start_time, 2))
            print("共耗时：%s秒" % (end_time - start_time))
            return result

        return wrapper

    def run(self, func):
        def wrapper(*args, **kwargs):
            running_process = multiprocessing.Process(target=self.running)
            running_process.daemon = True  # 方法一：开始前设置守护主进程
            running_process.start()
            result = func(*args, **kwargs)
            # running_process.terminate()  # 方法二：结束时手动结束子进程
            return result

        return wrapper

    def running(self):
        while True:
            print('...running...')
            time.sleep(0.1)


if __name__ == '__main__':
    pass
