from threading import Thread, Lock
import time


start_time = time.time()
g_num = 0
end_time = 0


def worker1():
    global g_num
    # mutex.acquire()
    for i in range(1000000):
        mutex.acquire()
        g_num += 1
        mutex.release()
    # mutex.release()
    print("--worker1--g_num=%d" % g_num)


def worker2():
    global g_num
    global end_time
    # mutex.acquire()
    for i in range(1000000):
        mutex.acquire()
        g_num += 1
        mutex.release()
    # mutex.release()
    print("--worker2--g_num=%d" % g_num)
    end_time = time.time()
    print("运行时间：", end_time - start_time)


mutex = Lock()

t1 = Thread(target=worker1)
t1.start()

t2 = Thread(target=worker2)
t2.start()

print("---g_num=%d---" % g_num)


# ---g_num=50688---
# --worker1--g_num=1718378
# --worker2--g_num=2000000
# 运行时间： 2.1652121543884277

# 避免全局变量被修改的办法：避免多线程共享数据出错。
#     事务的原子性：要么别做，要做就做完。g_num+=1：这一步分离为两步执行：g_num = g_num + 1
#           第一步：g_num + 1  原值 加 1
#           第二步：加值后赋值！
#           在内核中运行时：第一步执行后，此时若发生内核切换任务时：赋值没有执行。
#               如果此时worker2执行，那么全局变量的值再次切换任务，加1操作被覆盖。


# 解决方案1：轮询：
#   只要条件不满足，就一直询问，直到条件满足为止。
#       时间效率不高，因为上面执行时，下面一直在等待。
#       资源效率不高，因为上面执行时，下面一直在判断，一直占用CPU。
# 解决方案2：比轮询效率更高：互斥锁。
#       当多个线程几乎同时修改某一个共享数据的时候，需要进行同步控制
#
#       线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁。
#
#       互斥锁为资源引入一个状态：锁定/非锁定。

#       被上锁的线程，不占用CPU。


# 关于互斥锁：上锁位置：能不加锁就不加锁，一旦加锁，加锁期间就不是多任务了，还是单任务。
#       所以加锁位置：
#           一次性锁定不要太大。加锁时间不要太长。
#           能不加的就不加，必须加的（多线程对同一资源进行操作时），加锁的地方要尽量小少。
# 此时耗时时间，要比放在外面用时更长久。因为每一步都要资源争夺。重新加锁解锁，都要用时。
# 并且此时第一个并非1000000。因为两个线程对锁争抢时，各有所得。此处反而放在外面更好。


# 互斥锁在锁定状态下，并非轮询。因为轮询还是会占用CPU。正确做法是：通知机制：睡眠，等通知。
