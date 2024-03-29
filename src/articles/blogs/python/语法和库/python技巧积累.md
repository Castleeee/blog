---
title: python技巧积累
date: 2022-05-25 09:42:46
prev: ./深入python.md  
next: false
category:
- python🐍
tag:
- python🐍
---
::: info 📝Note
积累一些技巧，比如读写超大文件这种小技巧
:::
<!-- more -->
[[toc]]
<div align="center" style="font-size:1.4em;"><h2><strong> python技巧积累</strong></h2></div>

🕊[python 进阶技能_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1QE411u7vK)  
[Python 进阶视频_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1jz411b7DH)  
## 零散的?
### 使用方法链
类中的一些函数没有返回值的时候，可以返回self使用方法链，如果是不修改自身实例，返回一个新的，可以使用type创建新实例使用方法链  
::: details Click to see more
**链式调用**<br/>

```python
class Player:  
    def __init__(self,name,x,y):  
        self.name=name  
        self.x=x  
        self.y=y  
    def zero(self):  
        self.x=0  
        self.y=0  
        return self # 返回自身，使用链式调用  
    def moveX(self,offset):  
        self.x+=offset  
        return self # 返回自身，使用链式调用  
        # return type(self)(self.name,self.x+offset,self.x) # 不改变自身返回新对象的链式调用  
    def moveY(self,offset):  
        self.y+=offset  
        return self # 返回自身，使用链式调用  
    def __str__(self):  
        return "%s:(%s,%s)"%(self.name,self.x,self.y)  
  
p=Player("player1",5,5)  
(  
   p.zero()  # 也可以用\
    .moveX(3)  
    .moveY(1)  
)  
# 等价于 p.zero().moveX(3).moveY(1)
print(p)
```
运行结果
```
player1:(3,1)
```
:::

## 好习惯

- 禁止使用`"a"+b+"c"`使用`"a{b}c"`
- 不要`except:`空Error
- 检查参数是否为不可变
- 使用推导式注意可读性
- 替换原则，子类代替父类
- 不要用`═ ═`检查布尔值,用is，用if检查bool直接if x
- 使用`for i,v in enumerate(list)`代替`for i in range(len(list))`获取索引+元素
    - 甚至可以zip`for i,(v1,v2) in enumerate(zip(list1,list2))`
- 约定优于配置
- tuple解包`x,y=atuple`
- 测试运行时间使用`time.perf_counter`时钟时间代替`time.time`更加精确
- 试运行使用log模块而不是打印
- 多进程不要总是`shell=True`，这会让进程在shell里运行（他是这么说的，但是我也不知道是啥问题）
- 不要`import *`会命名空间混乱
- python虽然是解释型语言但也不是不编译，他只是编译到字节码阶段
- 遵守[PEP8](https://peps.python.org/pep-0008/)  
- 看到奇怪语法，想想是不是python2的遗留代码
- 查看文件(夹)是否存在,使用os.path或pathlib里的函数，这样不用打开文件性能高
- 不要在循环过程中修改可变类型etc数组
- 两个字符串中间没东西会自动合并
- 给俩变量一块赋值，发现不对劲检查括号
- 使用tuple函数声明传入可迭代类型会挨个构建

## 命名
驼峰法使用大小写来命名变量的方法，分为大驼峰和小驼峰  
特点
大驼蜂: UserName
- 第一个字母大写，后边也大写
    - 类名
    - 函数名
    - 属性名
    - 命名空间

小驼蜂userName
- 第一个字母小写，后边大写
    - 变量  

循环记得打括号

## Pythonic
pass 

`#coding=utf-8`
`#-*- coding: utf-8 -*-`

一直搞不清楚这俩头什么区别。直觉上一样。今天特意查了一下，大致明白了：  
对于python解释器来说，这两种写法一样。但是对于编辑器来讲，可能会出现识别问题。  
  
[参考PEP-0236](http://www.python.org/dev/peps/pep-0263/) Defining the Encoding
::: details Click to see more


    Python will default to ASCII as standard encoding if no other
    encoding hints are given.

    To define a source code encoding, a magic comment must
    be placed into the source files either as first or second
    line in the file, such as:

          # coding=<encoding name>

    or (using formats recognized by popular editors)

          #!/usr/bin/python
          # -*- coding: <encoding name> -*-

    or

          #!/usr/bin/python
          # vim: set fileencoding=<encoding name> :

    More precisely, the first or second line must match the regular
    expression "coding[:=]\s*([-\w.]+)". The first group of this
    expression is then interpreted as encoding name. If the encoding
    is unknown to Python, an error is raised during compilation. There
    must not be any Python statement on the line that contains the
    encoding declaration.

    To aid with platforms such as Windows, which add Unicode BOM marks
    to the beginning of Unicode files, the UTF-8 signature
    '\xef\xbb\xbf' will be interpreted as 'utf-8' encoding as well
    (even if no magic encoding comment is given).

    If a source file uses both the UTF-8 BOM mark signature and a
    magic encoding comment, the only allowed encoding for the comment
    is 'utf-8'.  Any other encoding will cause an error.
:::
 
 
