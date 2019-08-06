
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

from random import randint

d = {k: randint(60, 100) for k in "abcdefg"}

# 列表解析
l = [(v, k) for k, v in d.items()]
print(sorted(l, reverse=True))

# zip
l = list(zip(d.values(), d.keys()))
print(sorted(l, reverse=True))

# 直接使用sorted的key方法
print(sorted(d.items(), key=lambda item: item[1], reverse=True))


```

```python
from random import randint

d = {k: randint(60, 100) for k in "abcdefg"}

l = sorted(d.items(), key=lambda item: item[1], reverse=True)

# 更新字典
for i, (k, v) in enumerate(l, 1):
    print(i, k, v)
    d[k] = (i, v)

print(d)

# 重新生成字典
d_new = {k: (i, v) for i, (k, v) in enumerate(l, 1)}
print(d_new)

```

## 如何统计序列中元素的频度

## 实际案例

+ 某随机序列[12, 5, 6, 4, 6, 5, 5, 7]中，找到出现次数最高的三个元素，他们粗线的次数是多少？
+ 对某英文文章的单次，进行词频统计，找到出现次数最高的10个单次，他们出现的次数是多少？

## 解决方案
1. 将序列转换为字典{元素: 频度}，根据字典中的值排序
```bash
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
>>> sorted(((v, k) for k, v in d.items()), reverse=True)[:3]  # 使用生成器解析
[(3, 16), (3, 15), (3, 11)]
>>>

```

2.
