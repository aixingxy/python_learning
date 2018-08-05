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
4. 绝不要描述代码，假设阅读的代码比你更多Python，他只是不知道你的代码要做什么？

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


# 01.列表
## 1.1列表的定义
+ `List`(列表)是python中使用最频繁的数据类型
+ 专门用于存储一串信息
+ 列表用`[]`定义，数据之间使用`,`分隔
+ 列表的索引从`0`开始
> 注意：从列表中取值时，如果超出索引范围，程序会报错

## 1.2列表的常用操作
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
```
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list.index(4)
3
>>> my_list.index(0)  # 如果没有找到会报错
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 0 is not in list
```

### insert(索引,数据)方法
```ipython
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
```
# 合并两个列表
>>> my_list = [1, 2, 3, 4, 5]
>>> temp_list = ['a', 'b', 'c']
>>> my_list.extend(temp_list)
>>> my_list
[1, 2, 3, 4, 5, 'a', 'b', 'c']
```
### 修改列表元素
```
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list[0] = 'a'
>>> my_list
['a', 2, 3, 4, 5]
```
### 删除列表元素
```
>>> my_list = [1, 2, 3, 4, 5]
>>> del my_list[0]
>>> my_list
[2, 3, 4, 5]
```
### remove(value)
```
# 删除第一个出现的value值
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
```
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
```
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list.clear()
>>> my_list
[]
```
### sort()方法
```
>>> my_list = [1, 3, 5, 2, 4]
>>> my_list.sort()
>>> my_list
[1, 2, 3, 4, 5]
>>> my_list.sort(reverse=True)
>>> my_list
[5, 4, 3, 2, 1]
```
### reverse()方法
```
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list.reverse()
>>> my_list
[5, 4, 3, 2, 1]

