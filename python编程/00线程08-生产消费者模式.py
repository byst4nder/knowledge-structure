# 当有速度不匹配时，爬虫爬取和存储速度不匹配。生产和消费不匹配就会出现浪费堆积或者不足现象。
# 此时需要在生产者和消费者之间架设一个缓冲区域，管道。缓冲容器足够大。

# FIFO和FILO:first in first out,first in last out.队列和栈
# 数据生产     数据处理

# encoding=utf-8
import threading
import time

# python2中
# from Queue import Queue

# python3中
from queue import Queue
# 此处Queue与mutilprocess中的Queue不是同一个。


class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0   # 非全局
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = self.name + '生成产品' + str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + '消费了 '+queue.get()
                    print(msg)
            time.sleep(1)


if __name__ == '__main__':
    queue = Queue()

    for i in range(500):
        queue.put('初始产品'+str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()
# 最重要的是处理问题的模式：
#     这个阻塞队列就是用来给生产者和消费者解耦的。
#     纵观大多数设计模式，都会找一个第三者出来进行解耦。
