import frida
import sys
import queue
import threading
import requests
from urllib import parse


class Producer(threading.Thread):
    def __init__(self, baoming):
        threading.Thread.__init__(self)
        self.baoming = baoming

    def run(self):
        process = frida.get_remote_device().attach(self.baoming)
        script = process.create_script(jscode)
        script.on("message", message)
        script.load()
        sys.stdin.read()


class Consumer(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        global sums
        while True:
            try:
                sign = self.q.get(timeout=10)
            except:
                break
            nid, sign = sign.split(':')
            while True:
                try:
                    response = requests.get(
                        'https://sekiro.virjar.com/yuanrenxue/query?id=' + nid + '&sign=' + parse.quote(sign)).json()
                    break
                except:
                    pass
            print(nid)
            print(response)
            sums += response['data']


sums = 0
workqueue = queue.Queue(maxsize=0)

jscode = """
Java.perform(function () {
    var OnlineJudgeApp = Java.use('com.yuanrenxue.onlinejudge2020.OnlineJudgeApp');
    OnlineJudgeApp.getSign.implementation = function (j){
        console.log('HOOK 开始');
        for (i = 0; i < 100; i++){
            var sign = this.getSign(i);
            send(i+':'+sign);
        }
        console.log('HOOK 结束');
        return this.getSign(j);;
    };
});
"""


def message(message, data):
    global i
    global workqueue
    if message["type"] == 'send':
        sign = message['payload']
        workqueue.put(sign)
    else:
        print(message['stack'])


def main():
    global workqueue
    global sums
    # 创建线程列表
    threads = []

    # 创建新线程，并开始线程
    for eachthread in range(0, 32):
        thread = Consumer(workqueue)
        thread.start()
        threads.append(thread)

    baoming = 'com.yuanrenxue.onlinejudge2020'
    thread = Producer(baoming)
    thread.start()

    # 等待所有线程结束
    for t in threads:
        t.join()

    print(sums)
    # 总和：4925000


if __name__ == '__main__':
    main()
