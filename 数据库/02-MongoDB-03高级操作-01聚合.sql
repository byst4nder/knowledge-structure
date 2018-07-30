MongoDB高级操作：
	
1、聚合：
	主要用于计算数据，类似sql中的sum()、avg()
	db.集合名称.aggregate([{管道:{表达式}}]):
		注意：aggregate接受的参数是一个 `数组` [数组] 。
		(1)`管道`：管道在Unix和Linux中一般用于将当前命令的输出结果作为下一个命令的输入。
			ps ajx | grep mongo

			在mongoDB中：文档处理完毕后，通过管道进行下一次处理。

		常用管道：
			·$group：将集合中的文档分组，可用于统计结果。类似mysql中的groupby
			·$match：过滤数据，只输出符合条件的文档。
			·$project：修改输入文档的结构，如重命名、增加、删除字段、创建计算结果。作用相当于投影。
			·$sort：将输入文档排序后输出。
			·$limit：限制聚合管道返回的文档数。
			·$skip：跳过指定数量的文档，并返回余下的文档。
			·$unwind：将数组类型的字段进行拆分。


		(2)`表达式`:处理输入文档并输出
			表达式:'$列名'

		常用表达式
			·$sum：计算总和，$sum:1同count表示计数
			·$avg：计算平均值
			·$min：获取最小值
			·$max：获取最大值
			·$push：在结果文档中插入值到一个数组中
			·$first：根据资源文档的排序获取第一个文档数据
			·$last：根据资源文档的排序获取最后一个文档数据


	以管道的方式实现聚合操作：


	管道 一：$group：
		将集合中的文档 分组，可用于统计结果.
		_id表示分组的依据，使用某个字段的格式为'$字段'
		注意：aggregate接受的参数是一个 `数组`
		
		db.stu.aggregate([
			{$group:   # 选择要做的操作的管道。
				{
					_id:'$gender',  # 选择哪些字段做分组操作。
					counter:{$sum:1} # 做何种类型的统计，是求和，还是求最值？$sum:1效果通 同count计数。
				}
			}
		])	
		修改一下：表达式1：
		db.stu.aggregate([
			{$group:   # 选择要做的操作的管道。
				{
					_id:'$gender',  # 选择哪些字段做分组操作。
					counter:{$sum:'$age'} # 做何种类型的统计:加$关键字，基于何种属性进行求和统计。分组后基于age求和。
				}
			}
		])			
		
		修改一下：表达式2：
		db.stu.aggregate([
			{$group:   # 选择要做的操作的管道。
				{
					_id:'$gender',  # 选择哪些字段做分组操作。
					counter:{$avg:'$age'} # 做何种类型的统计:加$关键字，基于何种属性进行统计。
					# 分组后基于age求均值。
				}
			}
		])	

		修改一下：表达式3：
		db.stu.aggregate([
			{$group:   # 选择要做的操作的管道。
				{
					_id:'$gender',  # 选择哪些字段做分组操作。
					counter:{$push:'$age'} # 做何种类型的统计:加$关键字，基于何种属性进行统计。分组后将age字段的数值放在数组中去。
					# 将差异性数据放在一个组中。
				}
			}
		])	

		修改一下：表达式4：
		db.stu.aggregate([
			{$group:   # 选择要做的操作的管道。
				{
					_id:'$gender',  # 选择哪些字段做分组操作。
					counter:{$push:'$$ROOT'} # 做何种类型的统计:$$ROOT，基于整个文档统计。
					# 使用$$ROOT可以将文档内容加入到结果集的数组中。
					# 分组和统计后，还将元数据信息显示出来。透视数据。
				}
			}
		])			

		修改一下：表达式5：将集合中所有文档分为一组：
		db.stu.aggregate([
			{$group:   # 选择要做的操作的管道。
				{
					_id:null,  # 直接将_id修改为null即可。不分组。
					counter:{$sum:'$age'} # 做何种类型的统计:加$关键字，基于何种属性进行求和统计。分组后基于age求和。
				}
			}
		])	




	管道 二：$match:
		用于过滤数据，只输出符合条件的文档。
		查询年龄大于20的学生:
		db.stu.aggregate([{$match{age:{$gt:20}}}])
		查询年龄大于20的男生、女生人数:
		db.stu.aggregate([
			{$match:{age:{$gt:20}}},
			{$group:{_id:'$gender',counter:{$sum:1}}}
		])



	管道三：$project:
		修改输入文档的结构，如重命名、增加、删除字段、创建计算结果.
		特殊：对于_id列默认是显示的，如果不显示需要明确设置为0
		查询学生的姓名、年龄。
		db.stu.aggregate([
			{$project:{_id:0,name:1,age:1}}
		])

		查询男生、女生人数，输出人数
		db.stu.aggregate([
			{$group:{_id:'$gender',counter:{$sum:1}}},
			{$project:{_id:0,counter:1}}
		])

	管道四：$sort：
		将输入文档排序后输出。
		db.stu.aggregate([{$sort:{age:1}}])
		db.stu.aggregate([
			{$group:{_id:'$gender',counter:{$sum:1}}},
			{$sort:{counter:-1}}
		])

	管道五：	$limit：限制聚合管道返回的文档数。
			$skip：跳过指定数量的文档，并返回余下的文档。
			db.stu.aggregate([{$limit:2}])
			db.stu.aggregate([{$skip:2}])
			db.stu.aggregate([
			    {$group:{_id:'$gender',counter:{$sum:1}}},
			    {$sort:{counter:1}},
			    {$skip:1},
			    {$limit:1}
			])  # 先写skip，再写limit。

	管道六：$unwind：
		将文档中的某一个数组类型字段拆分成多条，每条包含数组中的一个值。
			db.t1.insert({_id:1,title:'T-shirt',size:['M','L','S']})
			db.t1.aggregate([{$unwind:'$size'}])

		当拆分字段有空值的时候：阻止数据丢失：
			db.inventory.aggregate([
				{$unwind:{
					path:'$字段名称'，
					preserveNullAndEmptyArrays:<boolean> #防止数据丢失。
					}
				}
			])

			db.t3.aggregate([{$unwind:{path:'$size',preserveNullAndEmptyArrays:true}}])











