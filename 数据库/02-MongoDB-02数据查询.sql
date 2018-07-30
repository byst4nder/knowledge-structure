数据查询：

1、基本查询：
	方法：find():查询
		db.集合名称.find({条件文档})
	方法findOne():查询，只返回第一个：
		db.集合名称.findOne()
			特别注意findOne中O是大写。
	方法pretty():将结果格式化：
		db.集合名称.find({条件文档}).pretty()

2、筛选条件格式：
	比较运算符：
		等于：默认就是等于。
		小于：$lt
		小于或等于：$lte
		大于：$gt
		大于或等于：$gte
		不等于：$ne

			db.sub.find(count:{$gte:5})查找count大于或等于5的。


	逻辑运算符：
		逻辑与：逗号分隔，默认就是逻辑与。
			db.sub.find({title:'css',count:5})
		逻辑或：$or
			db.sub.find({$or:[{age:{gte:18}},{gender:1}]})
		逻辑“或”与“与”
			db.sub.find({$or:[{age:{$gte:18}},{gender:1}],name:'guojing'})
		

	范围运算符
		使用"$in"，"$nin" 判断是否在某个范围内。
		例查询年龄为18、28的学生。
		db.sut.find({age:{$in:[18,28]}})	取义为“和”。

	
	支持正则表达式：
		使用//或$regex编写正则表达式
			例查询姓黄的学生
			db.stu.find({name:/^黄/})
			db.stu.find({name:{$regex:'^黄'}}})


	自定义查询：通过JS语句编辑函数。
		使用$where后面写一个函数，返回满足条件的数据：
			查询年龄大于30的学生：
			db.stu.find({$where:function(){return this.age > 20}})
			this关键字代表了当前这个集合。
			该语句其实本质就是js语言：
			
			以g开头的name查询结果：
			db.stu.find({$where:
				function(){return this.name.indexOf('g')==0}
			})

			只要名字中有x的。
			db.stu.find({$where:
				function(){return this.name.indexOf('x')>=0}
			})


3、查询方法：

	Limit方法:用于读取指定数量的文档:条数。
		db.stu.find().limit(NUMBER)


	skip方法：用于跳过指定数量的文档：条数。
		db.stu.find().skip(NUMBER)

	limit和skip一起使用：
		不分先后顺序。
		完成分页功能。
		for(i=0;i<15;i++){db.t1.insert({_id:i})}
		db.stu.find().limit(4).skip(5)
		db.stu.find().skip(5).limit(4)

	投影：
		有时候每条文档的内容（属性）很多，但我们不需要显示那么多，所以需要做投影。
		find方法的第二个参数控制：
			参数为字段与值，值为1表示显示，值为0不显示
			db.stu.find({},{name:1,gender:1,_id：0})
				默认_id是会显示的，但是我们设置0后不再显示。

	排序：sort方法：
		·参数1为升序排列
		·参数-1为降序排列	
		db.stu.find().sort({gender:-1,age:1})	

	统计个数：count()
		方法count()用于统计结果集中文档条数
		db.stu.find({条件}).count()
		或者：
		db.stu.count({条件})

		统计年龄大于20的男生人数
		db.stu.count({age:{$gte:20},gender:1})


	消除重复：
		方法：distinct()
		db.jihe.distinct('去重字段'，{条件})
		查找年龄大于等于18的性别（去重）
		db.stu.distinct('gender',{age:{$gte:18}})








