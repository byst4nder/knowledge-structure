import redis


re = redis.Redis(host='192.168.85.20', port=6379)
re.set('py100', b'hello world')
print(re.get('key_name'))

re.mset(key_name1='key_tom1', key_name2='key_tom2')
res = re.mget('key_name1', 'key_name2')
print(res)
print(res[0].decode('utf8'))
print(res[1].decode('utf8'))

