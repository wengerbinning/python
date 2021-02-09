# bs4

[//]: # (__author__ = "Clark Aaron")
[//]: # (__version__ = "v0.0")

bs4是一个虚拟库，其官方名是beautifulsoup4；而beautifulsoup4是一个快速提取网页信息的库，是基于html与xml解析器之上的，提供了迭代、提取、修改解析树的API。

* `BeautifulSoup(<document>,<parser>,<from_encoding>) -> BeautifulSoup`：BeautifulSoup的构造函数，返回一个BeautifulSoup对象。

  > * `document`：指网页文档，包括html、xml，仅xml解析器支持xml解析。
  > * `parser`：语法解析器，包括html.parser、lxml、xml、html5lib四个解析器。
  >
  >   * `html.parser`：Python的内置标准库，执行速度适中，文档容错能力强。
  >   * `lxml`：速度快，文档容错能力强。
  >   * `xml`：速度快，唯一支持xml文档的解析器。
  >   * `html5lib`：容错性最好，以浏览器的方式解析文档，生成html5格式的文档。
  >
  > * `from_encoding`：指定解析的编码格式。
  > * `BeauifulSoup`：函数的返回值，是一个BeautifulSoup对象，其文档首先会被转换成Unicode编码，然后使用解析器来解析成一个复杂的树结构，树的节点可以分为四大类：Tag、navigableString、BeautifulSoup、comment。

* `BeautifulSoup`：解析生成的对象。

  * `Tag`：与HTML的标签相同。
  * `navigableString`：包装Tag中的字符串，使用replace_with()方法，无子节点。
  * `BeautifulSoup`：文档的全部内容。
  * `comment`：是一个特殊的navigableString对象，

* `<BeautifulSoup>.<Tag>`：提取文档中第一个Tag标签。
* `<Tag>.contents`：将所有直接子节点以列表形式返回。
* `<Tag>.children`：返回所有直接子节点的生成器。
* `<Tag>.descendants`：返回所有子节点的生成器。
* `<Tag>.string`：如果Tag只有一个navigableString类型的子节点，则可以使用string属性，否则返回None。
* `<Tag>.strings`：返回tag中所有navigableString。
* `<Tag>.stripped_strings`：返回tag中所有navigableString，并去除多余空白内容。
* `<Tag>.parent`：获取标签的父节点。
* `<Tag>.parents`：获取标签的所有父节点。
* `<Tag>.next_sibling`：获取标签的下一个兄弟节点，一般为空白符，下下一个兄弟节点才是。
* `<Tag>.previous_sibling`：获取标签的上一个兄弟节点。
* `<Tag>.next_siblings`：获取标签的下方所有兄弟节点。
* `<Tag>.previous_siblings`：获取标签的上方所有兄弟节点。
* `<Tag>.next_element`：当前解析对象的下一个解析对象。
* `<Tag>.previous_element`：当前解析对象的上一个解析对象。
* `<Tag>.next_elements`：迭代器。
* `<Tag>.previous_elements`：迭代器。

* `<BeautifulSoup>.find(<tag>,<attrs>,<recursive>,<string>,<**kargs>)`：tag过滤器，寻找指定条件的tag。

  * `tag`：搜索的标签名，可以是re.compile()生成的正则表达式对象，会以re.match()匹配；也可以是多个标签名的列表；可以是bool，也可以是一个返回bool的函数。
  * `attrs`：指定的属性条件。
  * `attrs`：通过指定一个字典类型的参数指定属性。
  * `**kargs`：将该参数均当作tag的属性处理，class是python的关键字，只能使用class_来使用CSS选择。
  * `limit`：限定搜索数量。
  * `id`
  * `class_`
  * `recursive`：默认会搜索所有子节点，设置recursive为false，则只搜索直接子节点

* `<BeautifulSoup>.find()`：与find_all()相同，但是只搜索第一条。
* `find_parent()`
* `find_parents()`
* 
  