# 0、正常copy方法。1、多进程测试。
import os
import time
import shutil


from_dir = "./edges2handbags/"
to_dir = "../copyFolderTest00/"
if not os.path.exists(to_dir):
    os.mkdir(to_dir)
# os.sep = "\\"


def main():
    start_time = time.time()
    num = 0
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
            shutil.copy(src, dst)
            num += 1
            copyRate = num/file_total
            print("\rcopy的进度是：%.2f%%" % (copyRate*100), end="")

    end_time = time.time()
    print("\n运行时间：%d s" % (end_time - start_time))


if __name__ == '__main__':
    main()
# 运行时间：811 s
