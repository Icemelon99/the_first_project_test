from redis import StrictRedis

sr = StrictRedis()
ret = sr.hgetall('a2')
print(ret)

