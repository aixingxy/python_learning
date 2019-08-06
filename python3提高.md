
# python3提高

## 如何在列表，字典，集合中根据条件筛选数据

### 实际案例

+ 过滤掉列表[3, 9, -1, 10, 20, -2, ...]中的负数

+ 筛选出字典{'LiLi': 79, 'Jim': 88, 'Lucy': 92, ...}中高于90的项

+ 筛选出集合{77, 89, 32, 20, ...}中能被3整除的元素

### 解决方法

+ 列表

    列表解析：[x for x in data if x > 0]

    filter函数：filter(lambda x: x > 0, data)

+ 字典

    字典解析：{k: v for k, v in d.items() for v > 90}

+ 集合

    集合解析：{x for x in s if x % 3 == 0}

## 如何为元祖中的每个元素命名，提高程序可读性

### 实际案例
学生信息系统中数据为固定格式：（名字，年龄，性别，邮箱）

('jim', 16, 'male', 'jim123@gmail.com')

访问时，使用索引(index)访问，大量索引降低程序可读性

### 解决方法
+ 定义一系列数据常量或枚举类型


```python3
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
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'male', 'email'])
s2 = Student('Jim', 16, 'male', '123@qq.com')

print(isinstance(s2, tuple))

print(s2[0])

print(s2.age)

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













