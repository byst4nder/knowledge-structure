Python与MySQL交互

1、安装引入模块：
	
	安装mysql模块
	sudo apt-get install python-mysqldb
	在文件中引入模块
	import MySQLdb

	connect 方法默认开启了事务功能。
	主要学习模块中封装的类。


2、配置pycharm连接mysql数据库
	（1）安装MySQLdb包：
		从【File】【Settings】【Project】【Project Interpreter】中点击【 + 】从【Available Packages】中搜索【pymysql】并安装。
	（2）Pycharm配置数据库：
		参考网址：
			https://blog.csdn.net/xiongchun11/article/details/64922619
			https://blog.csdn.net/yjz_sdau/article/details/79211309
		【 View 】【 Tool Windows 】【 Database 】【 Alt+Insert 或者 + 】【Data Source】
		【MySQL】,填写【User】和【Password】;点击Test Connection（如果Test Connection按钮不能用的话，应该是Driver没有下载，在页面下方会有Download按钮，单击后直接下载就行）

		或者：安装数据库驱动方法：
		jetbrains家的IDE一般都是java写的，于是猜想可能是java缺少mysql的驱动
		
		网址：https://dev.mysql.com/downloads/connector/j/
		
		选择【 Platform Independent 】中【 Platform Independent (Architecture Independent), ZIP Archive 】并解压；
		【 mysql-connector-java-8.0.11.jar 】

3、Sql 语句参数化：
	SQL注入攻击方式：
	a' or 1=1 or '
	select * from students where name='a' or 1=1 or '' 
	用户输入不按指定格式输入。所以最好是 参数化：

	#encoding=utf-8
	import MySQLdb
	try:
	    conn=MySQLdb.connect(host='localhost',port=3306,db='test1',user='root',passwd='mysql',charset='utf8')
	    cs1=conn.cursor()
	   
	   `sname=raw_input("请输入学生姓名：")`
	    `params=[sname]`
	    `count=cs1.execute('insert into students(sname) values(%s)',params)`
	   
	    print(count)
	    conn.commit()
	    cs1.close()
	    conn.close()
	except Exception,e:
	    print e.message
	应用参数变量params以列表形式保存变量，防止出现非法输入。


4、封装：
	观察前面的文件发现，除了sql语句及参数不同，其它语句都是一样的。所以我们定义类来封装。
	只要是重复使用的代码就要考虑封装。

		# coding=utf-8
		import pymysql


		class MysqlHelper:
		    def __init__(self, host, port, db, user, passwd, charset='utf8'):
		        self.host = host
		        self.port = port
		        self.db = db
		        self.user = user
		        self.passwd = passwd
		        self.charset = charset

		    def open(self):
		        self.conn = pymysql.connect(
		            host=self.host,
		            port=self.port,
		            db=self.db,
		            user=self.user,
		            passwd=self.passwd,
		            charset=self.charset
		        )
		        self.cursor = self.conn.cursor()

		    def close(self):
		        self.cursor.close()
		        self.conn.close()

		    # 操作方法：create,update,read,delete.
		    def curd(self, sql, params=()):
		        try:
		            self.open()

		            self.cursor.execute(sql, params)
		            self.conn.commit()

		            self.close()
		            print("test---ok---")
		        except Exception as e:
		            print(e)

		    def get_all(self, sql, params=()):
		        try:
		            self.open()

		            self.cursor.execute(sql, params)
		            result = self.cursor.fetchall()

		            self.close()
		            return result
		        except Exception as e:
		            print(e)


5、用户登录：

	S1:接收用户输入：用户名、密码；
	S2:根据用户名，查询密码；
		查询用户名：
			如果未查到：用户名错误
			如果查到了：匹配密码；
	S3：根据输入，匹配密码；
		如果匹配到了：登录成功；
		如果匹配不到：密码错误。

	数据库中：
		包含：用户表：
			id name passwd isdelete
			其中passwd在数据库中用SHA1加密：

	使用hashlib模块加密即可。
		# 对密码加密：
		s1 = hashlib.sha1()
		s1.update(pwd.encode('utf-8'))
		pwd2 = s1.hexdigest()


6、总结：
	
	Connection：尽量晚打开，尽量早关闭；因为占用数据库连接数：
		connect(host,port,user,passwd,db,charset)
		cursor()
		commit
		close
	cursor:
		execute()
		如果执行insert update delete语句时，需要conn.commit()
		fetchall()
		fetchone()
		close
