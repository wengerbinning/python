# Python模块扩展

[//]: # (__author__ = "Clark Aaron")

Python在开发中常使用的内置标准库及第三方库;

## 标准库

### datetime

处理日期和时间的标准库;1970年1月1日 00:00:00 (UTC+00:00) 为epoch time,相对于此时间的秒数为时间戳;

* datetime.now():获取当前时间和日期;

  ```python
  current_time = datetime.datetime.now()
  year = current_time.year
  month = current_time.month
  day = current_time.day
  hour = current_time.hour
  minute = current_time.minute
  second = current_time.second
  ```

* strftime(fmt):对时间进行格式化：
  
  ```python
  format_time = current_time.strftime(fmt)
  ```

* fromtimestamp(timestamp):对时间戳进行格式化;
* uctfromtimestamp(timestamp):对时间进行UTC标准时区转换;
  
  ```python
  time = time.time()
  ftime = datetime.datetime.fromtimestamp(time)
  ```

* timedelta类:时间间隔类;
* timestamp():将datatime转换为时间戳;
* strptime():对字符串进行时间转换;

### hashlib

提供常见的哈希算法;

* MD5:128字节,通常是一个32位的16进制字符串表示;
  
  ```python
  import hashlib

    md5 = hashlib.md5()
    md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())
  ```

* SHA1:160字节,40位16进制字符串表示;
* SHA256:
* SHA512:

### cpllections

* Python的一个集合模块;
* namedtuple():
* deque:双向列表;
* defaultdict:设置字典key不存在时的返回值;
* OrderedDict:保持key的顺序;

### base64

* 一种使用64个字符表示任意二进制数据的方法;

### struct

* 解决bytes和其他二进制数据类型的转化;

## hmac

* Keyed-Hashing for Message Authentication;

## itertools

* 提供常用的操作迭代对象的函数;

## contextlib

* 上下文管理器:实现__enter__()于__exit__()后使用with调用上下文管理器;
* @contextmanager
* @closing():

## urllib

* 提供一些列操作URL的功能;

## XML

* 提供XML数据操作;

## HTMLParser

* 以下为第三方库:

## Numpy

* Numpy是进行科学计算及数据分析的常用库;
  
### 创建ndarray矩

* 创建一维数组:
  ```
  import numpy as np
  list_name = [1,2,3,4]
  array = np.array(list_name)
  ```
* 创建多维数组:
  ```
  import numpy as np
  list_name = [[1,2,3,4],[1,2,3,4]]
  array = np.array(list_name)
  ```
* shape(row,lie):返回数组的维数;
  ```
  array.shape
  ```
* reshape:改变数组的结构;
  ```
  newarray = array.reshape(m,n)
  ```
* 创建特殊数组:
  ```
  array1 = np.zeros(5)
  array2 = np.ones()
  array3 = np.empty()
  array4 = np.arange()
  array5 = np.eye()
  ```
* dtype:存储矩阵数据类型;
* astype():改变矩阵数据类型;

### 数学与统计函数
* 统计运算:
  ```
  array.sum()
  array.mean()
  array.var()
  array.std()
  array.max()
  array.min()
  array.cumsum()
  array.cumprod()
  array.argmax()
  array.argmin()
  ```
* 矩阵运算
  ```
  array.T
  array.dot(array_)
  array1 = np.linalg.inv(array)
  value = np.trace(array)
  ```
* 数据处理
  ```
  array.sort(axis=0)
  array1 = np.unique(array)
  ```
    
### 文件读入和读出
* 写文件:
  ```
  np.savetxt("arr.txt",array)
  ```
* 读文件:
  ```
  array = np.loadtxt("arr.txt")
  ```

## Pandas 库
---
* Pandas是用于处理高级数据结构和数据分析的第三方库,是基于numpy构建,增加了大量模块的标准数据模型;

### Pandas数据结构
* Series(list[,index]):
  ```
  import pandas as pd
  var = pd.Series([1,2,3,4],index=['A','B','C','D'])
  dictionary = {}
  var = pd.Series(dictionary)
  ```
* DataFrame数据结构(类似二位表格的形式):
  ```
  dict = {}
  var = pd.DataFrame(dict)
  ``` 
### 数学与统计计算

| 符号 | 说明 | 符号 | 说明 | 符号 | 说明 |
|:---- |:---- |:--- |:---- |:---- |:---- |
| mean | 均值 | median | 中位数 | count | 非缺省值数量 |
| min、max | 最小、大值 | describe | 汇总统计 | var | 方差 |
| std | 标准差 | skew | 偏度 | kurt | 峰度 |
| diff | 一阶差分 | cummin、cummax | 累计最大值、最小值 | cumsum、cumprod | 累计和、累计积 |
| cov、corr | 协方差、相关系数 |

### DataFrame的文件操作 
* 读文件:
  ```
  pd.read_cvs(file)
  pd.read_table(file)
  pd.read_excel(file)
  pd.read_sql()
  pd.read_json(file)
  pd.read_html(file)
  ```
* 写文件：
  ```
  pd.to_cvs()
  pd.to_table()
  pd.to_excel()
  pd.to_sql()
  pd.to_json()
  pd.to_html()
  pd.to_clipboard()
  ```

### 数据处理
* 缺省值处理: 查找缺省值,过滤缺省值,填充缺省值,
* 重复值处理:查找重复值,去除重复值;
* 数据记录合并与分组:





## chardet 库
---
* 检测编码;

## psutil 库
---
* process and system utilities;

## virtuallenv 库
---
* 船舰一套"隔离"的Python环境;



## 第三方库
---
### Pillow 库 >>>
* 基于PIL(Python Imaging Library)开发,处理图像标准库;
---
### requests 库
* 基于urllib库数据获取库;


************************
            
************************

* 发布一个第三方库是需要在pypi.python.org网站上注册;