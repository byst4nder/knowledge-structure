mySQL数据库

工具拓展人脑的功能。
	随着数据量的越来越大，记录（存储并查找）数据的方式和工具不断完善和创新。方便存储和快速查找大量数据的工具：数据库。


1、基本认识和简介：

	关系型数据库设计模型：
		E-R设计模型结构。

	数据的3范式：
		三个规则。

	数据字段的类型：
		变量类型：
	
	字段约束：
		系统自动检查。

	主要操作：
		·数据库的操作：	增、删
		·表的操作：		增、删、改
		·数据库的操作： 	增、删、改、查。简称：crud(creat,read,update,delet)


	数据库分类：
		·文档型：sqlite 			就是一个文件：复制文件完成数据的复制。手机上大多是这种。
		·服务型：mySQL和postgre	存储在物理文件中。需要使用 C/S终端 以tcp/ip协议连接，进行数据库的读写操作。


	E-R模型：
		E表示entry： 		实体。	一个 实体 转换为数据库的一个表。
		R表示relationship 	关系。 	
			关系描述两个实体之间的对应规则，包括
				· 一对一
				· 一对多
				· 多对多
			关系 转换为数据库表中的一个 列 *在关系型数据库中一 行 就是一个 对象
		设计一个数据库，首先要分析出E-R。
			实体是什么？
			有哪些属性？
			比如学生数据库：
				姓名：
				年龄：
				生日：

	三范式：
		·第一范式（1NF）：	列不可拆分：		列是属性。属性不能再拆分了。比如姓名，普通学生系统可以了，但是公安系统却需要把姓和名分开。生产日期。原则够用就行了。
		·第二范式（2NF）：	唯一标识：		可以通过一个属性，唯一的找到一个对象。	
		·第三范式（3NF）： 	引用主键： 		关系，引用的时候只能引用标识。


	数据库工作流程：
		实际开发之前，要先去产品经理去沟通：明白他要做什么。把需要操作的规范化持久化数据提取出来。
		设计实体：就是表。并建立实体之间的关系。然后转化为表。
		然后再用python去编程，实现crud。


2、安装数据库：
	安装：
		sudo apt-get install mysql-server mysql-client
	启动：
		service mysql start
	停止：
		service mysql stop
	重启：
		service mysql restart

	允许远程连接：
	找到mysql配置文件并修改：
		sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
		将bind-address=127.0.0.1注释

	登录mysql，运行命令：
		grant all privileges on *.* to 'root'@'%' identified by 'mysql' with grant option;
		flush privileges;

	重启mysql：
	    service mysql restart


3、数据完整性：
	为保障数据正确有效，数据库增加一些验证功能：
		·数据字段类型：
			·数字：int、decimal(小数)decimal(5,2):一共五位，小数两位。
			·字符串：char定长、varchar不定长、test
			·日期：datetime
			·布尔：bit
		·约束：
			·主键primary key
			·非空not null
			·唯一unique
			·默认default
			·外键foreign key


4、图形界面操作：
	有经验的研发，会在新建数据库的时候 预留 几个栏位prop1。防止产品经理后期改动。
	默认四个系统数据库
	新建数据库：python3:
		字符集：utf-8
		数据库中把属性叫字段：
			一个实体对应一个表：
			一个属性对应一个字段：



5、逻辑删除
	·对于重要数据，并不希望物理删除，一旦删除，数据无法找回
	·一般对于重要数据，会设置一个isDelete的列，类型为bit，表示逻辑删除
	·大于大量增长的非重要数据，可以进行物理删除
	·数据的重要性，要根据实际开发决定
	删除数据一定要慎重。

	做法：
	新增一个栏位：用于标记是否删除，如果删除了，就显示为1.否则为0或者相反。
		isDelete的列，类型为bit，表示逻辑删除.逻辑上完成了删除，实际上还在，只是不再显示。非常巧妙。

6、命令脚本操作

	mysql --help查找命令。

	远程连接：mysql -hip地址 -uroot -p

	
	(1)数据库操作：
		创建数据库：
			create database 数据库名 charset=utf8;

		删除数据库
			drop database 数据库名;

		切换数据库
			use 数据库名;
		
		查看当前选择的数据库
			select database();
			show databases;


	(2)表操作：
		
		查看当前数据库中所有表
			show tables;

		创建表
			auto_increment表示自动增长
			create table 表名(列及类型);
			如：
				create table students(
				id int auto_increment primary key,
				sname varchar(10) not null
				);
		修改表
			alter table 表名 add|change|drop 列名 类型;
			如：
			alter table students add birthday datetime;
		
		删除表
			drop table 表名;
		
		查看表结构
			desc 表名;
		
		更改表名称
			rename table 原表名 to 新表名;
		
		查看表的创建语句
			show create table '表名';

	（3）数据操作：

		查询
			select * from 表名
		
		增加	
		全列插入：
			insert into 表名 values(...)
		缺省插入：
			insert into 表名(列1,...) values(值1,...)
		同时插入多条数据：
			insert into 表名 values(...),(...)...;
		或 insert into 表名(列1,...) values(值1,...),(值1,...)...;
		主键列是自动增长，但是在全列插入时需要占位，通常使用0，插入成功后以实际数据为准
		
		修改
			update 表名 set 列1=值1,... where 条件
		
		删除
			delete from 表名 where 条件
			
			逻辑删除，本质就是修改操作update
				alter table students add isdelete bit default 0;
		如果需要删除则
			update students  set isdelete=1 where ...;

	(4)数据库备份与恢复
		迁移工作：

		数据备份：

			进入超级管理员
				sudo -s
			
			进入mysql库目录
				cd /var/lib/mysql
			
			运行mysqldump命令
				mysqldump –uroot –p 数据库名 > ~/Desktop/备份文件.sql;
			按提示输入mysql的密码
				合成数据库文件：然后通过scp发送到服务器。
				scp 备份文件.sql root@192.168.85.10:`~`

		数据恢复:

			连接mysqk，创建数据库:
				最好是与原库相关。比如还叫follow.

			退出连接，执行如下命令

			mysql -uroot –p 数据库名 < ~/Desktop/备份文件.sql
			根据提示输入mysql密码。完成导入数据库操作。
				大于小于号完成指向功能。







