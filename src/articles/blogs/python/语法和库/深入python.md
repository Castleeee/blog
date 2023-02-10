---
title: 深入python
date: 2022-05-23 09:46:14
prev: ./py踩坑记录.md  
next: ./python技巧积累.md
category:
- python🐍
tag:
- python🐍
---
::: tip 📌Tip
深入这个概念和大数据是一样的，多深入才叫深入？  
这里会放一些自觉比较深的知识点和技巧，有些时候会和踩坑联动  
:::

<!-- more -->
[[toc]]



<div align="center" style="font-size:1.4em;"><h2><strong> 深入python</strong></h2></div>

## GC原理剖析

^08132d

#TODO GC看这里
[Python垃圾回收机制！非常实用 - 知乎](https://zhuanlan.zhihu.com/p/83251959)<br/>
[记一次面试问题——Python 垃圾回收机制 · TesterHome](https://testerhome.com/topics/16556)

[2小时吃透python内存管理和垃圾回收机制_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Ei4y1b7mo?spm_id_from=333.337.search-card.all.click)
### 环形数据结构
著名的环形引用
[Python 如何在环状数据结构中管理内存 - i'm jackey - i'm jackey](https://ijackey.com/python-%E5%A6%82%E4%BD%95%E5%9C%A8%E7%8E%AF%E7%8A%B6%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%AD%E7%AE%A1%E7%90%86%E5%86%85%E5%AD%98-956.html)

## 普通技巧
## 网络编程详解
### twisted
### gevent
## 函数式编程
### 函数式编程思想
::: tip 📌Tip
这里就不局限于python了，只是我用的顺手拿python当例子，思想是通用的
:::
可以配合CS61A视频  
### python的函数式编程
## 异步进阶
^347f89

异步的内容其实还有很多，这里只放已经收集到的   
gevent的缺点，使用C实现底层协程，使用猴子将普通库打补丁，会导致有些错误无法捕捉  

### 多线程异步
有些时候外部接口只提供了阻塞方法，没有提供异步方法，还是需要使用线程  
申请一个线程池，
::: details Click to see more

```python
import asyncio,time,random  
from concurrent.futures import ThreadPoolExecutor  
import socket  
from urllib.parse import urlparse  
  
def func(a):  
    # 阻塞方法  
    t=random.randint(0,5)  
    print("arg is %s"%a)  
    print("start sleep %s"%t)  
    time.sleep(t)  
    print("end sleep %s"%t)  
  
if __name__ == "__main__":  
    start_time = time.time()  
  
    loop = asyncio.get_event_loop()  
    executor = ThreadPoolExecutor(3) # 申请线程池  
    tasks = []  
    for i in range(0,20):  
        task = loop.run_in_executor(executor, func, i)  
        # 注意协程的这个函数，传入的是executor，返回是封装的Future对象，可以直接放在协程中使用  
        tasks.append(task)  
    loop.run_until_complete(asyncio.wait(tasks))  
  
    print("last time:{}".format(time.time()-start_time))
```
运行结果
```
arg is 0
start sleep 4
arg is 1
start sleep 4
arg is 2
start sleep 3
end sleep 3
arg is 19
start sleep 3
end sleep 4
end sleep 4
...
```
:::
#TODO debug正常run不正常的异步多线程
### 多进程异步

## 混合编程

## 热加载
#todo
python程序的热加载还是程序的热加载？