```
## 关键字、函数和方法
+ **关键字**是python内置的、具有特殊意义的标识符
```python
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
```
> 关键字后面不需要使用括号

+ **函数**封装了独立功能，可以直接调用
```python
函数名(参数）
```
> 函数需要死记硬背
+ 方法和函数类似，同样是封装了独立的功能
+ 方法需要通过对象来调用，表示针对这个对象要做的操作
```python
对象.方法名(参数)
```
> 在变量后面输入`.`，然后针对这个变量要执行的操作，记忆起来比函数要简单多了

## 1.4循环遍历
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

# 02.元组
## 2.1元组的定义
+ `Tuple`(元组)与列表类似，不同之处在于元组元素不能修改
  + **元组** 表示多个元素组成的序列
  + **元组** 在`python`开发中，有特定的应用场景
+ 用于存储一串信息，数据之间使用`,`分隔
+ 元组使用`()`定义
+ 元组的索引从`0`开始
  + 索引就是数据在元组中的位置编号

```
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
>>>
```

## 2.2元组的常用操作
|方法名|作用|描述|
|:-|:-|:-|
|**T.count(value) -> integer**|return number of occurrences of value|数据在元组中出现的次数|
|**T.index(value, [start, [stop]]) -> integer**|return first index of value|指定值在元组中的索引

## 2.3演练

### count(value)方法
```
>>> my_tuple = (1, 2, 3, 4, 5)
>>> my_tuple.count(1)
1
```
### index(value)方法
```
>>> my_tuple = (1, 2, 3, 4, 5)
>>> my_tuple.index(1)
0
```

# 03.字典
## 3.1字典的定义
+ `dinctionary`(字典)是除列表以外python之中最灵活的数据类型
+ 字典统一可以用来存储多个数据
  + 通常用于存储描述一个物体的相关信息
+ 和列表的区别
  + 列表是有序的对象集合
  + 字典是无序的对象集合
+ 字典用`{}`定义
+ 字典使用键值对存储数据，键值对之间使用`,`分隔
  + 键`key`是索引
  + 值`value`是数据
  + 键和值之间使用`:`分隔
  + 键必须是唯一的

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

## 3.2字典的常用操作
```python
xiaoming_dict = {"name":"小明"，
                 "age":18}
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

## 3.3演练
### clear()方法
```
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> my_dict.clear()
>>> my_dict
{}
```
### copy()方法
```
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> temp_dict = my_dict.copy()
>>> temp_dict
{1: 'a', 2: 'b', 3: 'c'}
```
#### fromkeys()方法
```
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
```
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
```
# 返回字典中的键-值对
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
```
# 返回字典中的键(key)值
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> my_dict.keys()
dict_keys([1, 2, 3])
```
### values()方法
```
# 返回字典中的值(value)值
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> my_dict.values()
dict_values(['a', 'b', 'c'])
```
### pop()方法
```
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
```
# 由于字典是无序的，所以popitem()没有指定参数，就是随机删除字典中的元素
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> my_dict.popitem()
(3, 'c')
```
### setdefault()方法
```
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
```
# 既可以新增键值对，也可以对已有键值对进行更新
>>> my_dict = {1:'a', 2:'b', 3:'c'}
>>> my_dict.update({1:1, 2:2, 3:3})
>>> my_dict
{1: 1, 2: 2, 3: 3}
>>> my_dict.update({4:4, 5:5})
>>> my_dict
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
```

# 04.字符串

## 4.1字符串的常用操作

### capitalize()方法
```
# 居首首字母大写，其他字母不大写
>>> my_str = 'hello world'
>>> my_str.capitalize()
'Hello world'
>>> my_str
'hello world'  # 字符串本身不会发生变化
```

### title()方法
```
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
```
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
```
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
```
# 返回在字符串中出现指定字符的个数，返回一个整数
>>> my_str = 'abcabcbbbcddabc'
>>> my_str.count('abc')
3
>>> my_str.count('abcd')  # 若不存在就返回0
0  
```

### encode()方法
```
# 转换字符串的编码格式
>>> my_str = '你好'
>>> my_str.encode('gbk')
b'\xc4\xe3\xba\xc3'
>>> my_str
'你好'
```

### endswith()方法
```
# 判断字符串以某个指定的字符结束，如果是，返回True，否则返回False
>>> my_str = 'abc'
>>> my_str.endswith('c')
True
```

### expandtabs()方法
```
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
```
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
```
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
```
# 格式化输出
>>> my_str = "Name:{_name} Age:{_age} Job:{_job}".format_map({'_name':name, '_age':age, '_job':job})
>>> my_str
'Name:xingxiaoyang Age:28 Job:IT'
```

### isalnum()方法
```
# 判断字符串中是都所有元素只有数字和字母组成,alnum是单词**alphanumeric的缩写，字母数字**
>>> my_str = 'hello world'
>>> my_str.isalnum()
False
>>> my_str = 'helloworld'
>>> my_str.isalnum()
True
```

### isalpha()方法
```
# 判断字符串中所有的元素是否都是字母组成
>>> my_str = 'hello world'
>>> my_str.isalpha()
False
>>> my_str = 'helloworld'
>>> my_str.isalpha()
True
```

### isdecimal()方法
```
# 如果字符串中只包含十进制的数字，则返回True；否则返回布尔值False.
>>> my_str.isdecimal()
False
>>> my_str = '123'
>>> my_str.isdecimal()
True
```


### isdigit()方法
```
# 判断字符串是否仅仅由数字组成
>>> my_str = '123'
>>> my_str.isdigit()
True
>>> my_str = '123a'
>>> my_str.isdigit()
False
```

### isidentifier()方法
```
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
```
# 判断是否都是小写
>>> my_str = 'Alex'
>>> my_str.islower()
False
>>> my_str = 'alex'
>>> my_str.islower()
True
```

### isnumeric()方法
```
# 判断字符串S中是否值包含数字在里面，如果是，返回True;否则返回False#
>>> my_str = 'a123'
>>> my_str.isnumeric()
False
>>> my_str = '123'
>>> my_str.isnumeric()
True
```


### isprintable()方法
```
# 判断一个字符串是否里面的字符都是可以打印出来的或者字符串是空的，如果是返回True;否则返回False
>>> my_str = '  123'
>>> my_str.isprintable()
False
>>> my_str = '123'
>>> my_str.isprintable()
True
```

### isspace()方法
```
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
```
# 判断是否首字母大写，如果是返回True;否则返回False
>>> my_str = 'ABC'
>>> my_str.istitle()
False
>>> my_str = 'Abc'
>>> my_str.istitle()
True
```

### isupper()方法
```
# 判断字符串中所有字符是否都是大写形式
>>> my_str = 'ABC IS'
>>> my_str.isupper()
True
>>> my_str = 'ABC Is'
>>> my_str.isupper()
False
```

### join()方法
```
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
```
# 固定长度，字符串左边拼接指定的字符
>>> my_str = 'name'
>>> my_str.ljust(10, '-')
'name------'
```


### rjust()方法
```
# 固定长度，字符串右边边拼接指定的字符
>>> my_str = 'name'
>>> my_str.rjust(10, '-')
'------name'
```


### lower()方法
```
# 将字符串全部转化为小写形式
>>> my_str = 'NAME'
>>> my_str.lower()
'name'
>>> my_str = 'NaMe'
>>> my_str.lower()
'name'
```

### lstrip()方法
```
# 删除字符串左侧的空格，默认是删除空格，可以指定删除任意字符
>>> my_str = ' NaMe '
>>> my_str.lstrip()
'NaMe '
>>> my_str
' NaMe '
```

### rstrip()方法
```
# 删除字符串右侧的空格
>>> my_str = ' NaMe '
>>> my_str.lstrip()
'NaMe '
>>> my_str
' NaMe '
```


### strip()方法
```
# 删除字符串两侧的空格
>>> my_str = ' NaMe '
>>> my_str.strip()
'NaMe'
```

### maketrans()与translate()方法
```
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
```
# 字符串分隔，以sep分隔为前中后三部分
>>> str = "This is string example .... wow!!!"
>>> str.partition('is')
('Th', 'is', ' is string example .... wow!!!')
>>> str.partition('T')
('', 'T', 'his is string example .... wow!!!')
```

### replace()方法
```
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
```
# 从右侧开始查找
>>> my_str = 'AbcAbc'
>>> my_str.rfind('A')
3
>>> my_str.rfind('d')
-1
```


### rindex()方法
```
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
```
# 字符串右侧开始查找分隔，与partition(self,sep)正好相反，示例如下,分隔字符串得到一个元组
>>> my_str = 'AbcAbc'
>>> my_str.rpartition('A')
('Abc', 'A', 'bc')
>>> my_str.rpartition('c')
('AbcAb', 'c', '')
```

### rsplit()方法和split()方法
```
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
```
# 以"\n"换行符的形式分隔字符串>>> my_str = """
... alex
... aoi
... marry
... """
>>> my_str.splitlines()
['', 'alex', 'aoi', 'marry']
```

### startswith()方法
```
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
```
# 将一个字符串中所有大写字符转换为小写，小写转换为大写
>>> my_str = "Alexsbegcex"
>>> my_str.swapcase()
'aLEXSBEGCEX'
```

### title()方法
```
# 将字符串的首字母转换为大写

```

### upper()方法
```
# 将字符串所有字母都转换为大写
```

### zfill()方法
```
# 指定宽度，不足左侧补零
>>> my_str = "Alexsbegcex"
>>> my_str.zfill(20)
'000000000Alexsbegcex'
>>> my_str
'Alexsbegcex'
```

# python3深浅复制
## 赋值
```
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
```
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
```
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
```
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
