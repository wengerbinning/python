# Python

[//]: # (__author__ = "Clark Aaron")

Python是一种面向对象的解释型编程语言,是由Guido van Rossum开发,并于1991年发布第一个公开发行版.

## 资源链接

* [官方网站](https://www.python.org/) ☛ <https://www.python.org/>

  1. [官方介绍](https://www.python.org/about/) ☛ <https://www.python.org/about/>
  2. [官方文档](https://docs.python.org/3/) ☛ <https://docs.python.org/3/>

* [廖雪峰网站](https://9www.liaoxuefeng.com/) ☛ <https://www.liaoxuefeng.com/wiki/1016959663602400/1017497232674368>

* [Segmentfault](https://segmentfault.com/) ☛ <https://segmentfault.com/>
  
  1. [迭代器](https://segmentfault.com/a/1190000013460584) ☛ <https://segmentfault.com/a/1190000013460584>

## 目录结构

该目录结构是按照我自己学习Python的进度管理的。

  01. [Python数据结构]([01]Python数据结构.md) ☛ [**[01]Python数据结构.md**]([01]Python数据结构.md)
  02. [Python流程结构]([02]Python流程结构.md) ☛ [**[02]Python流程结构.md**]([02]Python流程结构.md)
  03. [Python函数编程]([03]Python函数编程.md) ☛ [**[03]Python函数编程.md**]([03]Python函数编程.md)
  04. [Python程序设计]([04]Python程序设计.md) ☛ [**[04]Python程序设计.md**]([04]Python程序设计.md)
  05. [Python异常处理]([05]Python异常处理.md) ☛ [**[05]Python异常处理.md**]([05]Python异常处理.md)
  06. [Python系统管理]([06]Python系统管理.md) ☛ [**[06]Python系统管理.md**]([06]Python系统管理.md)
  07. [Python软件测试]([07]Python软件测试.md) ☛ [**[07]Python软件测试.md**]([07]Python软件测试.md)
  08. [Python的多任务]([08]Python的多任务.md) ☛ [**[08]Python的多任务.md**]([08]Python的多任务.md)
  09. [Python网络编程]([09]Python网络编程.md) ☛ [**[09]Python网络编程.md**]([09]Python网络编程.md)

## 学习日志

* Python应用领域有运维开发、后端开发、数据分析（数据采集+数据分析+量化交易）、人工智能(机器学习+深度学习)、网络爬虫、网站开发、自动化测试、页面开发、游戏开发、就业方向、Python全栈开发工程师、爬虫工程师、数据分析工程师、数据挖掘工程师、机器学习工程师、人工智能工程师。Python开发案例有Tencent、NASA、知乎、YouTube、Instagram、豆瓣、例如Google、Yahoo、NASA大量使用Python。

#### python 库安装源

阿里云 http://mirrors.aliyun.com/pypi/simple/ 
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/ 
豆瓣(douban) http://pypi.douban.com/simple/ 
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/ 
中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

```cmd
python -m pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com 
```

* 在py文件中编译py文件:

```python
import py_compile
py_compile.compile(<Pythonfilename>)
```

```bash
python -O-m py_compile <pythonfilename>
```

### Python用户自定义模块安装位置

在python的安装装目录下有一个`lib/site.py`文件,将在文件中的USER_BASE与USER_SITE修改为自定义的位置,并且当前用户必须拥有这两个文件完全控制权限.通过`python -m site`来查看路径是否修改成功.

### PEP

### PEP 0

### PEP 8

This is Style Guide for Python Code,writing by Guido van Rossum, Barry Warsaw, Nick Coghlan.

* Introduction

This document gives coding conventions for the Python code comprising the standard library in the main Python distribution. Please see the companion informational PEP describing style guidelines for C code in the C implementation of Python.

This document and PEP 257 ware adpated form Guido's original Python style Guide essay, with some additions from Barry's style guide.

This style guide evolves over time as additional conventions are identified and past conventions are rended obsolete by changes in the language itself.

* A foolish consistency is the Hobgoblin of Little Minds
* Code Lay-out
 
  1. Use 4 spaces per indentation level,the 4-space rule is optional for continuation lines;
  2. The closing brace/bracket/parenthesis onn multiline constructs may either line up under the first non-whitespace character of the last line of list or it may be lined up under the first character of the line that start the multiline construct;
  3. Spaces are the perferred indentation method,Tabs should be used solely to remain consistant with code that is already indented with tabs,Python3 disallows mixing the use of tabs and spaces for indentation.
  4. Maximum Line Length: Limit all lines to a maximumof 79 characters.
  Blank Lines: Surround top-level function and class definitions with two blank lines.
  5. Source file encoding: utf-8;
  6. Import: import should usually be on separate lines,import are always put at the top of file ,just after any module comments and docstrings,and before moudle globalsand constants,and Import should be frouped in the following order(you should put a blank line between each group of imports);
    
    * Standard library imports;
    * Relate third party imports;
    * local application/library specific imports;

  7. Module level dunder(names with two leading and two trailing undescores) names.for eaample:

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
  8. For triple-quoted strings,always use double quote characters to be consistent with the docstring convention

* Whitespace in Expressions and statements

  1. Avoid extraneous whitespace in the following situations;
  2. Function annotations should use the normal rules for colons and always have sapces around the -> arrow if present.

  ```python
  # Correct:
  def munge(input: AnyStr): ...
  def munge() -> PosInt: ...
  ```
  3. Trailing Commas: making a tupleof one element,

* Comments:

  1. Block Comments: Block comments generally apply to some code that follows them, and are indented to the same level as that code,each line of a block comment starts with a `#` and a single space.
  2. Inline Comments: Use inline comments sparingly,.
  3. Documentation Strings(PEP 257):  This comment should appear after the `def`line.

* Naming Conventions: 

* Function Annotations: PEP 484 
* Variable Annotations: PEP 526
