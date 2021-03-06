
python2.x默认不支持中文
ASCII字符值包含256个字符，不支持中文

# 解释器python/python3

```python
# 使用python 2.x解释器
python xxx.py

# 使用python 3.x解释器
python3 xxx.py
```

# 注释
单行注释（行注释）
```python
# xxxxx
```

多行注释（块注释）
```python
"""
"""
```
什么时候需要注释

1. 注释不是越多越好，对于一目了然的代码，不需要添加注释
2. 对于复杂的操作，应该在操作开始前写上若干行注释
3. 对于不是一目了然的代码，应该在其行尾添加注释（注释应该至少离开代码2个空格）
4. 绝不要描述代码，假设阅读的代码比你更懂Python，他只是不知道你的代码要做什么？

# 算数运算符
## 01.算术运算符
|运算符|描述|
|:-:|:-:|
|+|加|
|-|减|
|*|乘|
|/|除|
|//|取整数|
|%|取余数|
|**|幂运算|

## 02.运算符的优先级
+ 先乘除后加减
+ 同级运算符是从左至右计算
+ 可以使用()调整优先级

|运算符|描述|
|:-:|:-:|
|**|幂(优先级最高)|
|* / % //|乘、除、取余数、取整数|
|+ -|加法、减法|

# 高级变量类型
## 目标
+ 列表
+ 元组
+ 字典
+ 字符串
+ 公共方法
+ 变量高级

## 知识点回归
+ python中数据类型可以分为数字型和非数字型
+ 数字型
  + 整型(int)
  + 浮点型(float)
  + 布尔型(bool)
    + 真`True` `非零数` --非零即真
    + 假`False` `0`
  + 复数型(complex)
    + 主要用于科学计算
+ 非数字型
  + 列表
  + 元组
  + 字典
  + 字符串

在python中，所有非数字型变量都支持以下特点
1. 都是一个序列`sequence`，也可以理解为容器
2. 取值`[]`
3. 遍历`for in`
4. 计算长度、最大/最小值、比较、删除
5. 链接`+`和重复`*`
6. 切片

参考： https://www.cnblogs.com/gengcx/category/987813.html


# 01 列表
## 1.1 列表的定义
+ `list`(列表)是python中使用最频繁的数据类型
+ 专门用于存储一串信息
+ 列表用`[]`定义，数据之间使用`,`分隔
+ 列表的索引从`0`开始
> 注意：从列表中取值时，如果超出索引范围，程序会报错

