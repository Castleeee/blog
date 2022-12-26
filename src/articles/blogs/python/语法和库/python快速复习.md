---
title: python快速复习
date: 2022-05-16 15:57:35
prev: false  
next: ./python语言进阶.md
category:
- python🐍
tag:
- python🐍
---

很零碎，很基础，不容易想起来的知识点。  
配合廖学峰和python文档快速熟悉知识
<!-- more -->

[[toc]]

<div align="center"><h1><strong> python快速复习</strong></h1></div>

## 一些资料
- [官方文档#第三方包](https://docs.python.org/zh-cn/3/library/index.html)
- [内置函数Built-in Functions](https://docs.python.org/3/library/functions.html)
- [第三方包查询pypi](https://pypi.org/)  
- [windows WHL站](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

## 环境管理相关
### 环境常用
三个常用的就够了，venv和virtualenv，conda  
venv的创建就是`python -m venv /path/to/new/virtual/environment` 此时进入创建的目录bin文件夹，activate就可以激活了。  
venv创建的环境python版本和外部的大版本相同，只是把环境独立了出来，python解释器是指向那个的软连接,venv只隔离包  
windows上激活就是运行脚本，linux激活就是source activate  
  
virtualenv和conda都是解释器级别的隔离，但是这俩是不兼容的有一个会不起效，会直接创建新的解释器，可以指定python的版本  
virtualenv需要安装`pip install virtualenv`,

### pip包常用



## 数字和字符串
- Python允许在数字中间以`_`分隔，因此，写成`10_000_000_000`和`10000000000`是完全一样的。十六进制数也可以写成`0xa1b2_c3d4`。浮点数运算可能会有四舍五入的误差  
- `str`通过`encode()`方法可以编码为指定的`bytes` `'ABC'.encode('ascii')`   
    - 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是`bytes`。要把`bytes`变为`str`，就需要用`decode()`,参数`errors='ignore'`忽略错误的字节
    - `len()`函数计算的是`str`的字符数，如果换成`bytes`，`len()`函数就计算字节数
- 对于单个字符的编码，Python提供了`ord()`函数获取字符的整数表示，`chr()`函数把编码转换为对应的字符
-  `'Age: %s. Gender: %s' % (25, True)`如果你不太确定应该用什么，`%s`永远起作用，它会把任何数据类型转换为字符串,双`%%`可以打印正常%
- `'Hello, {name}, 成绩提升了 {score:.1f}%'.format(name='小明', score=17.125)`
- 通过dict提供的`get()`方法，如果key不存在，可以返回`None`，或者自己指定的value，`d.get("key",value)`
- int的base参数可以指定进制
## 函数
```python
def add_end(L=[]):
    L.append('END')
    return L
```
Python函数在定义的时候，默认参数`L`的值就被计算出来了，即`[]`，因为默认参数`L`也是一个变量，它指向对象`[]`，每次调用该函数，如果改变了`L`的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的`[]`了
::: warning Warning
定义默认参数要牢记一点：默认参数必须指向不变对象！
:::
```python
def person(name, age, *, city, job):
    print(name, age, city, job)
```

和关键字参数`**kw`不同，命名关键字参数需要一个特殊分隔符`*`，`*`后面的参数被视为命名关键字参数。  
如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符`*`了  
命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：  
### 尾递归优化
解决递归调用栈溢出的方法是通过**尾递归**优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。  
尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
```python
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
```
尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。  
遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的`fact(n)`函数改成尾递归方式，也会导致栈溢出。

`functools.partial`的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单，`int2 = functools.partial(int, base=2)`


## 特性

### 列表生成式
```python
# 以下代码正常输出偶数：
[x for x in range(1, 11) if x % 2 == 0]
[2, 4, 6, 8, 10]

# 以下代码奇负偶正：
[x if x % 2 == 0 else -x for x in range(1, 11)]
[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

```
如果使用`()`那就是生成器了，生成器使用`next()`获取下一个值抛出`StopIteration`的错误停止，generator也是可迭代对象  
在函数中使用`yield`阻塞函数执行并return值使用next回复执行，使用时需要创建对象，类似于类的使用  
可以使用`isinstance()`判断一个对象是否是`Iterable`或`Iterator` 对象`from collections.abc import Iterable,Iterator`
生成器都是`Iterator`对象，但`list`、`dict`、`str`虽然是`Iterable`，却不是`Iterator`,把`Iterable`变成`Iterator`可以使用`iter()`函数  
- 凡是可作用于`for`循环的对象都是`Iterable`类型；
- 凡是可作用于`next()`函数的对象都是`Iterator`类型，它们表示一个惰性计算的序列
- `for`循环本质上就是通过不断调用`next()`函数实现的  

### 排序
`sorted()`函数也是一个高阶函数，它还可以接收一个`key`函数来实现自定义的排序，例如按绝对值大小排序  
`sorted([36, 5, -12, 9, -21], key=abs)`  
```python

# 自定义字段排序
sorted(obj, key=lambda x: x['a'])

# 多字段优先级排序
sorted(obj, key=lambda x: (x['a'], x['b']))

# 有个第三方包
sorted(obj, key=operator.itemgetter('a'))

# 自定义排序函数，实际上是重载了比较函数
from functools import cmp_to_key

sorted(obj, key=cmp_to_key(func))

```

### 装饰器格式
```python
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__) # 功能代码
        return func(*args, **kw)
    return wrapper
```


```
assert x >= 0 : "x must >= 0";
```

这样，断言失败的时候，`AssertionError`会带上消息`x must >= 0`，更加便于调试。
## OOP
`_`可以访问但不建议
`__`私有变量（private）不能直接访问`__name`是因为Python解释器对外把`__name`变量改成了`_ClassName__name`
`__xxx__`是特殊变量

和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量`self`，并且，调用时，不用传递该参数  
对于静态语言（例如Java）来说，如果需要传入`Animal`类型，则传入的对象必须是`Animal`类型或者它的子类，否则，将无法调用`run()`方法。  
对于Python这样的动态语言来说，则不一定需要传入`Animal`类型。我们只需要保证传入的对象有一个`run()`方法就可以了  

::: info 📝Note
就这样吧，剩下的详细放在进阶里
:::
