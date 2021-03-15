# Python系统管理

[//]: # (__author__ = "Clark aaron")

## 时间日期管理

Python使用time或datetime模块来访问系统的时间。

### time

* 【功能】获取当前时间日期：

  ```python
  import time
  # 以时间戳的形式返回当前时间。
  timestamp = time.time()
  # 无参数时以struct_timede对象的形式返回当前时间,或接受一个时间戳的参数转化为struct_time对象。
  local_time = time.localtime()
  ```

* 【功能】格式化时间日期：

  ```python
  import time
  # 接受一个struct_time对象参数，按照自定义的格式格式化时间。
  format_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
  # 接受一个格式化时间与格式化字符串返回一个struct_time对象。
  local_time = time.strptime(format_time,"%Y-%m-%d %H:%M:%S")
  # 接受一个struct_time对象返回对应的时间戳。
  timestamp = time.mktime(local_time)
  ```

  > 格式化字符：
  >
  > | 格式 | 说明 | 格式 | 说明 | 格式 | 说明 |
  > |:---- |:---- |:---- |:---- |:--- |:--- |
  > | %y | 两位数年份表示 | %Y | 四位数年份表示 | %j | 一年中的第几天 |
  > | %m | 月份表示 | %M | 分钟表示 | %p | 显示本地日期的AM或PM |
  > | %d | 日期表示 | %H | 24小时表示 | %U | 一年的第几周表示 |
  > | %a | 本地简化星期表示 | %I | 12小时表示 | %w | 星期几表示 |
  > | %b | 本地简化的月份表示 | %S | 秒表示 | %W | 一年中的星期数 |
  > | %c | 本地相对应的日期和时间表示 | %A | 本地完成星期表示 | %Z | 当前时区名称 |
  > | %x | 本地日期表示 | %X | 本地时间表示 | %B | 本地月份完整表示 |

* 【功能】程序暂停：

    ```python
    # 控制程序暂停时间。
    time.sleep(<second>)
    ```

### datetime

* 【功能】获取当前时间日期：

  ```python
  local_time = datetime.datetime.now()
  ```

## 内存空间管理

### I/O管理

* IO(Input/Output):标准输入与输出;

* input输入:
  
  ```python
  string = input([<提示字符>])      #返回为一字符串
  ```

* output输出:
  
  ```python
  print(<content>[,end='\n'])   #输出内容,end为最后一位字符,默认为换行符;
  ```


  * StringIO:在内存中读写str:
  ```
  >>> from io import StringIO
  >>> f = StringIO()
  >>> f.write('hello')
  5
  >>> f.write(' ')
  1
  >>> f.write('world!')
  6
  >>> print(f.getvalue())
  hello world!
  ```
* BytesIO在内存中二进制操作:
  
  ```python
  >>> from io import BytesIO
  >>> f = BytesIO()
  >>> f.write('中文'.encode('utf-8'))
  6
  >>> print(f.getvalue())
  b'\xe4\xb8\xad\xe6\x96\x87
  ```

### 文件管理

文件操作在开发中经常使用;

* 检测文件是否存在：

  * 使用os模块:

    ```python
    status = os.path.exists(path)         # path.exits()可以同时检测文件或目录是否存在;
    status = os.path.isfile(file_path)    # path.isfile()只能判断是否是文件;
    status = os.access(path,mode)         # access()可以判断文件的存在及权限状态;
    ```

* 使用try语句捕捉文件不存在的异常(FileNotFindError):
  
  ```python
  try:
    file = open(path,'r')
  excrpt FileNotFindError as error:
    print(error)
  ```

* 使用pathlib模块:
  
  ```python
  path = pathlib.Path("path/file")      # 创建path对象
  path.exist()                          # 检测路径是否存在
  path.is_file()                        # 检测是否是文件
  ```

* 【功能】打开文件：

  * open()方式打开文件:(打开文件不存在时抛出FileNotFoundError异常)

    ```python
    file = open("<文件路径>",'<打开模式>')
    ```

    | 符号 | 说明 | 符号 | 说明 | 符号 | 说明 |
    |:---- |:---- |:--- |:---- |:---- |:---- |
    | r | 只读模式 | w | 只写模式 | a | 追加模式 |
    | r+ | 可读可写 | w+ | | a+ | |

  * with open() as file:方式打开文件,无需显式关闭文件;

    ```python
    with open("<文件路径>",'打开模式') as file:
      <文件的操作>
    ```
  
* 【功能】读取文件：

  * read():一次性读取文件中所有内容；

    ```python
    string = file.read()
    ```

  * readline():一次读取一行文件;

  * readlines():一次性读取所有文件内容,但没一行为一元素,组成列表返回,元素末尾包括一个换行符;
  
    ```python
    list_name = file.listlines()
    ```

* 【功能】写入文件：

  * wirte():将字符串写入文件,**只能将一个字符串写入且不会换行**;
    
    ```python
    file.write(string)
    ```

  * writelines():将序列中多个字符串写入文件中**没一个字符串换行**;
  
    ```python
    file.writelines(list_name)
    ```

* 【功能】关闭文件：close():在使用open打开文件时显式关闭文件;
  
  ```python
  file.close()
  ```

* 使用os模块对文件进行管理;
* mkdir(path):在指定路径下创建目录;
  
  ```python
  import os
  os.mkdir("<路径/文件夹>")
  ```

* rename(oldfile,newfile):对文件及文件夹重命名;
  
  ```python
  import os
  os.rename(oldfile,newfile)
  ```

* getwd():获取运行程序的绝对路径;
  
  ```python
  import os
  path = os.getwd()
  ```

* listdir(path):获取路径下的文件及目录,返回列表;
  
  ```python
  import os
  list_name = os.listdir(path)
  ```

* remove(path):删除指定文件;
  
  ```python
  import os
  os.remove(path)
  ```

* rmdir(path):删除指定空文件夹,文件夹下有文件有抛出OSError异常,如果想删除非空目录,使用shutil模块rmtree();
  
  ```python
  import os
  os.rmdir(path)
  ```

* 读出系统信息

  ```python
  import os
  print(os.name)  #如果是poaix是Linux,mac OS,Unix,如果是nt就是Windows,详细系统信息使用uname()<在Windows不提供>;
  ```

* 环境变量:

  ```python
  imort os
  print(os.environ) #打印所有环境变量;
  print(os.environ.get('key')) #获取变量的值
  ```

#### json

* 使用json模块处理json格式文件;
* dumps(python_dict):将Python数据转换为JSON编码的字符串;
* loads(json_str):将JSON编码的字符串转换为Python字典;
* dump(dict_name,file):将Python数据写入JSON文件:
  
  ```python
  import json
  with open("file.json",'w') as file:
    json.dump(dict_name,file)
  ```

* load(file):读取json格式的文件,并转换值Python数据;

#### cvs

* 使用csv模块处理csv,,写入中文时,设置打开方式为utf-8;
* writerow([row_data]):一次写入一行数据;
  
  ```python
  import cvs
  with open(path,'w') as file:
    writer = cvs.writer(file)
    writer.writerrow(row_data)
  ```

* writerrows(<二级列表>):一次写入多行数据;
  
  ```python
  import cvs
  with open(path,'w') as file:
    writer = cvs.writer(file)
    writer.writerrows(<二级列表>)
  ```

* reader(file):读取CVS文件;
  
  ```python
  import cvs
  with open(path,'r') as file
    reader = cvs.reader(file)
  ```

### 内存回收

在Python中，使用引用计数的计数来实现跟踪和垃圾回收，当对象被创建时，就会有一个引用计数器记录被引用的次数，当次数变为0时，它就会被垃圾回收，但不是立即被回收。垃圾回收机制也可以处理循环引用，即循环垃圾收集器，作为计数器的补充；

## 上下文管理器

任何实现了__enter__()和__exit__()的对象都可以称为上下文管理器。可以使用contextmanger装饰器来实现。