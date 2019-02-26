# coding=utf-8
from RedisHelper import RedisHelper
from MysqlHelper import MysqlHelper
from hashlib import sha1


'''
    首先请求redis数据库服务器，如果redis服务器中有，则直接验证;
    如果redis服务器中没有，则直接去mysql数据库中查找。
'''
# 接收输入：
name = input('请输入用户名：')
pwd1 = input("请输入密码：")

# 密码加密：
s1 = sha1()
s1.update(pwd1.encode('utf-8'))
pwd2 = s1.hexdigest()

# 先判断redis中判断是否有此用户名。

# 查询redis中是否存在此用户和密码：
r = RedisHelper()
m = MysqlHelper('192.168.85.20', 3306, 'follow', 'root', '123456')
# print(r.get('name'))


# 判断redis中是否有此用户名和密码：

if r.get(name) is None:
    print("redis数据库服务器中无此用户信息。将转至MySQL数据库中查找....")
    sql = 'select passwd from users where name=%s'
    pwd3 = m.get_one(sql, [name])
    if pwd3 is None:
        print("用户名错误")
    elif pwd3[0] == pwd2:
        print("\nMySQL数据库服务器中有此用户信息：")
        print("登陆成功1\n")
        # 如果用户在mySql中存在，则将其添加到Redis服务器中。

        # 下面这种情况：无法满足多用户情况。所以使用再下方：{name:pwd}格式。
        # r.set('name', name)
        # r.set('pwd', pwd2)

        r.set(name, pwd3[0])
        print('redis服务器已收录此用户登陆信息。')
    else:
        print("密码错误1")


else:
    print('redis服务器中有此用户信息。')
    if r.get(name).decode('utf8') == pwd2:  # 如果不加.decode('utf-8')将会输入b''格式数据。所以必须转码。
        print("登陆成功2")
    else:
        print("密码错误2")
