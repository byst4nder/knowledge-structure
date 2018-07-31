MongoDB高级操作02-索引、账户管理、冗余、备份、恢复

1、索引：
	目的：提高查询速度。	
	步骤一：创建大量数据：
		for(i=o;i<100000;i++){
			db.ti.insert({name:'test'+i,age:i})
			注意+用法，字符串拼接。
		}

	步骤二：数据查询性能分析：
		查找姓名为“test10000”的文档
			db.t1.find({name:'test10000'})
		使用explain()命令进行查询性能分析
			db.t1.find({name:'test10000'}).explain('executionStats')

	步骤三：建立索引
		创建索引：1表示升序，-1表示降序。
		db.t1.ensureIndex({name:1})

	步骤四：对索引属性查询
		执行上面的同样的查询，并进行查询性能分析
		db.t1.find({name:'test10000'}).explain('executionStats')

	索引的命令：
		建立唯一索引，实现唯一约束的功能：
			db.t1.ensureIndex({'name':1},{'unique':true})
		联合索引：对多个属性建立一个索引，按照find()出现的顺序
			db.t1.ensureIndex({name:1,age:1})
		查看文档中所有的索引
			db.t1.getIndexes()
		删除索引：
			db.t1.dropIndexes('索引名称')


2、MongoDB账户管理
	常用系统角色如下：
		root：只在admin数据库中可用，超级账号，超级权限
		Read：允许用户读取指定数据库
		readWrite：允许用户读写指定数据库


	(1)创建超级管理用户：
		use admin
		db.createUser({
			uesr:'admin',
			pwd:'123',
			roles:[{role:'root',db:'admin'}]
		})

	(2)修改配置文件，改为授权登陆模式。
		sudo vi /etc/mongod.conf
		在security中添加：
		security:
			authorization: enabled
			注意：缩进，并且在enabled前面有个空格。
			意为：安全性上，要求：启用身份安全验证。
	(3)此时需要重新启动mongod服务。
		sudo service mongod restart
		mongo --help  # 查看登陆命令。
	(4)使用超级管理员登陆	
		mongo -u admin -p 123 --authenticationDatabase amdin
		db
		use admin
		db
		show collections
		db.system.users.find()
	（5）创建普通用户
		use py3
		db.createUser({user:'py3',pwd:'123',roles:[{role:'readWrite',db:'py3'}]})
		mongo -u py3 -p 123 --authenticationDatabase py3

	（6）修改用户：可以修改pwd、roles属性
		db.update('py3',{pwd:'456'})


3、复制（副本集）：
	复制的工作原理：
		·复制至少需要两个节点A、B...
		·A是主节点，负责处理客户端请求
		·其余的都是从节点，负责复制主节点上的数据
		·节点常见的搭配方式为：一主一从、一主多从
		·主节点记录在其上的所有操作，从节点定期轮询主节点获取这些操作，然后对自己的数据副本执行这些操作，从而保证从节点的数据与主节点一致
		·主节点与从节点进行数据交互保障数据的一致性

	复制的特点：
		·N 个节点的集群
		·任何节点可作为主节点
		·所有写入操作都在主节点上
		·自动故障转移
		·自动恢复

	设置复制节点：
		最好是在xshell中配置，因为涉及开启终端数量较多。
		step1：
			·创建数据库目录：t1、t2
			mkdir t1
			mkdir t2

		step2：
			·启动mongod服务，注意replSet的名称是一致的。两台服务器备份集一样的名称。
			mongod --bind_ip 192.168.85.20 --port 27017 --dbpath ~/Desktop/t1 --replSet rs0
			mongod --bind_ip 192.168.85.20 --port 27018 --dbpath ~/Desktop/t2 --replSet rs0
				注意修改端口递增和文件夹。

		step3：
			·连接主服务器，此处设置192.168.196.128:27017为主服务器。
			此时新开两个客户端来连接这两个服务器。
			mongo --host 192.168.196.128 --port 27017
			mongo --host 192.168.196.128 --port 27018

		step4：
			初始化，在一台上初始化，做主。
			·谁做主服务器，谁初始化：
			rs.initiate()
			在客户端3中初始化，设为主服务器。
		step5：
			·查看当前状态：
			rs.status()

		step6：
			·在主服务器上操作添加副本集：
			rs.add('192.168.85.20:27018')
		step7：
			·添加完成后，查看状态。
			rs.status()
		step8：
			·在第二个客户端终端上运行：
			rs.status()
			发现，一个是primary,一个是Secondary。
		step9：
			·向主服务器中插入数据：
			use py3
			for(i=0;i<10;i++){db.stu.insert({_id:i,name:'stu_'+i+'00',age:i})}
			db.stu.find()
		step10:
			·在从服务器上进行查询数据：
			说明：如果在从服务器上进行读操作，需要设置rs.slaveOk()
			rs.slaveOk()    # 注意此处O是大写，k是小写。
			db.stu.find()			


		step11：
			·删除从节点：
			rs.remove('192.168.85.20:27018')
			关闭主服务器后，再重新启动，会发现原来的从服务器变为了从服务器，新启动的服务器（原来的从服务器）变为了从服务器

		以上不用考虑用户身份权限登录问题：

4、备份：
	mongodump -h dbhost -d dbname -o dbdirectory
		-h：服务器地址，也可以指定端口号
		-d：需要备份的数据库名称
		-o：备份的数据存放位置，此目录中存放着备份出来的数据
			sudo mkdir test1bak
			sudo mongodump -h 192.168.196.128:27017 -d test1 -o ~/Desktop/test1bak

			但是此时需要身份验证:
			mongodupm -u admin -p 123 --authenticationDatabase admin -d admin -o bak



5、恢复
	mongorestore -h dbhost -d dbname --dir dbdirectory
		-h：服务器地址
		-d：需要恢复的数据库实例
		--dir：备份数据所在位置
	身份验证该输入还是要输入。
		mongorestore -h 192.168.128.20:27017 -u admin -p 123 --authenticationDatabase amin -d py31 --dir bak/py3
		用超级管理员账户可以完成操作。





