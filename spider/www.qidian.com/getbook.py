#!/usr/local/bin python3

__author__ = "Clark Aaron"
__version__ = "v0.0"

import redis
books = []
dataBase = redis.Redis(host="localhost",port=6379,db=6)

data = dataBase.keys('*')

for book in data:
    books.append({"name":book.decode("utf-8"),"author":dataBase.hget(book,"author").decode("utf-8"),"url":dataBase.hget(book,"url").decode("utf-8")})

for book in books:
    print("《%s》（%s）：%s"%(book["name"],book["author"],book["url"]))
