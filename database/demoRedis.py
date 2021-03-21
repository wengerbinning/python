#!/usr/local/bin python3

__author__ = "Clark Aaron"
__version__ = "v0.0"

import redis

redisScoket = redis.Redis(host='127.0.0.1',port=6379,db=1)
# status = redisScoket.set('name',"Clark Aaron")
# print(status)
reasult = redisScoket.get('age')
print(reasult)
