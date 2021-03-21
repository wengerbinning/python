# -*- coding:utf-8 -*-
# author: Clark
# creationTime: 2019-12-30 20:26
# description: PyMySQL模块的演示
# packages: pymysql

import pymysql.cursors

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'jianghu',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO 'Demo'('user', 'password') VALUES (%s, %s)"
        cursor.execute(sql, ('clarkaaron@163.com', '2803611373zwb'))
    connection.commit()

    with connection.cursor() as cursor:
        sql = "SELECT 'id', 'password' FROM 'Demo' WHERE 'user' = %s"
        cursor.excute(sql,('clarkaaron@163.com', ))
        result = cursor.fetchone()
        print(result)
#except:
 #   print("某些地方可能写错了哦!")
finally:
    connection.close()

