
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

### 解决方案

1. 使用容量为n的队列存储历史记录，使用标准库collections中的deque，它是一个双端队列

2. 使用pickle模块将历史记录存储到硬盘，以便下次启动使用


```python
>>> from collections import deque
>>> deque([], 5)
deque([], maxlen=5)
>>> q = deque([], 5)
>>> q.append(1)
>>> q.append(2)
>>> q.append(3)
>>> q.append(4)
>>> q.append(5)
>>> q
deque([1, 2, 3, 4, 5], maxlen=5)
>>> q.append(6)
>>> q
deque([2, 3, 4, 5, 6], maxlen=5)
>>>
```

```python

from random import randint
from collections import deque
def guess(n, k):
    if n == k:
        print("猜对了，这个数字是%d" % k)
        return True

    if n < k:
        print("猜大了，比%d小" % k)
    elif n > k:
        print("猜小了，比%d大" % k)
    return False

def main():
    n = randint(1, 100)
    i = 1
    hq = deque([], 5)
    while True:
        line = input("[%d] 请输入一个数字：" % i)
        if line.isdigit():
            k = int(line)
            hq.append(k)
            i += 1
            if guess(n, k):
                break
        elif line == 'quit':
            break
        elif line == 'h?':
            print(list(hq))

if __name__ == '__main__':
    main()


[1] 请输入一个数字：1
猜小了，比1大
[2] 请输入一个数字：2
猜小了，比2大
[3] 请输入一个数字：3
猜小了，比3大
[4] 请输入一个数字：4
猜小了，比4大
[5] 请输入一个数字：5
猜小了，比5大
[6] 请输入一个数字：6
猜小了，比6大
[7] 请输入一个数字：7
猜小了，比7大
[8] 请输入一个数字：h?
[3, 4, 5, 6, 7]
[8] 请输入一个数字：

```


```python

>>> import pickle  # pickl直接将对象保存
>>> q
deque([2, 3, 4, 5, 6], maxlen=5)
>>> pickle.dump(q, open('save.pkl', 'wb'))  # 注意pickle要以二进制形式写入
>>> q2 = pickle.load(open('save.pkl', 'rb')) # 读也要以二进制读
>>> q2
deque([2, 3, 4, 5, 6], maxlen=5)
>>>

```


```python
from random import randint
from collections import deque
import pickle
import os


def guess(n, k):
    if n == k:
        print("猜对了，这个数字是%d" % k)
        return True

    if n < k:
        print("猜大了，比%d小" % k)
    elif n > k:
        print("猜小了，比%d大" % k)
    return False


def main():
    n = randint(1, 100)
    i = 1
    if os.path.exists("hq.pkl"):
        hq = pickle.load(open("hq.pkl", "rb"))
    else:
        hq = deque([], 5)

    while True:
        line = input("[%d] 请输入一个数字：" % i)
        if line.isdigit():
            k = int(line)
            hq.append(k)
            i += 1
            if guess(n, k):
                break
        elif line == 'quit':
            break
        elif line == 'h?':
            print(list(hq))
    pickle.dump(hq, open("hq.pkl", "wb"))


if __name__ == '__main__':
    main()


```


## 如何拆分含有多种分隔符的字符串

### 实际案例

我们要把某个字符串依据分隔符号拆分不同的字段，该字符串包含多种不同的分隔符，例如

s = 'ab;cd|efg|hi,jkl|mn\opq;rst,uvw\txyz' 

其中<,>，<;>，<|>，<\t>都是分隔符，如何处理

### 解决方案

1. 连续使用str.split()方法，每次处理一种分隔符

