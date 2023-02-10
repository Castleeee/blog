---
title: python库
date: 2022-05-18 10:16:08
prev: ./python语言进阶.md
next: ./py踩坑记录.md
category:
- python🐍
tag:
- python🐍
---

<!-- more -->

[[toc]]

<div align="center" style="font-size:1.4em;"><h2><strong> python库</strong></h2></div>

## collections
首当其冲，这个高性能扩展数据类型库是每一个pythoner必须的  

## numbers
列举出了基本的数据类型

## bisect序列排序

^194418

[文档](https://docs.python.org/zh-cn/3.9/library/bisect.html)  
`insort`是`insort_right`默认方式  
`bisect`是`bisect_right`默认方式  
一共四个算法，二分查找`bisect`和插入`insort`，分别是从左或者右  
可以用来维护一个排序序列  
`insort`不会返回值，`bisect`会返回适合插入的位置，可以直接用序列的`insert`插入
```python
import bisect  

a=[]  
bisect.insort_right(a,6)  
bisect.insort_right(a,7)  
bisect.insort_right(a,2)  
bisect.insort_right(a,4)  
  
a.insert(bisect.bisect_right(a,5),5)  
print(a)
#----结果----
[2, 4, 5, 6, 7]
```
用来查找的时候按照官方文档包装一下  
## functools
[functools模块学习 - 简书](https://www.jianshu.com/p/15757099a395)
### 偏函数

^ff28bf

提前把函数的参数固定住，配合闭包看  
### cache
加速缓存
## itertools
用于更好遍历和封装的库
#todo
itertools.groupby数组只会去相邻的重，groupby的本质是使用前使用前先排序
[【python技巧059】用itertools处理各种花样的迭代_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV19V4y1F7if)
## time和date库
### 测试程序性能
### arrow
## try-except的使用规范

## 哈希
## 文件和序列化IO
## 图像音视频
pillow
opencv
moviepy
musicpy
pydub
## 网络

pywifi
paramiko

## 有趣的包
### tqdm进度条
提供文本动画进度条，使用方法：

```Python
import time
from tqdm import tqdm
for i in tqdm(range(1000)):
    time.sleep(.01)
#----------
65%|██████████████████▏           | 649/1000 [00:07<00:04, 86.51it/s]
```

### 代码流程可视化

#### pycallgraph
#### code2flow
