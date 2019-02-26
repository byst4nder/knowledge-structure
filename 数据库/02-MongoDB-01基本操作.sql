MongoDB

1、NoSQL简介：

	Not Only SQL：非关系型数据库。设计结构不同。没有统一的结构，不再维护关系。数据处理效果更强一些。
	在mySQL中为了提高查询速度，我们可以创建索引。
	但是如果数据量非常大的时候，有很多人的时候，仅仅索引的优化远远不够，所以提出了内存级的数据读写数据库。不需要维护关系。
	`最大的优化就在内存级的读写。`


	分类：
		列存储：			Hbase
		文档存储：		MongoDB
		key-value存储：	redis
		图存储：			Neo4j
		对象存储：		db4o、Versant
		xml数据库：		BaseX
	Nosql的目的就是提高检索速度。


2、MongoDB简介：
	分布式 文件存储的NoSQL数据库。物理加内存两个级别的。
	C++编写。运行稳定，性能高。

	我们在访问网站页面时，打开页面的上的所有信息。HTML,图片，音频css
		html决定了页面的布局。css决定了她的样式。图片填充，js实现动态效果。剩下的是更新请求数据。


	三元素：数据库，集合，文档
		集合就是关系数据库中的表
		文档对应着关系数据库中的行
	文档，就是一个对象，由键值对构成，是json的扩展Bson形式
		{'name':'guojing','gender':'男'}
	集合：类似于关系数据库中的表，储存多个文档，结构不固定，如可以存储如下文档在一个集合中
		{'name':'guojing','gender':'男'}
		{'name':'huangrong','age':18}
		{'book':'shuihuzhuan','heros':'108'}
	数据库：是一个集合的物理容器，一个数据库中可以包含多个文档
	一个服务器通常有多个数据库。


3、安装MongoDB：
	下载mongodb的版本，两点注意
		·根据业界规则，偶数为稳定版，如1.6.X，奇数为开发版，如1.7.X
		·32bit的mongodb最大只能存放2G的数据，64bit就没有限制
	安装指南：

	1.导入软件源的公钥
		sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
	2.为mongodb创建软件源list文件 
		ubuntu12.04
		echo "deb http://repo.mongodb.org/apt/ubuntu precise/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
	
		ubuntu14.04
		echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
	
		ubuntu16.04
		echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
	
	3.更新软件源并安装mongodb

		sudo apt-get update
		sudo apt-get install -y mongodb-org
	4.配置启动文件 
		如果是ubuntu16.04的版本，需要手动新建/lib/systemd/system/mongod.service文件，并写入下面内容：
			[Unit]
			Description=High-performance, schema-free document-oriented database
			After=network.target
			Documentation=https://docs.mongodb.org/manual

			[Service]
			User=mongodb
			Group=mongodb
			ExecStart=/usr/bin/mongod --quiet --config /etc/mongod.conf

			[Install]
			WantedBy=multi-user.target
	5.启动、重启和关闭命令
		sudo service mongod start
		sudo service mongod restart
		sudo service mongod stop

	6.mongodb的完全卸载 
		先停止运行mongodb：
			sudo service mongod stop
		再卸载软件：
			sudo apt-get purge mongodb-org*
		删除数据库和日志文件：
			sudo rm -r /var/log/mongodb
			sudo rm -r /var/lib/mongodb

4、连接：
	服务端的叫：mongod
	客户端的叫：mongo
		sudo service mongod restart
		mongo
	默认连接的是test的数据库：
		db 查看当前数据名称
		db.stats() 查看当前数据信息。
	exit退出，或者ctrl + c

5、mongodb的图形界面：
	
	GUI：robomongo，解压后在bin目录下找到运行程序
	直接在bin下将文件打开，【create】 【save】【connnect】
	
	看到的数据库，到命令行中查看
		show dbs       <<<=======
		查看是否真的存在。
	
	如果本地连接失败：检查vmware workstations中，网络虚拟编辑器的NAT设置。
		

6、数据库操作：
	切换数据库
	如果数据库不存在，则指向数据库，但不创建，直到插入数据或创建集合时数据库才被创建
		use 数据库名称  		<<<=======
	默认连接的是test的数据库：为test，如果你没有创建新的数据库，集合将存放在test数据库中。

	数据库删除：
		删除当前指向的数据库
		如果数据库不存在，则什么也不做
		db.dropDatabase()		<<<=======

7、集合操作：
	集合创建：
		db.createCollection(name,options)		<<<=======
	·name是要创建的集合的名称
	·options是一个文档，用于指定集合的配置
	·选项​​参数是可选的，所以只需要到指定的集合名称。以下是可以使用的选项列表：
		db.createCollection("sub", { capped : true, size : 10 } )		<<<=======
			参数capped：默认值为false表示不设置上限，值为true表示设置上限
			参数size：当capped值为true时，需要指定此参数，表示上限大小，当文档达到上限时，会将之前的数据覆盖，单位为字节
	删除集合：
		db.集合名.drop()			<<<=======

8、数据类型：

	object ID：文档ID 			<<<=======
	每个文档都有一个属性，为_id，保证每个文档的唯一性
	Object ID：文档ID 			<<<=======
	String：字符串，最常用，必须是有效的UTF-8
	Boolean：存储一个布尔值，true或false 		<<<=======
	Integer：整数可以是32位或64位，这取决于服务器
	Double：存储浮点值
	Arrays：数组或列表，多个值存储到一个键
	Object：用于嵌入式的文档，即一个值为一个文档
	Null：存储Null值
	Timestamp：时间戳
	Date：存储当前日期或时间的UNIX时间格式


9、数据操作：
	插入：
		db.集合名称.insert(document) 		<<<=======
		·插入文档时，如果不指定_id参数，MongoDB会为文档分配一个唯一的ObjectId
		·而且如果集合不存在则自动创建一个集合。不需要事先存在集合。
			db.stu.insert({name:'gj',gender:1})
		简单查询：
			db.stu.find()

	修改：
		db.集合名称.update(
		   <query>,
		   <update>,
		   {multi: <boolean>}
		)	

		参数query:查询条件，类似sql语句update中where部分。可以为空{}，但不能不写。
		参数update:更新操作符，类似sql语句update中set部分。
		参数multi:可选，默认是false，表示只更新找到的第一条记录，值为true表示把满足条件的文档全部更新。
		为了测试先多加一条数据：
			db.stu.insert({name:'hurong',age:18})
			db.stu.update({},{name:'guojing1'})
			默认第一个筛选条件都没有写，应该所有匹配的都改，但是第三个参数为默认，所以只修改了第一条记录。
			如果想修改多条，只要把第三个参数修改即可。同时需要用 `$set` 指定属性更新。如果不加则是全文档修改，
			导致文档结构也被修改。
			注意：`$set`后面用的是冒号： `:`

	保存：
		db.集合名称.save(document)
			如果文档存在则修改，如果文档则添加。


	删除：
		db.集合名称.remove(
		   <query>,
		   {
		     justOne: <boolean>
		   }
		)
		·参数query:可选，删除的文档的条件
		·参数justOne:可选，如果设为true或1，则只删除一条，默认false，表示删除多条。
			db.stu.remove({gender:0},{justOne:true})
		全部删除
			db.stu.remove({})

	Size：
		大小限制规定。
			当数据量大小超过多少时，会覆盖之前的数据。
			db.createCollection('sub',{capped:true,size:10})
			





