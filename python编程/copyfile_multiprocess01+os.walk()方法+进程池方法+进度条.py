import os
import time
import shutil
from multiprocessing import Pool, Manager


from_dir = "./edges2handbags/"
to_dir = "../copyFolderTest01/"
if not os.path.exists(to_dir):
    os.mkdir(to_dir)
# os.sep = "\\"


def my_copy_file(src, dst, queue):
    shutil.copy(src, dst)
    queue.put(src)


def main():
    start_time = time.time()
    num = 0
    pool = Pool(5)
    queue = Manager().Queue()
    file_total = 0
    for root, dirs, files in os.walk(from_dir):
        for dir_ in dirs:
            child_folder_source = os.path.join(root, dir_)
            print(child_folder_source)
            file_num = len(os.listdir(child_folder_source))
            print(file_num)
            suffix_dir = child_folder_source[len(from_dir):]   # 如果不加1那么会出现\路径情况
            child_folder_aim = os.path.join(to_dir, suffix_dir)
            if not os.path.exists(child_folder_aim):
                os.mkdir(child_folder_aim)
            file_total += file_num
        print(file_total)
        for file in files:
            src = os.path.join(root, file)
            # 处理方式一：4通过len(source_dir.split(os.sep)) 来动态获取。普适性更好。
            # dst = os.path.join(to_dir, os.sep.join(src.split(os.sep)[4:]))
            # 处理方式二：22可以通过len(source_dir)+1。
            dst = os.path.join(to_dir, src[len(from_dir):])
            # num += 1
            # print(num)
            # print(dst)
            pool.apply_async(my_copy_file, args=(src, dst, queue))

    while num < file_total:
        queue.get()
        num += 1
        copyRate = num/file_total
        print("\rcopy的进度是：%.2f%%" % (copyRate*100), end="")

    end_time = time.time()
    print("\n运行时间：%d s" % (end_time - start_time))  # Pool(5)=453s,


if __name__ == '__main__':
    main()

# 运行时间：801 s
#
# 因为写文件的瓶颈在磁盘IO，不在CPU，你并行了有毛用……
# #
# # 机械硬盘的悬臂寻址，你并行越多寻址次数越多，性能反而成指数级下降
# # CPU大概比二级缓存快1个数量级，二级缓存大概比内存快1-2个数量级，内存大概比硬盘（极限速度）快2个数量级，而机械硬盘的磁头寻址大概是ms级，磁头寻址一次，CPU能跑大约百万条指令
# #
# # 换句话说，胡乱并行机械硬盘的I/O，多一次磁头寻址，意味着浪费了百万条CPU指令时间
