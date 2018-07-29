高级查询

1、关系
	关系是一种数据，需要存储。

	学生信息是由学生维护的，科目信息是由科目表维护的。两者可以共同提供成绩表。
	这样的关系可以存储下来。第三范式：引用主键。

	一个学生会有多个科目的成绩。一对多。
	一个科目成绩只能有一个学生。重分也是多个人。
	综合起来：一对多。

	查询优化，把经常查询用的，新建一个A表，不常用的另一个表B。先查A表。就能满足大多数，而不用特别庞大的数据库。

	关系在设计的时候要特别注意一点：不能闭合。一旦闭合，会导致数据冗余。

	引入外键对数据库内容做约束。保证数据的完整性。
	创建时添加：
		create table scores(
		id int primary key auto_increment,
		stuid int,
		subid int,
		score decimal(5,2),
		foreign key(stuid) references students(id),
		foreign key(subid) references subjects(id)
		);
	或者后期约束时添加；
		alter table scores add constraint stu_sco foreign key(stuid) references students(id);

		在删除students表的数据时，如果这个id值在scores中已经存在，则会抛异常,推荐使用 `逻辑删除`，还可以解决这个问题



2、连接：
	满足各种功能显示需要，需要调用一些字段的时候：
		select students.sname,subjects.stitle,scores.score
		from scores
		inner join students on scores.stuid=students.id
		inner join subjects on scores.subid=subjects.id;

	连接查询分类如下：
		·表A inner join 表B：表A与表B匹配的行会出现在结果中
		·表A left join 表B：表A与表B匹配的行会出现在结果中，外加表A中独有的数据，未对应的数据使用null填充
		·表A right join 表B：表A与表B匹配的行会出现在结果中，外加表B中独有的数据，未对应的数据使用null填充



	`学会分析的过程比记录语句更重要：`
		查询学生的姓名、平均分
			select students.sname,avg(scores.score)
			from scores
			inner join students on scores.stuid=students.id
			group by students.sname;
		查询男生的姓名、总分
			select students.sname,sum(scores.score)
			from scores
			inner join students on scores.stuid=students.id
			where students.gender=1
			group by students.sname;
		查询科目的名称、平均分
			select subjects.stitle,avg(scores.score)
			from scores
			inner join subjects on scores.subid=subjects.id
			group by subjects.stitle;
		查询未删除科目的名称、最高分、平均分
			select subjects.stitle,avg(scores.score),max(scores.score)
			from scores
			inner join subjects on scores.subid=subjects.id
			where subjects.isdelete=0
			group by subjects.stitle;



3、自关联：

	`表中的某一列，关联了这个表中的另外一列`，但是它们的业务逻辑含义是不一样的，城市信息的pid引用的是省信息的id。
	create table booktest_areas(
	id int primary key auto_increment not null
	title varchar(20),
	pid int,
	foreign key(pid) references booktest_areas(id)
	);

	从sql文件中导入数据
		source areas.sql;

	自关联查询：
		select * from areas where
		pid=(select id from areas where title='山西省')；

		select sheng.id as sid,sheng.title as stitle,
		shi.id as shiid,shi.title as shititle
		from booktest_areas as sheng
		inner join areas as shi on shend.id=shi.pid
		where sheng.pid is null and sheng.tile='山西省'
		limit 0,100;
	连接查询注意实现，实际物理上是一张表，但是逻辑上看成两（多）张表。

	选出所有省：
		select sheng.id as sid,sheng.title as stitle 
		from booktest_areas as sheng
		where sheng.id is null
		limit 0.50;



4、视图：view
	复杂的 select 语句每次在用的时候，维护成本较高，所以用一个办法来封装，实现方便的多次调用。
	视图本质就是对查询的一个封装。

	定义视图
		create view v_stu_sub_sco as 
		select stu.*,sco.score,sub.title from scores as sco
		inner join students as stu on sco.stuid=stu.id
		inner join subjects as sub on sco.subid=sub.id
		where stu.isdelete=0 and sub.isdelete=0;


	视图的用途就是查询：
		select * from v_stu_sub_sco;


5、事务：

	当一个业务逻辑需要多个sql完成时，如果其中某条sql语句出错，则希望整个操作都退回。
	使用事务可以完成退回的功能，保证业务逻辑的正确性。


	事务四大特性(简称ACID)
		·原子性(Atomicity)：事务中的全部操作在数据库中是`不可分割的`，要么全部完成，要么均不执行。
		·一致性(Consistency)：几个并行执行的事务，其执行结果必须与按某一顺序串行执行的结果相一致。
		·隔离性(Isolation)：事务的执行不受其他事务的干扰，事务执行的中间结果对其他事务必须是透明的。加锁。
		·持久性(Durability)：对于任意已提交事务，系统必须保证该事务对数据库的改变不被丢失，即使数据库出现故障。
	
	要求：表的类型必须是 innodb 或bdb类型，才可以对此表使用事务。
	

	使用事务的情况：当数据被更改时，包括：insert、update、delete
	
	begin;
	此时锁定数据库中的表。只是放在了内存中。其他地方查询不影响。
	update students set name='小郭' where id=1；
		执行此句时，先在`内存级的临时表中`,完成id=1中name修改为‘小郭’。然后
		只是放在了内存中。其他地方查询不影响。
		本地自己查询时修改后的。其他地方查询为改变。
	commit;
	commit会将内存级临时表更新到数据库表中。解锁表。此时查询之后就是修改后的。
	rollback;
	rollback会将所有begin后面的操作删除掉，恢复到原表。解锁表。




6、索引：

	索引让我们快速找到数据，主键是一种非常好的索引，索引会增加物理空间上的开销。
	用空间换取时间。
	优化查询的办法。

	数据库的优化很多时候都是修改where后面的语句。where 后面的字段建立索引。
		where gender=0 and isdelete=0 and birthday>'1990-1-1':
		此处注意：等号放在前面，范围放在后面。sql语句顺序会影响速度和性能。


	查看索引：
		show index from table_name;

	创建索引：
		create index indexName on mytable(username(length),datetime(datetime),gender);

	删除索引：
		drop index [indexName] on mytable;



	性能检索工具：
		查看执行时间：
			show profiles;
		限于本次连接：
		set profiling=1;
		select * from areas where title='北京市'
		show profiles;

		使用索引之后的速度：
		show index from areas;
		create index titleIndex on areas(title(20));
		select * from areas where title='北京市'
		show profiles;










	

