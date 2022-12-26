---
title: linux踩坑记录
date: 2022-08-03 22:35:16
category:
- linux🐧
tag:
- linux🐧
- 踩坑
---

<!-- more -->
<div align="center"><h1><strong> 踩坑记录</strong></h1></div>


## linux出现ssl错误
使用pip安装包的时候发现ssl错误，怀疑是openssl的问题。排查证书发现都在，没问题。  
测试网络，虚拟机与宿主机通信正常，测试curl google发现报ssl的问题，怀疑不仅是pip的ssl，进一步搜索网上说可能是系统时间有问题。  
date hwclock查看一下，硬件时间与本地时间差30分钟。  
`date -s 11/03/2009` 将系统日期设定成2009年11月3日的命令  
`date -s 17:55:55`将系统时间设定成下午5点55分55秒的命令  
`hwclock -w` 将当前时间和日期写入BIOS，避免重启后失效  
调整好时间后正常了  