```python
>>> s = 'ab;cd|efg|hi,jkl|mn\opq;rst,uvw\txyz'
>>> s.split(';')  # 一次只能处理一个分隔符
['ab', 'cd|efg|hi,jkl|mn\\opq', 'rst,uvw\txyz']
>>> [ss.split('|') for ss in s.split(';')]
[['ab'], ['cd', 'efg', 'hi,jkl', 'mn\\opq'], ['rst,uvw\txyz']]
>>> map(lambda ss: ss.split('|'), s.split(';'))
<map object at 0x103cc6780>
>>> list(map(lambda ss: ss.split('|'), s.split(';')))
[['ab'], ['cd', 'efg', 'hi,jkl', 'mn\\opq'], ['rst,uvw\txyz']]
>>> t = []
>>> list(map(t.extend, [ss.split('|') for ss in s.split(';')]))  # 将二维列表转一维列表
[None, None, None]
>>> t
['ab', 'cd', 'efg', 'hi,jkl', 'mn\\opq', 'rst,uvw\txyz']
>>> sum([ss.split('|') for ss in s.split(';')], [])  # 二维列表转一维列表，注意初始值的设置
['ab', 'cd', 'efg', 'hi,jkl', 'mn\\opq', 'rst,uvw\txyz']
>>> def my_split(s, seps):
...     res = [s]
...     for sep in seps:
...             t = []
...             list(map(lambda ss: t.extend(ss.split(sep)), res))
...             res = t
...     return res
...
>>> my_split(s, ';|,\t')
['ab', 'cd', 'efg', 'hi', 'jkl', 'mn\\opq', 'rst', 'uvw', 'xyz']
>>> from functools import reduce
>>> reduce(lambda l, sep: sum(map(lambda ss: ss.split(sep), l), []), ',;|\t', [s])  # 注意添加l的初始值
['ab', 'cd', 'efg', 'hi', 'jkl', 'mn\\opq', 'rst', 'uvw', 'xyz']
>>>
```

2. 使用正则表达式的re.split()方法
```python
>>> s = 'ab;cd|efg|hi,jkl|mn\opq;rst,uvw\txyz'
>>> import re
>>> re.split(r'[,;|\t]+', s)
['ab', 'cd', 'efg', 'hi', 'jkl', 'mn\\opq', 'rst', 'uvw', 'xyz']
>>>

```

## 如何判断字符串a是否以字符串b开头或结尾

### 实际案例
某文件系统目录下有一些列文件：
quicksort.c
graph.py
heap.java
stack.cpp
...
编写程序给其中所有.sh文件和.py文件加上用户可执行权限

## 解决方案

使用str.startswith()和str.endswith()方法
（注意：多个匹配时参数使用元祖）

```python
>>> fn.endswith(('.py', '.sh'))
True
>>> import os
>>> os.listdir()
['python_from_job.md', 'python3提高.md', 'libsample.so', 'python_learning.md', 'learn_deepcopy.md', '线程', 'python3-cookbook', '.gitignore', 'sample.py', '.git', 'main.py', 'save.pkl']
>>> os.stat('sample.py')  # 查看文件状态信息
os.stat_result(st_mode=33188, st_ino=12887567929, st_dev=16777221, st_nlink=1, st_uid=501, st_gid=20, st_size=540, st_atime=1565083577, st_mtime=1564885721, st_ctime=1564885721)
>>> s = os.stat('sample.py')
>>> s.st_mode
33188
>>> oct(s.st_mode)
'0o100644'
>>> s.st_mode | 0o100
33252
>>> oct(s.st_mode | 0o100)
'0o100744'
>>> import stat
>>> stat.S_IXUSR
64
>>> os.chmod('sample.py', s.st_mode | stat.S_IXUSR)  # 改变文件用户执行权限
```

## 如何调整字符串中文本的格式

### 实际案例

某软件的log文件，其中的日期为'yyyy-mm-dd'

2016-05-21 10:39:26 status unpacked python3-pip:all

...

我们想把其中的日期改为美国日期的格式'mm/dd/yyyy'

2016-05-21 => 05/23/2016

### 解决方案

使用正则表达式re.sub()方法做字符串替换，利用正则表达式的捕获组，捕获每个部分内容，在替换字符串中调整各个捕获组的顺序


