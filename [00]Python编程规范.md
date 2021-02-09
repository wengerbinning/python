# Python编程规范

[//]: # (__author__ = "Clark Aaron"Markdown+MathMarkdown+Math)

## 资料链接

* [Python官方网站](https://www.python.org/) ☛ <https://www.python.org>
  
  * [PEPs](https://www.python.org/dev/peps/) ☛ <https://www.python.org.dev/peps>
  
  > PEP（Python Enhancement Proposals，Python增强方案），PEP编号被确定后将不会改动，都是改自Guido van Rossum的
  > Python样式指南，又增加了Barry的样式指南。
  >
  > * [PEP 8: Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)给出了构成主要Python发行版中标
  >   准库的Python代码的编码约定。
  >
  > * [PEP 275: Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)描述了与Python文档字符串相关联的语义
      和约定。

一份适合的代码布局可以使阅读者更易于理解。

## 源码注释

注释为一个完整的句子，第一个单词首字母大写（除标识符之外）；推荐使用英语。

### 块注释

* 函数注释：

  ```python
  def munge(input: AnyStr): ...
  def munge() -> PosInt: ...
  def munge(sep: AnyStr = None): ...
  def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
  ```
  
### 行注释

### 文档注释

  ```python
  """Return a foobang

  Optional plotz says to frobnicate the bizbaz first.
  """
  ```

* 命名规则：

  1. 单个小写字母：a
  2. 单个大写字母：A
  3. 首字母大写的单词：Var
  4. 首字母小写的单词；var
  5. 小驼峰原则：varName
  6. 大驼峰原则：VarName
  7. 下划线原则：var_name
  8. 常量原则：VAR， VAR_NAME

### 变量的名称

3， 7

### 类的名称

4， 6

### 函数的名称



### 模块的名称

4

## 命名规范

### Dunder

* dunder即以`__<name>__`格式的变量：模块级的Dunder

  ```python
  """This is the example module.

  This module does stuff.
  """

  from __future__ import barry_as_FLUFL

  __all__ = ['a', 'b', 'c']
  __version__ = '0.1'
  __author__ = 'Cardinal Biggles'

  import os
  import sys
  ```

  > Note：` __future__ `模块的导入必须出现在除文档字符串之外的前面。

### 模块导入

模块的导入位于任何模块注释和文档字符串之后，以及模块全局变量和常量之前。应该按照标准模块、第三方模块、本地库的顺序导入，并在每个导入组间添加一个空行。标准库使用绝对导入，

* 使用import导入模块时，推荐使用：

  ```python
  import os
  import sys
  from subprocess import Popen, PIPE
  ```

* 绝对导入：

  ```python
  import mypkg.sibling
  from mypkg import sibling
  from mypkg.sibling import example
  ```

* 相对导入：

  ```python
  from . import sibling
  from .sibling import example
  ```

### 表达式间的空格

* 表达式间的空格：

```python
spam(ham[1], {eggs: 2})
foo = (0,)
if x == 4: print x, y; x, y = y, x
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]
spam(1)
dct['key'] = lst[index]
x = 1
y = 2
long_variable = 3
```

### 尾逗号

* 尾逗号的使用：

  ```python
  FILES = ('setup.cfg',)

  FILES = [
      'setup.cfg',
      'tox.ini',
      ]
  initialize(FILES,
            error=True,
            )


  ```

```python
import keyword            #引入keyword模块
print(keyword.kwlist)     #打印模块中的列表kwlist
```

## 源码格式

### 缩进

缩进推荐使用4个空格实现缩进，缩进是Python区分代码块的依据；空格也是首选的缩进方法，Python 3不允许在缩进中混合使用制表符和空格；当使用-t选项调用Python 2命令行解释器时，它会发出关于非法混合制表符和空格的代码的警告。当使用-tt时，这些警告变成错误。强烈推荐这些选项!

* 连续行应该使用Python的隐式行连接括号、方括号和大括号，或者使用悬挂缩进对包装的元素进行垂直对齐。在使用悬挂缩进时，应考虑以下因素;在第一行应该没有参数，进一步的缩进应该被用来清楚地区分自己是一个延续行：

  ```python
  # Aligned with opening delimiter. And arguments on first line forbidden when not using vertical alignment.
  foo = long_function_name(var_one, var_two,
                          var_three, var_four)

  # Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
  def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

  # Hanging indents should add a level.
  foo = long_function_name(
      var_one, var_two,
      var_three, var_four)
  ```

* 当条件一个if语句的一部分足够长要求编写跨多个行,值得注意的是,两个字符的组合关键字(即如果),加上一个空格,加上开括号创建一个自然4空格缩进的后续行多行条件。这可能会与嵌套在if语句中的缩进代码集产生视觉上的冲突，该代码集自然也会缩进为4个空格。对于如何(或者是否)进一步从if语句中的嵌套套件中在视觉上区分这些条件行，PEP不采取明确的立场。在这种情况下可以接受的选择包括但不限于:

  ```python
  # No extra indentation.
  if (this_is_one_thing and
      that_is_another_thing):
      do_something()

  # Add a comment, which will provide some distinction in editors
  # supporting syntax highlighting.
  if (this_is_one_thing and
      that_is_another_thing):
      # Since both conditions are true, we can frobnicate.
      do_something()

  # Add some extra indentation on the conditional continuation line.
  if (this_is_one_thing
          and that_is_another_thing):
      do_something()
  ```

* 在多行结构中，右大括号/括号/圆括号可以在列表最后一行的第一个非空白字符下面：

  ```python
  my_list = [
      1, 2, 3,
      4, 5, 6,
      ]
  result = some_function_that_takes_arguments(
      'a', 'b', 'c',
      'd', 'e', 'f',
      )
  # or
  my_list = [
      1, 2, 3,
      4, 5, 6,
  ]
  result = some_function_that_takes_arguments(
      'a', 'b', 'c',
      'd', 'e', 'f',
  )
  ```

### 行宽

所有代码行长度限制在79个字符以下，对于输出结构限制较少的长文本块(文档字符串或注释)，行长度应限制为72个字符；限制所需的编辑器窗口宽度可以让几个文件同时打开，并且当使用在相邻列中显示两个版本的代码审查工具时工作得很好。该限制是为了避免在窗口宽度设置为80的编辑器中换行，因为一些基于web的工具可能根本不提供动态行包装。有些团队更喜欢长行，对于专门或主要由能够在这个问题上达成一致的团队维护的代码，可以将行长度限制增加到99个字符，前提是注释和文档字符串仍然包装为72个字符。Python标准库比较保守，要求行数限制在79个字符(文档字符串/注释限制在72个字符)。

包装长行的首选方法是在圆括号、方括号和大括号内使用Python的隐含行延续。通过将表达式包装在括号中，可以将长行拆分为多行。这些应该优先使用，而不是使用反斜杠进行行继续。

* 有时反斜杠仍然是合适的。例如，长、多个with-语句不能使用隐式延续，所以反斜杠是可以接受的：

  ```python
  with open('/path/to/some/file/you/want/to/read') as file_1, \
      open('/path/to/some/file/being/written', 'w') as file_2:
      file_2.write(file_1.read())
  ```

* 运算符在多行中的处理遵循Donald Knuth样式：运算符前断行。

  ```python
  # easy to match operators with operands
  income = (gross_wages
            + taxable_interest
            + (dividends - qualified_dividends)
            - ira_deduction
            - student_loan_interest)
  ```

### 空行

在定义的类和函数前后各增加一个空行，在定义类的方法时仅在方法前添加一个空行。