## 1.2 列表的常用操作
|方法名|作用|描述|
|:-|:-|:-|
|**L.append(object) -> None**|append object to end|向列表末尾进行追加元素|
|**L.clear() -> None**|remove all items from L|删除列表中所有的值|
|**L.copy() -> list**|a shallow copy of L|复制(浅复制)一个列表|
|**L.count(value) -> integer**|return number of occurrences of value|统计一个值(value)在一个列表中(list)出现的次数(发生的次数|
|**L.extend(iterable) -> None**|extend list by appending elements from the iterable|合并两个列表|
|**L.index(value, [start, [stop]]) -> integer**|return first index of value|查找指定元素在列表中的位置，index()方法必须指定第一个参数，要查找哪个值在列表中的位置，也可以指定查找的起始位置；如果查找不到，系统会报错|
|**L.insert(index, object)**|insert object before index|向列表中指定的位置添加元素，有两个参数，index(索引位置)，object(值）,向列表中指定位置的前面添加元素，占用原来元素的位置|
|**L.pop([index]) -> item**|remove and return item at index (default last)|弹出指定位置（默认是最后一个）的元素|
|**L.remove(value) -> None**|remove first occurrence of valu|移除列表中第一个出现的指定的值|
|**L.reverse()**|reverse *IN PLACE*|列表的元素进行颠倒|
|**L.sort(key=None, reverse=False) -> None**|stable sort *IN PLACE*||
|**del操作**|del[index]|删除列表中的元素，这是关键字操作|


|序号|分类|关键字/函数/方法|说明|
|:-|:-|:-|:-|
|1 |增加|列表.insert(索引,数据)|在指定位置插入数据|
|  |  |列表.append(数据)|在末尾追加数据|
|  |  |列表.extend(列表2)|将列表2的数据追加到列表|
|2 |修改|列表[索引]=数据|修改指定索引的数据|
|3 |删除|del 列表[索引]|删除指定索引的数据|
|  |  |列表.remove[数据]|删除第一个出现的指定数据|
|  |  |列表.pop|删除末尾数据|
|  |  |列表.pop(索引)|删除指定索引数据|
|  |  |列表.clear|清空列表|
|4 |统计|len(列表)|列表长度|
|  |  |列表.count(数据)|数据在列表中出现的次数|
|5 |排序|列表.sort()|升序排序|
|  |  |列表.sort(reverse=True)|降序排序|
|  |  |列表.reverse()|逆序、反转|

## 1.3 演练
### index(value)方法
```python
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list.index(4)
3
>>> my_list.index(0)  # 如果没有找到会报错
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 0 is not in list
```

### insert(索引,数据)方法
```python
# 向指定位置的前面插入元素
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list.insert(2, 'a')
>>> my_list
[1, 2, 'a', 3, 4, 5]
# 如果指定位置超过列表的长度，就插入到最后一个位置
>>> my_list.insert(20, 'b')
>>> my_list
[1, 2, 'a', 3, 4, 5, 'b']
```
###  append()方法
```ipython
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list.append('a')
>>> my_list
[1, 2, 3, 4, 5, 'a']
```
### extend()方法
```python
# 合并两个列表
>>> my_list = [1, 2, 3, 4, 5]
>>> temp_list = ['a', 'b', 'c']
>>> my_list.extend(temp_list)
>>> my_list
[1, 2, 3, 4, 5, 'a', 'b', 'c']
```
### 修改列表元素
```python
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list[0] = 'a'
>>> my_list
['a', 2, 3, 4, 5]
```
### 删除列表元素
```python
>>> my_list = [1, 2, 3, 4, 5]
>>> del my_list[0]
>>> my_list
[2, 3, 4, 5]
```
### remove(value)
```python
# 删除第一个出现的value值
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list.remove(4)
>>> my_list
[1, 2, 3, 5]
>>> my_list.remove(4)  # 若没有找到会报错
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>>
```
### pop([index])方法
```python
# pop()不带参数默认删除最后一个
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list.pop()
5
>>> my_list
[1, 2, 3, 4]

# pop(index)删除指定位置上的值
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list.pop(3)
4
>>> my_list
[1, 2, 3, 5]
```
### clear()方法
```python
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list.clear()
>>> my_list
[]
```
### sort()方法
```python
>>> my_list = [1, 3, 5, 2, 4]
>>> my_list.sort()
>>> my_list
[1, 2, 3, 4, 5]
>>> my_list.sort(reverse=True)
>>> my_list
[5, 4, 3, 2, 1]
```
### reverse()方法
```python
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list.reverse()
>>> my_list
[5, 4, 3, 2, 1]

```
## 关键字、函数和方法
关键字是python内置的、具有特殊意义的标识符
```python
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> print(len(keyword.kwlist))
35
```
> 关键字后面不需要使用括号

函数封装了独立功能，可以直接调用

`函数名(参数）`
> 函数需要死记硬背
+ 方法和函数类似，同样是封装了独立的功能
+ 方法需要通过对象来调用，表示针对这个对象要做的操作

`对象.方法名(参数)`

在变量后面输入`.`，然后针对这个变量要执行的操作，记忆起来比函数要简单多了

## 1.4 循环遍历
+ 遍历就是从头到尾以此从列表中获取数据
  + 在循环体内部针对每一个元素，执行相同的操作
+ 在python中为了提高列表的遍历效率，专门提供了迭代iteration遍历
+ 使用`for`就能够实现迭代遍历
```python
# for循环内部使用的变量in列表
for name in name_list:
    # 循环内部针对列表元素进行操作
    print(name)
```

# 02 元组
## 2.1 元组的定义
+ `Tuple`(元组)与列表类似，不同之处在于元组元素不能修改
  + **元组** 表示多个元素组成的序列
  + **元组** 在`python`开发中，有特定的应用场景
+ 用于存储一串信息，数据之间使用`,`分隔
+ 元组使用`()`定义
+ 元组的索引从`0`开始
  + 索引就是数据在元组中的位置编号
  + **定义只包含一个元素的元组时，需要在元素后面添加逗号**

```python
# 元组元素不能有重复
>>> my_tuple = (1, 2, 3, 4, 5，1)
  File "<stdin>", line 1
    my_tuple = (1, 2, 3, 4, 5，1)

# 元组素不能修改
>>> my_tuple = (1, 2, 3, 4, 5)
>>> my_tuple[1] = 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

# 元组元素不能删除
>>> my_tuple = (1, 2, 3, 4, 5)
>>> del my_tuple[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object doesn't support item deletion

# 空元组的定义
>>> my_tuple = ()
>>> type(my_tuple)
<class 'tuple'>

# 定义只包含一个元素的元组时，需要在元素后面添加逗号
>>> my_tuple = (1)
>>> type(my_tuple)
<class 'int'>
>>> my_tuple = (1, )
>>> type(my_tuple)
<class 'tuple'>
```

## 2.2 元组的常用操作
|方法名|作用|描述|
|:-|:-|:-|
|**T.count(value) -> integer**|return number of occurrences of value|数据在元组中出现的次数|
|**T.index(value, [start, [stop]]) -> integer**|return first index of value|指定值在元组中的索引

## 2.3 演练

### count(value)方法
```python
>>> my_tuple = (1, 2, 3, 4, 5)
>>> my_tuple.count(1)
1
```
### index(value)方法
```python
>>> my_tuple = (1, 2, 3, 4, 5)
>>> my_tuple.index(1)
0
```

# 03 字典
## 3.1 字典的定义
+ `dinctionary`(字典)是除列表以外python之中最灵活的数据类型
+ 字典可以用来存储多个数据
  + 通常用于存储描述一个物体的相关信息
+ 和列表的区别
  + 列表是有序的对象集合
  + 字典是无序的对象集合
+ 字典用`{}`定义
+ 字典使用`键:值`对存储数据，键值对之间使用`,`分隔
  + 键`key`是索引
  + 值`value`是数据
  + 键和值之间使用`:`分隔
  + 键必须是唯一的

> 字典的key只能使用不可变类型的数据（数字、字符串、元组）。
> 列表、字典都是可变数据类型。

在python中，设置字典的键值对时，会首先对key进行hash，来决定如何在内存中保存字典的数据，以方便后续对字典的操作：增、删、改、查

+ 键值对的`key`必须是不可变类型的数据
+ 键值对的`value`可以是任何类型的数据

字典.keys()所有key列表
字典.values()所有value列表
字典.iterms()所有(key, value)元组列表

```python
xiaoming_dict = {"name":"小明"}
# 1.取值
print(xiaoming_dict["name"])
# 在取值的时候如果指定的key不存在，程序会报错

# 2.增加/修改
# 如果key不存在，会新增键值对
xiaoming_dict["age"] = 18
# 如果key存在，会修改已经存在的键值对
xiaoming_dict["name"] = "小小明"

# 3.删除
xiaoming_dict.pop["age"]
# 在删除指定键值对的时候，如果指定的key不存在，程序会报错
```

## 3.2 字典的常用操作
```python
xiaoming_dict = {"name":"小明"，"age":18}
# 1.统计键值对数量
print(len(xiaoming_dict))

# 2.合并字典
temp_dict = {"height":1.75}
# 注意：如果被合并的子弟啊中包含已经存在的键值对，会覆盖原有的键值对
xiaoming_dict.update(temp_dict)
print(xiaoming_dict)

# 3.清空字典
xiaoming_dict.clear()
print(xiaoming_dict)
```



|方法名|作用|描述|
|:-|:-|:-|
|**D.clear() -> None**|Remove all items from D|清除字典中的元素|
|**D.copy()**|a shallow copy of D|一个字典赋给另一个变量|
|fromkeys(*args,**kwargs)|Returns a new dict with keys from iterable and values equal to value|生成一个新字典，键(key)不同，值(value)相同|
|**D.get(k[,d]) -> D[k]**|if k in D, else d. d defaults to None|获取字典中的键，返回对应的值，如果键不存在，则返回d=None，默认是None，我们也可以自己定义，如果获取不到会怎样|
|**D.items() -> a set-like object**|providing a view on D's items|返回字典中的键-值对|
|**D.keys() -> a set-like object**| providing a view on D's keys|返回字典中的键值|
|**D.values() -> an object**|providing a view on D's values|返回字典中的值|
|**D.pop(k[,d]) -> v**|remove specified key and return the corresponding value.If key is not found, d is returned if given, otherwise KeyError is raised|删除字典元素|
|**D.popitem() -> (k, v)**|remove and return some (key, value) pair as a 2-tuple; but raise KeyError if D is empty|随机删除字典中的元素|
|**D.update([E, ]**F) -> None**|Update D from dict/iterable E and F|更新列表中的值|

## 3.3 演练
### clear()方法
```python
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> my_dict.clear()
>>> my_dict
{}
```
### copy()方法
```python
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> temp_dict = my_dict.copy()
>>> temp_dict
{1: 'a', 2: 'b', 3: 'c'}
```
#### fromkeys()方法
```python
# 生成一个新字典，键(key)不同，值(value)相同
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> temp_dic = my_dict.fromkeys([1, 2, 3], 'aa')
>>> temp_dic
{1: 'aa', 2: 'aa', 3: 'aa'}
>>> temp_dic = my_dict.fromkeys([1], 'aa')
>>> temp_dic
{1: 'aa'}
>>>
```
### get()方法
```python
>>> my_dict = {1:'a', 2:'b', 3:'c'}
# 如果使用[]方法取值，如果是字典中存在的键，就直接返回值
>>> my_dict[1]
'a'
# 如果不是字典中存在的键，就会报错
>>> my_dict[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 4

# 使用get方法，如果是字典中存在的键，也直接返回
>>> my_dict.get(1)
'a'
# 如果不是字典中存在的键，不会报错，返回None
>>> my_dict.get(4)

# 也可以自己定义返回值
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> my_dict.get(4, 'no value')
'no value'
```
### items()方法
```python
# 返回字典中的键:值对
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> my_dict.items()
dict_items([(1, 'a'), (2, 'b'), (3, 'c')])
>>> for (k, v) in my_dict.items():
...     print(k, v)
...
1 a
2 b
3 c
```
### keys()方法
```python
# 返回字典中的键(key)值
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> my_dict.keys()
dict_keys([1, 2, 3])
```
### values()方法
```python
# 返回字典中的值(value)值
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> my_dict.values()
dict_values(['a', 'b', 'c'])
```
### pop()方法
```python
>>> my_dict = {1:'a', 2:'b', 3:'c'}
# 由于字典是无序的，所以一定要指定key值
>>> my_dict.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pop expected at least 1 arguments, got 0

# 若是字典中存在的key值，就会返回其value值
>>> my_dict.pop(2)
'b'
>>> my_dict
{1: 'a', 3: 'c'}
>>>>>> my_dict.pop(2)
'b'
>>> my_dict
{1: 'a', 3: 'c'}

# 若不是字典中存在的key值，会报错，也可以指定返回信息
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> my_dict.pop(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 4
>>> my_dict.pop(4, 'no key')
'no key'
```
### popitem()方法
```python
# 由于字典是无序的，所以popitem()没有指定参数，就是随机删除字典中的元素
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> my_dict.popitem()
(3, 'c')
```
### setdefault()方法
```python
# 向字典中加入键-值对
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> my_dict.setdefault(4, 5)
5
>>> my_dict
{1: 'a', 2: 'b', 3: 'c', 4: 5}

# 如果没有指定key值，那么value默认值为None
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> my_dict.setdefault(4)
>>> my_dict
{1: 'a', 2: 'b', 3: 'c', 4: None}

# 如果加入的值是已经存在的，就会返回其value值
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> my_dict.setdefault(1)
'a'
>>> my_dict
{1: 'a', 2: 'b', 3: 'c'}
```
### update()方法
```python
# 既可以新增键值对，也可以对已有键值对进行更新
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> my_dict.update({1:1, 2:2, 3:3})
>>> my_dict
{1: 1, 2: 2, 3: 3}
>>> my_dict.update({4:4, 5:5})
>>> my_dict
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
```

# 04 字符串

## 4.1 字符串中的转义字符
|转义字符|描述|
|:-|:-|
|\\|反斜杠符号|
|\'|单引号|
|\"|双引号|
|\n|换行(windows中是\n\r)|
|\t|横向制表符|
|\r|回车|

## 4.2 字符串的常用操作

### capitalize()方法
```python
# 居首首字母大写，其他字母不大写
>>> my_str = 'hello world'
>>> my_str.capitalize()
'Hello world'
>>> my_str
'hello world'  # 字符串本身不会发生变化
```

### title()方法
```python
# 所有单词的首字母都大写
>>> my_str = 'atom is a boy and of some'
>>> my_str.capitalize()
'Atom is a boy and of some'
>>> my_str.title()
'Atom Is A Boy And Of Some'
>>> my_str
'atom is a boy and of some'  # 字符串本身不会发生变化
```

### casefold()方法
```python
# 将大写字母转化为小写
>>> my_str = 'HELLO WORLD'
>>> my_str.casefold()
'hello world'
>>> my_str.lower()
'hello world'
>>> my_str
'HELLO WORLD'
```

### center()方法
```python
>>> my_str = '你好'
>>> my_str.center(12)
'     你好     '
>>> my_str
'你好'
>>> my_str.center(12, '-')
'-----你好-----'
>>> my_str
'你好'
```

### count()方法
```python
# 返回在字符串中出现指定字符的个数，返回一个整数
>>> my_str = 'abcabcbbbcddabc'
>>> my_str.count('abc')
3
>>> my_str.count('abcd')  # 若不存在就返回0
0
```

### encode()方法
```python
# 转换字符串的编码格式
>>> my_str = '你好'
>>> my_str.encode('gbk')
b'\xc4\xe3\xba\xc3'
>>> my_str
'你好'
```

### endswith()方法
```python
# 判断字符串以某个指定的字符结束，如果是，返回True，否则返回False
>>> my_str = 'abc'
>>> my_str.endswith('c')
True
```

### expandtabs()方法
```python
# 将字符串中的tab键转化为空格，默认时8个位置的空格，可以自己设置参数
>>> my_str = 'abc'
>>> my_str.endswith('c')
True
>>> my_str = '  abc'
>>> my_str.expandtabs()
'        abc'
>>> my_str.expandtabs(0)
'abc'
>>> my_str.expandtabs(4)
'    abc'
>>>
```

### find()方法
```python
# 查找指定字符在字符串中的位置，返回位置索引，如果查找不到，则返回-1
>>> my_str = 'abcabcbbbcddabc'
>>> my_str.find('bc')
1
>>> my_str.find('bbb')
6
>>> my_str.find('bbbb')
-1
```

### index()方法
```python
# index跟find一样是查找指定字符在字符串中的位置索引，不同的是，如果index查找失败，则报错
>>> my_str = 'abcabcbbbcddabc'
>>> my_str.index('bc')
1
>>> my_str.index('bbb')
6
>>> my_str.index('bbbb')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>>
```

### format_map()方法
```python
# 格式化输出
>>> my_str = "Name:{_name} Age:{_age} Job:{_job}".format_map({'_name':name, '_age':age, '_job':job})
>>> my_str
'Name:xingxiaoyang Age:28 Job:IT'
```

### isalnum()方法
```python
# 判断字符串中是都所有元素只有数字和字母组成,alnum是单词**alphanumeric的缩写，字母数字**
>>> my_str = 'hello world'
>>> my_str.isalnum()
False
>>> my_str = 'helloworld'
>>> my_str.isalnum()
True
```

### isalpha()方法
```python
# 判断字符串中所有的元素是否都是字母组成
>>> my_str = 'hello world'
>>> my_str.isalpha()
False
>>> my_str = 'helloworld'
>>> my_str.isalpha()
True
```

### isdecimal()方法
```python
# 如果字符串中只包含十进制的数字，则返回True；否则返回布尔值False.
>>> my_str.isdecimal()
False
>>> my_str = '123'
>>> my_str.isdecimal()
True
```

### isdigit()方法
```python
# 判断字符串是否仅仅由数字组成
>>> my_str = '123'
>>> my_str.isdigit()
True
>>> my_str = '123a'
>>> my_str.isdigit()
False
```

### isidentifier()方法
```python
# 判断字符串是否为合法标识符
>>> my_str = '55'
>>> my_str.isidentifier()
False
>>> my_str = '_123A'
>>> my_str.isidentifier()
True
>>> my_str = '123A'
>>> my_str.isidentifier()
False
```

### islower()方法
```python
# 判断是否都是小写
>>> my_str = 'Alex'
>>> my_str.islower()
False
>>> my_str = 'alex'
>>> my_str.islower()
True
```

### isnumeric()方法
```python
# 判断字符串S中是否值包含数字在里面，如果是，返回True;否则返回False#
>>> my_str = 'a123'
>>> my_str.isnumeric()
False
>>> my_str = '123'
>>> my_str.isnumeric()
True
```


### isprintable()方法
```python
# 判断一个字符串是否里面的字符都是可以打印出来的或者字符串是空的，如果是返回True;否则返回False
>>> my_str = '  123'
>>> my_str.isprintable()
False
>>> my_str = '123'
>>> my_str.isprintable()
True
```

### isspace()方法
```python
# 判断字符串中是否都是空白
>>> my_str = ' '
>>> my_str.isspace()
True
>>> my_str = '   '
>>> my_str.isspace()
True
>>> my_str = '  a '
>>> my_str.isspace()
False
```

### istitle()方法
```python
# 判断是否首字母大写，如果是返回True;否则返回False
>>> my_str = 'ABC'
>>> my_str.istitle()
False
>>> my_str = 'Abc'
>>> my_str.istitle()
True
```

### isupper()方法
```python
# 判断字符串中所有字符是否都是大写形式
>>> my_str = 'ABC IS'
>>> my_str.isupper()
True
>>> my_str = 'ABC Is'
>>> my_str.isupper()
False
```

### join()方法
```python
# 拼接，字符串和列表直接的拼接

# 1.字符串与字符串进行拼接，将拼接中的字符串的每一个元素与字符串中的元素进行拼接sign = '-'
>>> name = 'abc'
>>> sign.join(name)
'a-b-c'

# 2.字符串和列表进行拼接，列表中的每一个元素都与字符串的元素进行拼接
>>> my_list = ['a', 'b', 'c']
>>> sign.join(my_list)
'a-b-c'
```


### ljust()方法
```python
# 固定长度，字符串左边拼接指定的字符
>>> my_str = 'name'
>>> my_str.ljust(10, '-')
'name------'
```


### rjust()方法
```python
# 固定长度，字符串右边边拼接指定的字符
>>> my_str = 'name'
>>> my_str.rjust(10, '-')
'------name'
```


### lower()方法
```python
# 将字符串全部转化为小写形式
>>> my_str = 'NAME'
>>> my_str.lower()
'name'
>>> my_str = 'NaMe'
>>> my_str.lower()
'name'
```

### lstrip()方法
```python
# 删除字符串左侧的空格，默认是删除空格，可以指定删除任意字符
>>> my_str = ' NaMe '
>>> my_str.lstrip()
'NaMe '
>>> my_str
' NaMe '
```


### rstrip()方法
```python
# 删除字符串右侧的空格
>>> my_str = ' NaMe '
>>> my_str.lstrip()
'NaMe '
>>> my_str
' NaMe '
```


### strip()方法
```python
# 删除字符串两侧的空格
>>> my_str = ' NaMe '
>>> my_str.strip()
'NaMe'
```


### maketrans()与translate()方法
```python
>>> intab = "aeiou"
>>> outtab = "12345"
>>> trantab = intab.maketrans(intab,outtab)
>>> trantab
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
>>> str = "This is string example .... wow!!!"
>>> str.translate(trantab)
'Th3s 3s str3ng 2x1mpl2 .... w4w!!!'
# 把intab中每个元素与outtab中每个元素一一对应，然后translate()替换其中对应的元素。
```


### partition()方法
```python
# 字符串分隔，以sep分隔为前中后三部分
>>> str = "This is string example .... wow!!!"
>>> str.partition('is')
('Th', 'is', ' is string example .... wow!!!')
>>> str.partition('T')
('', 'T', 'his is string example .... wow!!!')
```


### replace()方法
```python
# 字符串的查找替换
# 默认全部替换
>>> my_str = 'AbcAbc'
>>> my_str.replace('A', '1')
'1bc1bc'
>>> my_str
'AbcAbc'

# 也可以指定替换的个数
>>> my_str.replace('A', '1', 1)
'1bcAbc'
>>> my_str
'AbcAbc'
```

### rfind()方法
```python
# 从右侧开始查找
>>> my_str = 'AbcAbc'
>>> my_str.rfind('A')
3
>>> my_str.rfind('d')
-1
```


### rindex()方法
```python
# 从字符串右侧查找指定字符的位置索引，如果查找不到就会报错。
>>> my_str = 'AbcAbc'
>>> my_str.rindex('b')
4
>>> my_str.rindex('d')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```

### rpartition()方法
```python
# 字符串右侧开始查找分隔，与partition(self,sep)正好相反，示例如下,分隔字符串得到一个元组
>>> my_str = 'AbcAbc'
>>> my_str.rpartition('A')
('Abc', 'A', 'bc')
>>> my_str.rpartition('c')
('AbcAb', 'c', '')
```

### rsplit()方法和split()方法
```python
# rsplit()从右边以指定字符串分隔，分隔成一个列表，并且可以指定分隔的次数
>>> my_str = "Alexsbegcex"
>>> my_str.rsplit('e')
['Al', 'xsb', 'gc', 'x']
>>> my_str.rsplit('e', 0)
['Alexsbegcex']
>>> my_str.rsplit('e', 1)
['Alexsbegc', 'x']
>>> my_str.rsplit('e', 2)
['Alexsb', 'gc', 'x']
>>> my_str.rsplit('e', 3)
['Al', 'xsb', 'gc', 'x']
>>> my_str.rsplit('e', 4)
['Al', 'xsb', 'gc', 'x']
>>> my_str.rsplit('e', -1)
['Al', 'xsb', 'gc', 'x']

# split()从左边以指定字符串分隔，分隔成一个列表，并且可以指定分隔的次数
>>> my_str = "Alexsbegcex"
>>> my_str.split('e')
['Al', 'xsb', 'gc', 'x']
>>> my_str.split('e', 0)
['Alexsbegcex']
>>> my_str.split('e', 1)
['Al', 'xsbegcex']
>>> my_str.split('e', 2)
['Al', 'xsb', 'gcex']
>>> my_str.split('e', 3)
['Al', 'xsb', 'gc', 'x']
>>> my_str.split('e', 4)
['Al', 'xsb', 'gc', 'x']
>>> my_str.split('e', -1)
['Al', 'xsb', 'gc', 'x']
```

### splitlines()方法
```python
# 以"\n"换行符的形式分隔字符串>>> my_str = """
>>> my_str = " alex aoi marry"
>>> my_str.splitlines()
[' alex aoi marry']
```

### startswith()方法
```python
# 字符串是否以指定字符开始，可以指定起始位置
>>> my_str = "Alexsbegcex"
>>> my_str.startswith('A')
True
>>> my_str.startswith('w')
False
>>> my_str.startswith('e', 2, 5)
True
```

### swapcase()方法
```python
# 将一个字符串中所有大写字符转换为小写，小写转换为大写
>>> my_str = "Alexsbegcex"
>>> my_str.swapcase()
'aLEXSBEGCEX'
```

### title()方法
```python
# 将字符串的首字母转换为大写

```

### upper()方法
```python
# 将字符串所有字母都转换为大写
```

### zfill()方法
```python
# 指定宽度，不足左侧补零
>>> my_str = "Alexsbegcex"
>>> my_str.zfill(20)
'000000000Alexsbegcex'
>>> my_str
'Alexsbegcex'
```

# python3深浅复制
## 赋值
```python
>>> a = {"A1":1, "A2":2}
>>> b = a
>>> print('a', a, id(a))
a {'A1': 1, 'A2': 2} 4562897440
>>> print('b', b, id(b))
b {'A1': 1, 'A2': 2} 4562897440
# b与a公用一个地址
>>> b.clear()
>>> a
{}
```

## 浅复制(列表、字典的copy属于浅拷贝)
```python
# import copy
# copy.copy()  #浅拷贝
>>> a = {"A1":1, "A2":2}
>>> b = a.copy()
>>> print('a', a, id(a))
a {'A1': 1, 'A2': 2} 4556630272
>>> print('b', b, id(b))
b {'A1': 1, 'A2': 2} 4562896432
# 使用copy会创建一个新的对象
>>> b.clear()
>>> a
{'A1': 1, 'A2': 2}
```

对于浅复制来说，第一层创建的是新的内存地址，但是从第二层开始，指向的是同一个内存地址。
```python
>>> a = [1, [21, 22, 23, 24], 3, 4, 5]
>>> b = a.copy()
# 第一层的地址是不同的
>>> print(a, id(a))
[1, [21, 22, 23, 24], 3, 4, 5] 4562900872
>>> print(b, id(b))
[1, [21, 22, 23, 24], 3, 4, 5] 4562891464

# 第二层开始地址就相同了
>>> print(a[1], id(a[1]))
[21, 22, 23, 24] 4562891208
>>> print(b[1], id(b[1]))
[21, 22, 23, 24] 4562891208

# 用修改来验证
>>> a = [1, [21, 22, 23, 24], 3, 4, 5]
>>> b = a.copy()
>>> b[0] = 'a'  # 修改b第一层，不会影响到a
>>> a
[1, [21, 22, 23, 24], 3, 4, 5]
>>> b[1][0] = 'a1'  # 修改b的第二层，就会影响到a
>>> a
[1, ['a1', 22, 23, 24], 3, 4, 5]
```

## 深拷贝
```python
>>> import copy
>>> a = [1, [21, 22, 23, 24], 3, 4, 5]
>>> b = copy.deepcopy(a)
>>> print(a, id(a))
# 第一层地址不相同
[1, [21, 22, 23, 24], 3, 4, 5] 4562891336
>>> print(b, id(b))
[1, [21, 22, 23, 24], 3, 4, 5] 4562891272
# 第二层地址也不相同
>>> print(a[1], id(a[1]))
[21, 22, 23, 24] 4562892040
>>> print(b[1], id(b[1]))
[21, 22, 23, 24] 4562892232

# 用修改来验证
>>> b[0] = 'a'
>>> a
[1, [21, 22, 23, 24], 3, 4, 5]
>>> b[1] = 'a1'
>>> a
[1, [21, 22, 23, 24], 3, 4, 5]
```

# 函数的参数
##　位置参数
---
位置参数：调用函数时根据函数定义的参数位置来传递参数
```python
def user_info(name, age, gender):
    print(name, age, gender)

user_info('Tom', 20, '男')
```
> 注意：传递和定义参数的顺序及个数必须一致。

## 关键字参数
函数调用，通过“键=值”形式加以指定。可以让函数更加清晰、容易使用，同时也清除乐乐参数的顺序需求

```python
def user_info(name, age, gender):
    print(name, age, gender)

user_info('Tom', age=20, gender='男')
user_info('Tom', gender='男', age=20)
```
> 注意：函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序。

## 缺省参数
缺省参数也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值（注意：所有位置参数必须出现在默认参数前，包括函数定义和调用）
```python
def user_info(name, age, gender="男"):
    print(name, age, gender)

user_info('Tom', 20)
user_info('Tom', 20, '女')
```
> 注意：函数调用时，如果为缺省参数传值则修改默认参数值；否则使用这个默认值

## 不定长参数
不定长参数也叫可变参数。用于不确定调用的时候会传递多少个参数（不传参也可以）的场景。此时，可用包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会显得非常方便。

### 包裹位置传递
```python
def user_info(*args):
    print(args)

user_info("Tom")
user_info("Tom", 20)
```
> 注意：传进去的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元祖(tuple)。
> args是元祖类型，这就是包裹位置传递

### 包裹关键字传递
```python
def user_info(**args):
    print(args)

user_info(name="Tom")
user_info(name="Tom", age=20)
```
> 综上：无论是包裹位置传递还是包裹关键字传递，都是一个组包的过程

# 高阶函数
## map()
map(func, lst)，将传入的函数变量func作用到lst变量的每个元素中，并将结果组成迭代器返回。
```python
# 计算list1序列中各个数字的2次方
list1 = [1, 2, 3, 4, 5]
def func(x):
    return x**2

result = map(func, list1)
print(result)  # <map object at 0x7f2916214da0>
print(list(result))  # [1, 4, 9, 16, 25]


```

## reduce()
reduce(func, lst)，其中func必须有两个参数。每次计算func的结果
> 注意：reduce()传入的参数必须接收2个参数。需要导入functools包
```python
# 计算list1序列中各个数字的累加和
import functools
list1 = [1, 2, 3, 4, 5]
def func(a, b):
    return a + b

result = functools.reduce(func, list1)
print(result)  # 15
```


## filter()
filter(func, lst)用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象。
```python
# 过滤掉list1中的奇数
list1 = [1, 2, 3, 4, 5]
def func(x):
    return x % 2 == 0

result = filter(func, list1)

print(result)  # <filter object at 0x7fe1fae07a58>
print(list(result))  # [2, 4]
```

# lambda的参数形式
## 无参数
```python
>>> fun1 = lambda : 100
>>> print(fun1())
100
```

## 一个参数
```python
>>> fun1 = lambda a: a
>>> print(fun1("hello world"))
hello world
```

## 默认参数
```python
>>> fun1 = lambda a, b, c=100: a + b + c
>>> print(fun1(10, 20))
130
```

## 可变参数
```python
>>> fun1 = lambda *args: args
>>> print(fun1(10, 20, 30))
(10, 20, 30)
```

## 可变参数
```python
>>> fun1 = lambda **args: args
>>> print(fun1(name="python", age=20))
{'name': 'python', 'age': 20}
```

# 多线程
## 多线程默认情况
在默认情况下，主线程执行完自己的任务后，就退出了，此时子线程会继续执行自己的任务，直到自己的任务结束。

```python
# -*- coding: utf-8 -*-
import time
import threading


def run():
    time.sleep(2)
    print("当前线程的名字", threading.current_thread().name)


if __name__ == '__main__':
    start_time = time.time()

    print("这是主线程", threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.start()

    print("主线程结束！", threading.current_thread().name)
    print("使用时间", time.time() - start_time)


"""
这是主线程 MainThread
主线程结束！ MainThread
使用时间 0.0007381439208984375
当前线程的名字 Thread-3
当前线程的名字 Thread-1
当前线程的名字 Thread-2
当前线程的名字 Thread-4
当前线程的名字 Thread-5

分析：
1.计时的是主线程，在主线程结束后就打印时间了
2.主线程的任务完成之后，主线程随之结束，子线程继续执行自己的任务，知道全部的子线程的任务全部结束，程序结束
"""
```

## 设置守护线程
设置子线程为守护线程时，主线程一旦结束，则全部线程全部被终止执行。
可能会出现的状况是，子线程的任务还没完全执行结束，就被被迫终止了。

```python
# -*- coding: utf-8 -*-
import time
import threading


def run():
    time.sleep(2)
    print("当前线程的名字", threading.current_thread().name)


if __name__ == '__main__':
    start_time = time.time()

    print("这是主线程", threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.setDaemon(True)
        t.start()

    print("主线程结束！", threading.current_thread().name)
    print("使用时间", time.time() - start_time)

"""
这是主线程 MainThread
主线程结束！ MainThread
使用时间 0.0008144378662109375

分析：
守护的是主线程，希望主线程结束的时候子线程也结束
主线程结束后，子线程也结束了，整个程序退出了
"""
```

## join()
join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程再终止

```python
# -*- coding: utf-8 -*-
import time
import threading


def run():
    time.sleep(2)
    print("当前线程的名字", threading.current_thread().name)


if __name__ == '__main__':
    start_time = time.time()

    print("这是主线程", threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.setDaemon(True)
        t.start()

    for t in thread_list:
        t.join()

    print("主线程结束！", threading.current_thread().name)
    print("使用时间", time.time() - start_time)

"""
这是主线程 MainThread
当前线程的名字 Thread-1
当前线程的名字 Thread-3
当前线程的名字 Thread-5
当前线程的名字 Thread-2
当前线程的名字 Thread-4
主线程结束！ MainThread
使用时间 2.002138614654541

分析：
运行的时候可以发现，主线程在等待子线程结束后才结束，主线程结束后才打印时间
"""
```


## 多线程共享全局变量问题
```python
# -*- coding: utf-8 -*-

import threading
import time

g_num = 0


# work1
def work1():
    """一个线程往全局变量写程序"""
    global g_num
    for i in range(10):
        g_num += 10
    print("work1", g_num)  # 100


# work2
def work2():
    """一个线程读全局变量"""
    print("work2", g_num)  # 100 g_num可以在对个线程中共享


if __name__ == '__main__':
    # 创建2个子线程
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    # 启动线程
    t1.start()
    t2.start()

    # 让主线程等待子线程结束后再结束
    # 循环判断线程数，当线程数不为1时，主线程等待子线程结束
    while len(threading.enumerate()) != 1:
        time.sleep(1)

    # 在t1和t2线程执行完成后再打印

    print("main", g_num)  # 100

"""
work1 100
work2 100
main 100
"""
```

## 多线程共享全局变量——问题
```python
# -*- coding: utf-8 -*-

import threading
import time

g_num = 0


# work1
def work1():
    """一个线程往全局变量写程序"""
    global g_num
    for i in range(100000000):
        g_num += 1
    print("work1", g_num)


# work2
def work2():
    """另一个线程也往全局变量写程序"""
    global g_num
    for i in range(10000000):
        g_num += 1
    print("work2", g_num)


if __name__ == '__main__':
    # 创建2个子线程
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    # 启动线程
    t1.start()
    t2.start()

    # 让主线程等待子线程结束后再结束
    # 循环判断线程数，当线程数不为1时，主线程等待子线程结束
    while len(threading.enumerate()) != 1:
        time.sleep(1)

    # 在t1和t2线程执行完成后再打印

    print("main", g_num)  # 100

"""
work2 14073822
work1 103585455
main 103585455

结论：
当多个线程修改同一个资源的时候，会出现资源竞争，导致计算有误
"""
```

### 解决方法——使用join()方法
```python
# -*- coding: utf-8 -*-

import threading
import time

g_num = 0


# work1
def work1():
    """一个线程往全局变量写程序"""
    global g_num
    for i in range(10000000):
        g_num += 1
    print("work1", g_num)


# work2
def work2():
    """另一个线程也往全局变量写程序"""
    global g_num
    for i in range(10000000):
        g_num += 1
    print("work2", g_num)


if __name__ == '__main__':

    # 创建2个子线程
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    # 启动线程
    t1.start()
    t1.join()  # 优先让t1先执行完，（join方法就是某个线程优先执行）
    t2.start()

    # 让主线程等待子线程结束后再结束
    # 循环判断线程数，当线程数不为1时，主线程等待子线程结束
    while len(threading.enumerate()) != 1:
        time.sleep(1)

    # 在t1和t2线程执行完成后再打印

    print("main", g_num)  # 100

"""
work2 14073822
work1 103585455
main 103585455

结论：
当多个线程修改同一个资源的时候，会出现资源竞争，导致计算有误
"""
```

## 同步和异步
同步：多任务，多个任务之间执行的时候要求有先后顺序，必须一个先执行完成之后，另一个才能继续执行，只有一个主线程，如：你说完，我再说（同一时间只能做一件事情）

异步：多个任务之间执行没有先后顺序，可以同时运行，执行的先后顺序不会有什么影响，存在的多条运行主线。如：发微信（可以不用等对方回复，继续发），点外卖（点了外卖后，可以继续忙其他的事情，而不是坐等外卖，啥也不做）

线程的锁机制：当线程获取资源后，立刻进行锁定，资源使用完毕后再解锁，有效地保证同一时间之后线程在使用资源。

### 互斥锁
当多个线程几乎同时修改某一个共享数据的时候，需要进行同步控制。

线程同步能够保证多个线程安全访问竞争资源，最贱的同步机制是引入互斥锁。

互斥锁为资源引入一个状态：锁定/非锁定

某个线程变更共享资源时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改，直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确执性。

threading模块中定义了Lock类，可以方便地处理锁定

```python
# 创建锁
mutex = threading.Lock()
# 锁定
mutex.acquire()
# 释放
mutex.release()

```
注意：
+ 如果 这个锁之前是没有上锁的，那么acquire不会堵塞
+ 如果在调用acquire对这个锁上锁之前已经被其他线程上了锁，那么此时acquire会堵塞，直到这个锁被解锁为止。
### 互斥锁的使用
```python
# -*- coding: utf-8 -*-

import threading
import time

g_num = 0


# work1
def work1():
    """一个线程往全局变量写程序"""
    global g_num
    for i in range(10000000):
        # 上锁
        lock1.acquire()
        g_num += 1
        # 解锁
        lock1.release()
    print("work1", g_num)


# work2
def work2():
    """另一个线程也往全局变量写程序"""
    global g_num
    for i in range(10000000):
        lock1.acquire()
        g_num += 1
        lock1.release()
    print("work2", g_num)


if __name__ == '__main__':

    # 创建一把互斥锁
    lock1 = threading.Lock()

    # 创建2个子线程
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    # 启动线程
    t1.start()
    t2.start()

    # 让主线程等待子线程结束后再结束
    # 循环判断线程数，当线程数不为1时，主线程等待子线程结束
    while len(threading.enumerate()) != 1:
        time.sleep(1)

    # 在t1和t2线程执行完成后再打印

    print("main", g_num)  # 100
"""
work1 19890824
work2 20000000
main 20000000

"""
```

## 死锁
在线程间共享多个资源，如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。



# 进程
工作中，任务数往往大于cpu的核数，即一定有一些任务正在执行，而另外一些任务在等待cpu进行执行，因此导致了有不同的状态。

就绪状态：运行的条件已经满足，正在等待cpu执行
执行态：cpu正在执行其功能
等待态：等待某些条件满足，例如一个程序sleep了，此时就处于等待状态

### 进程的基本使用
```python
# -*- coding: utf-8 -*-

import multiprocessing
import time


def work1():
    for i in range(10):
        print("正在运行 work1 ....")
        time.sleep(0.5)


if __name__ == '__main__':
    process_obj = multiprocessing.Process(target=work1)
    process_obj.start()

    print("主进程")

"""
程序启动以后有一个默认的主进程，在主进程中有一个主线程
"""
```


## 获取进程的编号，获取进程的父id
+ 获取进程的编号
```python
multiprocessing.current_process().pid
# or
os.getpid()
```
+ 设置子进程名
```python
multiprocessing.Process(target=work1, name="p1")  # 通过name设定子进程名
```
+ 获取父id
```python
os.getppid()
```

### 完整案例
```python
# -*- coding: utf-8 -*-

import multiprocessing
import time
import os

def work1():
    for i in range(10):
        # 获取进程的编号
        # print("正在运行 work1 ....", multiprocessing.current_process().pid)
        print("正在运行 work1 ....", os.getpid())

        # 获取进程的父id
        print("正在运行 work1 ....", os.getpid(), "父进程", os.getppid())
        time.sleep(2)


if __name__ == '__main__':
    # 获取主进程的名称
    print(multiprocessing.current_process())

    # 获取进程的编号
    # 1) multiprocessing.current_process().pid
    # print("主进程编号", multiprocessing.current_process().pid)

    # 2) 使用os模块
    print("主进程编号", os.getpid())

    # target: 指定子进程要执行的分支函数
    # name: 指定子进程的名称
    process_obj = multiprocessing.Process(target=work1, name="p1")
    process_obj.start()

    print("主进程")

"""
<_MainProcess(MainProcess, started)>
主进程编号 6556
主进程
正在运行 work1 .... 6560
正在运行 work1 .... 6560 父进程 6556
正在运行 work1 .... 6560
正在运行 work1 .... 6560 父进程 6556
正在运行 work1 .... 6560
正在运行 work1 .... 6560 父进程 6556
正在运行 work1 .... 6560
正在运行 work1 .... 6560 父进程 6556
正在运行 work1 .... 6560
正在运行 work1 .... 6560 父进程 6556
正在运行 work1 .... 6560
正在运行 work1 .... 6560 父进程 6556
正在运行 work1 .... 6560
正在运行 work1 .... 6560 父进程 6556
正在运行 work1 .... 6560
正在运行 work1 .... 6560 父进程 6556
正在运行 work1 .... 6560
正在运行 work1 .... 6560 父进程 6556
正在运行 work1 .... 6560
正在运行 work1 .... 6560 父进程 6556
"""
```

## 进程间共享全局变量的问题
```python
# -*- coding: utf-8 -*-

import multiprocessing
import time

g_num = 10


def work1():
    global g_num
    for i in range(10):
        g_num += 1

    print("work1", g_num)


def work2():
    print("work2", g_num)


if __name__ == '__main__':
    work1_process = multiprocessing.Process(target=work1)
    work2_process = multiprocessing.Process(target=work2)
    work1_process.start()
    work2_process.start()

    time.sleep(3)
    print("mian", g_num)
"""
子进程之间不能实现全局变量的共享
"""
```

## 守护进程

+ 进程守护：当主进程结束时，子进程也随之结束
+ 结束子进程

```python
# -*- coding: utf-8 -*-

import multiprocessing
import time


def work1():
    for i in range(10):
        print("正在运行 work1...")
        time.sleep(0.5)


if __name__ == '__main__':
    work1_object = multiprocessing.Process(target=work1)
    # 设置子进程守护主进程
    work1_object.daemon = True
    work1_object.start()
    time.sleep(2)
    print("主进程")
    # terminate()终止子进程的执行
    work1_object.terminate()
    exit()
```

## 进程和线程的对比

## 消息队列-基本操作

使用消息队列的目的：为了进程间的通信
```python
# -*- coding: utf-8 -*-

import multiprocessing

# 1)创建队列（指定长度）
# 2)放值
# 3)取值

# 1)创建队列（指定长度）
queue = multiprocessing.Queue(maxsize=5)
# 2)放值
queue.put(1)
queue.put("hello")
queue.put([1, 2, 3])
queue.put((4, 5, 6))
queue.put({"a": 1, "b": 10})
# queue.put(110)  # 长度为5，放入第6个数据后，队列进入了阻塞状态，默认会等待队列先取出值再放入新的值。
# queue.put_nowait(10) 如果队列满了直接报错
# 3)取值
print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())  # 当队列已经空的时候，再次get()，程序进入阻塞状态，等待放入新的值，然后再取
print(queue.get_nowait())  # 当列表已空，直接报错

```

## 消息队列－常用判断
```python
# -*- coding: utf-8 -*-

import multiprocessing

# 1)创建队列（指定长度）
# 2)放值
# 3)取值

# 1)创建队列（指定长度）
queue = multiprocessing.Queue(maxsize=5)
# 2)放值
queue.put(1)
queue.put("hello")
queue.put([1, 2, 3])
queue.put((4, 5, 6))
queue.put({"a": 1, "b": 10})

# 判断队列是否已满
print("队列是否为满", queue.full())


# 3)取值
print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())

# 取队列中消息的个数
print("队列中消息的个数", queue.qsize())

print(queue.get())

# 判断队列是否已空
print("队列是否已空", queue.empty())

```

## 使用queue实现进程间的通信

```python
# -*- coding: utf-8 -*-
import time
import multiprocessing


def write_queue(queue):
    for i in range(10):
        if queue.full():
            print("队列已满！")
            break
        queue.put(i)
        print("写入成功，已经写入：", i)
        time.sleep(0.5)


def read_queue(queue):
    while True:
        if queue.qsize() == 0:
            print("队列已空")
            break
        value = queue.get()
        print("已经读取：", value)



if __name__ == '__main__':
    queue = multiprocessing.Queue(5)

    process1 = multiprocessing.Process(target=write_queue, args=(queue,))
    process2 = multiprocessing.Process(target=read_queue, args=(queue,))

    process1.start()
    process1.join()  # 优先让写进程执行结束后，再读取数据
    process2.start()
```

## 进程池
当创建的子进程数量巨大的时候，可以使用multiprocessing模块提供的Pool方法

初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到指定的最大值，那么该请求就会等待，直到池中有进程结束，才会用之前的进程来执行新的任务。

### 核心方法
+ apply(): 进程池以同步的方式执行
+ apply_async(func， args, kwds): 使用非阻塞的方式调用func
  - 并行执行，阻塞方式必须等待上一个进程退出才能执行下一个进程

```python
# -*- coding: utf-8 -*-
import time
import multiprocessing


# 1.创建一个函数，用于模拟文件拷贝
# 2.创建一个进程池，长度为3
# 3.进程池同步的方式拷贝文件
# 4.进程池异步的方式拷贝文件


def copy_work():
    print("正在拷贝文件...", multiprocessing.current_process())
    time.sleep(1)


if __name__ == '__main__':
    # 进程池创建
    pool = multiprocessing.Pool(3)

    for i in range(10):
        # cooy_work()
        # 3.进程池同步的方式拷贝文件
        # pool.apply(copy_work)  # 同步的方式
        # 4.进程池异步的方式拷贝文件
        #如果使用异步方式，需要做两点：
        # 1)pool.close() 表示不再接收新的任务
        # 2)主进程不再等待进程池结束后再退出，需要进程池join()
        # pool.join()让主进程等待进程池执行结束后再退出

        pool.apply_async(copy_work)
    pool.close()
    pool.join()

```

## 进程中进程间的通信queue
```python
# -*- coding: utf-8 -*-
import time
import multiprocessing


def write_queue(queue):
    for i in range(10):
        if queue.full():
            print("队列已满！")
            break
        queue.put(i)
        print("写入成功，已经写入：", i)
        time.sleep(0.5)


def read_queue(queue):
    while True:
        if queue.qsize() == 0:
            print("队列已空")
            break
        value = queue.get()
        print("已经读取：", value)



if __name__ == '__main__':

    # 1、创建进程池
    pool = multiprocessing.Pool()
    # 2、创建进程池中的队列
    queue = multiprocessing.Manager().Queue(5)
    # 3、使用同步进程池执行
    # pool.apply(write_queue, (queue,))
    # pool.apply(read_queue, (queue,))

    # 4、使用异步进程池执行
    # apply_async返回值ApplyResult对象，该对象有一个wait()的方法
    # wait()方法类似join()，表示让当前进程执行完毕后，后续进程才能启动
    result = pool.apply_async(write_queue, (queue, ))
    result.wait()

    pool.apply_async(read_queue, (queue, ))
    pool.close()  # 表示不在接收新的任务
    pool.join()  # 主进程等待进程池执行结束后再退出

```


## 并行与并发
并行是指两个或多个进程同时运行。这是在多核心平台上可以实现，比如每个处理器上运行一个进程。
并发是指在同一个处理器上运行多个进程。在操作系统中，通常使用时隙(time slicing)技术来解决这类问题。但是，这种办法并非真正的并发，只是由于处理器切换任务的速度非常快，看起来像是并行的。


# UDP
+ 发送端

```python
# -*- coding: utf-8 -*-
"""
1. 导入模块
2. 创建套接字
3. 绑定端口(发送方)
4. 发送数据
*. 接受数据(可选)
5. 关闭套接字

"""

import socket

# AF_INET: 表示IP4
# SOCK_DGRAM: 表示UPD传输协议
udp_client_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

udp_client_sock.bind(("", 8888))  # 客户端可以不绑定端口，但是服务器端必须绑定端口

udp_client_sock.sendto("你好".encode(), ("192.168.1.232", 8080))

recv_data = udp_client_sock.recvfrom(1024)
print("来自%s的信息：%s" % (str(recv_data[1]), recv_data[0].decode()))

udp_client_sock.close()
```

+ 接收端
```python
# -*- coding: utf-8 -*-
import socket

udp_server_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

udp_server_sock.bind(("", 8080))

recv_data = udp_server_sock.recvfrom(1024)

print("来自%s的信息：%s" % (str(recv_data[1]), recv_data[0].decode()))

udp_server_sock.sendto("hello".encode(), ("192.168.1.153", 8888))

udp_server_sock.close()
```

# TCP
+ 客户端
```python
# -*- coding: utf-8 -*-
"""
1.导入模块
2.创建套接字
3.建立链接
4.发送数据
5.关闭套接字

"""
import socket

# 创建套接字
tcp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# 建立链接
tcp_client_socket.connect(("192.168.1.232", 8080))

while True:
    send_text = input()
    if send_text:
        # 发送数据
        tcp_client_socket.send(send_text.encode())
    else:
        print("客户端停止输入！")
        break
# 关闭套接字
tcp_client_socket.close()
```

+ 服务器端
```python
# -*- coding: utf-8 -*-

"""
1.导入模块
2.创建套接字
3.绑定端口
4.开启监听
6.接受数据
7.关闭套接字
"""
import socket

tcp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
tcp_server_socket.bind(("192.168.1.232", 8080))
# 设置listen() 作用是设置tcp为被动监听模式，不能主动发送数据
# 128 允许接受的最大链接数，在Windows中有效，在Linux中无效
tcp_server_socket.listen(128)
while True:
    new_clinet_sockt, client_ip_port = tcp_server_socket.accept()
    print("新客户端来了！", client_ip_port)
    while True:
        recv_data = new_clinet_sockt.recv(1024)
        if recv_data:  # 当接受数据为空时，表示客户端断开链接
            recv_text = recv_data.decode()

            print("接受来自：%s的信息：%s" % (str(client_ip_port), recv_text))
        else:
            print("客户端断开链接")
            break

    new_clinet_sockt.close()

tcp_server_socket.close()


```
