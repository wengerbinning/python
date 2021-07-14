# Redis

[//]: # (__author__ = "Clark Aaron")
[//]: # (__version__ = "v0.0")

redis是一个Python接口，用于连接redis数据库。

## Redis安装

安装redis可以使用pip安装或在Github下载源码安装

  * pip安装：

  ```shell
  pip install redis
  ```

  * 源码安装（首先在[Github](https://github.com/andymccurdy/redis-py)下载源码），在源码目录中数执行：
  ```shell
  python setup.py install
  ```

## Redis演示

在学习之前演示一个python管理Redis的项目（`demo.py`）

```python
#!/usr/local/bin python3

import redis

redisSocket = redis.Redis(host="127.0.0.1",port="6379",db=0)

status = redisSocket.set('name',"Clark Aaron")
print(status)

result = redisSocket.get('name')
print(result.decode('utf-8'))
```

> Notes：redis接口在python3中返回的数据默认为字节，需要使用decode解码转化为str，在python2中默认返回str；如果所有的返回数据需要str类型，则可以通过指定Redis.\_\_init\_\_()的decode_response=True对返回数据自动解码。redis-py3.0仅支持字节、字符串与数字类型，如果使用其他述据类型会抛出一个DataError的异常。

## 