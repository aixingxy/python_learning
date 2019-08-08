
# python3提高

## 如何在列表，字典，集合中根据条件筛选数据

### 实际案例

+ 过滤掉列表[3, 9, -1, 10, 20, -2, ...]中的负数

+ 筛选出字典{'LiLi': 79, 'Jim': 88, 'Lucy': 92, ...}中高于90的项

+ 筛选出集合{77, 89, 32, 20, ...}中能被3整除的元素

### 解决方法

+ 列表
  + 列表解析
  + filter函数

```python
>>> from random import randint
>>> l = [randint(-10, 10) for _ in range(10)]
>>> l
[-6, 0, 4, 8, 10, -3, 5, -4, -6, 6]
>>> [x for x in l if x < 0]  # 列表解析
[-6, -3, -4, -6]
>>> filter(lambda x: x < 0, l)
<filter object at 0x7feb71995c88>
>>> list(filter(lambda x: x < 0, l))  # filter函数
[-6, -3, -4, -6]
>>>
```


+ 字典
 + 字典解析

```python
>>> from random import randint
>>> d = {x: randint(-10, 10) for x in "abcde"}
>>> d
{'a': -2, 'b': 0, 'c': 6, 'd': 8, 'e': 6}
>>> {k: v for k, v in d.items() if v < 0}
{'a': -2}
>>>
```


+ 集合
  + 集合解析
```python
>>> from random import randint
>>> s = {randint(-10, 10) for _ in range(10)}
>>> s
{4, 5, 9, -9, -8, -6, -5}
>>> {x for x in s if x < 0}
{-8, -6, -5, -9}
>>>
```

## 如何为元祖中的每个元素命名，提高程序可读性

### 实际案例

学生信息系统中数据为固定格式：（名字，年龄，性别，邮箱）

('jim', 16, 'male', 'jim123@gmail.com')

访问时，使用索引(index)访问，大量索引降低程序可读性

### 解决方法
+ 定义一系列数据常量或枚举类型

```python
# 数据常量
NAME, AGE, SEX = range(3)

def xxx_func(student):
    if student[AGE] < 18:
        pass
    if student[SEX] == "male":
        pass

student = ('Jim', 19, 'male')
xxx_func(student)

# 枚举类型
from enum import IntEnum

s = ('Jim', 16, 'male')
t = (34, 'lishang')

class StudentEnum(IntEnum):
    NAME = 0
    AGE = 1
    SEX = 2
    EMAIL = 3

print(StudentEnum.NAME)

print(isinstance(StudentEnum.NAME, int))

print(s[StudentEnum.NAME])
```

+ 使用标准库中collections.namedtuple替代内置tuple
```python
>>> from collections import namedtuple
>>> Student = namedtuple('Student', ['name', 'age', 'male', 'email'])
>>> Student
<class '__main__.Student'>
>>> s2 = Student('jim', 16, 'male', '123@qq.com')
>>> s2.name
'jim'
>>> s2[0]
'jim'
>>>
```

## 如何根据字典中值的大小，对字典中的项排序

### 实际案例
某班的英语成绩以字典形式存储为：

{
    'LiLi': 79,
    'Jim': 88,
    'Lucy': 92,
    ...
}

如何根据成绩高低，计算学成排名。


### 解决方案

将字典中的各项转换为元祖，使用内置函数sorted排序（因为元祖是可以比较大小的）
+ 将字典中的项转化为(值, 键)元祖。（列表解析或zip）


```bash
# 元祖比较大小
>>> (1, 2) < (1, 1)
False
```

```python
>>> from random import randint
>>> d = {k: randint(60, 100) for k in "abcdekg"}
>>> d
{'a': 91, 'b': 61, 'c': 62, 'd': 96, 'e': 83, 'k': 69, 'g': 83}
>>> l = [(v, k) for k, v in d.items()]  # 列表解析
>>> l
[(91, 'a'), (61, 'b'), (62, 'c'), (96, 'd'), (83, 'e'), (69, 'k'), (83, 'g')]
>>> sorted(l, reverse=True)
[(96, 'd'), (91, 'a'), (83, 'g'), (83, 'e'), (69, 'k'), (62, 'c'), (61, 'b')]
>>> sorted(zip(d.values(), d.keys()), reverse=True)  # zip方法
[(96, 'd'), (91, 'a'), (83, 'g'), (83, 'e'), (69, 'k'), (62, 'c'), (61, 'b')]
>>> sorted(d.items(), key=lambda item: item[1], reverse=True)  # 直接使用sorted的key方法
[('d', 96), ('a', 91), ('e', 83), ('g', 83), ('k', 69), ('c', 62), ('b', 61)]
>>>
```


