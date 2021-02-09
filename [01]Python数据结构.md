# Python数据结构

[//]: # (__author__ = "Clark Aaron")

Python是一个类型判断的编程语言。

## 数据对象

数据对象即计算机具有实际内存空间的数据，根据数据的可变性可以分为变量与常量。

### 数据变量

数据变量即存储内容可以改变的数据对象。

### 数据常量

即数据类型不可以改变的数据对象。

### 对象的序列化

* 序列化:将变量从内从中变成可存储或传输的过程;
* 反序列化:将变量的内容从序列化的对象读到内存里称为反序列化;
* 使用 pickle 模块实现序列化;
* 对象序列化:
  ```
  >>> import pickle
  >>> d = dict(name='Bob', age=20, score=88)
  >>> pickle.dumps(d)
  b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'
  ```
  * pickle.dumps()将任意对象序列化成一个bytes,可以写入一个file-like Object中:
  ```
  >>> f = open('dump.txt', 'wb')
  >>> pickle.dump(d, f)
  >>> f.close()
  ```
* 反序列化:
  ```
  >>> f = open('dump.txt', 'rb')
  >>> d = pickle.load(f)
  >>> f.close()
  >>> d
  {'age': 20, 'score': 88, 'name': 'Bob'} 
  ```

## 数据类型

### 数值类型

* `int`:
* `float`:
* `complex`:

### 字符类型

* `str`

* 字符串由一组引号包含,为不可变类型:
  
  ```python
  STRING = "ABCDEFGHIJKLMNOPQRSTUVQWXYZ"
  ```

* 字符串一般为常量,不可改变,在给字符串变量赋值时,只是将变量名指向新建的数据空间;
* 字符串切片(Slice):

#### 字符串格式化

```python
name = "ClarkAaron"
age = 21
hight = 178.5
```

* 拼接字符串:
  
  ```python
  print( "名字: ",name + '\n' + "年龄: ",str(age) + '\n' + "身高: ",str(hight) )
  ```

* 使用格式化符号:
  
  | 符号 | 说明 | 符号 | 说明 | 符号 | 说明 | 符号 | 说明 |
  |:---- |:---- |:----- |:------ |:---- |:---- |:----- |:------ |
  | %d | 有符号十进制整数格式化 | %f | 浮点数格式化 | %s | 字符串格式化 | %x | 十六进制整数 |
  
  ```python
  print( "名字: %s \n年龄: %d \n身高: %.2f" %(name, age, hight) )
  ```

* 使用format格式化函数
  
  ```python
  print("名字: {} \n年龄: {} \n身高: {:.2f}".format(name, age, hight) )
  ```

#### 字符串的内置方法
  
| 函数名 | 说明 | 返回值 |
|:----- |:----- |:----- |
| find(str[,start,end]) | 查找指定子字符串 | 找到返回第一个子字符串的的起始索引,否则返回-1 |
| count(str[,start,end]) | 统计子字符串的个数 | 返回字符串中子字符串的个数 |
| replace(old,new[,count]) | 将子字符串替换为新的字符串 | 返回替换过的新字符串 |
| split(sep[,maxsplit]) | 按指定分隔符将字符串分割成子字符串 | 返回子字符串的列表 |
| startwith(prefix[,start,end]) | 判断字符串是否以指定的前缀开头 | 返回布尔值 |
| endwith(suffix[,start, end]) | 判断字符串是否以指定的后缀结束 | 返回布尔值 |
| upper() | 将所有字符串大写 | 返回布尔值 |
| lower() | 将所有字符串小写 | 返回布尔值 |
| join(<序列>) | 将序列的元素拼成一个字符串 | 返回字符串 |
| strip(char) | 去掉字符串开头和结尾的指定字符与空白字符 | 返回字符串 |

#### 转义字符
* '\'可以将普通字符转义成为特殊字符;
* Python默认会将字符转义,使用r前缀可以设置默认字符串不转义;
* '%'转义字符;

### 元组类型

* `tuple`:
* 一种特殊的序列,为不可变类型;
* 元组定义:

  ```python
  # tuple_name = tuple()
  tuple_name = ()
  ```

* 元组元素提取同列表;

### 列表类型

* `list`:

* 列表是有序的数据集合,是可修改数据类型,由元素与对应的下标组成;
* 列表的定义:
  
  ```python
  # list_name = list()
  list_name = []
  ```

* 列表元素提取:
  
  ```python
  list_name[index]
  ```

* 列表添加元素:
  
  ```python
  list_name.append(value)               #列表尾部添加
  list_name.insert(index, value)        #列表指定位置添加
  list_name.extend()                    #将列表中添加另一列表的所有元素
  list_name = list_name1 + list_name2   #拼接两列表形成新的列表
  ```

* 列表中元素的修改:
  
  ```python
  list_name[index] = new_value
  ```

* 列表中元素的删除:
  
  ```python
  del list_name[index]          # 根据索引删除;
  list_name.remove(value)       # 根据元素删除;
  list_name.pop(index)          # 删除指定索引的值,默认最后一个,并返回删除值;
  ```

* 列表切片
  
  ```python
  list_name[start:end:step]     #对列表切片,并返回一个新列表
  ```

* 列表排序
  
  ```python
  list_name.sort(reverse)       #对列表进行排序,默认升序(reverse=False);
  ```

### 字典类型

* `dict`:

* 用于存储key-value键值对形式的数据,是值可变数据类型,关键字时=是不可变数据类型;
* 字典的定义:

  ```python
  dictionary_name = {key:value[,key0:value0]}
  ```

* 字典的查询:

  ```python
  dictionary_name[key]      # 返回字典中key对应的值,必须确保key在字典中存在;
  dictionary_name.get(key[,<不存在时返回的默认值>])  # 返回字典中的key对应的值,不存在时返回None;
  ```

* 字典键值对的添加与修改:

  ```python
  dictionary_name[key] = value
  ```

* 字典键值对的删除:

  ```python
  del dictionary_name[key]
  ```

* 字典中的遍历:

  ```python
  dictionary_name.keys()    #获取字典中所有的key
  dictionary_name.values()  #获取字典红所有的value
  dictionary_name.items()   #获取每一对键值对组成的元组
  ```

### 集合类型

* 无序存储任意类型集合,元素具有唯一性;
* 集合的定义:

  ```python
  # set_name = set()
  set_name = {}
  ```

* 集合元素的添加:

  ```python
  set_name.add(value)        #向集合中添加元素
  set_name.update(<序列>)     #将虚序列中每一个元素添加进集合
  ```

* 集合元素的删除:

  ```python
  set_name.remove(value)        #确保元素存在
  set_name.discard(value)       #无限制
  set_name.pop(value)           #随机删除元素并返回
  ```

* 集合的运算:

  ```python
  set_name3 = set_name1 & set_name2     # 交集
  set_name4 = set_name1 | set_name2     # 并集
  set_name5 = set_name1 - set_name2     # 差集
  ```

### 抽象类型

在Python只有一个类支持抽象数据类型的实现，即抽象类型就是抽象类；是我们可以自定义的数据类型。

* `class`：

## 数据转换

数据的转换涉及数值的进制转换与数据的类型转换。

### 进制转换

* 在进制转换时,也可以使用hex()、int()、oct()、bin()函数进行转换;

* 在计算机中使用到的进制有十六进制、十进制、八进制、二进制，其表示方法如下表:
  | 进制 | 前缀 | 字符集 |
  |:----:|:----:|:------ |
  | 十六进制 | `{0X|0x}` | `{0~9,A~F}` |
  | 十进制 | `-` | `{0~9}` |
  | 八进制 | `{0O|0o}` | `{0~7}` |
  | 二进制 | `{0B|0b}` | `{0,1}` |

### 类型转换

* int()
* float()
* str()
* tuple()
* list()
* set()
* ord()
* long()
* complex()
* repr()
* eval()
* chr()
* unichr()
* hex()

* types:可以判断对象是否是函数;
* isintance()
* dir()
* setatter()
* getattr()
* hasattr()

## 数据运算

### 算数运算符

* `**`：数值的幂运算。
* `*`数值的乘积运算。
* `/`：数值的除法运算。
* `//`：数值的整除运算。
* `%`：数值的取余运算。
* `+`：数值的加法运算。
* `-`

### 关系运算符

* `==`
* `!=`
* `>`
* `<=`
* `<`
* `>=`
* `is`
* `is not`

### 布尔运算符

* `and`
* `or`
* `not`

### 赋值运算符

* `=`
* `*=`
* `/=`
* `//=`
* `%=`
* `+=`
* `-=`

* 具有不同标识的类的实例比较结果通常为不相等，除非类定义了 __eq__() 方法;
* 一个类实例不能与相同类或的其他实例或其他类型的对象进行排序，除非该类定义了足够多的方法，包括 __lt__(), __le__(), __gt__() 以及 __ge__() (而如果你想实现常规意义上的比较操作，通常只要有 __lt__() 和 __eq__() 就可以了);
* is 和 is not 运算符无法自定义；并且它们可以被应用于任意两个对象而不会引发异常;
* 还有两种具有相同语法优先级的运算 in 和 not in，它们被 iterable 或实现了 __contains__() 方法的类型所支持;
* 逻辑值检测: 任何对象都可以进行逻辑值的检测，以便在 if 或 while 作为条件或是作为下文所述布尔运算的操作数来使用。一个对象在默认情况下均被视为真值，除非当该对象被调用时其所属类定义了 __bool__() 方法且返回 False 或是定义了 __len__() 方法且返回零.
* 基本完整地列出了会被视为假值的内置对象:被定义为假值的常量: None 和 False;任何数值类型的零: 0, 0.0, 0j, Decimal(0), Fraction(0, 1);空的序列和多项集: '', (), [], {}, set(), range(0).

## 生成器

* 生成器(generator):用于按需生成元素的对象;
* 可以使用next()方法获取下一个值;
* 方法一(生成器表达式):使用生成式返回生成器
  
  ```python
  geerator = ( x*x for x in range(0,10) )
  ```

* 方法二(生成器函数):使用yield返回一个生成器
  
  ```python
  def func(var1):
      for index in range(0,var1):
          yield index
  ```

* 方法三(生成器工厂函数):返回生成器的函数,可以没有yield关键字;

### 生成表达式

* 列表生成式:
* 字典生成式:
* 集合生成式:

## 迭代器  

* 迭代器(iterator):用于从序列取出元素的对象,每一个元素仅可迭代一次,迭代器用于遍历与拆包,使用isinstance()函数判断对象是否为Iterator,生成器都是Iterator对象,list,dict,str不是iterator,可以使用iter()函数将list,dict,str转换为iterator;

#### 可迭代对象

* 可迭代对象:当对象实现__iter__()或__getitem__()函数时,可以称为可迭代对象,序列均为可迭代对象;

#### 列表生成式( List Comprehensions):

* 举例:

  ```python
  list = [x*x for x in range(1,11)]
  lists = [m+n for m in 'ABC' for n in 'XYZ']
  ```
