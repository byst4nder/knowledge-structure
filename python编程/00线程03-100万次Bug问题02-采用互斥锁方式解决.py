from threading import Thread, Lock
import time


start_time = time.time()
g_num = 0
end_time = 0


def worker1():
    global g_num
    # 这个线程和worker2线程都在抢着对这个锁进行上锁。
    # 如果有一方成功的上锁，那么导致另外一方会堵塞（一直等待）到这个锁被解开为止。
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()   # 用来对mutex指向的这个锁，进行解锁。
    # 只要开了锁，那么接下来，会让所有因为这个锁被上锁而堵塞的其他线程进行争抢。
    # 上了锁，就可以保证其他线程不占用CPU。
    print("--worker1--g_num=%d" % g_num)


def worker2():
    global g_num
    global end_time
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()
    print("--worker2--g_num=%d" % g_num)
    end_time = time.time()
    print("运行时间：", end_time - start_time)


# 创建一把互斥锁，这个锁默认是没有上锁的。
mutex = Lock()

t1 = Thread(target=worker1)
t1.start()

# time.sleep(2)  # 开关1：取消屏蔽之后 再次运行程序，结果会不一样，，，为啥呢？

t2 = Thread(target=worker2)
t2.start()
# time.sleep(3)   # 开关2：取消屏蔽之后 再次运行程序，结果会不一样，，，为啥呢？
print("---g_num=%d---" % g_num)


# ---g_num=220883---
# --worker1--g_num=1000000
# --worker2--g_num=2000000
# 运行时间： 0.1685490608215332

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
