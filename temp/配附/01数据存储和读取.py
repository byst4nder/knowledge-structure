# 第一种方式：csv文件，建立行列关键词。一个文件保存，太大，不建议。https://www.cnblogs.com/xiaozi/p/10488653.html
# 直接写无格式文件。来尝试。
# f.open() python 写入中文文本文件。

# 第一种情况：
f = open("中文输入测试", "rt", encoding="utf-8")
data = f.read()
# print(data)
f.close()


# 第二种情况：
with open("中文输入测试", "rt", encoding="utf-8") as f:
    # 新读法：
    for line in f:
        print(line)
    # 老读法：
    # data = f.read()
    # print(data)

# 写入文件：
with open("写入文件", "wt", encoding="utf-8", newline="\n") as f:
    f.write("写入测试\n")
    f.write("空格测试\n")
    f.writelines("中文写入测试\n")
    f.writelines("李四\n")
    f.writelines("女\n")
    f.writelines("18\n")

