# Python软件测试

[//]: # (__author__ = "Clark Aaron")

软件是包含程序与数据文档的整体运行环境；程序包括所有实现该软件功能的所有源码，数据文档包含配置文件、说明文档等内容。

## 文档生成

文档生成是指提取源码中的文档注释来生成一份说明文档。

## 软件测试

软件测试的方法有黑盒测试、白盒测试；根据测试状态又可以分为静态测试与动态测试。Python提供doctest模块与unittest框架来进行测试。

### doctest

doctest根据字符文档中的格式来对独立单元进行测试：

* 嵌入源码测试：

  ```python
  def Sum(a,b):
      """
      >>>Sum(1,2)
      3
      >>>Sum(2,3)
      5
      """
      return a+b
  
  if __name__ == "__main__":
      import doctest
      doctest.testmod(verbose=True)
  ```

  > 在程序执行时，会将字符文档中的内容放到python交互终端中执行并与之后的结果进行比较。

* 分离测试文件：

  ```python
  # sum.test
  >>> from sum import Sum
  >>>Sum(1,2)
  3
  >>>Sum(2,3)
  5
  ```

  > Note：编辑完上面文件后使用`python -m doctest -v sum.test`来执行该测试。

### unittest

uinttest是python提供一个测试框架。

* 使用unittest进行单元测试:
  
  ```python
  import unittest

  from mydict import Dict

  class TestDict(unittest.TestCase):

      def test_init(self):
          d = Dict(a=1, b='test')
          self.assertEqual(d.a, 1)
          self.assertEqual(d.b, 'test')
          self.assertTrue(isinstance(d, dict))

      def test_key(self):
          d = Dict()
          d['key'] = 'value'
          self.assertEqual(d.key, 'value')

      def test_attr(self):
          d = Dict()
          d.key = 'value'
          self.assertTrue('key' in d)
          self.assertEqual(d['key'], 'value')

      def test_keyerror(self):
          d = Dict()
          with self.assertRaises(KeyError):
              value = d['empty']

      def test_attrerror(self):
          d = Dict()
          with self.assertRaises(AttributeError):
              value = d.empty

  ```

  * 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行;对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的;
* 运行单元测试:
* 测试模块最后增加以下两句并执行,或使用-m unittest参数执行文件;
  
  ```python
  if __name__ == '__main__':
    unittest.main()
  ```

* 在测试类中可以增加setUp()tearDown()方法,分别在测试前与测试后自动调用;

## 测试阶段

### 单元测试

即针对实现某一特定功能的模块进行测试。

### 集成测试

集成测试是单元测试的下一个阶段，是指将通过测试的单元模块组装成系统或子系统，再进行测试，重点测试不同模块的接口部分。

### 系统测试

系统测试指的是将整个软件系统看作一个整体进行测试，包括对功能、性能，以及软件所运行的软硬件环境进行测试。

### 验收测试

验收测试可以分为α测试与β测试；α测试是用户、测试人员、开发人员参与的内部测试，β测试是交由用户的公开测试。