```python
>>> f = open('log.log', 'r')
>>> log = f.read()
>>> log
'2019-08-11 10:18:39+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB\n2019-08-11 10:24:09+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB\n2019-08-11 10:29:39+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB\n2019-08-11 10:35:08+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB\n2019-08-11 10:40:39+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB\n'
>>> import re
>>> print(re.sub('(\d{4})-(\d{2})-(\d{2})', '\2/\3/\1', log))
// 10:18:39+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB
// 10:24:09+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB
// 10:29:39+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB
// 10:35:08+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB
// 10:40:39+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB

>>> '\2'  # 这是一个字符
'\x02'
>>> len('\2')
1
>>> len('\\2')  # re要这样的字符
2
>>> ord('a')
97
>>> oct(ord('a'))
'0o141'
>>> '\141'
'a'

>>> print(re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', log))  # 使用r(raw)标记，就不用转义字符了 
08/11/2019 10:18:39+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB
08/11/2019 10:24:09+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB
08/11/2019 10:29:39+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB
08/11/2019 10:35:08+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB
08/11/2019 10:40:39+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB

# 用()取组，在替换中使用被分组的内容，组的编号从每个组的左括号在字符串中出现的顺序
>>> print(re.sub(r'(?P<y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})', r'\g<m>/\g<d>/\g<y>', log))  # 给组命名
08/11/2019 10:18:39+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB
08/11/2019 10:24:09+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB
08/11/2019 10:29:39+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB
08/11/2019 10:35:08+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB
08/11/2019 10:40:39+08 xxydeMBP system_installd[358]: PackageKit: Install sandbox purging reclaimed 0 KB

>>>

```

## 如何将多个小字符串拼接成一个大字符串

### 实际案例

将程序中的歌歌参数按次序收集到列表中：
["<0112>", "<32>", "<1024>", "<60>"]
最终要把各个参数拼接成一个数据报进行发送
"<0112><32><1024><60>"

### 解决方案

1. 迭代列表，连续使用'+'操作以此拼接每一个字符串

2. 使用str.join()方法，更加快速的拼接列表中所有字符串

```python
In [1]: from functools import reduce

In [2]: l = ["<0112>", "<32>", "<1024>", "<60>"]

In [3]: l
Out[3]: ['<0112>', '<32>', '<1024>', '<60>']

In [4]: %timeit reduce(str.__add__, l)
432 ns ± 2.56 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [5]: %timeit ''.join(l)
117 ns ± 0.281 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

```

## 如何对字符串进行左，右，居中对齐

## 实际案例

某字典存储了一些列属性值
{
	"loadDist": 100,
	"SmallCull": 0.04,
	"DistCull": 500.0,
	"trilinear": 40,
	"farclip": 477
}

在程序中，我们想以工整的格式将其内容输出，如何处理？
SmallCull: 0.04
farclip  : 477
loadDist : 100.0
trilinear : 40

1. 使用字符串的str.ljust()，str.rjust(),str.center()进行左，右，居中对齐

2. 使用format()方法，传类似'<20'，‘>20’，'^20'参数完成同样任务

```python
>>> s = 'abc'
>>> s.ljust(10)
'abc       '
>>> s.ljust(10, '*')
'abc*******'
>>> s.rjust(10, '*')
'*******abc'
>>> s.center(10, '*')
'***abc****'
>>> format(s, '<10')
'abc       '
>>> format(s, '>10')
'       abc'
>>> format(s, '^10')
'   abc    '
>>> format(s, '*^10')
'***abc****'
>>> format(5, '>10')
'         5'
>>> n = 5
>>> n.__format__('>10')
'         5'
>>> format(123, '+')
'+123'
>>> format(-123, '+')
'-123'
>>> format(-123, '=+10')
'-      123'
>>> format(-123, '0=+10')
'-000000123'
>>>
>>> for k, v in d.items():
...     print(k.ljust(w), ':', v)
...
loadDist  : 100
SmallCull : 0.04
DistCull  : 500.0
trilinear : 40
farclip   : 477
>>>

```


## 如何去掉字符串中不需要的字符

### 实际案例

1.过滤掉用户输入中前后多余的空白字符：' nick2008@gmail.com '
2.过滤某Windows下编辑文本中的'\r'：'hello word\r\n' 
3.去掉文本中的unicode组合符号（音调）：'nǐ hǎo, chī fà'

