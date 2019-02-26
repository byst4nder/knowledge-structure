redis 高级操作

1、发布订阅：
	搭建`信息推送`这种功能的设计模式：代码结构，开发方式。

	消息的发送方式有两种：
		1)明确请求：客户端请求，服务端返回。
		2)发布订阅：订阅后，当服务器有新消息时不需要客户端请求，服务端主动推送，常链接。

	·发布者不是计划发送消息给特定的接收者（订阅者），而是发布的消息分到不同的频道，不需要知道什么样的订阅者订阅
	·订阅者对一个或多个频道感兴趣，只需接收感兴趣的消息，不需要知道什么样的发布者发布的
	·发布者和订阅者的解耦合可以带来更大的扩展性和更加动态的网络拓扑
	·客户端发到频道的消息，将会被推送到所有订阅此频道的客户端
	·客户端不需要主动去获取消息，只需要订阅频道，这个频道的内容就会被推送过来

	消息的格式：	
		推送消息的格式：三部分：
			
			part1:消息类型，包含三种类型
				subscribe,表示订阅成功
				unsubscribe，表示取消订阅成功
				message,表示其他终端发布消息
			part2/3:
				如果第一部分是：
					subscribe，则第二部分是频道，第三部分是现在订阅的频道的数量
					unsubscribe，则第二部分是频道，第三部分是现在订阅的频道的数量，
						如果为0则表示当前没有订阅任何频道，
						当在Pub/Sub以外状态，客户端可以发出任何redis命令
					message，则第二部分是来源频道的名称，第三部分是消息的内容

	操作命令：
		订阅：
			subscribe 频道名称
		取消订阅：如果不写参数，表示取消所有订阅
			unsubscribe 频道名称

		发布：
			publish 频道 消息

	仿真：开两个客户端：
		cli_s:
			切换到数据库：
				redis-cli
				select 1
				keys *
			订阅一个频道：
				subscribe py111
					显示内容：对应上方消息格式。
					1) "subscribe"
					2) "py111"
					3) (integer) 1


				输入完后，停在等待显示发布状态中。


		cli_p:
				redis-cli
				publish py111 hello
				publish py111 world
					显示内容：
						(integer) 2 显示频道订阅数。
			此时订阅端显示：
				1) "message"
				2) "py111"
				3) "hello"
				1) "message"
				2) "py111"
				3) "world"

			对应上方消息格式:
			测试输入unsubscribe py111

	不需要主动请求页面数据，自动实现信息的更新，比如你购买一个商品后，商品数量。自动在页面上修改。


2、主从配置：
	一个master可以拥有多个slave，一个slave又可以拥有多个slave，如此下去，形成了强大的多级服务器集群架构
	比如，将ip为192.168.1.10的机器作为主服务器，将ip为192.168.1.11的机器作为从服务器
	
	设置主服务器的配置	
		修改redis配置文件/etc/redis/redis.conf 
		bind 192.168.1.10
	
	设置从服务器的配置
		注意：在slaveof后面写主机ip，再写端口，而且端口必须写
		bind 192.168.1.11
		slaveof 192.168.1.10 6379

		启动服务：
		可以通过redis-server --help来查看命令的用法。
		./redis-server --port 6379 --slaveof 192.168.85.20 6379
		redis-cli -h 192.168.85.20
		此时完成主从配置。

	重启redis服务：
		sudo server redis restart
	
	在master和slave分别执行info命令，查看输出信息
		主服务器上写数据，从服务器上读数据。

	此时redis-cli无法登陆：
	redis-cli --help去查询修改默认主机ip
	redis-cli -h 192.168.85.20

	https://blog.csdn.net/github_26672553/article/details/69568259


3、与Python交互
	https://blog.csdn.net/babados/article/details/78575145

	Pycharm 集成Redis可视化插件Iedis
		需要解决连接报错问题，包括主从配置中出现的错误，都是同一个错误。redis网络化配置问题。

		先复制一份conf文件，或者重新安装吧。见下文4。

	import redis


	re = redis.Redis(host='192.168.85.20', port=6379)
	re.set('py100', b'hello world')
	print(re.get('key_name'))

	re.mset(key_name1='key_tom1', key_name2='key_tom2')
	res = re.mget('key_name1', 'key_name2')
	print(res)
	print(res[0].decode('utf8'))
	print(res[1].decode('utf8'))

	封装：
		# encoding=utf-8
		import redis


		class RedisHelper:
		    def __init__(self, host='192.168.85.20', port=6379):
		        self.__redis = redis.Redis(host, port)

		    def get(self, key):
		        if self.__redis.exists(key):
		            return self.__redis.get(key)
		        else:
		            return None

		    def set(self, key, value):
		        self.__redis.set(key, value)






4、错误信息处理：
	Exception in thread "main" redis.clients.jedis.exceptions.JedisDataException: DENIED Redis is running in protected mode because protected mode is enabled, no bind address was specified, no authentication password is requested to clients. In this mode connections are only accepted from the loopback interface. If you want to connect from external computers to Redis you may adopt one of the following solutions:
 1) Just disable protected mode sending the command 'CONFIG SET protected-mode no' from the loopback interface by connecting to Redis from the same host the server is running, however MAKE SURE Redis is not publicly accessible from internet if you do so. Use CONFIG REWRITE to make this change permanent.
 2) Alternatively you can just disable the protected mode by editing the Redis configuration file, and setting the protected mode option to 'no', and then restarting the server
 3) If you started the server manually just for testing, restart it with the '--protected-mode no' option. 
 4) Setup a bind address or an authentication password. NOTE: You only need to do one of the above things in order for the server to start accepting connections from the outside.
    at redis.clients.jedis.Protocol.processError(Protocol.java:127)
    at redis.clients.jedis.Protocol.process(Protocol.java:161)
    at redis.clients.jedis.Protocol.read(Protocol.java:215)
    at redis.clients.jedis.Connection.readProtocolWithCheckingBroken(Connection.java:340)
    at redis.clients.jedis.Connection.getStatusCodeReply(Connection.java:239)
    at redis.clients.jedis.BinaryJedis.ping(BinaryJedis.java:196)
    at com.example.redis.JedisTest.main(JedisTest.java:24)
    
    (error) DENIED Redis is running in protected mode because protected mode is enabled, no bind address was specified, no authentication password is requested to clients. 
    In this mode connections are only accepted from the loopback interface. If you want to connect from external computers to Redis you may adopt one of the following solutions: 
1) Just disable protected mode sending the command 'CONFIG SET protected-mode no' from the loopback interface by connecting to Redis from the same host the server is running, 
however MAKE SURE Redis is not publicly accessible from internet if you do so. Use CONFIG REWRITE to make this change permanent. 
2) Alternatively you can just disable the protected mode by editing the Redis configuration file, and setting the protected mode option to 'no', and then restarting the server. 
3) If you started the server manually just for testing, restart it with the '--protected-mode no' option. 
4) Setup a bind address or an authentication password. NOTE: You only need to do one of the above things in order for the server to start accepting connections from the outside.
	按照第一种方法：重启一个客户端：然后在里面是输入：
		redis-cli:
		CONFIG SET protected-mode no
	返回OK即可。
	然后用：
		redis-cli -h 192.168.85.20


	此时pycharm中的链接也通。



	遇到问题多种方法都要去尝试，一点点找问题，在不断的摸索中解决问题，只会越来越迅速。


