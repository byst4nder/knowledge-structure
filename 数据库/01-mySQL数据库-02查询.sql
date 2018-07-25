数据库查询：
	数据库使用中，百分之九十的是查询功能的使用。
	类C的语言：区分大小写。
	类B的语言：不区分大小写。mysql不区分大小写。

	select * from 表名；
	消除重复行：
		select distinct gender from students;
		在 select 后面列前使用 distinct 可以消除重复的行
		select distinct id,gender from students;

1、条件：
	select * from 表名 where 条件；
	使用where子句对表中的数据筛选，结果为true的行会出现在结果集中。

	比较运算符：
	逻辑运算符：
	
	模糊查询：
		like
		% 表示任意多个字符
		_ 表示一个任意字符
	
	范围查询：
		in ：非连续的范围内。
			select * from students where id in(1,3,8);
		between ... and ...：表示在一个连续的范围内
			select * from students where id between 3 and 8;

	空判断：
		注意：null 与 ''是不同的
		判空： is null
			select * from students where hometown is null;
		判非空：is not null
			select * from students where hometown is not null;

	优先级：
		·小括号，not，比较运算符，逻辑运算符
		·and比or先运算，如果同时出现并希望先算or，需要结合()使用


2、聚合：
	对多行数据进行统计：
	看不到原始数据集合，只能看到统计结果。就5个函数。

	count()
		count(*)：不区分某一列：计算总行数。
			写*与写列名等效：
		select count(*) from students;

	max()
		max(列)：求此列最大值
	min()
		min(列)
		select * from students where id=(select min(id) from students where isdelete=0)
		复合形式：

	sum(列)：数字类型。
		select sum(id) from students where gender=1;
	avg(列)：求此列平均值。
		select avg(id) from students where isdelete=0 and gender=0;


3、分组：group by 
	·按照字段分组，表示此字段相同的数据会被放到一个组中。
	·分组后，只能查询出相同的数据列，对于有差异的数据列无法出现在结果集中。
	·可以对分组后的数据进行统计，做聚合运算。

	select 列1，列2，列3,聚合...from 表名 group by 列1，列2，列3
	select gender,count(*) from students group by gender;
	select count(*) from students group by gender;

	分组之后对数据筛选：
	select 列1，列2，聚合...from 表名 group by 列1，列2，列3...having 列1,...聚合...
		`having后面的条件运算符与where的相同`
		select gender,count(*) as rs from students group by gender having rs>2;
		select gender,count(*) from students group by gender having count(*)>2;

	对比where与having
		·where是对from后面指定的表进行数据筛选，属于对原始数据的筛选
		·having是对group by的结果进行筛选


4、排序：order by 

	·将行数据按照列1进行排序，如果某些行列1的值相同时，则按照列2排序，以此类推
	·默认按照列值从小到大排列
	·asc从小到大排列，即升序
	·desc从大到小排序，即降序

	select * from students where gender=1 and isdelete=0 order by id desc;


5、分页：一页显示查看数据，以及数据库一次性导出所有负担太重。所以分页显示：
	select * from 表名 limit start,count
		·从start开始，获取count条数据
		·start索引从0开始
		select * from students where isdelete=0 limit (n-1)*m,m；


总结：
	完整的select语句
		select distinct *
		from 表名
		where ....
		group by ... having ...
		order by ...
		limit star,count
	执行顺序为：
		from 表名
		where ....
		group by ...
		select distinct *
		having ...
		order by ...
		limit star,count
	实际使用中，只是语句中某些部分的组合，而不是全部