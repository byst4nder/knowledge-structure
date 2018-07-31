MongoDB与python交互

一、概括认识

	https://blog.csdn.net/qq_15058425/article/details/79516195
	
	解决pycharm无法连接Ubuntu下mongodb服务的问题：
		在配置文件/etc/mongod.conf中，
		将bind_ip=127.0.0.1修改为0.0.0.0意为，对ip地址不做限制。或者注释掉。
	
	http://api.mongodb.com/python/current/tutorial.html官方网站。

	https://blog.csdn.net/kun1280437633/article/details/80512223
	步骤：
	1、引入包：pymongo

	2、MongoClient对象：用于与MongoDB服务器建立连接
		client=MongoClient('主机ip',端口)

	3、DataBase对象：对应着MongoDB中的数据库
		db=client.数据库名称

	4、Collection对象：对应着MongoDB中的集合
		col=db.集合名称

	5、Cursor对象：查询方法find()返回的对象，用于进行多行数据的遍历
		当调用集合对象的find()方法时，会返回Cursor对象
		结合for...in...遍历cursor对象


	主要方法:
		insert_one：加入一条文档对象
		insert_many：加入多条文档对象
		find_one：查找一条文档对象
		find：查找多条文档对象
		update_one：更新一条文档对象
		update_many：更新多条文档对象
		delete_one：删除一条文档对象
		delete_many：删除多条文档对象

二、方法实现。
	1、插入方法：
	    insert_one() 传入一个字典，表示插入一个文档。
	    insert_many() 传入一个列表，列表的元素为字典，插入多条文档。

    2、查询方法：
        find_one()返回满足条件的文档集中第一条数据，类型为字典
            如果没有查询结果返回None
        find()返回满足条件的所有文档，类型为Cursor对象，可以使用for...in遍历，每项为字典对象
            如果没有查询结果返一个空的Cursor对象

        cursor = stu.find({'age':{'$gt':20}}).sort({'_id','DESCENDING'}).skip(1).limit(1)
        for s in cursor:
        	print(s)
        排序：返回Cursor类型的对象
        	升序使用ASCENDING,降序使用DESCENDING:

    3、修改方法：
	     update_one()修改满足条件的文档集中的第一条文档
	     update_many()修改满足条件的文档集中的所有文档
	     注意：使用$set操作符修改特定属性的值，否则会修改整个文档

	4、删除方法：
	    delete_one()删除满足条件的文档集中第一条文档
	    delete_many()删除满足条件的所有文档
	    注意：使用$set操作符修改特定属性的值，否则会修改整个文档

    