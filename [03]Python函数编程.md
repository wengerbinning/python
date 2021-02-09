# Python函数编程

[//]: # (__author__ = "Clark Aaron")

## 函数

函数实现某一具体功能的程序模块，Python中内置许多标准函数，我们也可以自定义函数，实现模块化编程。

### 函数的定义

* 函数的定义:

  ```python
  def <函数名称>(<参数>):
    <函数体>
    return  <返回值>
  ```

<!-- > 函数的参数: default argument values, keyword arguments(* arguments, **keywords), special parameter  -->

参数可以在函数间进行数据传输,多个参数以逗号隔开参数顺序为:必选参数、默认参数、可变参数、关键字参数、命名关键字参数;

1. 必选参数:

    ```python
    def function_name(var1, var2):
        print(var1,var2)
        return var1+var2
    ```

2. 缺省参数:带有默认值的参数,如果不给函数参数,则使用默认值,缺省参数必须位于普通参数之后,必须指向不变参数;
  
    ```python
    def function_name(var1, var2=10):
        print(var1,var2)
        return var1+var2
    ```

3. 命名参数:通过指定参数名传入 缺省参数:
  
    ```python
    def function_name(var1=None,var2=None):
        print(var1,var2)
        return var1+var2
    var = function_name(var1=1,var2=2)
    ```

4. 命名关键字参数,使用*作为一个分隔符,表示之后参数被视为命名关键字参数:
  
    ```python
    def func(var1, *, var2, var2):
        <函数体>
    ```

* 不定长参数:
  1. 元组不定长参数(可变参数)

      ```python
      def function_name(*args):
          print(type(args).__name__)
          return len(args)
      ```

  2. 字典不定长参数(关键字参数):

      ```python
      def function_name(**args):
          print(type(args).__name__)
          return len(args)
      ```

  * 拆包:将列表、元组、字典拆分成不定长参数传给函数:

    ```python
    list_name = [1,2,3,4]
    dictionary_name = {1:A, 2:B}

    function_name(*list_name, **dictionary_name)
    ```

> 函数的返回值: 使用return语句将参数返回
  
  ```python
  def function_name(var1, var2):
      return var1+var2, var1*var2
  ```

### 函数的参数

* 默认参参数
* 元组不定长参数args，*args：
* 字典不定长参数kwargs，**kwargs：

### 函数的返回

### 函数的应用

* 递归函数:函数体调用函数自身,由递归初始条件及递归公式组成,容易堆栈溢出;
  
  ```python
  def func(count):
      if( count == 1 ):
          return count
      else:
          return count+func(count-1)
  ```

* 尾递归优化:在函数返回值时,调用自身函数,并且返回值不能包括表达式,只会使用一个堆栈,大多数编程语言没有针对尾递归进行优化,Python也没有,也会堆栈溢出;
  
  ```python
  def fact(n):
    return fact_iter(n, 1)
  def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
  ```

* 匿名函数:即lambda函数;

  ```python
    retur_function = lambda var1, var2 : var1+var2
    print( return_function(1, 2) )
  ```

* 匿名函数作参数:

  ```python
  def function_name(var1, var2, function):
      print( function(var1, var2) )

  function_name(1, 2, lambda x, y: x*y)
  ```

* 闭包: 函数作为返回值: 闭包即当函数嵌套时,内部函数使用外部函数的的变量,且外部函数返回值时内部函数的引用,返回值为内部函数;

  ```python
  def func():
    def func0():
      value = 0
      return value
    return func0()
  ```

* 装饰器(Decorator): 即使用@语法将定义的函数传递到闭包中,装饰器一般由两层函数,外层接收被装饰的函数,内层接收被装饰函数的参数,也可以定义三层函数,增加最外一层接收装饰器的参数;
  
  ```python
  def fun(function):
      def fun1(x,y):
          print("闭包的内部函数")
          function(x,y)
      return fun1

  @fun
  def fun2(x, y):
      print("被装饰的函数")
      print(x,y,x+y)

  fun2(2,3)
  ```

* 高阶函数(Higher-order function)

  * 变量可以指向函数
  * 函数名也是变量
  * 函数作参数

* 偏函数

  * 在functools中提供许多函数,偏函数(Partial Function)是其中之一;
  * 偏函数可以固定函数的参数并返回函数;

    ```python
    func2 = functools.partial(func,var2=3) 
    ```
  
#### 内置函数

* map(func,< iterator >)将迭代器中的值依次传入func,并将返回值作为迭代器返回;

  ```python
  Iter = (i for i in range(0,10) )
  return_iter = map(func,Iter)
  ```

* reduce(func,<序列>):将序列的元素依次累计计算;

  ```python
  sum = reduce(func,list) #等同于 sum( sum(x1,x2),x3 )
  ```

* filter(func,<序列>)用于过滤序列,返回迭代器;

  ```python
  list_var = [1,2,3,4,5,6,7,8,9,0]
  return_iter = filter(func,list_var)
  ```

* sorted(list,key=value):对序列排序函数,通过key指定排序依据; 

## 装饰器  

### 装饰器的应用

* property装饰器：
* staticmethod装饰器：
* classmethod装饰器：
* contextmanager装饰器：在context模块中。
