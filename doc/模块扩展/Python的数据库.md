# Python的数据库

[//]: # (__author__ = "Clark Aaron")

Python提供丰富的库来操作数据库。

## SQLite

* SQLite:一种嵌入式数据库,C语言开发,体积小,在Python中内置了SQLite3;
* 使用sqlite3模块连接SQLite数据库;
  ```
  # 导入SQLite驱动:
    >>> import sqlite3
    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在，会自动在当前目录创建:
    >>> conn = sqlite3.connect('test.db')
    # 创建一个Cursor:
    >>> cursor = conn.cursor()
    # 执行一条SQL语句，创建user表:
    >>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    <sqlite3.Cursor object at 0x10f8aa260>
    # 继续执行一条SQL语句，插入一条记录:
    >>> cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
    <sqlite3.Cursor object at 0x10f8aa260>
    # 通过rowcount获得插入的行数:
    >>> cursor.rowcount
    1
    # 关闭Cursor:
    >>> cursor.close()
    # 提交事务:
    >>> conn.commit()
    # 关闭Connection:
    >>> conn.close()
  ```
  * 查询记录;
  ```
  >>> conn = sqlite3.connect('test.db')
    >>> cursor = conn.cursor()
    # 执行查询语句:
    >>> cursor.execute('select * from user where id=?', ('1',))
    <sqlite3.Cursor object at 0x10f8aa340>
    # 获得查询结果集:
    >>> values = cursor.fetchall()
    >>> values
    [('1', 'Michael')]
    >>> cursor.close()
    >>> conn.close()
  ```

## MySQL

* 安装驱动
  ```
   #pip install mysql-connector-python --allow-external mysql-connector-python
  pip install mysql-connector
  ```
* 连接数据库:
  ```
  # 导入MySQL驱动:
    >>> import mysql.connector
    # 注意把password设为你的root口令:
    >>> conn = mysql.connector.connect(user='root', password='password', database='test')
    >>> cursor = conn.cursor()
    # 创建user表:
    >>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    # 插入一行记录，注意MySQL的占位符是%s:
    >>> cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
    >>> cursor.rowcount
    1
    # 提交事务:
    >>> conn.commit()
    >>> cursor.close()
    # 运行查询:
    >>> cursor = conn.cursor()
    >>> cursor.execute('select * from user where id = %s', ('1',))
    >>> values = cursor.fetchall()
    >>> values
    [('1', 'Michael')]
    # 关闭Cursor和Connection:
    >>> cursor.close()
    True
    >>> conn.close()
  ```

## SQLAlchemy

* ORM(Object-Relational Mapping)
* Python中,最有名的ORM框架是SQLAlchemy
  ```
  pip install SQLAlchemy
  ```
  ```
  # 导入:
    from sqlalchemy import Column, String, create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base

    # 创建对象的基类:
    Base = declarative_base()

    # 定义User对象:
    class User(Base):
        # 表的名字:
        __tablename__ = 'user'

        # 表的结构:
        id = Column(String(20), primary_key=True)
        name = Column(String(20))

    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
  ```
  ```
  
  ```
