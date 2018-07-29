# coding=utf-8
import mysqlhelper
import hashlib


# 接收用户输入：
name = input("请输入用户名：")
pwd = input('请输入密码：')

# 对密码加密：
s1 = hashlib.sha1()
s1.update(pwd.encode('utf-8'))
pwd2 = s1.hexdigest()


# 根据用户名查询密码：
sql = 'select passwd from users where name=%s'
helper = mysqlhelper.MysqlHelper('192.168.85.20', 3306, 'follow', 'root', '123456')
result = helper.get_all(sql, [name])
if len(result) == 0:
    print("用户名错误。")
elif result[0][0] == pwd2:
    print("登录成功。")
else:
    print("密码错误。")
# print(result)



