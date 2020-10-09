# 爬虫学习

## 1. 网站检查

### 1.1 识别网站所用技术

`pip install builtwith`

~~~python
import builtwith
print(builtwith.parse('http://example.webscraping.com))
~~~

### 1.2 识别网站所有者

`pip install python-whois`

~~~py
import whois
print(whois.whois('baidu.com'))
~~~

## 2. 基础知识

### 2.1 序列化

把内存中的变量变成可存储或可传输的过程，就是序列化。

Python中几乎所有的数据类型都可以用pickle来序列化，序列化后的数据可读性差，人一般无法识别。

`cpickle`是用`C`语言编写的，据说比`pickle`快很多倍，在`Python3`中，`cpickle`已经更名为`_pickle`，可以直接使用`import _pickle as cpickle`。