```python
>>> from random import randint
>>> l = sorted(d.items(), key=lambda item: item[1], reverse=True)
>>> l
[('f', 96), ('c', 95), ('g', 92), ('e', 91), ('b', 78), ('d', 73), ('a', 62)]

>>> for i, (k, v) in enumerate(l, 1):  # 更新字典
...     d[k] = (i, v)
...
>>> d
{'a': (7, 62), 'b': (5, 78), 'c': (2, 95), 'd': (6, 73), 'e': (4, 91), 'f': (1, 96), 'g': (3, 92)}

>>> d_new = {k: (i, v) for i, (k, v) in enumerate(l, 1)}  # 新建字典
>>> d_new
{'f': (1, 96), 'c': (2, 95), 'g': (3, 92), 'e': (4, 91), 'b': (5, 78), 'd': (6, 73), 'a': (7, 62)}
>>>
```


## 如何统计序列中元素的频度

### 实际案例

+ 某随机序列[12, 5, 6, 4, 6, 5, 5, 7]中，找到出现次数最高的三个元素，他们粗线的次数是多少？
+ 对某英文文章的单次，进行词频统计，找到出现次数最高的10个单次，他们出现的次数是多少？

### 解决方案
1. 将序列转换为字典{元素: 频度}，根据字典中的值排序
```pyton
>>> from random import randint
>>> data = [randint(0, 20) for _ in range(30)]
>>> data
[4, 11, 2, 20, 0, 10, 16, 9, 3, 16, 10, 11, 3, 11, 16, 15, 15, 20, 1, 13, 8, 18, 15, 17, 13, 10, 7, 12, 2, 3]
>>> d = dict.fromkeys(data, 0)
>>> d
{4: 0, 11: 0, 2: 0, 20: 0, 0: 0, 10: 0, 16: 0, 9: 0, 3: 0, 15: 0, 1: 0, 13: 0, 8: 0, 18: 0, 17: 0, 7: 0, 12: 0}
>>> for x in data:
...     d[x] += 1
...
>>> d
{4: 1, 11: 3, 2: 2, 20: 2, 0: 1, 10: 3, 16: 3, 9: 1, 3: 3, 15: 3, 1: 1, 13: 2, 8: 1, 18: 1, 17: 1, 7: 1, 12: 1}
>>> sorted([(v, k) for k, v in d.items()], reverse=True)  # 使用列表解析
[(3, 16), (3, 15), (3, 11), (3, 10), (3, 3), (2, 20), (2, 13), (2, 2), (1, 18), (1, 17), (1, 12), (1, 9), (1, 8), (1, 7), (1, 4), (1, 1), (1, 0)]
>>> sorted([(v, k) for k, v in d.items()], reverse=True)[:3] # 取最大的前三个
[(3, 16), (3, 15), (3, 11)]
>>> sorted(((v, k) for k, v in d.items()), reverse=True)[:3]  # 使用生成器解析，方括号改成圆括号，生成器解析节省空间
[(3, 16), (3, 15), (3, 11)]
>>>
```
这方法不是很好，如果列表很大，只要找到最大的前三个，需要对所有数据进行排序，显然是浪费的


2. 从很大数据中找到最小的前三个，应该使用堆这种数据结构
```python
>>> import heapq
>>> heapq.nlargest(3, ((v, k) for k, v in d.items()))
[(3, 16), (3, 15), (3, 11)]
>>>
```

3. 使用标准库collections中的Counter对象
```python
>>> from random import randint
>>> data = [randint(0, 20) for _ in range(30)]
>>> data
[2, 0, 2, 13, 20, 4, 9, 1, 20, 16, 19, 8, 4, 7, 3, 11, 0, 14, 14, 5, 3, 0, 7, 16, 14, 20, 20, 3, 4, 18]
>>> from collections import Counter
>>> c = Counter(data)
>>> c
Counter({20: 4, 0: 3, 4: 3, 3: 3, 14: 3, 2: 2, 16: 2, 7: 2, 13: 1, 9: 1, 1: 1, 19: 1, 8: 1, 11: 1, 5: 1, 18: 1})
>>> c.most_common(3)
[(20, 4), (0, 3), (4, 3)]
>>>
```

## 如何快速找到多个字典的工共键(key)？

### 实际案例

西班牙足球甲级联赛，每轮球员进球统计

