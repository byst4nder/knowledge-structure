# 第一种方式：csv文件，建立行列关键词。一个文件保存，太大，不建议。https://www.cnblogs.com/xiaozi/p/10488653.html
# 第二种方式：直接写无格式文件。来尝试。f.open() python 写入中文文本文件。
# 关于数据格式问题，选择字典dict方式考虑最合适。


# 第一种情况：
# f = open("中文输入测试", "rt", encoding="utf-8")
# data = f.read()
# # print(data)
# f.close()


# 第二种情况：
# with open("中文输入测试", "rt", encoding="utf-8") as f:
#     # 新读法：
#     for line in f:
#         print(line)
#     # 老读法：
#     data = f.read()
#     print(data)

# 写入文件：
# with open("写入文件", "wt", encoding="utf-8", newline="\n") as f:
#     f.write("写入测试\n")
#     f.write("空格测试\n")
#     f.writelines("中文写入测试\n")
#     f.writelines("李四\n")
#     f.writelines("女\n")
#     f.writelines("18\n")

# 考虑字典的最佳保存方式：
import json
dict_info = {"basic_info": {"Name": "张三", "Age": 19, "Sex": "男"}, "bg_info": {"Home": "北京", "Blood": "", }}

# 写入方式一：
# jsonData = json.dumps(dict_info)
# with open("写入json测试.json", "wt", encoding="utf-8") as f:
#     f.write(jsonData)

# 写入方式二：这种写法最漂亮。
# with open("写入json测试.json", "wt", encoding="utf-8") as f:
#     json.dump(dict_info, f, ensure_ascii=False, indent=4)

# json中文显示的问题:  通过：ensure_ascii=False,来解决。
# https://blog.csdn.net/weixin_44731100/article/details/90903110

# https://www.cnblogs.com/XhyTechnologyShare/p/12033690.html
# 读取一下json文件：
with open("写入json测试.json", "rt", encoding="utf-8") as fr:
    data = json.load(fr)
print(data)


# python 结构体的方式来保存数据。https://www.cnblogs.com/nyist-xsk/p/10470527.html
class Myclass(object):
    class Struct(object):
        def __init__(self, name, age, job):
            self.name = name
            self.age = age
            self.job = job

    def make_struct(self, name, age, job):
        return self.Struct(name, age, job)


myclass = Myclass()
test1 = myclass.make_struct('xsk', '22', 'abc')
test2 = myclass.make_struct('mtt', '23', 'def')

print(test1.name)
print(test1.job)
print(test1.job)
print(test2.name)
print(test2.age)
print(test2.job)
