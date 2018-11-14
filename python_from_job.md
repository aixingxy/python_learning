# python中的星号*和双星号**
# 0.最常见的是‘相乘’和‘乘幂’


# 1 对函数传递的参数进行打包和拆解，其中元祖的打包和解包使用单星号*，字典的打包和拆解使用**
# 1.1 打包
将传递给函数的任意多个（也可以是零个）非关键字参数/关键字参数打包成一个元祖/字典（元祖只能接受非关键字参数，字典只能接受关键字参数）

# 1.1.1 元祖打包的例子
 ```python3
 >>> def tuple_pack(a, *b):
...     print(a)
...     print(b)
...
>>> tuple_pack(1, 2, 3, 4)
1
(2, 3, 4)
>>> tuple_pack(1)
1
()
 ```
在上面的例子中，\*b这个位置可以接受任意多个（也可以是零个）非关键字参数，并将收集到的参数转换成一个元祖。

# 1.1.2 字典打包的例子
```python3
>>> def dictionary_pack(a, **b):
...     print(a)
...     print(b)
...
>>> dictionary_pack(1, one=1, two=2, three=3)
1
{'three': 3, 'two': 2, 'one': 1}
>>> dictionary_pack(1)
1
{}
```
在上面的例子中，\*\*b这个位置可以接受多个（也可以是零个关键字参数），并将收集到的参数转换成一个字典。

# 1.1.3 元祖和字典混合例子
```python3
>>> def tuple_dictionary_pack(*a, **b):
...     print(a)
...     print(b)
...
>>> tuple_dictionary_pack(1, 2, 3, one=2, two=3)
(1, 2, 3)
{'two': 3, 'one': 2}
>>> tuple_dictionary_pack(1, 2)
(1, 2)
{}
>>> tuple_dictionary_pack(one=2, two=3)
()
{'two': 3, 'one': 2}
>>> tuple_dictionary_pack(one=2, two=3, 1, 2)
  File "<stdin>", line 1
SyntaxError: non-keyword arg after keyword arg
```
在上面的例子中，\*a这个位置负责接受任意多个非关键字参数，\*\*b这位置可以接受任意多个关键字参数，注意二者在函数定义中的顺序不能颠倒。

# 2 拆解

将传递给函数的的一个列表、元祖或字典拆分成独立的多个元素然后赋值给函数中的参数量（包括普通的位置参数，关键字参数，元组也即*非关键字参数，字典也即**关键字参数）。在解字典时会有两种解法，一种使用*解，解出来传给函数的只有键值（.key）另一个是用**解，解出来的是地点的每一项。

# 2.1.1 位置变量和元祖混合拆解的例子
```python3
>>> def variable_tuple_unpack(a, b, c, *d):
...     print(a)
...     print(b)
...     print(c)
...     print(d)
...
>>> ee = [1, 2, 3, 4, 5]
>>> variable_tuple_unpack(*ee)
1
2
3
(4, 5)
```
# 2.1.2 元祖和字典混合的例子
```python3
>>> def tuple_dictionary_unpack(*a, **b):
...     print(a)
...     print(b)
...
>>> ee = (1, 2, 3)
>>> ff = {'one':1, 'two':2, 'three':3}
>>> tuple_dictionary_unpack(*ee, **ff)
(1, 2, 3)
{'one': 1, 'three': 3, 'two': 2}
```

# 2.1.3 字典的键值解成元祖的例子
```python3
>>> def tuple_dictionary(*a):
...     print(a)
...
>>> ff = {'one':1, 'two':2, 'three':3}
>>> tuple_dictionary(*ff)
('three', 'two', 'one')
```

非关键字参数指的就是位置参数，在函数参数传递中根据顺序对变量赋值；关键字参数可以根据变量的关键字乱序赋值，关键字参数也会在函数定义中赋予初值。另外，非关键字参数不可以通过关键字赋值，但是关键字参数可以通过位置参数赋值；而且在函数定义时，关键字参数后不能有非关键字参数。


# zip函数
zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元祖。然后返回这些元祖组成的列表。
若果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用*号操作符，可以将元祖解压为列表

*注意：zip方法在python2和python3中是不同的：在python3中为了减少内存，zip()返回的是一个对象。如需展示列表，需要手动list()转换*

```python2
>>> a = [1, 2, 3, 4]
>>> b = ['a', 'b', 'c', 'd']
>>> c = ['A', 'B', 'C', 'D']
>>> zip(a, b, c)
[(1, 'a', 'A'), (2, 'b', 'B'), (3, 'c', 'C'), (4, 'd', 'D')]
>>> for i, j, k in zip(a, b, c):
...     print(i, j, k)
...
(1, 'a', 'A')
(2, 'b', 'B')
(3, 'c', 'C')
(4, 'd', 'D')
>>> zip(*zip(a ,b ,c))
[(1, 2, 3, 4), ('a', 'b', 'c', 'd'), ('A', 'B', 'C', 'D')]
```

# python特殊函数__call__()
在python中，函数其实是一个对象
```python2
>>> f = abs
>>> f.__name__
'abs'
>>> f(-123)
123
```
由于f可以被调用，所以f被称为可调用对象

所偶的函数都是可调用的对象，一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call()__
```python
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print("My name is %s" % self.name)
        print("My friend is %s" % friend)


if __name__ == '__main__':
    p = Person('Bob', 'male')
    p('Tom')
```
# yield
```python3
>>> def foo():
...     for x in range(10):
...             yield x
...
>>> res = foo()
>>> print(res)
<generator object foo at 0x7fad70013840>
>>> for i in res:
...     print(i)
...
0
1
2
3
4
5
6
7
8
9
```

# python vars() 函数
vars() 函数返回对象object的属性和属性值的字典对象。