第一轮：{'苏亚雷斯': 1, '梅西': 2. '本泽马': 1, ...}
第二轮：{'苏亚雷斯': 1, 'C罗': 1, '格里兹曼': 2, ...}
第三轮：{'苏亚雷斯': 1, '托雷斯': 2. '贝尔': 1, ...}
...

统计出前N轮，每场比赛都有进球的球员。

在n个字典中，求公共键问题

### 解决方案
1. 尝试
```python
>>> from random import randint
>>> from random import randint, sample
>>>
>>> sample('abcdefg', randint(3, 6))
['c', 'b', 'd']
>>> d1 = {k: randint(1, 4)for k in sample('abcdefg', randint(3, 6))}
>>> d1
{'d': 3, 'g': 3, 'c': 2}
>>> d2 = {k: randint(1, 4)for k in sample('abcdefg', randint(3, 6))}
>>> d2
{'g': 1, 'd': 4, 'f': 2, 'e': 1}
>>> d3 = {k: randint(1, 4)for k in sample('abcdefg', randint(3, 6))}
>>> d3
{'g': 4, 'e': 1, 'b': 3, 'd': 1}
>>> dl = [d1, d2, d3]
>>> [k for k in dl[0] if all(map(lambda d: k in d, dl[1: ]))]
['d', 'g']
>>>
```

2. 利用集合(set)的交集操作
step1: 使用字典的keys()方法，得到一个字典啊keys的集合
step2: 使用map函数，得到每个字典keys的集合
setp3: 使用reduce函数，取所有字典的keys集合的交集
```python
>>> d1
{'d': 3, 'g': 3, 'c': 2}
>>> d2
{'g': 1, 'd': 4, 'f': 2, 'e': 1}
>>> d3
{'g': 4, 'e': 1, 'b': 3, 'd': 1}
>>> dl
[{'d': 3, 'g': 3, 'c': 2}, {'g': 1, 'd': 4, 'f': 2, 'e': 1}, {'g': 4, 'e': 1, 'b': 3, 'd': 1}]
>>> list(map(dict.keys, dl))
[dict_keys(['d', 'g', 'c']), dict_keys(['g', 'd', 'f', 'e']), dict_keys(['g', 'e', 'b', 'd'])]
>>> s = list(map(dict.keys, dl))
>>> isinstance(s[0], set)
False
>>> s[0]
dict_keys(['d', 'g', 'c'])
>>> type(s[0])
<class 'dict_keys'>
>>> reduce(lambda a, b: a & b, list(map(dict.keys, dl)))
{'d', 'g'}
>>>

```

## 如何让字典保持有序

某编程竞赛系统，对参赛选手编程解题进行计时，选手完成退后，把该选手解题勇士记录到字典中，以便赛后按选手名查询成绩。

{'LiLei':{2, 43}, 'HanMeimei': (5, 52), 'Jim': (1, 39)}

比赛结束后，需按顺序依次打印选手成绩，如何实现？

### 验证字典保存的无序性（python3.6以后字典存储有序）
原理解析：https://www.cnblogs.com/songyifan427/p/11198719.html

### 解决方案
以OrderedDict代替内置字典Dict，依次将选手成绩存入OrderedDict

```python
>>> from collections import OrderedDict
>>> od = OrderedDict()
>>> od['c'] = 1
>>> od['b'] = 2
>>> od['a'] = 3
>>> od
OrderedDict([('c', 1), ('b', 2), ('a', 3)])
>>> od.keys()
odict_keys(['c', 'b', 'a'])
>>> players = list('abcdedg')
>>> players
['a', 'b', 'c', 'd', 'e', 'd', 'g']
>>> from random import shuffle
>>> shuffle(players)
>>> players
['d', 'd', 'c', 'b', 'a', 'g', 'e']
>>> od = OrderedDict()
>>> for i, play in enumerate(players, 1):
...     od[play] = i
... p
>>> def query_by_name(d, name):
...     return d[name]
...
>>> query_by_name(od, 'd')
2
>>> iter(od)[2]  # 因为不支持切片操作
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'odict_iterator' object is not subscriptable
>>> from itertools import islice
>>> list(islice(range(10), 3, 6))
[3, 4, 5]
>>> list(islice(od, 3, 6))
['a', 'g', 'e']
>>> def query_by_order(d, a, b=None):
...     a -= 1
...     if b is None:
...             b = a + 1
...     return list(islice(d, a, b))
...
>>> query_by_order(od, 2)
['c']
>>> query_by_order(od, 2, 3)
['c', 'b']

```

## 如何实现用户的历史记录功能（最多n条）

### 实际案例

制作一个简单的猜数字的小游戏，如何添加历史记录功能，显示用户最近猜过的数字？