### 解决方案
1.字符串strip()，lstrip()，rstrip()方法去掉字符串两端字符
2.删掉单个固定位置的字符，可以使用切片+拼接的方法
3.字符串的replace()方法或正则表达式re.sub()删除任意子串
4.字符串的translate()方法，可以同时删除多种不同字符
```python3
>>> s = 'abc1234xyz'
>>> s.translate({'a':'x'})  # 键要求是unicode
'abc1234xyz'
>>> ord('a')
97
>>> s.translate({ord('a'):'X'})
'Xbc1234xyz'
>>> s.maketrans('abcxyz', 'XYZABC')
{97: 88, 98: 89, 99: 90, 120: 65, 121: 66, 122: 67}
>>> s.translate({97: 88, 98: 89, 99: 90, 120: 65, 121: 66, 122: 67})
'XYZ1234ABC'
>>> s.translate({ord('a'): None})
'bc1234xyz'
```


## 如何实现可迭代对象和迭代器对象

迭代器对象 ：Iterator
可迭代对象 ：Iterable


## 如何实现可迭代对象和迭代器对象

### 实际案例

某软件要求，从网络抓取各个城市气温信息，并依次显示：
北京：15-20
天津：15-22
长春：12-18
......

如果依次抓取所有城市气温再显示，显示第一个城市气温时，有很高的延时，并且浪费存储空间。我们期望以“用时访问”的策略，并且能把所有城市气温封装到一个对象里，可用for语句进行迭代，如何解决？

```python
>>> from collections import Iterable, Iterator
>>> l = [1, 2, 3]
>>> for x in l:
...     print(x)
...
1
2
3 
>>> isinstance(l, Iterable)  # 能放在for循环in后面的一定是可迭代对象
True
>>> issubclass(list, Iterable)  # 换一种描述，list是Iterable的子类
True
>>> issubclass(str, Iterable)
True
>>> issubclass(dict, Iterable)
True
>>> issubclass(int, Iterable)  # int不能放到in后面
False

# for循环拿到可迭代对象后调用iter()方法，生成迭代器对象， 
>>> iter(l)
<list_iterator object at 0x103473208>
>>> iter(l)
<list_iterator object at 0x103473710>
>>>
# 每次调用会生成不同的迭代器对象
# iter()是通过调用可迭代对象的__iter__方法 
>>> l.__iter__()
<list_iterator object at 0x103473208>
>>> Iterable.__abstractmethods__  # 查看抽象方法
frozenset({'__iter__'})
>>> it = iter(l)
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
# netx()方法是调用迭代器对象的__next__方法
```

```python
# 迭代器是一次性消费的
>>> l = [1, 2, 3]
>>> it = iter(l)
>>> next(it)
1
>>> list(it)
[2, 3]
>>> next(it)  # list操作已经把迭代器消耗了
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

```python
# 迭代器也能放到in后面
# 说明迭代器对象是可迭代对象的子类
>>> issubclass(Iterator, Iterable)
True
>>> it = iter(l)
>>> it.__iter__()  # 迭代器对象下也有__iter__方法，它返回的是自身
<list_iterator object at 0x103559208>
>>> it.__iter__() is it
True
# 说明it既是迭代器对象，也是可迭代对象，如果调用可迭代接口，返回它自己
# for循环中放入迭代器对象，它还是会先调用__iter__()方法，尽管它返回它自己
```

### 解决方法

1. 实现一个迭代器对象Weatheriterator,__next__方法每次返回一个城市的气温

2. 实现一个可迭代对象Weatheriterable,__iter__方法返回一个Weatheriterator对象

```python
from collections import Iterable, Iterator
import requests


class WeatherIterator(Iterator):
    def __init__(self, citys):
        self.citys = citys
        self.index = 0

    def __next__(self):  # 迭代器对象实现__next__方法
        if self.index == len(self.citys):
            raise StopIteration
        city = self.citys[self.index]
        self.index += 1
        return self.get_weather(city)

    def get_weather(self, city):
        url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city
        r = requests.get(url)
        data = r.json()['data']['forecast'][0]
        return city, data['high'], data['low']

    # 迭代器如果有__iter__方法，应该返回自己


class WeatherIterable(Iterable):
    def __init__(self, citys):
        self.citys = citys

    def __iter__(self):  # 可迭代对象实现__iter__方法，返回其迭代器对象
        return WeatherIterator(self.citys)


