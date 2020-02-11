from threading import Thread
import time


g_num = 0
g_flag = 1  # flag标记方法。


def worker1():
    global g_num
    global g_flag
    if g_flag == 1:
        for i in range(1000000):
            g_num += 1
        g_flag = 0
    print("--worker1--g_num=%d" % g_num)


def worker2():
    global g_num
    # 轮询：永无休止的判断某个条件是否满足。
    while True:
        if g_flag != 1:
            for i in range(1000000):
                g_num += 1
            break
    print("--worker2--g_num=%d" % g_num)


t1 = Thread(target=worker1)
t1.start()

# time.sleep(2)  # 开关1：取消屏蔽之后 再次运行程序，结果会不一样，，，为啥呢？

t2 = Thread(target=worker2)
t2.start()
# time.sleep(3)   # 开关2：取消屏蔽之后 再次运行程序，结果会不一样，，，为啥呢？
print("---g_num=%d---" % g_num)


# ---g_num=193847---
# --worker1--g_num=1046295
# --worker2--g_num=1186594

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
