from multiprocessing import Pool
import time
import os


def test():
    print("----进程池中的进程---pid=%d, ppid=%d---" % (os.getpid(), os.getppid()))
    for i in range(3):
        print("---%d---" % i)
        time.sleep(1)
    return "return返回值哈哈哈"


def test2(args):
    print("---callback func---pid=%d" % os.getpid())
    print("---callback func---args=%s" % args)


def main():
    pool = Pool(3)
    pool.apply_async(func=test, callback=test2)

    while True:
        time.sleep(1)
        print("---主进程--pid=%d----" % os.getpid())


if __name__ == '__main__':
    main()

# 正干着一件事，突然让你干另外一件事。
