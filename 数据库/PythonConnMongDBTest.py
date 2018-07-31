# coding=utf-8
from pymongo import *


'''
    1、插入方法：
        insert_one() 传入一个字典，表示插入一个文档。
        insert_many() 传入一个列表，列表的元素为字典，插入多条文档。
'''


def insert():
    try:
        # 1)创建连接对象
        client = MongoClient(host="192.168.85.20", port=27017)
        # 或者写为：
        # 无安全认证：client=MongoClient('mongodb://192.168.85.20:27017')、
        # 有安全认证：client=MongoClient('mongodb://用户名：密码@localhost:27017/数据库名称')
        # 2 获取数据库,
        # 如果这个数据库不存在，就在内存中虚拟创建
        # 当在库里创建集合的时候，就会在物理真实创建这个数据库
        db = client.py3   # 使用py3数据库
        # 向stu集合插入数据
        # 插入一条
        db.stu.insert_one({"name": "张三丰", "age": 20})
        # 插入多条
        db.stu.insert_many([{"name": '洪七公', 'age': '66'}, {"name": '太上老君', 'age': '100000'}])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    insert()


'''
    2、查询方法：
        find_one()返回满足条件的文档集中第一条数据，类型为字典
            如果没有查询结果返回None
        find()返回满足条件的所有文档，类型为Cursor对象，可以使用for...in遍历，每项为字典对象
            如果没有查询结果返一个空的Cursor对象
'''


def select():
    try:
        # 1 创建连接对象
        client = MongoClient(host="192.168.85.20", port=27017)
        # 2 获取数据库,
        # 如果这个数据库不存在，就在内存中虚拟创建
        # 当在库里创建集合的时候，就会在物理真实创建这个数据库
        db = client.py3   # 使用test数据库
        # 从stu查询数据
        # 查询一条,返回一个字典，如果没有结果返回None
        res = db.stu.find_one({"age": 18})
        print(res)
        print('test select')
        # 查询全部结果，返回一个Cursor可迭代对象，每一个元素是字典
        # 如果没有查询结果会返回一个空的Cursor对象
        res = db.stu.find({"age": {"$gt": 18}})
        print(res)
        print('test select2')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    select()


'''
3、修改方法：
     update_one()修改满足条件的文档集中的第一条文档
     update_many()修改满足条件的文档集中的所有文档
     注意：使用$set操作符修改特定属性的值，否则会修改整个文档
'''


def update():
    try:
        # 1 创建连接对象
        client = MongoClient(host="192.168.85.20", port=27017)
        # 2 获取数据库,
        # 如果这个数据库不存在，就在内存中虚拟创建
        # 当在库里创建集合的时候，就会在物理真实创建这个数据库
        db = client.py3   # 使用py3数据库
        # 修改数据
        # 修改第一条符合条件的数据，传入条件和修改结果
        db.stu.update_one({"age": 18}, {"$set": {"age": 100}})  # 把年龄是18的第一条年龄改成100
        # 所有符合条件数据都修改
        # db.stu.update_many({"age": 18},{"$set": {"age": 100}}) # 年龄18的所有数据年龄改成100
    except Exception as e:
        print(e)


if __name__ == '__main__':
    update()


'''
4、删除方法：
    delete_one()删除满足条件的文档集中第一条文档
    delete_many()删除满足条件的所有文档
    注意：使用$set操作符修改特定属性的值，否则会修改整个文档
'''


def delete():
    try:
        # 1 创建连接对象
        client = MongoClient(host="192.168.85.20", port=27017)
        # 2 获取数据库,
        # 如果这个数据库不存在，就在内存中虚拟创建
        # 当在库里创建集合的时候，就会在物理真实创建这个数据库
        db = client.py3    # 使用py3数据库
        # 修改数据
        # 修改第一条符合条件的文档删除
        db.stu.delete_one({"age": 18})  # 把年龄是18的第一条文档删除
        # 所有符合条件数据都删除
        db.stu.delete_many({"age": 18})  # 年龄18的所有文档删除
    except Exception as e:
        print(e)


if __name__ == '__main__':
    delete()

