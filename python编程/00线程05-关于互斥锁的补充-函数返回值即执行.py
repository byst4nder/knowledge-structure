from threading import Thread, Lock


mutex = Lock()
print(mutex.acquire())    # acquire()，命令是触发式，只要请求就激活锁。此时返回True。
# print(mutex.acquire())  # 第二次将不再执行。除非收到release()释放信号。
mutex.release()    # 释放。如果不释放，下面的语句还是无法通过，释放后，判断语句，此时重新加锁。
if mutex.acquire():
    print("text")
print(mutex.acquire())      # 在判断句中就触发了，不释放，此举无法执行，死锁。
