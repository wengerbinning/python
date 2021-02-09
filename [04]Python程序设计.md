# Python程序设计

[//]: # (__author__ = "Clark Aaron")

OOP（Object Oriented Programming，面向对象编程）是高级语言的核心,是程序设计的一种思想；类是一类事物的抽象，包含了事物的属性与方法；而对象是程序的基本单元，是类创建的具体事物。
  
## 数据类型抽象

抽象即通过数据抽象与行为抽象形成ADT，然后通过自定义数据类型封装实现ADT的过程。其中ADT包含数据成员与方法成员。

## 数据类型封装

封装即通过编程语言支持的自定义数据类型实现抽象出来的ADT的过程，并通过访问权限的控制来保护数据成员。Python支持的自定义数据类型是类。

### 类的定义

类即Python的自定义数据类型。通过`class`来定义类。

* 类的定义：

  ```python
  class <class name>:
    < class member>
  ```

### 类的成员权限

类的成员由成员名的前缀来限制访问权限，前缀为`__`时，表示该成员为私有成员，对类外部隐藏；前缀为`_`时，表示该成员为保护成员，不能被import；缺省默认为公开成员，对类外部可见。

* 类的成员权限：
  
  ```python
  class <class name>:
    __<class private name>
    _<class protected name>
    <class public name>
  ```

### 类的属性成员

类的属性直接定义，可以被类型直接调用，被所有实例化对象共享，只有一份；类的实例属性一般会在构造方法中定义，不能被类型调用。

#### 魔法属性

* `__name__`：类名。
* `__doc__`：类的文档字符串。
* `__bases__`：该类的所有超类。
* `__module__`：类定义所在的模块。
* `__dict__`：包含了类的属性和方法，是一个字典类型的值。
* `__slots__`：限制类能添加的属性,将可以添加的属性赋值给属性即可,仅对当前类起作用;
  
  ```python
  __slots__ = ('name','age')
  ```

* @property属性：将返回属性值的方法包装称属性的方式。

* `hasattr(<Object>,<property>)`：检查类中是否有该属性。
* `getattr(<Object>,<property>)`：获取类的属性值。
* `setattr(<Object>,<property>)`：设置类的属性值。
* `delattr(<Object>,<property>)`：删除类的属性。

### 类的方法成员

类的方法成员是ADT的抽象方法，其本质是带有self参数的函数。

* 方法的定义：

  ```python
  def <function name>(self,<parameter list>):
      <function code>
  ```

  > Note：`self`标识类自身，并不是固定标识符，可以替换成其他任意字符。

#### 魔法方法

* 【方法】`__init__()`：是类的初始化方法，在实例化是自动调用来初始化类实例化的对象。

  ```python
  def __init__(self,<parameterList>):
      <funcCode>
  ```

* 【方法】`__len__()`：在使用`len()`函数时自动调用。

  ```python
  def __len__(self):
    <function code>
  ```

* 【方法】`__str__()`:在判断对象类型是自动调用,用户见;

  ```python
  ```

* 【方法】`__repr__()`:转化为供解释器读取的形式，在实例化时对象,调试服务;通常与__str__一样:`__repr__ = __str__`;

  ```python
  ```

* 【方法】`__iter__()`:用于for in 循环中的迭代,返回迭代对象,与__next__()配合使用;

  ```python
  ```

* 【方法】`__getitem__()`:是对象能按下标取值;

  ```python
  ```

* 【方法】`__cmp()`：用于对象比较。

  ```python
  ```

* 【方法】`__getattr__()`:在属性不存在时,尝试在__getattr__(self,<属性>)中获取返回值;

  ```python
  ```

* 【方法】`__call__()`:可以直接对实例本身进行调试,将对象按函数的方式调用,使用Callable()判断一个对象能否被调用;

  ```python
  ```

* 【方法】`__del__()`：是类的析构方法，在对象销毁之前调用，也可以使用`del <objectName>`来删除一个对象。

  ```python
   def __del__(self,<parameter>):
      <funcCode>
  ```

#### 类型方法

类型方法即添加@classmethmod装饰器来修改类属性。默认参数为__class__。

#### 静态方法

添加一个@staticmethmod装饰器来指定一个静态方法。没有任何默认参数。

> Note：更多定制方法,参考[文档](https://docs.python.org/3/reference/datamodel.html#special-method-names)

### 类的继承

类的继承是实现代码重用的方法，通过继承，字类具有超类所有的属性与方法；在继承的过程中，字类可以通过重写超类的方法来实现自己的方法。Python支持多继承。

* 类的继承：

  ```python
  class <subClass name>(superClass name):
      <classCode>
  ```

  > Note：在Python中定义类时，如果未指定继承的超类，则默认继承自Object类；并且字类没有重写超类的构造方法时自动调用，否则需要使用`super(<SubClass>,self).__init__(<parameterList>)`或者使用`<SuperClass>.__init__()`显式的调用超类的构造方法，其中超类可以指定多个，构成多重继承；可以使用`issubclass(<subclass>,<superclass>)`来检测两个类的关系。

* 方法的重写：方法的重写是子类重写，是子类对超类方法的重新定义，参数与返回值类型与超类一样。

### 类的多态

类通过继承实现多态。

## 扩展库的打包

Python具有大量的扩展包来帮助开发，每一个包中又包含多个模块，每一个模块的所有功能均在一个源文件中实现。扩展包是一类相关模块的集合，本质为一个文件夹，其中必须有一个`__init__.py`模块，在扩展包中的模块被导入时自动运行该模块。

* 在Python中一个文件即一个模块,通常以**包名.模块**的方式区分不同包中同一模块,提高程序的维护性;
* 模块的引入:

  ```python
  import <包名>.<模块> [as rename]
  import <包名>.<模块> [as rename1], <包名>.<模块> [as rename2], <包名>.<模块> [as rename3]
  from <包名>.<模块> import <函数或类>
  ```

* 【模块】`__init__.py`：当包或包下的模块被引入时,`__init__`.py会被Python解释器自动调用执行,作为一个包的标志,本身是一个模块,模块名即包名;

## 程序设计应用

### 枚举类

* 定义枚举

  ```python
  from enum import Enum

  Month = Enum(''Month,('Jan','Feb') )
  ```

* 自定义枚举(@unique确保无重复值):

  ```python
  from enum import Enum, unique
  @unique
  class Weekday(Enum):
      Sun = 0 # Sun的value被设定为0
      Mon = 1
      Tue = 2
      Wed = 3
      Thu = 4
      Fri = 5
      Sat = 6
  ```

#### 元类

* 使用type()创建类:
  
  ```python
  Hello = type('Hello', (object,), dict(hello=fn)
  ```

* 在使用class创建类时,同样是在扫描定义语法后使用type()函数创建;
* 元类(metaclass):先定义元类,创建类,创建实例;
* metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
  
  ```python
  class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
  ```

* 根据元类创建类:当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过`ListMetaclass.__new__()`来创建，
  
  ```python
  class MyList(list, metaclass=ListMetaclass):
    pass
  ```

* 适用于ORM(Object Relational Mapping)框架;