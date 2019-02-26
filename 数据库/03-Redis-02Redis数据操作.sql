redis 数据操作：

	学习redis是根据值的 `数据类型` 来学习的。

1、数据格式：

	redis 是Key-Value的数据。键值对。
	键的类型：字符串。
	值的类型：
		字符串:string
		哈希：hash
		列表：list
		集合：set 
		有序集合：zset

	官网：http://redis.cn/commands.html

2、string:
	
	·string是redis最基本的类型
	·最大能存储512MB数据
	·string类型是二进制安全的，即可以为任何数据，比如数字、图片、序列化对象等

	命令1：设置
		设置键值：
			set key value
			set 'py3' 'hello'
		设置键值及过期时间，以秒为单位：
			SETEX key seconds value
			setex 'py32' 1 'hello'
		设置多个键值
			Mset key value [key value ...]
	命令2：获取
		根据键获取值
			get key
			如果没有此键，则返回nil
		Mget key key ...

	命令3：运算：
		要求值是数字：
		将key对应的value加1
			incr key
		将key对应的value加整数
			incrBY key increment

		将key对应的value减1
			decr key
		将key对应的value减整数
			decrBy key decrment

	命令4：追加值：
		append key value

	命令5：获取值长度：
		strlen key

3、键命令：
	keys * 查看所有的键。 
		keys '*1*'所有包含1的键
	exists key ：存在
		exist py32
	type key：类型
		type py3
	del key :删除
		de py3
	expire key seconds
		重新设置过期时间。
	TTL key
		查看过期时间。

4、hash
	存储对象：对象的格式为键值对。
	设置：
	hset key field value
		field为属性：
		hset py3 name '郭靖' 
		type py3
		HMset py3 name '黄蓉' gender '女'

	读取：
		Hget key field
		hMget key field
		hGetAll key 拿到所有属性。

	属性个数：
		hlen key

	获取所有值：
		hvals key

	判断属性是否存在：
		hexists key field

	删除属性及值：
		hdel key field

	返回值得字符串长度
		HstrLen key field


5、list
	·数组，列表的元素类型为string
	·按照插入顺序排序
	·在列表的头部或尾部添加元素
	
	设置：
		双向插入数据：

		Lpush key value：头
		Rpush key value：尾

		在一个元素的前后插入数据：

		Linsert key before|After pivot value

			lpush mylist '123'
			rpush mylist ' world'
			Linsert mylist before ' world' 'hello'
			lrange mylist 0 -1：显示所有
		
		Lset key index value


	获取：
		移除并返回：
			Lpop key
			Rpop key
		显示数据：
			lrange key start stop
			lrange mylist 0 -1：显示所有
	裁剪：	
		Ltrim key start stop
		其他的都被裁剪掉。

		Llen key：返回存储在key里面的list长度。

		返回列表里索引对应的元素。
			lindex key index

6、set:
	·无序集合
	·元素为string类型
	·元素具有唯一性，不重复

	设置：
		添加元素：
			SADD key member 
	获取：
		返回key集合所有的元素
			Smembers key
		返回集合元素个数
			scard key
	交集：SINTER key

	差集： Sdiff key

	合集：Sunion key 

	内含：Sismember key member 


7、zset
	·sorted set，有序集合
	·元素为string类型
	·元素具有唯一性，不重复
	·每个元素都会关联一个double类型的score，表示`权重`，通过权重将元素从小到大排序
	·元素的score可以相同

	设置：
		添加：
			Zadd key socre member score member

	获取：
		指定元素范围：
			Zrange key start stop
				Zrange py3 0 -1

		返回元素个数：
			Zcard key

		返回有序集key中：score值在min和max之间：
			zcount key min max

		返回有序集key中，成员member的score值：查权重。
			zscore key member













