# coding=utf-8
# from 01-mySQL数据库-04python连接mysql02封装模块 import MysqlHelper
import mysqlhelper


# name = input("请输入学生姓名：")
# id = input("请输入学生编号：")

# 修改
# sql = 'update students set name=%s where id=%s'
# 增加
# sql = 'insert into students(name,id) values(%s, %s)'
# 查询
sql = 'select * from students where id < 20'
# params = [name, id]   # 以列表形式封装。
sqlhelper = mysqlhelper.MysqlHelper('192.168.85.20', 3306, 'follow', 'root', '123456', 'utf8')
# sqlhelper.curd(sql, params)
result = sqlhelper.get_all(sql)
print(result)