def show(w):
    for x in w:
        print(x)


print("创建可迭代对象")
w = WeatherIterable(['北京', '上海', '广州'] * 3)
show(w)
print('*' * 20)
show(w)  # 每次都会创建一个迭代器

print("创建迭代器对象", end='\n\n')

w1 = WeatherIterator(['北京', '上海', '广州'] * 3)
show(w1)
print('*' * 20)
show(w1)  # 这个不会打印，因为迭代器对象是一次性的，只能迭代一次，消耗完了就没了

"""
创建可迭代对象
('北京', '高温 32℃', '低温 22℃')
('上海', '高温 33℃', '低温 26℃')
('广州', '高温 35℃', '低温 26℃')
('北京', '高温 32℃', '低温 22℃')
('上海', '高温 33℃', '低温 26℃')
('广州', '高温 35℃', '低温 26℃')
('北京', '高温 32℃', '低温 22℃')
('上海', '高温 33℃', '低温 26℃')
('广州', '高温 35℃', '低温 26℃')
********************
('北京', '高温 32℃', '低温 22℃')
('上海', '高温 33℃', '低温 26℃')
('广州', '高温 35℃', '低温 26℃')
('北京', '高温 32℃', '低温 22℃')
('上海', '高温 33℃', '低温 26℃')
('广州', '高温 35℃', '低温 26℃')
('北京', '高温 32℃', '低温 22℃')
('上海', '高温 33℃', '低温 26℃')
('广州', '高温 35℃', '低温 26℃')
创建迭代器对象

('北京', '高温 32℃', '低温 22℃')
('上海', '高温 33℃', '低温 26℃')
('广州', '高温 35℃', '低温 26℃')
('北京', '高温 32℃', '低温 22℃')
('上海', '高温 33℃', '低温 26℃')
('广州', '高温 35℃', '低温 26℃')
('北京', '高温 32℃', '低温 22℃')
('上海', '高温 33℃', '低温 26℃')
('广州', '高温 35℃', '低温 26℃')
********************

"""
```

## 如何使用生成器函数实现可迭代对象

### 实际案例

实现一个可迭代对象的类，它能迭代出给定范围所有素数：

pn = PrimeNumbers(1, 30)
for k in pn:
	print(k)

输出结果：
2 3 4 7 11 13 17 19 23 29

### 解决方案
将该类的__iter__方法实现成生成器函数，每次yield返回一个素数

```python
>>> def f():
...     print('in f 1')
...     yield 1
...     print('in f 2')
...     yield 2
...     print('in f 3')
...     yield 3
...
>>> f()  # 产生一个迭代器
<generator object f at 0x104670fc0>
>>> g = f()
>>> from collections import Iterable, Iterator
>>> isinstance(g, Iterable)
True
>>> isinstance(g, Iterator)
True
>>> iter(g) is g
True
>>> g.__iter__() is g
True
>>> next(g)
in f 1
1
>>> next(g)
in f 2
2
>>> next(g)
in f 3
3
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

>>> class XXX_Iterable(Iterable):
...     def __iter__(self):
...             yield 1
...             yield 2
...             yield 3
...
>>> # 创建一个可迭代对象，在__iter__中使用yield方法，就不用创建迭代器对象了。
...
>>> x = XXX_Iterable()
>>> for i in x:  # 先调用iter(x)，就得到了一个生成器对象，生成器对象是一个可迭代对象，然后就可以迭代
...     print(i)  # 就可以把迭代器的实现放到__iter__里面就可以了。用生成器函数实现迭代器
...
1
2
3
>>>

```

```python

from collections import Iterable

class PrimeNumbers(Iterable):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        for k in range(self.a, self.b + 1):
            if self.is_prime(k):
                yield k

    def is_prime(self, k):
        return False if k < 2 else all(map(lambda x: k % x , range(2, k)))
        # 小于2直接返回False
        # 大于2的依次与k-1取模，如果有一个0，all就返回False，否则返回True

pn = PrimeNumbers(1, 30)
for n in pn:
    print(n)

```













