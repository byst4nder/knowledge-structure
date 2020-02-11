# coding=utf-8
import threading
import time


class MyThread1(threading.Thread):
    def run(self):
        if mutexA.acquire():
            print(self.name+'----do1---up----')
            time.sleep(1)

            if mutexB.acquire():
                print(self.name+'----do1---down----')
                mutexB.release()
            mutexA.release()


class MyThread2(threading.Thread):
    def run(self):
        if mutexB.acquire():
            print(self.name+'----do2---up----')
            time.sleep(1)
            if mutexA.acquire(False):
                print(self.name+'----do2---down----')
                mutexA.release()
            mutexB.release()


if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    mutexA = threading.Lock()
    mutexB = threading.Lock()
    t1.start()
    t2.start()

# 彼此不释放，彼此互相请求。形成死锁。
# 解决方案：
#      1、设计阶段避免互相请求
#      2、添加超时时间：在mutex.acquire([bool]),如果超时放开。
#            如何保证程序的运行！
#               看门狗思路：
#                   隔一段时间喂狗，超时时间。如果不喂， 那么狗就重新把程序重启一遍。保证运行。
#                   隔开一段时间，给变量加一个值，如果没有加，那么把程序重新运行一遍。
#      3、银行家算法：
#           1、以目前手中拥有的资源，尽量满足当前已经投资的且最低期望的进程，
#           2、完成该进程后，回收资源，此时手中的资源增多了，再去满足下一个最低期望的进程，
#           3、直到所有的进程均满足，且完成。
#       哲学思路：立即行动，立即完成当前最低消耗的事务。然后收拢投入，获取回报。再进行更大的投入。
#           在哲学上：与立即完成最重要的事情并不矛盾。



